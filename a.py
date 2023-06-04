# vim: ft=python ts=4 sw=4 tw=999 expandtab
# -*- coding:utf-8 -*-
# ----------------------------------------------------------------------------
# File : a.py
# Author : yc0325lee
# Created : 2022-09-16 21:23:38 by lee2103
# Modified : 2022-09-16 21:23:38 by lee2103
# Description : 
# ----------------------------------------------------------------------------

class Vector:
    typecode = 'd' # double, 'f' -> float
    def __init__(self):
        pass

v = Vector()
print(v.typecode)
v.typecode = 'f'
print(v.typecode)
print(Vector.typecode)
