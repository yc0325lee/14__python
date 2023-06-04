# vim: ft=python ts=4 sw=4 tw=999 expandtab
# -*- coding:utf-8 -*-
# ----------------------------------------------------------------------------
# File : runtime_measure.py
# Author : yc0325lee
# Created : 2022-10-09 21:59:44 by lee2103
# Modified : 2022-10-09 21:59:44 by lee2103
# Description : 
# ----------------------------------------------------------------------------
import sys, os
import functools
import time
import timeit

def time2strf(tm):
    return time.strftime("%Y%m%d_%H%M%S", time.localtime(tm))

def measure_runtime(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        print("[info] {}()".format(func.__name__))
        print("[info] start=", time2strf(start))
        result = func(*args, **kwargs)
        end = time.time()
        print("[info] end=", time2strf(end))
        print("[info] elapsed=", end - start)

    return wrapper

@measure_runtime
def func_0():
    "returns a big list"
    cont = []
    for i in range(10000):
        cont.append(i)
    return cont

@measure_runtime
def func_1():
    "returns a big list"
    return [i for i in range(10000)]

def func_2():
    "returns a big list"
    cont = []
    for i in range(10000):
        cont.append(i)
    return cont

def func_3():
    "returns a big list"
    return [i for i in range(10000)]


if __name__ == '__main__':

    # using function decorator
    a = func_0()
    b = func_1()

    # - using 'timeit' library
    # timeit.timeit(stmt='pass', setup='pass', timer=<default timer>, number=1000000, globals=None)
    print("[info] func_2() elapsed=",
        timeit.timeit("func_2()", number=1000, globals=globals()))
    print("[info] func_3() elapsed=",
        timeit.timeit("func_2()", number=1000, globals=globals()))
