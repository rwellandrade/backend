from flask import Flask, jsonify, render_template, session, request, redirect, url_for
import db
import app_factory

db.init()
app = Flask(__name__)

def error(status, message):
    return jsonify({'status': status, 'error': True, 'message': message})


@app.route("/v1/<entity_name>", methods=['GET'])
def get(entity_name):
    (success, entities) = db.get(entity_name)
    if not success:
        return error(404, 'Endpoint not found')
    return jsonify(entities)


@app.route("/")
def index():
    return render_template('index.html', my_string="Wheeeee!", my_list=[0, 1, 2, 3, 4, 5])


@app.route("/<entity_name>", methods=['GET'])
def get_list(entity_name):
    (success, entities) = db.get(entity_name)
    if not success:
        return error(404, 'Endpoint not found')
    if len(entities) == 0:
        return error(404, 'empty')
    entity = entities[0]

    return render_template('list.html', data={
        'entity_name': entity_name,
        'entity_title': entity_name,
        'col_headers': list(entity.keys()),
        'entities': [list(ent.values()) for ent in entities],
    })

@app.route("/<entity_name>/edit", methods=['GET'])
def edit(entity_name):
    (success, entities) = db.get(entity_name)
    return error(404, 'Endpoint did found!')

@app.route("/<entity_name>/remove/<id>", methods=['GET'])
def remove(entity_name, id):
    (success, entities) = db.delete(entity_name, id)
    return redirect('/' + entity_name)

@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return render_template('login.html')


@app.route("/logout")
def logout():
    return redirect('/')


if __name__ == '__main__':
    app_factory.create_app(app)
