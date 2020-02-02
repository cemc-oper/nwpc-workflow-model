# coding=utf-8
from nwpc_workflow_model.bunch import Bunch as BaseBunch
from .node import NodeStatus


class Bunch(BaseBunch):
    """
    Node tree for ecFlow
    """
    def __init__(self):
        BaseBunch.__init__(self)
        self.status = NodeStatus.unknown
