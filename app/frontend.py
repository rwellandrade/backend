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
    (success, form) = resolve_forms(entity_name)
    (success, model) = resolve_entity(entity_name)
    if not success:
        return error(404, 'Endpoint not found')
    entity = model.query.filter_by(id=id).first()
    if entity is None:
        return error(404, entity_name + ' not found for id: ' + str(id))
    if request.method == 'GET':
        f = form(obj=entity)
        return render_template('form.html', form=f, data={
        'entity_name': entity_name,
        'entity_title': entity_name,
        'acion': f"/{entity_name}/edit/{id}"
    })
    f = form(request.form)
    if request.method == 'POST' and f.validate():
        f.populate_obj(entity)
        db.session.commit()
        if not success:
            return error(401, entity)
    return redirect('/' + entity_name)


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
