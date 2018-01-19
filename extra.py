import sys, hashlib, random
from pprint import pprint
import pickle

from functions import (
    isValidTxn,
    makeTransaction,
    hashMe,
    updateState
)

def create_genesis_block(initial_state): 
    genesisBlockTxns = [initial_state]
    genesisBlockContents = {u'blockNumber':0,u'parentHash':None,u'txnCount':1,u'txns':genesisBlockTxns}
    genesisHash = hashMe( genesisBlockContents )
    return {u'hash':genesisHash,u'contents':genesisBlockContents} # Genesis Block


def makeBlock(txns,chain):
    parentBlock = chain[-1]
    parentHash  = parentBlock[u'hash']
    blockNumber = parentBlock[u'contents'][u'blockNumber'] + 1
    txnCount    = len(txns)
    blockContents = {u'blockNumber':blockNumber,u'parentHash':parentHash,
                     u'txnCount':len(txns),'txns':txns}
    blockHash = hashMe( blockContents )
    block = {u'hash':blockHash,u'contents':blockContents}
    
    return block


# def add_transaction_to_block_chain(new_txn):
#     """Validate incoming transaction and add it to a block chain."""
#     state = read_data("resources/state.pkl")
#     if isValidTxn(new_txn, state):
#         state = updateState(new_txn, state)
#         chain = read_data("resources/chain.pkl")
#         new_block = makeBlock([new_txn], chain)
#         chain.append(new_block)
#         save_data(chain, "chain.pkl")
#         save_data(state, "state.pkl")
#         return True
#     else:
#         return False

def add_transaction_to_block_chain(new_txn, state, chain):
    """Add it to a block chain."""
    state = updateState(new_txn, state)
    new_block = makeBlock([new_txn], chain)
    chain.append(new_block)

    return state, chain


def save_data(data, file_name):
    with open("resources/{0}".format(file_name), 'wb') as file:
        pickle.dump(data, file)


def read_data(file_name):
    with open("{0}".format(file_name), 'rb') as file:
        contents = pickle.load(file)
    return contents


def main():
    txnBuffer = [makeTransaction() for i in range(3)]

    state = {u'Alice': 40, u'Sky': 600}
    genesis_block = create_genesis_block(state)

    chain = [genesis_block]

    add_transaction_to_block_chain(txnBuffer[0], state, chain)

    # Save chain 
    # pprint("0th Element of Chain: \n {}".format(chain[0]))
    # pprint("1th Element of Chain: \n {}".format(chain[1]))

    # print("State {} : \n".format(state))

    # print("Is it possible for {u'Alice': -3, u'Bob': 3}:  " , isValidTxn({u'Alice': -3, u'Bob': 3},state))  # Basic transaction- this works great!
    # print("Is it possible for {u'Alice': -3, u'Bob': 3}:  " , isValidTxn({u'Alice': -3, u'Bob': 3},state))  # Basic transaction- this works great!
    # print("Is it possible for {u'Alice': -3, u'Bob': 1, u'Alan': 2}:  " , isValidTxn({u'Alice': -3, u'Bob': 1, u'Alan': 2},state))  # Basic transaction- this works great!


if __name__ == '__main__':
    main()








































