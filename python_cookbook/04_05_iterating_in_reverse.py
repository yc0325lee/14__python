#!/usr/bin/env python
# -*- coding:utf-8 -*-
# vim: ft=python ts=4 sw=4 tw=78 expandtab
# ----------------------------------------------------------------------------
# - file : 04_05_iterating_in_reverse.py
# - author : yc0325lee
# - created : 2022-11-16 23:57:22 by yc032
# - modified : 2022-11-16 23:57:22 by yc032
# - description : 
# ----------------------------------------------------------------------------


if False:
    # built-in sequence type
    a = [1, 2, 3, 4]
    for x in reversed(a):
        print(x)

if False:
    # - turning an iterable into a list could consume a lot of memory
    #   if it’s large
    filename = 'input.txt'
    with open(filename, "r", encoding="utf8") as infile:
        for line in reversed(list(infile)):
            print(line, end='')


if True:
    # __reversed__() method for efficient iteration

    class CountDown:
        def __init__(self, start):
            self.start = start
     
        # forward iterator
        def __iter__(self):
            n = self.start
            while n > 0:
                yield n
                n -= 1
     
        # reverse iterator
        def __reversed__(self):
            n = 1
            while n <= self.start:
                yield n
                n += 1
        pass

    class CountUp:
        def __init__(self, start):
            self.start = start
     
        # forward iterator
        def __iter__(self):
            n = 1
            while n <= self.start:
                yield n
                n += 1
     
        # reverse iterator
        def __reversed__(self):
            n = self.start
            while n > 0:
                yield n
                n -= 1
        pass


    print('\n# CountDown(10)')
    for i in CountDown(10):
        print('i =', i)

    print('\n# CountUp(10)')
    for i in CountUp(10):
        print('i =', i)
