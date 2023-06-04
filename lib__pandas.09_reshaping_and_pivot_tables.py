#!/usr/bin/env python
# -*- coding:utf-8 -*-
# vim: ft=python ts=4 sw=4 tw=78 expandtab
# ----------------------------------------------------------------------------
# - file : lib__pandas.09_reshaping_and_pivot_tables.py
# - author : yc0325lee
# - created : 2023-05-06 19:58:44 by yc032
# - modified : 2023-05-06 19:58:44 by yc032
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


if False:
    # ---------------------------------
    # - DataFrame.stack(level=- 1, dropna=True)
    # ; stack the prescribed level(s) from columns to index.
    #
    # - DataFrame.unstack(level=-1, fill_value=None)
    # ; pivot a level of the (necessarily hierarchical) index labels.
    tuples = list(
        zip(
            ["bar", "bar", "baz", "baz", "foo", "foo", "qux", "qux"],
            ["one", "two", "one", "two", "one", "two", "one", "two"],
        )
    )
    # [
    #   ('bar', 'one'), ('bar', 'two'), ('baz', 'one'), ('baz', 'two'),
    #   ('foo', 'one'), ('foo', 'two'), ('qux', 'one'), ('qux', 'two')
    # ]
    index = pd.MultiIndex.from_tuples(tuples, names=["first", "second"])

    df1 = pd.DataFrame(np.random.randn(8, 2), index=index, columns=['A', 'B'])
    print("\ndf=", df1, sep='\n')
    # df1=
    #                      A         B
    # first second
    # bar   one     0.496714 -0.138264
    #       two     0.647689  1.523030
    # baz   one    -0.234153 -0.234137
    #       two     1.579213  0.767435
    # foo   one    -0.469474  0.542560
    #       two    -0.463418 -0.465730
    # qux   one     0.241962 -1.913280
    #       two    -1.724918 -0.562288

    df2 = df1[:4]
    print("\ndf2=", df2, sep='\n')
    # df2=
    #                      A         B
    # first second
    # bar   one     0.496714 -0.138264
    #       two     0.647689  1.523030
    # baz   one    -0.234153 -0.234137
    #       two     1.579213  0.767435

    stacked = df2.stack()
    print("\nstacked=", stacked, sep='\n')
    print("\nstacked.index=", stacked.index, sep='\n')
    # stacked=
    # first  second
    # bar    one     A    0.496714
    #                B   -0.138264
    #        two     A    0.647689
    #                B    1.523030
    # baz    one     A   -0.234153
    #                B   -0.234137
    #        two     A    1.579213
    #                B    0.767435
    #
    # stacked.index=
    # MultiIndex([('bar', 'one', 'A'),
    #             ('bar', 'one', 'B'),
    #             ('bar', 'two', 'A'),
    #             ('bar', 'two', 'B'),
    #             ('baz', 'one', 'A'),
    #             ('baz', 'one', 'B'),
    #             ('baz', 'two', 'A'),
    #             ('baz', 'two', 'B')],
    #            names=['first', 'second', None])

    unstacked = stacked.unstack() # level=-1(last index)
    print("\nunstacked=", unstacked, sep='\n')
    print("\nunstacked.index=", unstacked.index, sep='\n')
    # unstacked=
    #                      A         B
    # first second
    # bar   one     0.496714 -0.138264
    #       two     0.647689  1.523030
    # baz   one    -0.234153 -0.234137
    #       two     1.579213  0.767435

    unstacked = stacked.unstack(level=0) # level=-1(last index)
    print("\nunstacked=", unstacked, sep='\n')
    print("\nunstacked.index=", unstacked.index, sep='\n')
    # unstacked=
    # first          bar       baz
    # second
    # one    A  0.496714 -0.234153
    #        B -0.138264 -0.234137
    # two    A  0.647689  1.579213
    #        B  1.523030  0.767435

    unstacked = stacked.unstack(level=1) # level=-1(last index)
    print("\nunstacked=", unstacked, sep='\n')
    print("\nunstacked.index=", unstacked.index, sep='\n')
    # unstacked=
    # second        one       two
    # first
    # bar   A  0.496714  0.647689
    #       B -0.138264  1.523030
    # baz   A -0.234153  1.579213
    #       B -0.234137  0.767435


