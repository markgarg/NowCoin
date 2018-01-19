import sys, hashlib, random
from pprint import pprint

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

def main():
    txnBuffer = [makeTransaction() for i in range(10)]
    blockSizeLimit = 5

    state = {u'Alice':5,u'Bob':5}
    genesis_block = create_genesis_block(state)

    # Initialising chain
    chain = [genesis_block]

    # Appending new block to chain
    while len(txnBuffer) > 0:
        bufferStartSize = len(txnBuffer)
        
        ## Gather a set of valid transactions for inclusion
        txnList = []
        while (len(txnBuffer) > 0) & (len(txnList) < blockSizeLimit):
            newTxn = txnBuffer.pop()
            validTxn = isValidTxn(newTxn,state) # This will return False if txn is invalid
            
            if validTxn:           # If we got a valid state, not 'False'
                txnList.append(newTxn)
                state = updateState(newTxn,state)
            else:
                print("ignored transaction")
                sys.stdout.flush()
                continue  # This was an invalid transaction; ignore it and move on
            
        ## Make a block
        myBlock = makeBlock(txnList,chain)
        chain.append(myBlock)        


    pprint("0th Element of Chain: \n {}".format(chain[0]))
    pprint("1th Element of Chain: \n {}".format(chain[1]))

    print("State {} : \n".format(state))

    print("Is it possible for {u'Alice': -3, u'Bob': 3}:  " , isValidTxn({u'Alice': -3, u'Bob': 3},state))  # Basic transaction- this works great!
    print("Is it possible for {u'Alice': -3, u'Bob': 3}:  " , isValidTxn({u'Alice': -3, u'Bob': 3},state))  # Basic transaction- this works great!
 


    print("Is it possible for {u'Alice': -3, u'Bob': 1, u'Alan': 2}:  " , isValidTxn({u'Alice': -3, u'Bob': 1, u'Alan': 2},state))  # Basic transaction- this works great!


if __name__ == '__main__':
    main()








































