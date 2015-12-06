import os, sys, inspect
# realpath() will make your script run, even if you symlink it :)
cmd_folder = os.path.realpath(os.path.abspath(os.path.split(inspect.getfile( inspect.currentframe() ))[0]))
if cmd_folder not in sys.path:
    sys.path.insert(0, cmd_folder)

# use this if you want to include modules from a subfolder
subf = "pybitcoin"
cmd_subfolder = os.path.realpath(os.path.abspath(os.path.join(os.path.split(inspect.getfile( inspect.currentframe() ))[0], subf )))
if cmd_subfolder not in sys.path:
    sys.path.insert(0, cmd_subfolder)

import bitcoin
print bitcoin

"""
>>> p
'/Users/ben/lykke/Notary/glue/pybitcoin/bitcoin'
>>> sys.path.append(p)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'sys' is not defined
>>> import sys
>>> sys.path.append(p)
>>> import bitcoin
"""
