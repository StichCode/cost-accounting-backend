from flask import jsonify, request
from loguru import logger

from models.models import Accounting, Tag
from src.api import bp
from models.base import put_accounting, put_tag, to_dict_all


@bp.route('/api/v1/accounting', methods=["POST"])
def put():
    data = request.form.to_dict() or {}
    if not data:
        logger.error("backend didn't receive data")
        return jsonify(message="something wrong, where data?"), 400
    response = put_accounting(data)
    if not response:
        logger.exception("ALARM, something wrong, and no data has been added")
        return jsonify(message="something wrong when add new record"), 401
    return jsonify({"message": "ok"}), 200


@bp.route('/api/v1/tags', methods=["POST"])
def put_tags():
    data = request.form.to_dict() or {}
    if not data:
        logger.error("backend didn't receive data")
        return jsonify(message="something wring, where data?"), 400
    response = put_tag(data)
    if not response:
        logger.exception("ALARM, something wrong, and no data has been added")
        return jsonify(message="something wrong when add new record"), 401
    return jsonify({"message": "ok"}), 200


@bp.route('/api/v1/accounting', methods=["GET"])
def get_accounting():
    response = to_dict_all(Accounting)
    if not response:
        logger.exception("ALARM, something wrong, and user received no data")
        return jsonify({"message": "Something wrong when read from database"}), 403
    return jsonify(response), 200


@bp.route('/api/v1/tags', methods=["GET"])
def get_tags():
    response = to_dict_all(Tag)
    if not response:
        logger.exception("ALARM, something wrong, and user received no data")
        return jsonify({"message": "Something wrong when read from database"}), 403
    return jsonify(response), 200
