#!/usr/bin/env python
# coding=utf-8
"""
Alembic 中使用的 Model，models.py 中仅定义通用的记录表 Record，只对应某个 SMS Server，在使用时通过修改 __tablename__ 属性，
改变对象的映射关系，达到用一个类对应多个表的目的。
但使用 Alembic 创建表时，需要列出所有的表，所以在本模块中增加各个 SMS Server 对应的 Record 表。

后续需要修改多个相同结构表的实现方式，比如：
1. 在需要时动态生成
2. 在 Alembic 中使用单一类表示所有结构相同的表
"""

from .models import Model, RecordBase


class RecordNwpQuCma20n03(RecordBase, Model):
    __tablename__ = "record_nwp_qu_cma20n03"

    def __init__(self):
        pass

    def __repr__(self):
        return "<RecordNwpQuCma20n03(id={record_id}, string='{record_string}'".format(
            record_id=self.record_id,
            record_string=self.record_string.strip()
        )

    def columns(self):
        return [c.name for c in self.__table__.columns]

    def to_dict(self):
        return dict([(c, getattr(self, c)) for c in self.columns()])


class RecordNwpQuCma18n03(RecordBase, Model):
    __tablename__ = "record_nwp_qu_cma18n03"

    def __init__(self):
        pass

    def __repr__(self):
        return "<RecordNwpQuCma18n03(id={record_id}, string='{record_string}'".format(
            record_id=self.record_id,
            record_string=self.record_string.strip()
        )

    def columns(self):
        return [c.name for c in self.__table__.columns]

    def to_dict(self):
        return dict([(c, getattr(self, c)) for c in self.columns()])


class RecordNwpPdCma20n03(RecordBase, Model):
    __tablename__ = "record_nwp_pd_cma20n03"

    def __init__(self):
        pass

    def __repr__(self):
        return "<RecordNwpPdCma20n03(id={record_id}, string='{record_string}'".format(
            record_id=self.record_id,
            record_string=self.record_string.strip()
        )

    def columns(self):
        return [c.name for c in self.__table__.columns]

    def to_dict(self):
        return dict([(c, getattr(self, c)) for c in self.columns()])


class RecordNwpSpCma20n03(RecordBase, Model):
    __tablename__ = "record_nwp_sp_cma20n03"

    def __init__(self):
        pass

    def __repr__(self):
        return "<RecordNwpPdCma20n03(id={record_id}, string='{record_string}'".format(
            record_id=self.record_id,
            record_string=self.record_string.strip()
        )

    def columns(self):
        return [c.name for c in self.__table__.columns]

    def to_dict(self):
        return dict([(c, getattr(self, c)) for c in self.columns()])


class RecordNwpVfyCma18n01(RecordBase, Model):
    __tablename__ = "record_nwp_vfy_cma18n01"

    def __init__(self):
        pass

    def __repr__(self):
        return "<RecordNwpVfyCma18n01(id={record_id}, string='{record_string}'".format(
            record_id=self.record_id,
            record_string=self.record_string.strip()
        )

    def columns(self):
        return [c.name for c in self.__table__.columns]

    def to_dict(self):
        return dict([(c, getattr(self, c)) for c in self.columns()])