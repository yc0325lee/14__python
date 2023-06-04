#!/usr/bin/env python
# -*- coding:utf-8 -*-
# vim: ft=python ts=4 sw=4 tw=78 expandtab
# ----------------------------------------------------------------------------
# - file : lib__timeit.py
# - author : yc0325lee
# - created : 2022-12-18 16:44:47 by yc032
# - modified : 2022-12-18 16:44:47 by yc032
# - description : 
# ; provides a simple way to time small bits of Python code
# ----------------------------------------------------------------------------
import timeit

if False:
    # - timeit.timeit(
    #       stmt='pass', setup='pass', timer=<default timer>, number=1000000,
    #       globals=None
    #   )
    # ; create a timer instance with the given statement, setup code and timer
    #   function and run its timeit() method with number executions.
    print('test #1 :',
        timeit.timeit('"-".join(str(n) for n in range(100))', number=10000))

    print('test #2 :',
        timeit.timeit('"-".join([str(n) for n in range(100)])', number=10000))

    print('test #3 :',
        timeit.timeit('"-".join(map(str, range(100)))', number=10000))
    # test #1 : 0.0981032999989111
    # test #2 : 0.08060829999158159
    # test #2 : 0.09757640000316314
    pass


if True:
    # listcomp vs map/filter
    TIMES = 100000
    SETUP = """
symbols = '$¢£¥€¤'
def non_ascii(c):
    return c > 127
"""
    
    def clock(label, cmd):
        res = timeit.repeat(cmd, setup=SETUP, number=TIMES)
        print(label, *(f'{x:.3f}' for x in res))
    
    clock('listcomp        :', '[ord(s) for s in symbols if ord(s) > 127]')
    clock('listcomp + func :', '[ord(s) for s in symbols if non_ascii(ord(s))]')
    clock('filter + lambda :', 'list(filter(lambda c: c > 127, map(ord, symbols)))')
    clock('filter + func   :', 'list(filter(non_ascii, map(ord, symbols)))')
    # listcomp        : 0.073 0.071 0.072 0.071 0.073 ---> fastest!
    # listcomp + func : 0.121 0.119 0.119 0.119 0.119
    # filter + lambda : 0.096 0.096 0.095 0.096 0.096
    # filter + func   : 0.092 0.092 0.091 0.091 0.091
    pass
