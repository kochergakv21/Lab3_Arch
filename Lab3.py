from flask import Flask, json, render_template, request, g, jsonify
import operations
import redis


app = Flask(__name__)

@app.route('/')
def index():
    base = redis.StrictRedis(host='localhost', port=6379, db=0)
    all_keys = {}
    keys = base.keys()
    for key in keys:
        data = base.get(key)
        all_keys.update({key: data})
    return render_template('index.html', result=all_keys)


@app.route('/edit')
def update():
    return render_template('edit.html')

@app.route('/remove')
def delete():
    return render_template('delete.html')

@app.route('/add')
def create():
    return render_template('add.html')

@app.route('/read')
def get():
    return render_template('read.html')

@app.route('/api/read/', methods=['POST'])
def read():
    key = request.form['key']
    result = operations.read(key)
    return jsonify(result=result)


@app.route('/api/add/', methods=['POST'])
def add():
    key = request.form['key']
    data = request.form['data']
    result = operations.create(key, data)
    return jsonify(result=result)


@app.route('/api/remove/', methods=['POST'])
def remove():
    key = request.form['key']
    result = operations.delete(key)
    return jsonify(result=result)


@app.route('/api/edit/', methods=['POST'])
def edit():
    key = request.form['key']
    data = request.form['data']
    result = operations.update(key, data)
    return jsonify(result=result)


if __name__ == '__main__':
    app.run(debug=True)
