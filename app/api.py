from flask import Blueprint, jsonify
from . import db
from .json_encoder import to_json
from .crud_entity import resolve_entity

api = Blueprint('api', __name__)

def error(status, message):
    return jsonify({'status': status, 'error': True, 'message': message})


@api.route("/v1/<entity_name>", methods=['GET'])
def get(entity_name):
    (success, model) = resolve_entity(entity_name)
    if not success:
        return error(404, 'Endpoint not found')
    entities = model.query.all()
    return to_json(entities)
