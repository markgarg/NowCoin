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

from functions import (
    read_data,
    add_transaction_to_block_chain,
)
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

    chain = read_data("resources/chain.pkl")
    return json.dumps({"BlockChain": chain})

@app.route("/api/newTransaction",  methods=['POST'])
def add_new_transaction():

    tkn = {u'Alice': -10, u'Sky': 10}

    state = read_data("resources/state.pkl")
    chain = read_data("resources/chain.pkl")

    response = add_transaction_to_block_chain(tkn, state, chain)

    if not response: 
        return "Failed"
    get_block_chain()
