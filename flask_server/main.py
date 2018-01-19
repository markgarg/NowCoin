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
    isValidTxn,
    create_transaction,
    updateState
)
app = Flask(__name__)

@app.route("/",  methods=['GET'])
def index():
    resp = make_response(render_template('index.html'), 200)
    return resp

@app.route("/users",  methods=['GET'])
def users():
    resp = make_response(render_template('users.html'), 200)
    return resp


@app.errorhandler(404)
def not_found(error):
    return render_template('error.html'), 404

@app.route("/api/latestState",  methods=['GET'])
def get_latest_state():
    state = read_data("resources/state.pkl")
    return json.dumps({"lastestState": state})

@app.route("/api/state/<user>",  methods=['GET'])
def get_individual_state(user):
    state = read_data("resources/state.pkl")

    if user not in state.keys() or user == "Sky": 
        return json.dumps({
            "user": None, 
            "nowCoins" : 0
        })

    return json.dumps({
        "user": user, 
        "nowCoins" : state[user]
    })

@app.route("/api/blockchain",  methods=['GET'])
def get_block_chain():

    chain = read_data("resources/chain.pkl")
    return json.dumps({"blockChain": chain})

@app.route("/api/newTransaction",  methods=['POST'])
def add_new_transaction():

    if not request.json:
        abort(400)
    data = request.get_json()
    print("{}".json.loads(request.data))
    state = read_data("resources/state.pkl")
    new_txn = create_transaction(state, data['name'], data['cost'])

    state = updateState(new_txn, state)
    if not isValidTxn(new_txn, state):
        return "Failed"

    chain = read_data("resources/chain.pkl")
    updated_state, updated_chain = add_transaction_to_block_chain(new_txn, state, chain)
    
    save_data(updated_chain, "chain.pkl")
    save_data(updated_state, "state.pkl")

    return json.dumps({"BLockChain": chain})

