#!/usr/bin/env python
# -*- coding:utf-8 -*-
# vim: ft=python ts=4 sw=4 tw=78 expandtab
# ----------------------------------------------------------------------------
# - file : 01_06_mapping_keys_to_multiple_values_in_a_dictionary.py
# - author : yc0325lee
# - created : 2022-11-19 20:07:09 by yc032
# - modified : 2022-11-19 20:07:09 by yc032
# - description : 
# ----------------------------------------------------------------------------

if False:
    import collections
    import random
    # using 'collections.defaultdict(list)'
    table = collections.defaultdict(list)
    random.seed(a=int()) # seeding

    for _ in range(100):
        key = chr(random.randint(97, 122))
        val = random.randint(0, 9)
        table[key].append(val)

    for key in sorted(table.keys()):
        print('table[{}] : {}'.format(key, table[key]))
    # --------------------------------
    # table[a] : [2, 7, 7, 2, 9, 3, 1]
    # table[c] : [5, 3, 2, 7, 3]
    # table[d] : [3, 2, 4, 2, 2]
    # table[e] : [0, 6, 6, 8, 7, 5]
    # table[f] : [5, 2, 6]
    # table[g] : [1, 5, 9, 4, 3, 9]
    # table[h] : [0]
    # table[i] : [0, 6, 9, 1]
    # table[j] : [0, 5, 3, 6]
    # table[k] : [7, 3, 8]
    # table[l] : [6, 5, 7, 6, 7, 7]
    # table[m] : [1, 1, 6, 4, 1, 2, 0]
    # table[n] : [4]
    # table[o] : [0, 1, 2]
    # table[p] : [7, 0, 9, 8, 9, 8, 2]
    # table[r] : [3, 9, 8, 6]
    # table[s] : [8, 0, 0]
    # table[t] : [3, 9, 3, 8, 0, 2, 3]
    # table[u] : [3]
    # table[v] : [9, 6, 3]
    # table[w] : [3]
    # table[x] : [6, 3, 4, 3, 8]
    # table[y] : [2, 0]
    # table[z] : [1, 6, 9, 3, 3, 8]
    # --------------------------------

    # testing
    for _ in range(10):
        key = chr(random.randint(97, 122))
        val = random.randint(0, 9)
        if key in table:
            if val in table[key]:
                print('({}, {}) found'.format(key, val))

if False:
    import collections
    import random
    # using 'collections.defaultdict(set)'
    table = collections.defaultdict(set)
    random.seed(a=int()) # seeding

    for _ in range(20):
        key = chr(random.randint(97, 122))
        val = random.randint(0, 9)
        table[key].add(val)

    for key in sorted(table.keys()):
        print('table[{}] : {}'.format(key, table[key]))
    # table[b] : {4}
    # table[d] : {1, 5}
    # table[e] : {4}
    # table[j] : {2}
    # table[m] : {4, 6}
    # table[n] : {5}
    # table[o] : {8}
    # table[p] : {8, 5}
    # table[q] : {2, 7}
    # table[r] : {9, 7}
    # table[s] : {3}
    # table[t] : {3, 4}
    # table[v] : {5}
    # table[y] : {1}

    # testing
    for _ in range(10):
        key = chr(random.randint(97, 122))
        val = random.randint(0, 9)
        if key in table:
            if val in table[key]:
                print('({}, {}) found'.format(key, val))

    # print(table['a']) # this will create new entry!
    # for key in sorted(table.keys()):
    #     print('table[{}] : {}'.format(key, table[key]))
    # [note] if this is not what you want, you have to use dict.setdefault()
    if 'a' in table:
        print(table['a'])


if True:
    import collections
    import random
    random.seed(a=int()) # seeding

    table = dict()
    for _ in range(20):
        key = chr(random.randint(97, 122))
        val = random.randint(0, 9)
        table.setdefault(key, set()).add(val)
        #     ----------------------

    for key in sorted(table.keys()):
        print('table[{}] : {}'.format(key, table[key]))
    # table[b] : {4}
    # table[d] : {1, 5}
    # table[e] : {4}
    # table[j] : {2}
    # table[m] : {4, 6}
    # table[n] : {5}
    # table[o] : {8}
    # table[p] : {8, 5}
    # table[q] : {2, 7}
    # table[r] : {9, 7}
    # table[s] : {3}
    # table[t] : {3, 4}
    # table[v] : {5}
    # table[y] : {1}

    # testing
    for _ in range(10):
        key = chr(random.randint(97, 122))
        val = random.randint(0, 9)
        if key in table:
            if val in table[key]:
                print('({}, {}) found'.format(key, val))

    #print(table['a']) # this won't create new entry!
    # for key in sorted(table.keys()):
    #     print('table[{}] : {}'.format(key, table[key]))
    # [note] if this is not what you want, you have to use dict.setdefault()

    if 'a' in table:
        print(table['a']) # this won't create new entry!



# d = {}
# for key, value in pairs.items():
#     if key not in d:
#         d[key] = []
#     d[key].append(value)
# -> cumbersome!

# d = {}
# for key, value in pairs.items():
#     d.setdefault(key,[]).append(value)
# -> simpler!
