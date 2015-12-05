"""
example how to send from one brainwallet to another

Lykkex1
['16f9c43035061fda0fd54817d0ce075eaeec0cc6ba1e4e3ff207fbc847b3afd0',
'0435baa6822c6ad593cd33d1f33bca15f4ba0ad8fcc2369d7c1b541e4a05e6e5cb2b10a1fd6d85c6840e2b8f951c600a2ab5f147c5b5e312ad03543ed930a3fda5',
'13TZJXS5w6NoFUn9vwDJgMBDnTh2CQAz8Y',
[{'output': u'e4cce6e5cf0b2c3a0b95b8ff124a900757861b3ac722844aa6eab968935d0b97:0', 'block_height': 386667, 'value': 100000, 'address': u'13TZJXS5w6NoFUn9vwDJgMBDnTh2CQAz8Y'}]]

Lykkex2
['d270c73975a23dcb4e0ed24bc5cdce99e24e3689d23952ece15926196b34bdd9',
'04306ebfd54a65f7c43caf4bfc22fa155494160c7cb5df1fd720e16dd30a9716a892574467113afeb605520fb3aa84bfe232f559ca2692713fcb2a6cebc0b16ebe',
'15mfUNVsf1WUAbgvv5NfWsAbGheyHt5M3L',
[{'output': u'9a3797d92202ec53c16c21a600b899fdfab10c1dcecd7a5b1cee89a78d198bcd:0', 'block_height': 386680, 'value': 100000, 'address': u'15mfUNVsf1WUAbgvv5NfWsAbGheyHt5M3L'}]]
"""

from bitcoin import *

def getwallet(pw):
    """ simple wallet structure """
    priv = sha256(pw)
    pub = privtopub(priv)
    addr = pubtoaddr(pub)
    h = history(addr)
    return [priv,pub,addr,h]


wallet1 = getwallet('Lykkex1')
wallet2 = getwallet('Lykkex2')
print 'Lykkex1\n',wallet1
print 'Lykkex2\n',wallet2
