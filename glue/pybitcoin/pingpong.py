"""
example how to send from one brainwallet to another

13TZJXS5w6NoFUn9vwDJgMBDnTh2CQAz8Y
15mfUNVsf1WUAbgvv5NfWsAbGheyHt5M3L
"""

from bitcoin import *
from send import *

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

def print_balance():
    import time
    while True:
        wallet1 = getwallet('Lykkex1')
        wallet2 = getwallet('Lykkex2')
        print 'Lykkex1 : ',wallet1['addr'], ' ',wallet1['balance']
        print 'Lykkex2 : ',wallet2['addr'], ' ',wallet2['balance']

        time.sleep(10)

def print_wallets():
    wallet1 = getwallet('Lykkex1')
    wallet2 = getwallet('Lykkex2')
    print 'Lykkex1: ',wallet1
    print 'Lykkex2: ',wallet2
    print '========================================'

if __name__ =='__main__':
    print_balance()
    #sendbtc(wallet2, wallet1)
