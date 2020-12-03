from flask import jsonify, request
from loguru import logger

from models.models import Accounting, Tag
from src.api import bp


@bp.route('/api/v1/accounting', methods=["POST"])
def put():
    data = request.form.to_dict() or {}
    if not data:
        logger.error("backend didn't receive data")
        return jsonify(message="something wrong, where data?"), 400
    response = Accounting.from_dict(data)
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
    response = Tag.from_dict(data)
    if not response:
        logger.exception("ALARM, something wrong, and no data has been added")
        return jsonify(message="something wrong when add new record"), 401
    return jsonify({"message": "ok"}), 200


@bp.route('/api/v1/accounting', methods=["GET"])
def get_accounting():
    response = Accounting.to_dict_all()
    if not response:
        logger.exception("ALARM, something wrong, and user received no data")
        return jsonify({"message": "Something wrong when read from database"}), 403
    return jsonify(response), 200


@bp.route('/api/v1/tags', methods=["GET"])
def get_tags():
    response = Tag.to_dict_all()
    if not response:
        logger.exception("ALARM, something wrong, and user received no data")
        return jsonify({"message": "Something wrong when read from database"}), 403
    return jsonify(response), 200
