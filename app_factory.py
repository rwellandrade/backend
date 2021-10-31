from flask import Flask, jsonify, render_template, session, request, redirect, url_for
import db


def create_app(app):
    db.init()
    app.run(host='0.0.0.0', debug=True)
    app.secret_key = b'insert_secret_key'

    return app
