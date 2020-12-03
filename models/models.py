import enum
from typing import Dict, Union, List, Tuple

from src.objects.factory import db


class TypeAccounting(enum.Enum):
    spending = "spending"
    replenishment = "replenishment"

    def __str__(self):
        return str(self)


tags = db.Table('tags',
                db.Column('tag_id', db.Integer, db.ForeignKey('tag.id'), primary_key=True),
                db.Column('accounting_id', db.Integer, db.ForeignKey('accounting.id'), primary_key=True)
                )


class Tag(db.Model):
    __tablename__ = "tag"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name_tag = db.Column(db.String, unique=True, nullable=False)
    description = db.Column(db.String, nullable=False)

    def to_dict(self) -> Dict[str, Union[int, str]]:
        return {
            "id": self.id,
            "name_tag": self.name_tag,
            "description": self.description
        }


class Accounting(db.Model):
    __tablename__ = "accounting"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    data = db.Column(db.DateTime, nullable=False)
    type_accounting = db.Column(db.Enum(TypeAccounting))
    description = db.Column(db.String, nullable=False)
    sum = db.Column(db.Float, nullable=False)
    tags = db.relationship('Tag', secondary=tags, lazy='subquery',
                           backref=db.backref('accounting', lazy=True))

    def to_dict(self) -> Dict[str, Union[int, str, float, List[Tuple[int, str, str]]]]:
        return {
            "id": self.id,
            "data": self.data.strftime("%d-%m-%Y"),
            "type": self.type_accounting.value,
            "description": self.description,
            "sum": self.sum,
            "tags": [(tag.id, tag.name_tag, tag.description) for tag in self.tags]
        }
