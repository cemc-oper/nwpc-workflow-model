# coding: utf-8
from enum import Enum


class NodeStatus(Enum):
    # for ecFlow
    unknown = 'unknown'
    suspended = 'suspended'
    complete = 'complete'
    queued = 'queued'
    submitted = 'submitted'
    active = 'active'
    aborted = 'aborted'
    # the following three items are server status.
    SHUTDOWN = 'SHUTDOWN'
    HALTED = 'HALTED'
    RUNNING = 'RUNNING'

    # for SMS
    Unknown = 'unk'
    Suspend = 'sus'
    Complete = 'com'
    Queued = 'que'
    Submitted = 'sub'
    Active = 'act'
    Aborted = 'abo'
    Shutdown = 'shu'
    Halted = 'hal'

    @classmethod
    def get_node_status(cls, status: str):
        if status in cls.__members__:
            return NodeStatus[status]
        else:
            node_status = None
            try:
                node_status = NodeStatus(status)
            except ValueError:
                pass
            return node_status
