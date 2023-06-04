#!/usr/bin/env python
# vim: ft=python ts=4 sw=4 tw=78 expandtab
# -*- coding:utf-8 -*-
# ----------------------------------------------------------------------------
# - file : lib__bisect.py
# - author : yc0325lee
# - created : 2022-10-15 20:56:59 by lee2103
# - modified : 2022-10-15 20:56:59 by lee2103
# - description : 
# ; array bisection algorithm
# ; maintaining a list in sorted order without having to sort the list after
#   each insertion.
# ----------------------------------------------------------------------------
import bisect


if False:
    def index(a, x):
        'Locate the leftmost value exactly equal to x'
        i = bisect_left(a, x)
        if i != len(a) and a[i] == x:
            return i
        raise ValueError

    def find_lt(a, x):
        'Find rightmost value less than x'
        i = bisect_left(a, x)
        if i:
            return a[i-1]
        raise ValueError

    def find_le(a, x):
        'Find rightmost value less than or equal to x'
        i = bisect_right(a, x)
        if i:
            return a[i-1]
        raise ValueError

    def find_gt(a, x):
        'Find leftmost value greater than x'
        i = bisect_right(a, x)
        if i != len(a):
            return a[i]
        raise ValueError

    def find_ge(a, x):
        'Find leftmost item greater than or equal to x'
        i = bisect_left(a, x)
        if i != len(a):
            return a[i]
        raise ValueError

if False:
    # ------------------------------------------------------------------------
    # - bisect.bisect_left(a, x, lo=0, hi=len(a), *, key=None)
    # ; locate the insertion point for x in a to maintain sorted order
    # ; if x is already present in a, the insertion point will be before (to
    #   the left of) any existing entries.
    # - bisect.bisect_right(a, x, lo=0, hi=len(a), *, key=None)
    # - bisect.bisect(a, x, lo=0, hi=len(a), *, key=None)
    # ; similar to bisect_left(), but returns an insertion point which comes
    #   after (to the right of) any existing entries of x in a.
    # ------------------------------------------------------------------------
    pass

if False:
    # ------------------------------------------------------------------------
    # - bisect.insort_left(a, x, lo=0, hi=len(a), *, key=None)
    # ; insort(seq, item) inserts item into seq so as to keep seq in ascending
    #   order
    # ; bisect_left() + insert()
    # - bisect.insort_right(a, x, lo=0, hi=len(a), *, key=None)
    # - bisect.insort(a, x, lo=0, hi=len(a), *, key=None)
    # ; insert x in a in sorted order
    # ; bisect_left() + insert()
    # ------------------------------------------------------------------------
    import bisect
    import random

    SIZE = 16
    random.seed(1729)

    print('\n# testing bisect.insort_right()')
    bucket = []
    for i in range(SIZE):
        item = random.randrange(SIZE*2)
        bisect.insort_right(bucket, item)
        print('%2d ->' % item, bucket)
    # testing bisect.insort_right()
    #  2 -> [2]
    # 26 -> [2, 26]
    # 29 -> [2, 26, 29]
    # 10 -> [2, 10, 26, 29]
    #  3 -> [2, 3, 10, 26, 29]
    # 11 -> [2, 3, 10, 11, 26, 29]
    # 18 -> [2, 3, 10, 11, 18, 26, 29]
    # 23 -> [2, 3, 10, 11, 18, 23, 26, 29]
    # 18 -> [2, 3, 10, 11, 18, 18, 23, 26, 29]
    # 13 -> [2, 3, 10, 11, 13, 18, 18, 23, 26, 29]
    #  9 -> [2, 3, 9, 10, 11, 13, 18, 18, 23, 26, 29]
    # 31 -> [2, 3, 9, 10, 11, 13, 18, 18, 23, 26, 29, 31]
    #  0 -> [0, 2, 3, 9, 10, 11, 13, 18, 18, 23, 26, 29, 31]
    # 29 -> [0, 2, 3, 9, 10, 11, 13, 18, 18, 23, 26, 29, 29, 31]
    # 23 -> [0, 2, 3, 9, 10, 11, 13, 18, 18, 23, 23, 26, 29, 29, 31]
    # 25 -> [0, 2, 3, 9, 10, 11, 13, 18, 18, 23, 23, 25, 26, 29, 29, 31]

    print('\n# testing bisect.insort_left()')
    bucket = []
    for i in range(SIZE):
        item = random.randrange(SIZE*2)
        bisect.insort_left(bucket, item)
        print('%2d ->' % item, bucket)
    # testing bisect.insort_left()
    # 22 -> [22]
    # 26 -> [22, 26]
    # 22 -> [22, 22, 26]
    # 14 -> [14, 22, 22, 26]
    # 25 -> [14, 22, 22, 25, 26]
    #  3 -> [3, 14, 22, 22, 25, 26]
    #  3 -> [3, 3, 14, 22, 22, 25, 26]
    #  6 -> [3, 3, 6, 14, 22, 22, 25, 26]
    # 24 -> [3, 3, 6, 14, 22, 22, 24, 25, 26]
    # 19 -> [3, 3, 6, 14, 19, 22, 22, 24, 25, 26]
    # 22 -> [3, 3, 6, 14, 19, 22, 22, 22, 24, 25, 26]
    #  0 -> [0, 3, 3, 6, 14, 19, 22, 22, 22, 24, 25, 26]
    # 18 -> [0, 3, 3, 6, 14, 18, 19, 22, 22, 22, 24, 25, 26]
    # 29 -> [0, 3, 3, 6, 14, 18, 19, 22, 22, 22, 24, 25, 26, 29]
    # 30 -> [0, 3, 3, 6, 14, 18, 19, 22, 22, 22, 24, 25, 26, 29, 30]
    # 26 -> [0, 3, 3, 6, 14, 18, 19, 22, 22, 22, 24, 25, 26, 26, 29, 30]