if True:
    # - pandas.pivot_table(
    #       data, values=None, index=None, columns=None, aggfunc='mean',
    #       fill_value=None, margins=False, dropna=True, margins_name='All',
    #       observed=False, sort=True
    #   )
    # ; create a spreadsheet-style pivot table as a dataframe.
    # ; pivot_table() pivots a DataFrame specifying the values, index and columns
    # ; aggfuncfunction, list of functions, dict, default 'numpy.mean'
    df1 = pd.DataFrame({
        "A": ["one", "one", "two", "three"] * 3,
        "B": ["A", "B", "C"] * 4,
        "C": ["foo", "foo", "foo", "bar", "bar", "bar"] * 2,
        "D": np.random.randn(12),
        "E": np.random.randn(12),
    })
    print("\ndf1=", df1, sep='\n')
    # df1=
    #         A  B    C         D         E
    # 0     one  A  foo  0.496714  0.241962
    # 1     one  B  foo -0.138264 -1.913280
    # 2     two  C  foo  0.647689 -1.724918
    # 3   three  A  bar  1.523030 -0.562288
    # 4     one  B  bar -0.234153 -1.012831
    # 5     one  C  bar -0.234137  0.314247
    # 6     two  A  foo  1.579213 -0.908024
    # 7   three  B  foo  0.767435 -1.412304
    # 8     one  C  foo -0.469474  1.465649
    # 9     one  A  bar  0.542560 -0.225776
    # 10    two  B  bar -0.463418  0.067528
    # 11  three  C  bar -0.465730 -1.424748

    pivot_table = pd.pivot_table(
        df1, index=["A", "B"], columns=["C"], values="D",
        aggfunc=np.mean
    )
    print("\npivot_table(mean)=", pivot_table, sep='\n')
    # pivot_table(mean)=
    # C             bar       foo
    # A     B
    # one   A  0.542560  0.496714
    #       B -0.234153 -0.138264
    #       C -0.234137 -0.469474
    # three A  1.523030       NaN
    #       B       NaN  0.767435
    #       C -0.465730       NaN
    # two   A       NaN  1.579213
    #       B -0.463418       NaN
    #       C       NaN  0.647689

    pivot_table = pd.pivot_table(
        df1, index=["A", "B"], columns=["C"], values="D",
        aggfunc=np.max, fill_value=0.0
    )
    print("\npivot_table(max)=", pivot_table, sep='\n')
    # pivot_table(max)=
    # C             bar       foo
    # A     B
    # one   A  0.542560  0.496714
    #       B -0.234153 -0.138264
    #       C -0.234137 -0.469474
    # three A  1.523030  0.000000
    #       B  0.000000  0.767435
    #       C -0.465730  0.000000
    # two   A  0.000000  1.579213
    #       B -0.463418  0.000000
    #       C  0.000000  0.647689

    pivot_table = pd.pivot_table(
        df1, index=["A", "B"], columns=["C"], values="D",
        aggfunc=[np.mean, np.sum, np.min, np.max], fill_value=0.0
    )
    print("\npivot_table(mean,sum,min,max)=", pivot_table, sep='\n')
    # pivot_table(max)=
    #              mean                 sum                amin                amax
    # C             bar       foo       bar       foo       bar       foo       bar       foo
    # A     B
    # one   A  0.542560  0.496714  0.542560  0.496714  0.542560  0.496714  0.542560  0.496714
    #       B -0.234153 -0.138264 -0.234153 -0.138264 -0.234153 -0.138264 -0.234153 -0.138264
    #       C -0.234137 -0.469474 -0.234137 -0.469474 -0.234137 -0.469474 -0.234137 -0.469474
    # three A  1.523030  0.000000  1.523030  0.000000  1.523030  0.000000  1.523030  0.000000
    #       B  0.000000  0.767435  0.000000  0.767435  0.000000  0.767435  0.000000  0.767435
    #       C -0.465730  0.000000 -0.465730  0.000000 -0.465730  0.000000 -0.465730  0.000000
    # two   A  0.000000  1.579213  0.000000  1.579213  0.000000  1.579213  0.000000  1.579213
    #       B -0.463418  0.000000 -0.463418  0.000000 -0.463418  0.000000 -0.463418  0.000000
    #       C  0.000000  0.647689  0.000000  0.647689  0.000000  0.647689  0.000000  0.647689
