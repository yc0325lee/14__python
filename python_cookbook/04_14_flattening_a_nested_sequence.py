#!/usr/bin/env python
# -*- coding:utf-8 -*-
# vim: ft=python ts=4 sw=4 tw=78 expandtab
# ----------------------------------------------------------------------------
# - file : 04_14_flattening_a_nested_sequence.py
# - author : yc0325lee
# - created : 2022-11-17 23:34:09 by yc032
# - modified : 2022-11-17 23:34:09 by yc032
# - description : 
# ----------------------------------------------------------------------------
import collections.abc

if False:
    # - generator function - recursive
    # using 'yield from'
    def flatten(items, ignore_types=(str, bytes)):
        for x in items:
            if isinstance(x, collections.abc.Iterable) and not isinstance(x, ignore_types):
                yield from flatten(x)
            else:
                yield x
    
    items = [1, 2, [3, 4, [5, 6], 7], 8]
    flattened = list(flatten(items))
    print('items =', items)
    print('flattened =', flattened)
    # items = [1, 2, [3, 4, [5, 6], 7], 8]
    # flattened = [1, 2, <generator object flatten at 0x00000228AF2D1E40>, 8]
    
    # produces 1 2 3 4 5 6 7 8
    for x in flatten(items):
        print(x)
    
    # produces Dave Paula Thomas Lewis
    items = ['Dave', 'Paula', ['Thomas', 'Lewis']]
    for x in flatten(items):
        print(x)


if False:
    # without 'yield from'
    def flatten(items, ignore_types=(str, bytes)):
        for x in items:
            if isinstance(x, collections.abc.Iterable) and not isinstance(x, ignore_types):
                for y in flatten(x):
                    yield y
            else:
                yield x

    items = [1, 2, [3, 4, [5, 6], 7], 8]
    for x in flatten(items):
        print(x)
