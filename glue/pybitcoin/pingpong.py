"""
example how to send from one brainwallet to another
"""

from bitcoin import *

def getwallet(pw):
    """ simple wallet structure """
    priv = sha256(pw)
    pub = privtopub(priv)
    addr = pubtoaddr(pub)
    h = history(addr)
    return {'priv':priv, 'pub':pub, 'addr':addr, 'hist':h}


wallet1 = getwallet('Lykkex1')
wallet2 = getwallet('Lykkex2')
print 'Lykkex1\n',wallet1
print 'Lykkex2\n',wallet2

#from wallet1 to wallet2
outs = [{'value': 9000, 'address': wallet2['addr']}]
tx = mktx(wallet1['hist'],outs)
print tx
#sign first input
tx2 = sign(tx,0,wallet1['priv'])
print tx2
print pushtx(tx2)

"""
======
output
======
Lykkex1
{'hist': [{'output': u'e4cce6e5cf0b2c3a0b95b8ff124a900757861b3ac722844aa6eab968935d0b97:0', 'block_height': 386667, 'value': 100000, 'address': u'13TZJXS5w6NoFUn9vwDJgMBDnTh2CQAz8Y'}], 'addr': '13TZJXS5w6NoFUn9vwDJgMBDnTh2CQAz8Y', 'pub': '0435baa6822c6ad593cd33d1f33bca15f4ba0ad8fcc2369d7c1b541e4a05e6e5cb2b10a1fd6d85c6840e2b8f951c600a2ab5f147c5b5e312ad03543ed930a3fda5', 'priv': '16f9c43035061fda0fd54817d0ce075eaeec0cc6ba1e4e3ff207fbc847b3afd0'}
Lykkex2
{'hist': [{'output': u'9a3797d92202ec53c16c21a600b899fdfab10c1dcecd7a5b1cee89a78d198bcd:0', 'block_height': 386680, 'value': 100000, 'address': u'15mfUNVsf1WUAbgvv5NfWsAbGheyHt5M3L'}], 'addr': '15mfUNVsf1WUAbgvv5NfWsAbGheyHt5M3L', 'pub': '04306ebfd54a65f7c43caf4bfc22fa155494160c7cb5df1fd720e16dd30a9716a892574467113afeb605520fb3aa84bfe232f559ca2692713fcb2a6cebc0b16ebe', 'priv': 'd270c73975a23dcb4e0ed24bc5cdce99e24e3689d23952ece15926196b34bdd9'}
0100000001970b5d9368b9eaa64a8422c73a1b865707904a12ffb8950b3a2c0bcfe5e6cce40000000000ffffffff0128230000000000001976a9143452eb91417c48324ce4dfcfb6597ecfdeefc5b488ac00000000
0100000001970b5d9368b9eaa64a8422c73a1b865707904a12ffb8950b3a2c0bcfe5e6cce4000000008a4730440220088b1da7d907eda5e5d1ddabd9cf1b76226a0a656082bf896a66f2a26e9cd80a02201907d6f02325a1a835df644e545eed012f3f6b3304ace75c497f3ad9b15565f801410435baa6822c6ad593cd33d1f33bca15f4ba0ad8fcc2369d7c1b541e4a05e6e5cb2b10a1fd6d85c6840e2b8f951c600a2ab5f147c5b5e312ad03543ed930a3fda5ffffffff0128230000000000001976a9143452eb91417c48324ce4dfcfb6597ecfdeefc5b488ac00000000
Transaction Submitted
"""
