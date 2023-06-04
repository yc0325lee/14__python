#!/usr/bin/env python
# -*- coding:utf-8 -*-
# vim: ft=python ts=4 sw=4 tw=78 expandtab
# ----------------------------------------------------------------------------
# - file : 04_09_iterating_over_all_possible_combinations_or_permutations.py
# - author : yc0325lee
# - created : 2022-11-17 00:09:51 by yc032
# - modified : 2022-11-17 00:15:19 by yc032
# - description : 
# ----------------------------------------------------------------------------

if True:
    from itertools import permutations, combinations, combinations_with_replacement

    items = ['a', 'b', 'c']

    print('\n# permutations(3, 3)')
    for permute in permutations(items):
        print(permute)

    print('\n# permutations(3, 2)')
    for permute in permutations(items, 2):
        print(permute)

    print('\n# combinations(3, 3)')
    for combo in combinations(items, 3):
        print(combo)

    print('\n# combinations(3, 2)')
    for combo in combinations(items, 2):
        print(combo)

    print('\n# combinations_with_replacement(3, 3)')
    for combo in combinations_with_replacement(items, 3):
        print(combo)

    # permutations(3, 3)
    # ('a', 'b', 'c')
    # ('a', 'c', 'b')
    # ('b', 'a', 'c')
    # ('b', 'c', 'a')
    # ('c', 'a', 'b')
    # ('c', 'b', 'a')
    #
    # permutations(3, 2)
    # ('a', 'b')
    # ('a', 'c')
    # ('b', 'a')
    # ('b', 'c')
    # ('c', 'a')
    # ('c', 'b')
    #
    # combinations(3, 3)
    # ('a', 'b', 'c')
    #
    # combinations(3, 2)
    # ('a', 'b')
    # ('a', 'c')
    # ('b', 'c')
    #
    # combinations_with_replacement(3, 3)
    # ('a', 'a', 'a')
    # ('a', 'a', 'b')
    # ('a', 'a', 'c')
    # ('a', 'b', 'b')
    # ('a', 'b', 'c')
    # ('a', 'c', 'c')
    # ('b', 'b', 'b')
    # ('b', 'b', 'c')
    # ('b', 'c', 'c')
    # ('c', 'c', 'c')
