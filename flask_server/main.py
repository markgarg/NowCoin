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
    save_data,
    add_transaction_to_block_chain,
    isValidTxn
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
    if not request.json:
        abort(400)
    data = request.get_json()

    state = read_data("resources/state.pkl")
    new_txn = create_transaction(data['name'], data['cost'])

    if not isValidTxn(new_txn, state):
        return "Failed"

    chain = read_data("resources/chain.pkl")
    updated_state, update_chain = add_transaction_to_block_chain(new_txn, state, chain)
    
    save_data(updated_chain, "chain.pkl")
    save_data(updated_state, "state.pkl")

    return json.dumps({"BLockChain": chain})

def create_transaction(name, cost):
    return {u'{}'.format(name): cost * -1, u'Sky': cost}
