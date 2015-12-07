import hashlib
from bitcoin.wallet import CBitcoinAddress, CBitcoinSecret

#16f9c43035061fda0fd54817d0ce075eaeec0cc6ba1e4e3ff207fbc847b3afd0
#KwzNZV7uenfCrN1KCr26P85MjKuzzSGWgdrgJxkJfGsxG1ByEjTt

h = hashlib.sha256(b'Lykkex1').digest()
print h
seckey = CBitcoinSecret.from_secret_bytes(h)
print seckey
#txin_scriptPubKey = CScript([OP_DUP, OP_HASH160, Hash160(seckey.pub), OP_EQUALVERIFY, OP_CHECKSIG])
