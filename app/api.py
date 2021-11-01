from flask import Blueprint, jsonify
from . import db

api = Blueprint('api', __name__)

def error(status, message):
    return jsonify({'status': status, 'error': True, 'message': message})


@api.route("/v1/<entity_name>", methods=['GET'])
def get(entity_name):
    (success, entities) = db.get(entity_name)
    if not success:
        return error(404, 'Endpoint not found')
    return jsonify(entities)
