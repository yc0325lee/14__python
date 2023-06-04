# vim: ft=python ts=4 sw=4 tw=999 expandtab
# -*- coding:utf-8 -*-
# ----------------------------------------------------------------------------
# - file : data__set_frozenset.py
# - author : yc0325lee
# - created : 2022-10-16 11:23:10 by lee2103
# - modified : 2022-10-16 11:23:10 by lee2103
# - set & frozenset
# ; unordered collection of distinct hashable objects
# ; membership testing, removing duplicates from a sequence
# ; computing mathematical operations
# ; operations
#   -> x in set, x not in set, len(set), for x in set
#   -> intersection, union, difference, and symmetric difference
#   -> left.isdisjoint(right)
#   -> left <= right, left < right
#   -> left >= right, left > right
#   -> left | right, left.union(*right)
#   -> left & right, left.intersection(*right)
#   -> left - right, left.difference(*right)
#   -> left ^ right, left.symmetric_difference(right)
#
# - set
# ; mutable operation allowed
#   +---------------+-----------------------------------------------------+
#   | operation     | description                                         |
#   +---------------+-----------------------------------------------------+
#   | add(elem)     | add element elem to the set                         |
#   | remove(elem)  | remove element elem from the set                    |
#   |               | raises KeyError if elem is not contained in the set |
#   | discard(elem) | remove element elem from the set if it is present   |
#   | pop()         | remove and return an arbitrary element from the set |
#   |               | raises KeyError if the set is empty                 |
#   | clear()       | remove all elements from the set                    |
#   +---------------+-----------------------------------------------------+
# ; not hashable
#
# - frozenset
# ; immutable and hashable
# ; only immutable operations are allowed
# ----------------------------------------------------------------------------
if False:
    # - building set or fronzenset
    # s = {0, 1, 2, 3, 4}
    # s = set() --> empty set!
    #
    # frozen = frozenset(range(10))
    pass

if False:
    import random
    import pprint
    chars = [chr(n) for n in range(65, 91, 1)]
    print("chars=")
    pprint.pprint(chars)
    # char=
    # ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
    #  'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
    #  'U', 'V', 'W', 'X', 'Y', 'Z']

    l = [chars[random.randint(0, len(chars)-1)] for _ in range(100)]
    print("list=", len(l))
    pprint.pprint(l)
    # list= 100
    # ['N', 'I', 'K', 'V', 'R', 'P', 'A', 'L', 'I', 'M',
    #  'K', 'C', 'B', 'G', 'D', 'M', 'T', 'Z', 'B', 'M',
    #  'W', 'J', 'A', 'G', 'T', 'M', 'I', 'S', 'M', 'F',
    #  'J', 'M', 'Q', 'V', 'D', 'B', 'C', 'Q', 'T', 'S',
    #  'W', 'D', 'U', 'I', 'Z', 'C', 'V', 'V', 'Z', 'X',
    #  'C', 'T', 'L', 'I', 'Y', 'Z', 'Z', 'T', 'K', 'S',
    #  'L', 'K', 'Y', 'O', 'K', 'Y', 'O', 'H', 'Z', 'T',
    #  'I', 'O', 'X', 'H', 'Y', 'Q', 'J', 'R', 'D', 'B',
    #  'Y', 'O', 'N', 'X', 'A', 'Y', 'R', 'V', 'Z', 'V',
    #  'L', 'P', 'X', 'O', 'S', 'N', 'I', 'H', 'B', 'R']

    s = set(l)
    print("set=", len(s))
    pprint.pprint(s)
    # set= 26
    # {'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
    #  'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
    #  'U', 'V', 'W', 'X', 'Y', 'Z'}

    # if order is important, dict.fromkeys() should be used!
    unique_ordered = dict.fromkeys(l).keys()
    print("unique_ordered=", len(unique_ordered))
    pprint.pprint(unique_ordered)
    # unique_ordered= 26
    # dict_keys([
    #     'S', 'E', 'V', 'H', 'W', 'U', 'F', 'Z', 'Y', 'D',
    #     'A', 'B', 'M', 'P', 'J', 'Q', 'K', 'L', 'T', 'C',
    #     'O' , 'I', 'X', 'N', 'R', 'G'
    # ])

if False:
    a = set([0, 1, 2, 3, 4])
    b = set([3, 4, 5, 6, 7])
    print("a =", a)
    print("b =", b)
    print("a | b =", a | b) # a | b = {0, 1, 2, 3, 4, 5, 6, 7}
    print("a & b =", a & b) # a & b = {3, 4}
    print("a - b =", a - b) # a - b = {0, 1, 2}
    print("a ^ b =", a ^ b) # a ^ b = {0, 1, 2, 5, 6, 7}


