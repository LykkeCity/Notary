"""
example how to send from one brainwallet to another

13TZJXS5w6NoFUn9vwDJgMBDnTh2CQAz8Y
15mfUNVsf1WUAbgvv5NfWsAbGheyHt5M3L
"""

import os, sys, inspect

#ackward path import
#http://stackoverflow.com/questions/279237/import-a-module-from-a-relative-path
# realpath() will make your script run, even if you symlink it :)
cmd_folder = os.path.realpath(os.path.abspath(os.path.split(inspect.getfile( inspect.currentframe() ))[0]))
if cmd_folder not in sys.path:
    sys.path.insert(0, cmd_folder)

# use this if you want to include modules from a subfolder
subf = "pybitcoin"
cmd_subfolder = os.path.realpath(os.path.abspath(os.path.join(os.path.split(inspect.getfile( inspect.currentframe() ))[0], subf )))
if cmd_subfolder not in sys.path:
    sys.path.insert(0, cmd_subfolder)
#end ackward path import

import bitcoin
import bitcoin.main
import bitcoin.bci


#from bitcoin import *
#import hashlib
#print bitcoin
from sendtx import *

fee = 10000

def getwallet(password):
    """ simple brainwallet structure """
    priv = bitcoin.main.sha256(password)
    pub = bitcoin.main.privtopub(priv)
    addr = bitcoin.main.pubtoaddr(pub)
    h = bitcoin.bci.history(addr)
    unspent = bitcoin.bci.bci_unspent(addr)
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
    #print_balance()
    wallet1 = getwallet('Lykkex1')
    wallet2 = getwallet('Lykkex2')
    wallet3 = getwallet('Lykkex3')
    sendbtc(wallet1, wallet3)

    #print wallet3
