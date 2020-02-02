# coding=utf-8
from nwpc_workflow_model.node_type import NodeType
from nwpc_workflow_model.node_status import NodeStatus


class Node(object):
    """Node class.

    Attributes
    ----------
    name: str
        node name
    status: NodeStatus
        node status.
    parent: Node
        parent node
    children: list(Node)
        list of children nodes
    """
    def __init__(
            self,
            name="",
            status=NodeStatus.Unknown.value
    ):
        """

        Parameters
        ----------
        name: str
            node name
        status: str
            node status value.
        """
        self.parent = None
        self.children = list()
        self.name = name
        self.status = NodeStatus.get_node_status(status)

    def __str__(self):
        return self.get_node_path()

    def to_dict(
            self,
            include_path=True,
            include_status=True,
            include_empty_children=True,
    ) -> dict:
        """Convert to dict.

        Parameters
        ----------
        include_path: bool
            result contain `path` key if True.
        include_status: bool
            result contains `status` key if True.
        include_empty_children: bool
            result contains empty `children` key if True.

        Returns
        -------
        dict
            a dict represented Node.
            {
                'name': str, node name,
                'node_type': str, node type,
                'path': str, node path,
                'status': str, node status,
                'children': array, [
                    node dict,
                    node dict,
                    ...
                ]

            }

            node dict schema:
            {
                "name": "node",
                "type": "record",
                "fields": [
                    {"name": "name", "type": "string"},
                    {"name": "status", "type": "string"},
                    {"name": "path", "type": "string"},
                    {
                        "name": "children",
                        "type": "array",
                        "items": {"type":"node"}
                    }
                ]
            }
        """
        ret = dict()
        ret['name'] = self.name
        ret['node_type'] = self.get_node_type().value

        if include_path:
            ret['path'] = self.get_node_path()
        if include_status:
            ret['status'] = self.status.value

        if len(self.children) and not include_empty_children:
            return ret

        ret['children'] = list()
        for a_child in self.children:
            ret['children'].append(a_child.to_dict())
        return ret

    @classmethod
    def create_from_dict(
            cls,
            node_dict: dict,
            parent=None
    ):
        """Create `Node` from `dict` object.

        Notes
        -----
        use parent is evil.

        Parameters
        ----------
        node_dict: dict
            dict of node. See `to_dict` for dict schema.
        parent: Node
            parent node.

        Returns
        -------
        Node
        """
        node = Node()
        node.parent = parent
        node.name = node_dict['name']
        node.status = NodeStatus.get_node_status(node_dict.get("status", NodeStatus.Unknown))

        node.children = []
        for a_child_item in node_dict.get("children", []):
            a_child_node = Node.create_from_dict(a_child_item, parent=node)
            node.children.append(a_child_node)
        return node

    def add_child(self, node):
        self.children.append(node)
        node.parent = self

    def get_node_path(self) -> str:
        cur_node = self
        node_list = []
        while cur_node is not None:
            node_list.insert(0, cur_node.name)
            cur_node = cur_node.parent
        node_path = "/".join(node_list)
        if node_path == "":
            node_path = "/"
        return node_path

    def get_node_type(self) -> NodeType:
        if self.parent is None:
            return NodeType.Root

        if self.parent.parent is None:
            return NodeType.Suite

        if len(self.children) > 0:
            if self.children[0].is_alias():
                return NodeType.Task
            else:
                return NodeType.Family
        else:
            if self.name.find(":") != -1:
                return NodeType.NonTaskNode
            else:
                if self.is_alias():
                    return NodeType.Alias
                else:
                    return NodeType.Task

    def get_node_type_string(self) -> str:
        return NodeType.get_node_type_string(self.get_node_type())

    def is_leaf(self) -> bool:
        if len(self.children) == 0:
            return True
        else:
            # check whether child is an alias
            alias_flag = False
            for a_child in self.children:
                if a_child.is_alias():
                    alias_flag = True
                    break
            if alias_flag:
                return True
            else:
                return False

    def is_suite(self) -> bool:
        if self.parent:
            parent = self.parent
            if parent.parent is None:
                return True
        return False

    def is_alias(self) -> bool:
        if len(self.children) != 0:
            return False

        if self.name.startswith('alias'):
            return True

        return False
