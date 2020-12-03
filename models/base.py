from loguru import logger
from sqlalchemy.exc import IntegrityError

from models.func import get_all, add_instance


class BaseModel(object):

    def to_dict(self):
        data = {}
        for attr, column in self.__mapper__.c.items():
            data[column.key] = getattr(self, attr)
        return data

    @classmethod
    def to_dict_all(cls):
        try:
            return [r.to_dict() for r in get_all(cls)]
        except Exception as ex:
            logger.exception(ex)
            return None

    @classmethod
    def from_dict(cls, data: dict):
        result = {}
        keys = [column.key for _, column in cls.__mapper__.c.items()]
        for field in keys:
            if field == "id":
                continue
            elif field in data:
                result[field] = data[field]
        try:
            add_instance(cls, **result)
        except IntegrityError:
            return False
        return True