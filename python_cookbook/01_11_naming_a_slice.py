#!/usr/bin/env python
# -*- coding:utf-8 -*-
# vim: ft=python ts=4 sw=4 tw=78 expandtab
# ----------------------------------------------------------------------------
# - file : 01_11_naming_a_slice.py
# - author : yc0325lee
# - created : 2022-11-15 23:19:52 by yc032
# - modified : 2022-11-15 23:19:52 by yc032
# - description : 
# ; hardcoded slice indices -> unreadable mess!
# ----------------------------------------------------------------------------
if False:
    # - built-in slice() creates a slice object that can be used anywhere a
    #   slice is allowed
    record = '01234567890123456789012345678901.3456789'
    #                              ---       ----
    print('\nusing slice indices')
    print(record[21:24]) # 123
    print(record[31:35]) # 1.34
    cost = int(record[21:24]) * float(record[31:35])
    print('cost =', cost)
    # 123
    # 1.34
    # cost = 164.82000000000002
    # -> ugly!

    print('\nusing slice object')
    SHARES = slice(21, 24)
    PRICE = slice(31, 35)
    print('SHARES =', SHARES)
    print('PRICE =', PRICE)
    cost = int(record[SHARES]) * float(record[PRICE])
    print('cost =', cost)
    # SHARES = slice(21, 24, None)
    # PRICE = slice(31, 35, None)
    # cost = 164.82000000000002

if False:
    # using slice object
    items = [0, 1, 2, 3, 4, 5, 6]
    print('items =', items)
    a = slice(2, 4)
    print('items[2:4] =', items[2:4])
    print('items[2:4] =', items[a])
    items[a] = [10, 11]
    del items[a]
    print('items =', items)
    # items = [0, 1, 2, 3, 4, 5, 6]
    # items[2:4] = [2, 3]
    # items[2:4] = [2, 3]
    # items = [0, 1, 4, 5, 6]

    a = slice(0, 7, 2)
    print('a.start =', a.start)
    print('a.stop =', a.stop)
    print('a.step =', a.step)
    print('a.indices =', a.step)
    # a.start = 0
    # a.stop = 7
    # a.step = 2
