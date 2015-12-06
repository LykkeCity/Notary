"""
send tools
"""

from bitcoin import *

fee = 10000

def calc_total(h):
    total = 0
    for x in h:
        v = x['value']
        total += v
    return total

def sendbtc(fromwallet, towallet):
    outs = list()

    unspent = fromwallet['unspent']
    #spend the first output
    inputindex = 1
    print unspent
    spendoutput = unspent[inputindex]
    #print spendoutput

    outval = spendoutput['value'] - fee #totalout
    outs = [{'value': outval, 'address': towallet['addr']}]
    print outs
    tx = mktx(spendoutput,outs)
    signedtx = sign(tx,0,fromwallet['priv'])
    print signedtx
    print bci_pushtx(signedtx)

    #tx = mktx(fromwallet['hist'],outs)
    #TODO: gather all outputs from the address

    """
    for o in bci_unspent(fromwallet):
        print o
        outs.append({'value': o['value'], 'address': toaddr})
    """
    #list of previous outputs as new inputs
    """
    inputindex = 0
    txall = None
    pkey = wallet1['priv']
    for newinput in outs:
        sign(tx,inputindex,pkey)
        inputindex+=1
    """
