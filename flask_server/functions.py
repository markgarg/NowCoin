import random
random.seed(0)
import hashlib, json, sys
import pickle

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


def hashMe(msg=""):
    # For convenience, this is a helper function that wraps our hashing algorithm
    if type(msg)!=str:
        msg = json.dumps(msg,sort_keys=True)  # If we don't sort keys, we can't guarantee repeatability!
        
    if sys.version_info.major == 2:
        return unicode(hashlib.sha256(msg).hexdigest(),'utf-8')
    else:
        return hashlib.sha256(str(msg).encode('utf-8')).hexdigest()

def add_transaction_to_block_chain(new_txn, state, chain):
    """Add it to a block chain."""
    # state = updateState(new_txn, state)
    new_block = makeBlock([new_txn], chain)
    chain.append(new_block)

    return state, chain

def makeTransaction(maxValue=40):
    # This will create valid transactions in the range of (1,maxValue)
    amount    = random.randint(1, maxValue)
    alicePays = -1 * amount
    skyPays   = -1 * alicePays
    # By construction, this will always return transactions that respect the conservation of tokens.
    # However, note that we have not done anything to check whether these overdraft an account
    return {u'Alice': alicePays,u'Sky':skyPays}


def updateState(txn, state):
    # Inputs: txn, state: dictionaries keyed with account names, holding numeric values for transfer amount (txn) or account balance (state)
    # Returns: Updated state, with additional users added to state if necessary
    # NOTE: This does not not validate the transaction- just updates the state!
    
    # If the transaction is valid, then update the state
    state = state.copy() # As dictionaries are mutable, let's avoid any confusion by creating a working copy of the data.
    for key in txn:
        if key in state.keys():
            state[key] += txn[key]
        else:
            state[key] = txn[key]
    return state

def create_transaction(state, name, cost):

    '''Creates new dictionary of transaction from incoming json data'''

    txn = {}
    txn[u'{}'.format(name)] = cost * -1
    txn[u'Sky'] = cost

    return txn

def isValidTxn(txn,state):
    # Assume that the transaction is a dictionary keyed by account names

    # Check that the sum of the deposits and withdrawals is 0
    if sum(txn.values()) is not 0:
        print("Values do not add to 0")
        return False
    
    # Check that the transaction does not cause an overdraft
    for key in txn.keys():
        if key in state.keys(): 
            acctBalance = state[key]
        else:
            acctBalance = 0

        # Ensures the user cannot spend if they do no have enough on their balance
        if (acctBalance + txn[key]) < 0: 
            return False
    
    return True


def save_data(data, file_name):
    '''Used primarily to save the blockchain and the latest state as pickle files'''
    with open("resources/{0}".format(file_name), 'wb') as file:
        pickle.dump(data, file)


def read_data(file_name):
    '''Used primarily to read the blockchain and latest state pickle files'''
    with open("{0}".format(file_name), 'rb') as file:
        contents = pickle.load(file)
    return contents