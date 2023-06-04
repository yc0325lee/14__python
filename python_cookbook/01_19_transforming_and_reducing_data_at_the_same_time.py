#!/usr/bin/env python
# -*- coding:utf-8 -*-
# vim: ft=python ts=4 sw=4 tw=78 expandtab
# ----------------------------------------------------------------------------
# - file : 01_19_transforming_and_reducing_data_at_the_same_time.py
# - author : yc0325lee
# - created : 2022-11-19 17:54:36 by yc032
# - modified : 2022-11-19 17:54:36 by yc032
# - description : 
# ----------------------------------------------------------------------------

if False:
    # generator expression
    nums = [1, 2, 3, 4, 5]
    summation = sum(x*x for x in nums)
    #               -----------------
    #               generator expression

    print('summation =', summation)


if False:
    # - os.listdir(path='.')
    # ; return a list containing the names of the entries in the directory
    #   given by path. 
    import os
    files = os.listdir('dirname')

    if any(name.endswith('.py') for name in files):
        print 'There be python!'
    else:
        print 'Sorry, no python.'


if False:
    # tuple to csv format
    s = ('ACME', 50, 123.45) # tuple
    print ','.join(str(x) for x in s)
    # to be joined, contents should be converted to 'str' type


if False:
    # data reduction across fields of a data structure
    portfolio= [
        {'name':'GOOG', 'shares': 50},
        {'name':'YHOO', 'shares': 75},
        {'name':'AOL', 'shares': 20},
        {'name':'SCOX', 'shares': 65}
    ]
    min_shares = min(stock['shares'] for stock in portfolio)

    # or you can do this!
    min_shares = min(portfolio, key=lambda stock: stock['shares'])
