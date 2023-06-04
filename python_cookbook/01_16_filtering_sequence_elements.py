#!/usr/bin/env python
# -*- coding:utf-8 -*-
# vim: ft=python ts=4 sw=4 tw=78 expandtab
# ----------------------------------------------------------------------------
# - file : 01_16_filtering_sequence_elements.py
# - author : yc0325lee
# - created : 2022-11-19 23:32:09 by yc032
# - modified : 2022-11-19 23:32:09 by yc032
# - description : 
# ----------------------------------------------------------------------------

if False:
    # list comprehension
    basket = [1, 4, -5, 10, -7, 2, 3, -1]
    print('positives =', [n for n in basket if n > 0])
    print('negatives =', [n for n in basket if n < 0])
    # positives = [1, 4, 10, 2, 3]
    # negatives = [-5, -7, -1]

    # generator expression
    positives = (n for n in basket if n > 0)
    negatives = (n for n in basket if n < 0)
    print('positives =', positives)
    print('negatives =', negatives)

    for positive in positives:
        print('positive=', positive)
    for negative in negatives:
        print('negative=', negative)

if False:
    # filtering non-integers out using filter()
    values = ['1', '2', '-3', '-', '4', 'N/A', '5']

    def is_integer(val):
        try:
            x = int(val)
            return True
        except ValueError:
            return False

    filtered = filter(is_integer, values)
    # filtered= <filter object at 0x0000021466167D90>
    print('filtered=', filtered)
    for value in filtered:
        print('val=', value)


if False:
    import math
    # clipping values
    basket = [1, 4, -5, 10, -7, 2, 3, -1]
    clipped = [n if n > 0 else 0 for n in basket]
    print('clipped=', clipped)
    # clipped= [1, 4, 0, 10, 0, 2, 3, 0]


if True:
    import itertools
    # using itertools.compress()

    addresses = [
        '5412 N CLARK',
        '5148 N CLARK',
        '5800 E 58TH',
        '2122 N CLARK'
        '5645 N RAVENSWOOD',
        '1060 W ADDISON',
        '4801 N BROADWAY',
        '1039 W GRANVILLE',
    ]
    counts = [ 0, 3, 10, 4, 1, 7, 6, 1]

    criterion = [count > 5 for count in counts]
    more_than_5 = itertools.compress(addresses, criterion)
    print('criterion =', criterion)
    print(more_than_5)
    # criterion = [False, False, True, False, False, True, True, False]
    # <itertools.compress object at 0x000001E697F4BDF0>

    for address in more_than_5:
        print('address =', address)
    # address = 5800 E 58TH
    # address = 4801 N BROADWAY
    # address = 1039 W GRANVILLE
