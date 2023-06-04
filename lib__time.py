#!/usr/bin/env python
# -*- coding:utf-8 -*-
# vim: ft=python ts=4 sw=4 tw=78 expandtab
# ----------------------------------------------------------------------------
# - file : lib__time.py
# - author : yc0325lee
# - created : 2022-12-04 01:23:21 by yc032
# - modified : 2022-12-04 01:23:21 by yc032
# - description : 
# ----------------------------------------------------------------------------
import time


if False:
    # - time.time() -> float
    # ; return the time in seconds since the epoch as a floating point number
    # - time.gmtime([secs])
    # ; convert a time expressed in seconds since the epoch to a struct_time
    #   in utc in which the dst flag is always zero.
    print('time()=', time.time()) # 1648260583.246656

    print('gmtime=', time.gmtime(time.time()))
    # time.struct_time(
    #     tm_year=2022, tm_mon=12, tm_mday=3, tm_hour=16, tm_min=26, tm_sec=7,
    #     tm_wday=5, tm_yday=337, tm_isdst=0
    # )

    print('localtime=', time.localtime(time.time()))
    # time.struct_time(
    #     tm_year=2022, tm_mon=12, tm_mday=4, tm_hour=1, tm_min=26, tm_sec=7,
    #     tm_wday=6, tm_yday=338, tm_isdst=0
    # )

    # - time.asctime([t])
    # ; convert a tuple or struct_time representing a time as returned by
    #   gmtime() or localtime() to a string of the following form:
    #   'sun jun 20 23:21:05 1993'
    # ; if t is not provided, the current time as returned by localtime() is used.
    print('asctime=', time.asctime(time.localtime(time.time()))) # Sat Mar  5 19:40:42 2022

    # - time.ctime([secs])
    # ; convert a time expressed in seconds since the epoch to a string of a
    #   form: 'sun jun 20 23:21:05 1993' representing local time.
    print('ctime=', time.ctime()) # Sat Mar  5 19:40:42 2022

    # - time.strftime(format[, t])
    # ; convert a tuple or struct_time representing a time as returned by
    #   gmtime() or localtime() to a string as specified by the format argument.
    # ; if t is not provided, the current time as returned by localtime() is
    #   used.
    print('strftime(%c)=', time.strftime("%c", time.localtime(time.time()))) # Sat Mar  5 19:40:42 2022
    print('strftime(%x)=', time.strftime("%x", time.localtime(time.time())))

    def now():
        '''shortcut'''
        return time.strftime("%Y%m%d_%H%M%S", time.localtime(time.time()))

    print("now=", now())


if False:
    # - time.sleep(secs), type(secs) : float
    # ; Suspend execution of the calling thread for the given number of seconds.
    pass

if False:
    # - time.perf_counter() -> float
    # ; return the value (in fractional seconds) of a performance counter,
    #   i.e. a clock with the highest available resolution to measure a short
    #   duration.
    # - time.perf_counter_ns() -> int
    # ; use perf_counter_ns() to avoid the precision loss caused by the float type.

    def factorial(n): 
        return 1 if n < 2 else n * factorial(n-1)
    
    start = time.perf_counter_ns()
    for i in range(20):
        t0 = time.perf_counter_ns()
        #t0 = time.perf_counter_ns()
        print("factorial({})=".format(i), factorial(i), end=' ')
        elapsed = time.perf_counter_ns() - t0
        print('elapsed=', elapsed, '[ns]')
        #elapsed = time.perf_counter_ns() - t0
        #print("elapsed=", elapsed, "ns")
        time.sleep(0.1)
    end = time.perf_counter_ns()
    print('total_elapsed=', end - start, '[ns]')
    # factorial(0)= 1 elapsed= 16100 [ns]
    # factorial(1)= 1 elapsed= 23100 [ns]
    # factorial(2)= 2 elapsed= 22100 [ns]
    # factorial(3)= 6 elapsed= 25000 [ns]
    # factorial(4)= 24 elapsed= 22800 [ns]
    # factorial(5)= 120 elapsed= 21300 [ns]
    # factorial(6)= 720 elapsed= 21100 [ns]
    # factorial(7)= 5040 elapsed= 43900 [ns]
    # factorial(8)= 40320 elapsed= 21700 [ns]
    # factorial(9)= 362880 elapsed= 20500 [ns]
    # factorial(10)= 3628800 elapsed= 20100 [ns]
    # factorial(11)= 39916800 elapsed= 20600 [ns]
    # factorial(12)= 479001600 elapsed= 20600 [ns]
    # factorial(13)= 6227020800 elapsed= 21600 [ns]
    # factorial(14)= 87178291200 elapsed= 22500 [ns]
    # factorial(15)= 1307674368000 elapsed= 21400 [ns]
    # factorial(16)= 20922789888000 elapsed= 22600 [ns]
    # factorial(17)= 355687428096000 elapsed= 22400 [ns]
    # factorial(18)= 6402373705728000 elapsed= 21900 [ns]
    # factorial(19)= 121645100408832000 elapsed= 22500 [ns]
    # total_elapsed= 2008633100 [ns]
