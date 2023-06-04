#!/usr/bin/env python
# -*- coding:utf-8 -*-
# vim: ft=python ts=4 sw=4 tw=78 expandtab
# ----------------------------------------------------------------------------
# - file : merging_multiple_dictionaries.py
# - author : yc0325lee
# - created : 2023-05-10 20:19:21 by yc032
# - modified : 2023-05-10 20:19:21 by yc032
# - description : 
# ----------------------------------------------------------------------------
import random; random.seed(1729)
import pprint

def gen_dict(count=10, keylen=5):
    table = dict()
    for i in range(count):
        key = ''.join(chr(random.randint(ord('a'), ord('z'))) for _ in range(keylen))
        val = random.randint(10, 99)
        table[key] = val
    return table
        
if False:
    # - random dict generation
    d1 = gen_dict(5)
    d2 = gen_dict(5)
    print("\nd1=", d1)
    print("d2=", d2)

d1= {'dwzca': 50, 'cwjxm': 91, 'iexon': 75, 'ymnae': 57, 'gisnx': 36}
d2= {'bsyrc': 34, 'swqid': 57, 'uqubh': 78, 'pfsxn': 30, 'spiea': 98}
print("\nd1=", d1)
print("d2=", d2)


if False:
    # -------------------------------------
    # 1) crude(brute-force) way
    combined = dict()
    for key, val in d1.items():
        combined[key] = val
    for key, val in d2.items():
        combined[key] = val

    print("\ncombined=", len(combined))
    pprint.pprint(combined)
    # combined= 10
    # {'bsyrc': 34,
    #  'cwjxm': 91,
    #  'dwzca': 50,
    #  'gisnx': 36,
    #  'iexon': 75,
    #  'pfsxn': 30,
    #  'spiea': 98,
    #  'swqid': 57,
    #  'uqubh': 78,
    #  'ymnae': 57}


if False:
    # -------------------------------------
    # 2) using itertools.chain()
    import itertools
    combined = dict()
    for key, val in itertools.chain(d1.items(), d2.items()):
        combined[key] = val

    print("\ncombined=", len(combined))
    pprint.pprint(combined)
    # combined= 10
    # {'bsyrc': 34,
    #  'cwjxm': 91,
    #  'dwzca': 50,
    #  'gisnx': 36,
    #  'iexon': 75,
    #  'pfsxn': 30,
    #  'spiea': 98,
    #  'swqid': 57,
    #  'uqubh': 78,
    #  'ymnae': 57}


if False:
    # -------------------------------------
    # 3) using dict.update() method
    # - update([other])
    # ; update the dictionary with the key/value pairs from other,
    #   overwriting existing keys. return none.
    combined = d1.copy() # shallow copy
    combined.update(d2)

    print("\ncombined=", len(combined))
    pprint.pprint(combined)
    # combined= 10
    # {'bsyrc': 34,
    #  'cwjxm': 91,
    #  'dwzca': 50,
    #  'gisnx': 36,
    #  'iexon': 75,
    #  'pfsxn': 30,
    #  'spiea': 98,
    #  'swqid': 57,
    #  'uqubh': 78,
    #  'ymnae': 57}


if False:
    # -------------------------------------
    # 4) using unpacking operator **
    combined = { **d1, **d2 }

    print("\ncombined=", len(combined))
    pprint.pprint(combined)
    # combined= 10
    # {'bsyrc': 34,
    #  'cwjxm': 91,
    #  'dwzca': 50,
    #  'gisnx': 36,
    #  'iexon': 75,
    #  'pfsxn': 30,
    #  'spiea': 98,
    #  'swqid': 57,
    #  'uqubh': 78,
    #  'ymnae': 57}


if False:
    # -------------------------------------
    # 5) using collections.ChainMap
    # - class collections.ChainMap(*maps)
    # ; a ChainMap groups multiple dicts or other mappings together to create
    #   a single, updateable view.
    import collections
    combined = dict(collections.ChainMap(d1, d2))
    #               ----------------------------
    #                     ChainMap object

    print("\ncombined=", len(combined))
    pprint.pprint(combined)
    # combined= 10
    # {'bsyrc': 34,
    #  'cwjxm': 91,
    #  'dwzca': 50,
    #  'gisnx': 36,
    #  'iexon': 75,
    #  'pfsxn': 30,
    #  'spiea': 98,
    #  'swqid': 57,
    #  'uqubh': 78,
    #  'ymnae': 57}


if False:
    # -------------------------------------
    # 5) unpacking the 2nd dict
    # ; works only when the key of 2nd dict are string!
    combined = dict(d1, **d2)

    print("\ncombined=", len(combined))
    pprint.pprint(combined)
    # combined= 10
    # {'bsyrc': 34,
    #  'cwjxm': 91,
    #  'dwzca': 50,
    #  'gisnx': 36,
    #  'iexon': 75,
    #  'pfsxn': 30,
    #  'spiea': 98,
    #  'swqid': 57,
    #  'uqubh': 78,
    #  'ymnae': 57}


if True:
    # -------------------------------------
    # 5) using the merge operator '|' or '|='
    # ; similar to union operation of set
    combined = d1.copy()
    combined |= d2

    print("\ncombined=", len(combined))
    pprint.pprint(combined)
    # combined= 10
    # {'bsyrc': 34,
    #  'cwjxm': 91,
    #  'dwzca': 50,
    #  'gisnx': 36,
    #  'iexon': 75,
    #  'pfsxn': 30,
    #  'spiea': 98,
    #  'swqid': 57,
    #  'uqubh': 78,
    #  'ymnae': 57}
