#!/usr/bin/env python
# -*- coding:utf-8 -*-
# vim: ft=python ts=4 sw=4 tw=78 expandtab
# ----------------------------------------------------------------------------
# - file : 01_04_finding_the_largest_or_smallest_n_items.py
# - author : yc0325lee
# - created : 2022-11-19 19:01:31 by yc032
# - modified : 2022-11-19 19:01:31 by yc032
# - description : 
# ----------------------------------------------------------------------------

if False:
    # finding the largest or smallest n items
    import heapq

    nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
    print("largest_3=", heapq.nlargest(3, nums)) # Prints [42, 37, 23]
    print("smallest_3=", heapq.nsmallest(3, nums)) # Prints [-4, 1, 2]

    heap = list(nums)
    heapq.heapify(heap)
    print("heap=", heap)
    # heap= [-4, 2, 1, 23, 7, 2, 18, 23, 42, 37, 8]


if True:
    # passing key function to nsmallest() or nlargest()
    import heapq

    portfolio = [
         {'name': 'IBM',  'shares': 100, 'price': 91.1},
         {'name': 'AAPL', 'shares': 50,  'price': 543.22},
         {'name': 'FB',   'shares': 200, 'price': 21.09},
         {'name': 'HPQ',  'shares': 35,  'price': 31.75},
         {'name': 'YHOO', 'shares': 45,  'price': 16.35},
         {'name': 'ACME', 'shares': 75,  'price': 115.65}
    ]

    cheap = heapq.nsmallest(len(portfolio), portfolio, key=lambda k: k['price'])
    expensive = heapq.nlargest(len(portfolio), portfolio, key=lambda k: k['price'])

    print('\n# cheap')
    for item in cheap:
        print(item)
    # cheap
    # {'name': 'YHOO', 'shares': 45, 'price': 16.35}
    # {'name': 'FB', 'shares': 200, 'price': 21.09}
    # {'name': 'HPQ', 'shares': 35, 'price': 31.75}
    # {'name': 'IBM', 'shares': 100, 'price': 91.1}
    # {'name': 'ACME', 'shares': 75, 'price': 115.65}
    # {'name': 'AAPL', 'shares': 50, 'price': 543.22}

    print('\n# expensive')
    for item in expensive:
        print(item)
    # expensive
    # {'name': 'AAPL', 'shares': 50, 'price': 543.22}
    # {'name': 'ACME', 'shares': 75, 'price': 115.65}
    # {'name': 'IBM', 'shares': 100, 'price': 91.1}
    # {'name': 'HPQ', 'shares': 35, 'price': 31.75}
    # {'name': 'FB', 'shares': 200, 'price': 21.09}
    # {'name': 'YHOO', 'shares': 45, 'price': 16.35}
