# vim: ft=python ts=4 sw=4 tw=999 expandtab
# ----------------------------------------------------------------------------
# File : lib__pickle.py
# Description : 
# Author : yc0325lee
# Created : 2021-08-24 23:22:25 by lee2103
# Modified : 2021-08-24 23:22:25 by lee2103
# ----------------------------------------------------------------------------
import pickle

# An arbitrary collection of objects supported by pickle.
data = {
    'a': [1, 2.0, 3, 4+6j],
    'b': ("character string", b"byte string"),
    'c': {None, True, False}
}

print("data=", data)

filename = "lib__pickle.pkl"
print("[info] writing {} ...".format(filename))
with open(filename, "wb") as pklfile: # dumping
    pickle.dump(data, pklfile)

print("[info] reading {} ...".format(filename))
with open(filename, "rb") as pklfile: # re-loading
    data = pickle.load(pklfile)

print("data=", data)
