# coding: utf-8

try:
    from importlib.metadata import version
    __version__ = version("nwpc-workflow-model")
except Exception:
    __version__ = "unknown"
