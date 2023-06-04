#!/usr/bin/env python
# -*- coding:utf-8 -*-
# vim: ft=python ts=4 sw=4 tw=78 expandtab
# ----------------------------------------------------------------------------
# - file : 01_17_extracting_a_subset_of_a_dictionary.py
# - author : yc0325lee
# - created : 2022-11-20 13:34:41 by yc032
# - modified : 2022-11-20 13:34:41 by yc032
# - description : 
# ----------------------------------------------------------------------------

if True:
    # dictionary
    prices = {
        'ACME': 45.23,
        'AAPL': 612.78,
        'IBM': 205.55,
        'HPQ': 37.20,
        'FB': 10.75
    }

    # - dict comprehension
    # ; this will be the best
    subset = {key:value for key,value in prices.items() if value > 200}
    print('subset =', subset)

    tech_names = ['AAPL','IBM','HPQ','MSFT']
    subset = {key:value for key, value in prices.items() if key in tech_names}
    print('subset =', subset)

    subset = dict((key, value) for key, value in prices.items() if value > 200)
    print('subset =', subset)

    # the following is possble, but a little slower
    tech_names={'AAPL','IBM','HPQ','MSFT'}
    subset = {key:prices[key] for key in prices.keys() if key in tech_names}
