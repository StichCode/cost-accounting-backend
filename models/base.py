import ast
from typing import List

from loguru import logger

from models.func import get_one_by_id, add_instance, get_all
from models.models import Accounting, Tag
from src.objects.factory import db


def to_dict_all(model):
    try:
        return [r.to_dict() for r in get_all(model)]
    except Exception as ex:
        logger.exception(ex)
        return None


def put_accounting(data) -> bool:
    _tags = _get_tags(ast.literal_eval(data["tags"]))
    _acc = {
        "data": data["data"],
        "type_accounting": data["type_accounting"],
        "description": data["description"],
        "sum": data["sum"]
    }
    logger.debug("Insert a new record \n{}".format(_acc))
    try:
        acc = Accounting(**_acc)
        [acc.tags.append(t) for t in _tags]  # добавляем теги при связи M2M
        db.session.add(acc)
        db.session.commit()
    except Exception as ex:
        logger.exception(ex)
        return False
    return True


def _get_tags(tags_id: List[int]) -> List[Tag]:
    return [get_one_by_id(Tag, tag) for tag in tags_id]


def put_tag(data) -> bool:
    _tag = {
        "name_tag": data["name_tag"],
        "description": data["description"]
    }
    logger.debug("Insert a new record \n{}".format(_tag))
    try:
        add_instance(Tag, **_tag)
    except Exception as ex:
        logger.exception(ex)
        return False
    return True
