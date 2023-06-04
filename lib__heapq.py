#!/usr/bin/env python
# -*- coding:utf-8 -*-
# vim: ft=python ts=4 sw=4 tw=78 expandtab
# ----------------------------------------------------------------------------
# - file : lib__heapq.py
# - author : yc0325lee
# - created : 2022-11-19 19:00:08 by yc032
# - modified : 2022-11-19 19:00:08 by yc032
# - description : 
# ----------------------------------------------------------------------------
import heapq

if False:
    # -------------------------------------
    # - heapq.nlargest(n, iterable, key=None)
    # ; return a list with the n largest elements from the dataset defined by
    #   iterable. key, if provided, specifies a function of one argument that is
    #   used to extract a comparison key from each element in iterable (for
    #   example, key=str.lower). equivalent to: sorted(iterable, key=key,
    #   reverse=true)[:n].

    # - heapq.nsmallest(n, iterable, key=None)
    # ; return a list with the n smallest elements from the dataset defined by
    # iterable. key, if provided, specifies a function of one argument that is
    # used to extract a comparison key from each element in iterable (for
    # example, key=str.lower). equivalent to: sorted(iterable, key=key)[:n].
    pass


if False:
    # - heapsort
    def heapsort(iterable):
        h = []
        for value in iterable:
            heapq.heappush(h, value)
        return [heapq.heappop(h) for i in range(len(h))]

    before = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
    after = heapsort(before)
    print("\nbefore=", before)
    print("\nafter=", after)
    # before= [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
    # after= [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


if False:
    # - heap with tuple elements
    import pprint
    h = []
    heapq.heappush(h, (5, 'write code'))
    heapq.heappush(h, (7, 'release product'))
    heapq.heappush(h, (1, 'write spec'))
    heapq.heappush(h, (3, 'create tests'))
    heapq.heappush(h, (2, 'destroy tests'))
    heapq.heappush(h, (9, 'idle tests'))
    heapq.heappush(h, (4, 'powerdown tests'))
    heapq.heappush(h, (0, 'alwayson tests'))
    heapq.heappush(h, (6, 'dram tests'))
    heapq.heappush(h, (8, 'npu tests'))

    print("h=")
    pprint.pprint(h, indent=1)
    # [(0, 'alwayson tests'),
    #  (1, 'write spec'),
    #  (4, 'powerdown tests'),
    #  (2, 'destroy tests'),
    #  (3, 'create tests'),
    #  (9, 'idle tests'),
    #  (5, 'write code'),
    #  (7, 'release product'),
    #  (6, 'dram tests'),
    #  (8, 'npu tests')]
