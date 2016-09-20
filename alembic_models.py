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