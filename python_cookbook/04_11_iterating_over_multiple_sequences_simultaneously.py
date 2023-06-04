#!/usr/bin/env python
# -*- coding:utf-8 -*-
# vim: ft=python ts=4 sw=4 tw=78 expandtab
# ----------------------------------------------------------------------------
# - file : 04_11_iterating_over_multiple_sequences_simultaneously.py
# - author : yc0325lee
# - created : 2022-11-17 23:17:25 by yc032
# - modified : 2022-11-17 23:17:25 by yc032
# - description : 
# ----------------------------------------------------------------------------
if False:
    # ----------------------------------------------------------------------
    # - zip(*iterables, strict=False)
    # ; iterate over several iterables in parallel, producing tuples with an
    #   item from each one.
    # ; zip() creates an iterator as a result
    # ; pairing 2 lists with zip()
    # ----------------------------------------------------------------------
    xpts = [1, 5, 4, 2, 10, 7]
    ypts = [101, 78, 37, 15, 62, 99]
    for x, y in zip(xpts, ypts):
        print(x, y)
    # 1 101
    # 5 78
    # 4 37
    # 2 15
    # 10 62
    # 7 99


if False:
    # unbalanced sequences
    a = [1, 2, 3] # shorter
    b = ['w', 'x', 'y', 'z']
    for pair in zip(a, b):
        print(pair) # tuple
    # (1, 'w')
    # (2, 'x')
    # (3, 'y')


if False:
    # ------------------------------------------------------------------------
    # - itertools.zip_longest(*iterables, fillvalue=None)
    # ; make an iterator that aggregates elements from each of the iterables.
    #   if the iterables are of uneven length, missing values are filled-in with
    #   fillvalue. iteration continues until the longest iterable is exhausted.
    # ------------------------------------------------------------------------
    from itertools import zip_longest
    
    a = [1, 2, 3] # shorter
    b = ['w', 'x', 'y', 'z']
    
    print('\n# zip_longest -> None')
    for pair in zip_longest(a, b):
        print(pair)
    # (1, 'w')
    # (2, 'x')
    # (3, 'y')
    # (None, 'z')
    
    print('\n# zip_longest with fillvalue=0')
    for pair in zip_longest(a, b, fillvalue=0):
        print(pair)
    # (1, 'w')
    # (2, 'x')
    # (3, 'y')
    # (0, 'z')

if False:
    # building dict from sequences of keys and values
    headers = ['name', 'shares', 'price']
    values = ['ACME', 100, 490.1]

    lookup = dict(zip(headers, values))
    print('lookup =', lookup)
    # lookup = {'name': 'ACME', 'shares': 100, 'price': 490.1}
