import flask
from flask import jsonify
from flask_sqlalchemy import SQLAlchemy

app = flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/combinations'
SQLALCHEMY_TRACK_MODIFICATIONS = True
db = SQLAlchemy(app)


def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


@app.route('/', methods=['GET'])
def home():
    return "<h1>Backend API--Not an actual website!</h1>"


@app.route('/distributions', methods=['GET'])
def distributions():
    return jsonify({"test"})


app.run()
