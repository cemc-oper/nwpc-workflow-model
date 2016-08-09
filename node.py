# coding=utf-8
from nwpc_log.models import Record


class NodeType(object):
    Unknown = 1
    Root = 2
    Suite = 3
    Family = 4
    Task = 5
    Alias = 6
    NonTaskNode = 7
    Meter = 8

    node_type_mapper = {
        Unknown: 'unknown',
        Root: 'root',
        Suite: 'suite',
        Family: 'family',
        Task: 'task',
        Alias: 'alias',
        NonTaskNode: 'non-task',
        Meter: 'meter',
    }

    def __init__(self):
        self.node_state = self.Unknown

    def __getattr__(self, name):
        if name in self:
            return name
        raise AttributeError

    @staticmethod
    def get_node_type_string(node_type):
        return NodeType.node_type_mapper[node_type]


class Node(object):
    def __init__(self):
        self.parent = None
        self.children = list()
        self.name = ''

    def __str__(self):
        return self.get_node_path()

    def to_dict(self):
        """

        :return:
            {
                'name': str, node name,
                'node_type': str, node type,
                'node_path': str, node path,
                'children': array, [
                    node dict,
                    node dict,
                    ...
                ]

            }
        """
        ret = dict()
        ret['name'] = self.name
        ret['children'] = list()
        ret['node_type'] = self.get_node_type()
        ret['node_path'] = self.get_node_path()
        for a_child in self.children:
            ret['children'].append(a_child.to_dict())
        return ret

    @staticmethod
    def create_from_dict(node_dict, parent=None):
        # use parent is evil.
        node = Node()
        node.parent = parent
        node.name = node_dict['name']
        for a_child_item in node_dict['children']:
            a_child_node = Node.create_from_dict(a_child_item, parent=node)
            node.children.append(a_child_node)
        return node

    def add_child(self, node):
        self.children.append(node)

    def is_leaf(self):
        if len(self.children) == 0:
            return True
        else:
            return False

    def get_node_path(self):
        cur_node = self
        node_list = []
        while cur_node is not None:
            node_list.insert(0, cur_node.name)
            cur_node = cur_node.parent
        node_path = "/".join(node_list)
        if node_path == "":
            node_path = "/"
        return node_path

    def get_node_type(self):
        if self.parent is None:
            return NodeType.Root

        if self.parent.parent is None:
            return NodeType.Suite

        if len(self.children) > 0:
            return NodeType.Family
        else:
            if self.name.find(":") != -1:
                return NodeType.NonTaskNode
            else:
                return NodeType.Task

    def get_node_type_string(self):
        return NodeType.get_node_type_string(self.get_node_type())

    @staticmethod
    def node_is_valid_from_session(node_path, session):
        # TODO (windroc, 2015.05.15): 何时按照 owner/repo 准备 Record 对象。
        query = session.query(Record).filter(Record.record_fullname == node_path).limit(1).all()
        if len(query) == 0:
            return False
        else:
            return True

    @staticmethod
    def sub_node_is_valid_from_session(node_path, session):
        # NOTE: 花费太长时间，最好由 Spark 任务得到节点树后查找是否有子节点。
        path = node_path+'/'
        query = session.query(Record.record_fullname) \
            .filter("LEFT(record_fullname, {path_length}) = '{path}'".format(path_length=len(path), path=path))\
            .filter("LEFT(record_fullname, {alias_path_length}) != '{alias_path}'".format(
                alias_path_length=len(path+'alias'), alias_path=path+'alias'))\
            .limit(1)
        print query
        query = query.all()
        if len(query) == 0:
            return False
        else:
            return True

    @staticmethod
    def get_node_type_from_session(node_path, session):
        # NOTE：花费时间太长，最好由 Spark 任务得到节点树后再确定节点类型。
        node_type = NodeType.get_node_type_string(NodeType.Unknown)
        if node_path == '/':
            return NodeType.get_node_type_string(NodeType.Root)
        if not node_path.startswith('/'):
            return node_type
        # test whether the node is exists
        if not Node.node_is_valid_from_session(node_path, session):
            return node_type

        if node_path.find('/', 1) == -1:
            return NodeType.get_node_type_string(NodeType.Suite)

        if Node.sub_node_is_valid_from_session(node_path, session):
            return NodeType.get_node_type_string(NodeType.Family)
        else:
            if node_path.find(":") != -1:
                return NodeType.get_node_type_string(NodeType.NonTaskNode)
            else:
                return NodeType.get_node_type_string(NodeType.Task)