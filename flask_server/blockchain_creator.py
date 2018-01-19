import sys, hashlib, random
from pprint import pprint
import pickle

from functions import (
    isValidTxn,
    makeTransaction,
    hashMe,
    updateState,
    create_genesis_block,
    add_transaction_to_block_chain,
    save_data
)


def main():
    txnBuffer = [makeTransaction() for i in range(3)]

    state = {
        u'Sky': 0,
        u'Alice': 200,
        u'Bob': 130,
        u'Charlie': 40 
    }
    genesis_block = create_genesis_block(state)

    chain = [genesis_block]

    save_data(chain, "chain.pkl")
    save_data(state, "state.pkl")

    # Save chain 
    # pprint("0th Element of Chain: \n {}".format(chain[0]))
    # pprint("1th Element of Chain: \n {}".format(chain[1]))

    # print("State {} : \n".format(state))

    # print("Is it possible for {u'Alice': -3, u'Bob': 3}:  " , isValidTxn({u'Alice': -3, u'Bob': 3},state))  # Basic transaction- this works great!
    # print("Is it possible for {u'Alice': -3, u'Bob': 3}:  " , isValidTxn({u'Alice': -3, u'Bob': 3},state))  # Basic transaction- this works great!
    # print("Is it possible for {u'Alice': -3, u'Bob': 1, u'Alan': 2}:  " , isValidTxn({u'Alice': -3, u'Bob': 1, u'Alan': 2},state))  # Basic transaction- this works great!


if __name__ == '__main__':
    main()








































