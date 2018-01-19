import time
from flask import (
    Flask,
    request,
    url_for,
    redirect,
    make_response,
    render_template,
    jsonify
)
import pickle
import json

app = Flask(__name__)

@app.route("/",  methods=['GET'])
def index():
    resp = make_response(render_template('index.html'), 200)
    return resp

@app.errorhandler(404)
def not_found(error):
    return render_template('error.html'), 404

@app.route("/api/blockchain",  methods=['GET'])
def get_block_chain():

    with open('resources/chain.pkl', 'rb') as file:
        contents = pickle.load(file)

    return json.dumps({"content": contents})
