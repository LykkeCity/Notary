"""
example how to send from one brainwallet to another

13TZJXS5w6NoFUn9vwDJgMBDnTh2CQAz8Y
16f9c43035061fda0fd54817d0ce075eaeec0cc6ba1e4e3ff207fbc847b3afd0

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

import pybitcoin
import pybitcoin.main
import pybitcoin.bci


#from bitcoin import *
#import hashlib
#print bitcoin
from sendtx import *

fee = 10000

def getwallet(password):
    """ simple brainwallet structure """
    priv = pybitcoin.main.sha256(password)
    pub = pybitcoin.main.privtopub(priv)
    addr = pybitcoin.main.pubtoaddr(pub)
    h = pybitcoin.bci.history(addr)
    unspent = pybitcoin.bci.bci_unspent(addr)
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
    print wallet1
    print wallet2
    print wallet3

    #sendselftwo(wallet1)
    #sendbtc(wallet1, wallet2)
    #print wallet1
    #print wallet3
