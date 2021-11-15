from flask import Blueprint, render_template, flash, redirect, url_for, request
from flask import Flask, jsonify, render_template, session, request, redirect, url_for
from flask_nav.elements import Navbar, View, Link
from .crud_entity import resolve_entity, resolve_forms
from .db import db
from .json_encoder import to_json

from .nav import nav

frontend = Blueprint('frontend', __name__)

nav.register_element('frontend_top', Navbar(
    View('Popas Burger', '.index'),
    View('Home', '.index'),
    # View('Debug-Info', 'debug.debug_root'),
    Link('Pedidos', '/carts'),
    Link('Items', '/items'),
    Link('Produtos', '/products')))


# Our index-page just shows a quick explanation. Check out the template
# "templates/index.html" documentation for more details.
@frontend.route('/')
def index():
    return render_template('index.html')


def error(status, message):
    return jsonify({'status': status, 'error': True, 'message': message})


@frontend.route("/<entity_name>", methods=['GET'])
def get_list(entity_name):
    (success, model) = resolve_entity(entity_name)
    if not success:
        return error(404, 'Endpoint not found')
    entities = model.query.all()

    return render_template('list.html', data={
        'entity_name': entity_name,
        'entity_title': entity_name,
        'col_headers': model.HEADERS,
        'entities': entities,
    })


@frontend.route("/<entity_name>/edit/<id>", methods=['GET', 'POST'])
def edit(entity_name, id):
    if request.method == 'GET':
        (success, model) = resolve_forms(entity_name)
        if not success:
            return error(404, 'Endpoint not found')
        f = model()
        print(to_json(f))
        return render_template('form.html', form=f, data={
        'entity_name': entity_name,
        'entity_title': entity_name,
    })
    if request.method == 'POST':
        (success, model) = resolve_entity(entity_name)
        if not success:
            return error(404, 'Endpoint not found')
        (success, entity) = model.edit(id)
        if not success:
            return error(401, entity)
        return redirect('/' + entity_name + '/show/' + id)


@frontend.route("/<entity_name>/show/<id>", methods=['GET'])
def show(entity_name, id):
    (success, model) = resolve_entity(entity_name)
    if not success:
        return error(404, 'Endpoint not found')
    (success, entity) = model.get_single(id)
    if not success:
        return error(404, 'Endpoint not found')
    return render_template('list.html', data={
        'entity_name': model.TABLE_NAME,
        'entity_title': model.TABLE_NAME,
        'col_headers': list(entity.keys()),
        'entity': list(entity.values()),
    })


@frontend.route("/<entity_name>/remove/<id>", methods=['GET'])
def remove(entity_name, id):
    (success, model) = resolve_entity(entity_name)
    if not success:
        return error(404, 'Endpoint not found')
    entity = model.query.filter_by(id=id)
    if entity.first() is None:
        return error(404, entity_name + ' not found for id: ' + str(id))
    entity.delete()
    db.session.commit()
    return redirect('/' + entity_name)


@frontend.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return render_template('login.html')


@frontend.route("/logout")
def logout():
    return redirect('/')
