"""
send tools
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
import pybitcoin.transaction
import pybitcoin.main
import pybitcoin.bci

fee = 10000

def calc_total(h):
    total = 0
    for x in h:
        v = x['value']
        total += v
    return total

def sendself(wallet):
    """send all money from the address to itself"""
    unspent = wallet['unspent']
    print unspent
    inputindex = 0
    spendoutput = unspent[inputindex]
    txval = spendoutput['value']
    outval = txval - fee
    outs = [{'value': outval, 'address': wallet['addr']}]
    tx = pybitcoin.transaction.mktx(spendoutput,outs)
    signedtx = pybitcoin.transaction.sign(tx,0,wallet['priv'])
    print signedtx
    print bitcoin.bci.bci_pushtx(signedtx)

def sendselftwo(wallet):
    """send all money from the address to itself in two tx"""
    unspent = wallet['unspent']
    print unspent
    inputindex = 0
    spendoutput = unspent[inputindex]
    txval = spendoutput['value']
    outval1 = (txval/2) - fee
    outval2 = txval -outval1 - fee
    outs = [{'value': outval1, 'address': wallet['addr']},{'value': outval2, 'address': wallet['addr']}]
    print outs
    tx = pybitcoin.transaction.mktx(spendoutput,outs)
    signedtx = pybitcoin.transaction.sign(tx,0,wallet['priv'])
    print signedtx
    #print bitcoin.bci.bci_pushtx(signedtx)

def sendbtc(fromwallet, towallet):
    outs = list()

    unspent = fromwallet['unspent']
    #spend the first output
    inputindex = 0
    print unspent
    spendoutput = unspent[inputindex]
    #print spendoutput
    totalval = 270000 #spendoutput['value']
    outval = totalval - fee #totalout

    #2outputs . one to other wallet, rest back to itself
    outs = [{'value': outval, 'address': towallet['addr']},
            {'value': totalval - outval - fee, 'address': fromwallet['addr']}]

    print outs
    tx = pybitcoin.transaction.mktx(spendoutput,outs)
    signedtx = pybitcoin.transaction.sign(tx,0,fromwallet['priv'])
    print signedtx
    #print bci_pushtx(signedtx)

    rest = totalval - outval
    print rest

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
