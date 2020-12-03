from flask import jsonify, request

from src.api import bp


@bp.route('/api/v1/accounting', methods=['POST'])
def put():
    data = request.get_json() or {}
    return jsonify({"message": "not worked route"})


@bp.route('/api/v1/tags', methods=['POST'])
def put_tags():
    data = request.get_json() or {}
    return jsonify({"message": "not worked route"})


@bp.route('/api/v1/accounting', methods=['GET'])
def get_accounting():
    args = request.args
    return jsonify({"message": "not worked route"})


@bp.route('/api/v1/tags', methods=['GET'])
def get_tags():
    args = request.args
    return jsonify({"message": "not worked route"})
