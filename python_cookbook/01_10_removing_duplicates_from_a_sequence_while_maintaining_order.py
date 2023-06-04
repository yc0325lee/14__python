#!/usr/bin/env python
# -*- coding:utf-8 -*-
# vim: ft=python ts=4 sw=4 tw=78 expandtab
# ----------------------------------------------------------------------------
# - file : 01_10_removing_duplicates_from_a_sequence_while_maintaining_order.py
# - author : yc0325lee
# - created : 2022-11-16 23:37:00 by yc032
# - modified : 2022-11-16 23:37:00 by yc032
# - description : 
# ----------------------------------------------------------------------------

if False:
    # (1) generator function for hashable item
    def siftout_duplicate(items):
        seen = set()
        for item in items:
            if item not in seen:
                yield item
                seen.add(item)
    
    a = [1, 5, 2, 1, 9, 1, 5, 10] # items must be hashable! (here integer)
    print('filtered =', list(siftout_duplicate(a)))



if True:
    # (2) generator function for unhashable item
    # ; key -> a function that converts sequence items into a hashable type
    def siftout_duplicate(items, key=None):
        seen = set()
        for item in items:
            val = item if key is None else key(item)
            if val not in seen:
                yield item
                seen.add(val)
            
    a = [
        {'x':1, 'y':2},
        {'x':1, 'y':3},
        {'x':1, 'y':2},
        {'x':2, 'y':4}
    ]
    print('filtered =', list(siftout_duplicate(a, key=lambda d: (d['x'], d['y']))))
