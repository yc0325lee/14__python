#!/usr/bin/env python
# -*- coding:utf-8 -*-
# vim: ft=python ts=4 sw=4 tw=78 expandtab
# ----------------------------------------------------------------------------
# - file : 08_04_saving_memory_when_creating_a_large_number_of_instances.py
# - author : yc0325lee
# - created : 2022-11-20 19:59:48 by yc032
# - modified : 2022-11-20 19:59:48 by yc032
# - description : 
# ----------------------------------------------------------------------------

if False:
    # ; for memory-efficient data structure
    # ; adding more attributes not allowed
    class Date:
        __slots__ = ['year', 'month', 'day']
        def __init__(self, year, month, day):
            self.year = year
            self.month = month
            self.day = day

