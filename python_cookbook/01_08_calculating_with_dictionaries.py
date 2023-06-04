#!/usr/bin/env python
# -*- coding:utf-8 -*-
# vim: ft=python ts=4 sw=4 tw=78 expandtab
# ----------------------------------------------------------------------------
# - file : 01_08_calculating_with_dictionaries.py
# - author : yc0325lee
# - created : 2022-11-19 21:34:19 by yc032
# - modified : 2022-11-19 21:34:19 by yc032
# - description : 
# ----------------------------------------------------------------------------

if True:
    prices = {
        'ACME': 45.23,
        'AAPL': 612.78,
        'IBM': 205.55,
        'HPQ': 37.20,
        'FB': 10.75
    }

    # (1)
    minimun = min(zip(prices.values(), prices.keys()))
    maximun = max(zip(prices.values(), prices.keys()))
    print('minimun =', minimun)
    print('maximun =', maximun)

    # (2)
    prices_sorted = sorted(zip(prices.values(), prices.keys()))
    print('prices_sorted =', prices_sorted)

    minimun = prices_sorted[0]
    maximun = prices_sorted[-1]
    print('minimun =', minimun)
    print('maximun =', maximun)

    # (3)
    minKey = min(prices, key=lambda k: prices[k])
    maxKey = max(prices, key=lambda k: prices[k])
    print('minKey=', minKey) # Returns 'FB'
    print('maxKey=', maxKey) # Returns 'AAPL'
    print('minimun =', prices[minKey])
    print('maximun =', prices[maxKey])
