#!/usr/bin/env python
# -*- coding:utf-8 -*-
# vim: ft=python ts=4 sw=4 tw=78 expandtab
# ----------------------------------------------------------------------------
# - file : 04_12_iterating_on_items_in_separate_containers.py
# - author : yc0325lee
# - created : 2022-11-17 23:28:34 by yc032
# - modified : 2022-11-17 23:28:34 by yc032
# - description : 
# ----------------------------------------------------------------------------
if False:
    # - itertools.chain(*iterables)
    #   itertools.chain(iterable0, iterable1, iterable2, ...)
    # ; make an iterator that returns elements from the first iterable until
    #   it is exhausted, then proceeds to the next iterable, until all of the
    #   iterables are exhausted.
    import itertools
    a = [1, 2, 3, 4]
    b = ['x', 'y', 'z']

    for x in itertools.chain(a, b):
        print(x)

    # inefficent
    for x in a + b:
        print(x)

    # better
    for x in chain(a, b):
        print(x)


if False:
    # various working sets of items
    active_items = set()
    inactive_items = set()
    
    # Iterate over all items
    for item in itertools.chain(active_items, inactive_items):
        print(item)
