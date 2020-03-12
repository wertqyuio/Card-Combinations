import flask
from flask import jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

hands = {"fruits": ["oranges", "lemons"]}


@app.route('/', methods=['GET'])
def home():
    return "<h1>Backend API--Not an actual website!</h1>"


@app.route('/distributions', methods=['GET'])
def distributions():
    return jsonify(hands)


app.run()
