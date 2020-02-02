# coding=utf-8
from enum import Enum


class NodeVariableType(Enum):
    Variable = 'Variable'
    GeneratedVariable = 'generatedVariable'


class NodeVariable(object):
    def __init__(self, variable_type: NodeVariableType or str, name: str, value: object):
        self.variable_type = NodeVariableType(variable_type)
        self.name = name
        self.value = value

    def to_dict(self) -> dict:
        return {
            'name': self.name,
            'variable_type': self.variable_type.value,
            'value': self.value
        }

    @classmethod
    def create_from_dict(cls, var_dict: dict):
        var = NodeVariable(var_dict['variable_type'], var_dict['name'], var_dict['value'])
        return var
