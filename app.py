from flask import Flask, jsonify, request
import db

app = Flask(__name__)

products = [
    {"id": e, "name": "Produto " + str(e), "description":"Descrição "+str(e), "image":"https://cdn.pixabay.com/photo/2018/01/18/20/42/pencil-3091204_1280.jpg", "category": "Categoria "+str(e)} for e in range(1,11)]

def error(status, message):
    return jsonify({'status': status, 'error': True, 'message': message})

@app.route("/v1/<entity_name>", methods=['GET'])
def get(entity_name):
    (success, entities) = db.get(entity_name)
    if not success:
        return error(404, 'Endpoint not found')
    return jsonify(entities)

db.init()
if __name__ == "__main__":
    app.run(host='0.0.0.0')
