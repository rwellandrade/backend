from flask import Flask, jsonify, request
import json
import urllib.request
import random

app = Flask(__name__)

products = [
    {"id": e, "name": "Produto " + str(e), "description":"Descrição "+str(e), "image":"https://cdn.pixabay.com/photo/2018/01/18/20/42/pencil-3091204_1280.jpg", "category": "Categoria "+str(e)} for e in range(1,11)]

@app.route("/products", methods=['GET'])
def get():
    return jsonify(products)


if __name__ == "__main__":
    app.run(host='0.0.0.0')
