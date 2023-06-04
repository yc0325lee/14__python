#!/usr/bin/env python
# -*- coding:utf-8 -*-
# vim: ft=python ts=4 sw=4 tw=78 expandtab
# ----------------------------------------------------------------------------
# - file : 01_07_keeping_dictionaries_in_order.py
# - author : yc0325lee
# - created : 2022-11-19 21:20:26 by yc032
# - modified : 2022-11-19 21:20:26 by yc032
# - description : 
# ----------------------------------------------------------------------------
import collections
import random

if False:
    # - regular dictionary
    table = dict()
    for val in range(20):
        key = ''
        for _ in range(3):
            key += chr(random.randint(97, 122))
        table[key] = val


    print(table)

    while table:
        key, val = table.popitem()
        print('key= {}, val= {}'.format(key, val))


if True:
    #-------------------------------------------------------------------------
    # - class collections.OrderedDict([items])
    # ; return an instance of a dict subclass that has methods specialized for
    #   rearranging dictionary order.
    # - popitem(last=True)
    # ; the popitem() method for ordered dictionaries returns and removes a
    #   (key, value) pair. the pairs are returned in lifo order if last is true
    #   or fifo order if false.
    #-------------------------------------------------------------------------
    table = collections.OrderedDict()
    for val in range(20):
        key = ''
        for _ in range(3):
            key += chr(random.randint(97, 122))
        table[key] = val

    print(table)

    while table:
        key, val = table.popitem()
        print('key= {}, val= {}'.format(key, val))
