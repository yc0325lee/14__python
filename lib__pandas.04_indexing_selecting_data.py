#!/usr/bin/env python
# -*- coding:utf-8 -*-
# vim: ft=python ts=4 sw=4 tw=78 expandtab
# ----------------------------------------------------------------------------
# - file : lib__pandas.04_indexing_selecting_data.py
# - author : yc0325lee
# - created : 2023-05-06 21:24:58 by yc032
# - modified : 2023-05-06 21:24:58 by yc032
# - description : 
# ----------------------------------------------------------------------------
import os, os.path, sys
import random
import csv
import pickle
import numpy as np; np.random.seed(42)
import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd

# (1) boolean indexing for series
if False:
    s1 = pd.Series(range(-3, 4))
    print('\ns1=', s1, sep='\n')
    # s1=
    # 0   -3
    # 1   -2
    # 2   -1
    # 3    0
    # 4    1
    # 5    2
    # 6    3
    # dtype: int64

    print(s1 > 0)
    # 0    False
    # 1    False
    # 2    False
    # 3    False
    # 4     True
    # 5     True
    # 6     True
    # dtype: bool

    print(s1[s1 > 0])
    print(s1[(s1 < -1) | (s1 > 0.5)])
    print(s1[~(s1 < 0)])


# (2) boolean indexing for dataframe
if False:
    height = 15
    df1 = pd.DataFrame(
        data=np.random.randn(height, 5),
        index=pd.date_range("1/1/2023", periods=height),
        columns=['a', 'b', 'c', 'd', 'e']
    )
    print('\ndf1=', df1, sep='\n')
    # df1=
    #                    a         b         c         d         e
    # 2023-01-01  0.496714 -0.138264  0.647689  1.523030 -0.234153
    # 2023-01-02 -0.234137  1.579213  0.767435 -0.469474  0.542560
    # 2023-01-03 -0.463418 -0.465730  0.241962 -1.913280 -1.724918
    # 2023-01-04 -0.562288 -1.012831  0.314247 -0.908024 -1.412304
    # 2023-01-05  1.465649 -0.225776  0.067528 -1.424748 -0.544383
    # 2023-01-06  0.110923 -1.150994  0.375698 -0.600639 -0.291694
    # 2023-01-07 -0.601707  1.852278 -0.013497 -1.057711  0.822545
    # 2023-01-08 -1.220844  0.208864 -1.959670 -1.328186  0.196861
    # 2023-01-09  0.738467  0.171368 -0.115648 -0.301104 -1.478522
    # 2023-01-10 -0.719844 -0.460639  1.057122  0.343618 -1.763040
    # 2023-01-11  0.324084 -0.385082 -0.676922  0.611676  1.031000
    # 2023-01-12  0.931280 -0.839218 -0.309212  0.331263  0.975545
    # 2023-01-13 -0.479174 -0.185659 -1.106335 -1.196207  0.812526
    # 2023-01-14  1.356240 -0.072010  1.003533  0.361636 -0.645120
    # 2023-01-15  0.361396  1.538037 -0.035826  1.564644 -2.619745

    selected = df1[df1['a'] > 0]
    print('\nselected=', selected, sep='\n')
    # selected=
    #                    a         b         c         d         e
    # 2023-01-01  0.496714 -0.138264  0.647689  1.523030 -0.234153
    # 2023-01-05  1.465649 -0.225776  0.067528 -1.424748 -0.544383
    # 2023-01-06  0.110923 -1.150994  0.375698 -0.600639 -0.291694
    # 2023-01-09  0.738467  0.171368 -0.115648 -0.301104 -1.478522
    # 2023-01-11  0.324084 -0.385082 -0.676922  0.611676  1.031000
    # 2023-01-12  0.931280 -0.839218 -0.309212  0.331263  0.975545
    # 2023-01-14  1.356240 -0.072010  1.003533  0.361636 -0.645120
    # 2023-01-15  0.361396  1.538037 -0.035826  1.564644 -2.619745

    #selected = df1[(df1['a'] > 0) and (df1['b'] > 0)] -> 'and' not work!
    selected = df1[(df1['a'] > 0) & (df1['b'] > 0)]
    print('\nselected=', selected, sep='\n')
    # selected=
    #                    a         b         c         d         e
    # 2023-01-09  0.738467  0.171368 -0.115648 -0.301104 -1.478522
    # 2023-01-15  0.361396  1.538037 -0.035826  1.564644 -2.619745


# (3) dataframe
if False:
    df1 = pd.DataFrame({
        'a': ['one', 'one', 'two', 'three', 'two', 'one', 'six'],
        'b': ['x', 'y', 'y', 'x', 'y', 'x', 'x'],
        'c': np.random.randn(7)
    })
    print('\ndf1=', df1, sep='\n')
    # df1=
    #        a  b         c
    # 0    one  x  0.496714
    # 1    one  y -0.138264
    # 2    two  y  0.647689
    # 3  three  x  1.523030
    # 4    two  y -0.234153
    # 5    one  x -0.234137
    # 6    six  x  1.579213

    criterion = df1['a'].map(lambda x: x.startswith('t'))
    print('\ncriterion=', criterion, sep='\n')
    # criterion=
    # 0    False
    # 1    False
    # 2     True
    # 3     True
    # 4     True
    # 5    False
    # 6    False
    # Name: a, dtype: bool

    selected = df1[criterion]
    print('\nselected=', selected, sep='\n')
    #print('\nselected=', selected.reset_index(drop=True), sep='\n')
    # selected=
    #        a  b         c
    # 2    two  y  0.647689
    # 3  three  x  1.523030
    # 4    two  y -0.234153

    selected = df1[[x.startswith('t') for x in df1['a']]] # equivalent but slower
    #              -------------------------------------
    #                       list compression
    print('\nselected=', selected, sep='\n')
    # selected=
    #        a  b         c
    # 2    two  y  0.647689
    # 3  three  x  1.523030
    # 4    two  y -0.234153

    selected = df1[criterion & (df1['b'] == 'x')] # multiple criteria
    print('\nselected=', selected, sep='\n')
    # selected=
    #        a  b        c
    # 3  three  x  1.52303
