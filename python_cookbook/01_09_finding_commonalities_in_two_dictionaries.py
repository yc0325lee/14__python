#!/usr/bin/env python
# -*- coding:utf-8 -*-
# vim: ft=python ts=4 sw=4 tw=78 expandtab
# ----------------------------------------------------------------------------
# - file : 01_09_finding_commonalities_in_two_dictionaries.py
# - author : yc0325lee
# - created : 2022-11-16 00:17:21 by yc032
# - modified : 2022-11-16 00:17:21 by yc032
# - description : 
# - dict.keys() and dict.items()
# ; support common set operations such as unions, intersections, and differences
# ----------------------------------------------------------------------------

if True:
    a = {
        'x' : 1,
        'y' : 2,
        'z' : 3
    }

    b = {
        'w' : 10,
        'x' : 11,
        'y' : 2
    }

    # find keys in common
    print('a.keys() & b.keys() =', a.keys() & b.keys())

    # find keys in a that are not in b
    print('a.keys() - b.keys() =', a.keys() - b.keys())

    # find (key,value) pairs in common
    print('a.items() & b.items() =', a.items() & b.items())
    # a.keys() & b.keys() = {'y', 'x'}
    # a.keys() - b.keys() = {'z'}
    # a.items() & b.items() = {('y', 2)}

    # make a new dictionary with certain keys removed
    filtered = {key:a[key] for key in a.keys() - {'z','w'}}
    print('filtered =', filtered)
    # filtered = {'y': 2, 'x': 1}
