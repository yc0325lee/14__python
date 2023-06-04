#!/usr/bin/env python
# vim: ft=python ts=4 sw=4 tw=78 expandtab
# -*- coding:utf-8 -*-
# ----------------------------------------------------------------------------
# - file : 01_01_unpacking_a_sequence_into_separate_variables.py
# - author : yc0325lee
# - created : 2022-11-15 00:17:15 by yc032
# - modified : 2022-11-15 00:17:15 by yc032
# - description : 
# ----------------------------------------------------------------------------
if False:
    # - unpacking a sequence(or any iterable) using assignment allowed
    # ; as long as number of variables and structure match the sequence
    p = (4, 5)
    x, y = p
    
    data = ['ACME', 50, 91.1, (2012, 12, 21)]
    #       ------  --  ----  --------------
    #       name shares price date
    
    name, share, price, date = data
    name, shares, price, (year, mon, day) = data

    p = (4,5)
    x, y, z = p # ValueError: need more than 2 values to unpack


if False:
    # - unpacking works with any iterable in python includings tuples, lists,
    #   strings, files, iterators, generators
    s = 'Hello'
    a, b, c, d, e = s


if False:
    # discarding parts of the unpacked elements using throwaway variable '_'
    data = ['ACME', 50, 91.1, (2012, 12, 21)]
    _, share, price, _ = data # picking only share and price
