"""
>>> from bitcoin import *
>>> priv = sha256('Lykkex1')
>>> priv
'16f9c43035061fda0fd54817d0ce075eaeec0cc6ba1e4e3ff207fbc847b3afd0'
>>> pub = privtopub(priv)
>>> pub
'0435baa6822c6ad593cd33d1f33bca15f4ba0ad8fcc2369d7c1b541e4a05e6e5cb2b10a1fd6d85c6840e2b8f951c600a2ab5f147c5b5e312ad03543ed930a3fda5'
>>> addr = pubtoaddr(pub)
>>> addr
'13TZJXS5w6NoFUn9vwDJgMBDnTh2CQAz8Y'
>>> h = history(addr)
>>> h
[{'output': u'e4cce6e5cf0b2c3a0b95b8ff124a900757861b3ac722844aa6eab968935d0b97:0', 'block_height': 386667, 'value': 100000, 'address': u'13TZJXS5w6NoFUn9vwDJgMBDnTh2CQAz8Y'}]
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
print wallet1
print wallet2
