"""
example how to send from one brainwallet to another

13TZJXS5w6NoFUn9vwDJgMBDnTh2CQAz8Y
15mfUNVsf1WUAbgvv5NfWsAbGheyHt5M3L
"""

from bitcoin import *

fee = 10000

def getwallet(password):
    """ simple brainwallet structure """
    priv = sha256(password)
    pub = privtopub(priv)
    addr = pubtoaddr(pub)
    h = history(addr)
    unspent = bci_unspent(addr)
    balance = calc_total(unspent)
    return {'priv':priv, 'pub':pub, 'addr':addr, 'hist':h, 'unspent': unspent, 'balance':balance}

def calc_total(h):
    total = 0
    for x in h:
        v = x['value']
        total += v
    return total

def sendbtc(fromwallet, towallet):
    outs = list()
    fromwallet = wallet1
    towallet = wallet2

    unspent = bci_unspent(fromwallet['addr'])
    #spend the first output
    inputindex = 0
    print unspent
    spendoutput = unspent[inputindex]
    #print spendoutput

    outval = spendoutput['value'] - fee #totalout
    outs = [{'value': outval, 'address': towallet['addr']}]
    print outs
    tx = mktx(spendoutput,outs)
    signedtx = sign(tx,0,fromwallet['priv'])
    print signedtx
    #print bci_pushtx(signedtx)

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


if __name__ =='__main__':
    wallet1 = getwallet('Lykkex1')
    wallet2 = getwallet('Lykkex2')
    #print 'Lykkex1\n',wallet1
    #print 'Lykkex2\n',wallet2
    print '========================================'
    sendbtc(wallet1, wallet2)
