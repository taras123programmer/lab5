from flask import Flask
from flask import jsonify

app = Flask(__name__)


@app.route('/')
def hello():
    return jsonify({"message": "Hello, world!"})


@app.route('/add/<int:a>/<int:b>')
def add(a, b):
    return jsonify({"result": a + b})


if __name__ == '__main__':
    app.run(debug=True)
