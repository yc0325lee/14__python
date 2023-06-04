#!/usr/bin/env python
# -*- coding:utf-8 -*-
# vim: ft=python ts=4 sw=4 tw=78 expandtab
# ----------------------------------------------------------------------------
# - file : lib__pandas.concat_merge_join_compare.py
# - author : yc0325lee
# - created : 2023-05-05 11:47:13 by yc032
# - modified : 2023-05-05 11:47:13 by yc032
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
    # - pandas.concat(
    #       objs, *, axis=0, join='outer', ignore_index=False, keys=None,
    #       levels=None, names=None, verify_integrity=False, sort=False,
    #       copy=True
    #   )
    # ; concatenate pandas objects along a particular axis.
    # ; axis{0/’index’, 1/’columns’}, default 0
    # ; join : {'inner', 'outer'}, default 'outer'
    # ; keys : sequence, default none. construct hierarchical index using the
    #   passed keys as the outermost level. if multiple levels passed, should
    #   contain tuples.
    df1 = pd.DataFrame({
        "A": ["A0", "A1", "A2", "A3"],
        "B": ["B0", "B1", "B2", "B3"],
        "C": ["C0", "C1", "C2", "C3"],
        "D": ["D0", "D1", "D2", "D3"],
    }, index=[0, 1, 2, 3],)
    df2 = pd.DataFrame({
        "A": ["A4", "A5", "A6", "A7"],
        "B": ["B4", "B5", "B6", "B7"],
        "C": ["C4", "C5", "C6", "C7"],
        "D": ["D4", "D5", "D6", "D7"],
    }, index=[4, 5, 6, 7],)
    df3 = pd.DataFrame({
        "A": ["A8", "A9", "A10", "A11"],
        "B": ["B8", "B9", "B10", "B11"],
        "C": ["C8", "C9", "C10", "C11"],
        "D": ["D8", "D9", "D10", "D11"],
    }, index=[8, 9, 10, 11],)
    frames = [df1, df2, df3]
    print('\ndf1=', df1, sep='\n')
    print('\ndf2=', df2, sep='\n')
    print('\ndf3=', df3, sep='\n')
    # df1=
    #           A    B    C    D
    #     0    A0   B0   C0   D0
    #     1    A1   B1   C1   D1
    #     2    A2   B2   C2   D2
    #     3    A3   B3   C3   D3
    # df2=
    #           A    B    C    D
    #     4    A4   B4   C4   D4
    #     5    A5   B5   C5   D5
    #     6    A6   B6   C6   D6
    #     7    A7   B7   C7   D7
    # df3=
    #           A    B    C    D
    #     8    A8   B8   C8   D8
    #     9    A9   B9   C9   D9
    #     10  A10  B10  C10  D10
    #     11  A11  B11  C11  D11

    concatenated = pd.concat(frames)
    print('\nconcatenated=', concatenated, sep='\n')
    # concatenated=
    #       A    B    C    D
    # 0    A0   B0   C0   D0
    # 1    A1   B1   C1   D1
    # 2    A2   B2   C2   D2
    # 3    A3   B3   C3   D3
    # 4    A4   B4   C4   D4
    # 5    A5   B5   C5   D5
    # 6    A6   B6   C6   D6
    # 7    A7   B7   C7   D7
    # 8    A8   B8   C8   D8
    # 9    A9   B9   C9   D9
    # 10  A10  B10  C10  D10
    # 11  A11  B11  C11  D11

    concatenated = pd.concat(frames, keys=['one', 'two', 'three'])
    for thing in concatenated.index:
        print(thing)
    print('\nconcatenated=', concatenated, sep='\n')
    # concatenated=
    #             A    B    C    D
    # one   0    A0   B0   C0   D0
    #       1    A1   B1   C1   D1
    #       2    A2   B2   C2   D2
    #       3    A3   B3   C3   D3
    # two   4    A4   B4   C4   D4
    #       5    A5   B5   C5   D5
    #       6    A6   B6   C6   D6
    #       7    A7   B7   C7   D7
    # three 8    A8   B8   C8   D8
    #       9    A9   B9   C9   D9
    #       10  A10  B10  C10  D10
    #       11  A11  B11  C11  D11
    
    print(concatenated.loc["three"])
    #       A    B    C    D
    # 8    A8   B8   C8   D8
    # 9    A9   B9   C9   D9
    # 10  A10  B10  C10  D10
    # 11  A11  B11  C11  D11

    print(concatenated.loc[("three", 8), "C"]) # series
    #                      ------------
    #                         tuple

    df4 = pd.DataFrame({
        "B": ["B2", "B3", "B6", "B7"],
        "D": ["D2", "D3", "D6", "D7"],
        "F": ["F2", "F3", "F6", "F7"],
    }, index=[2, 3, 6, 7],)
    print('\ndf4=', df4, sep='\n')
    # df1=
    #           A    B    C    D
    #     0    A0   B0   C0   D0
    #     1    A1   B1   C1   D1
    #     2    A2   B2   C2   D2
    #     3    A3   B3   C3   D3
    # df4=
    #     B   D   F
    # 2  B2  D2  F2
    # 3  B3  D3  F3
    # 6  B6  D6  F6
    # 7  B7  D7  F7

    concatenated = pd.concat([df1, df4], axis=0, join='inner') # join='inner'
    print('\nconcatenated=', concatenated, sep='\n')
    # concatenated=
    #     B   D
    # 0  B0  D0
    # 1  B1  D1
    # 2  B2  D2
    # 3  B3  D3
    # 2  B2  D2
    # 3  B3  D3
    # 6  B6  D6
    # 7  B7  D7

    concatenated = pd.concat([df1, df4], axis=1) # join='outer'
    print('\nconcatenated=', concatenated, sep='\n')
    # concatenated=
    #      A    B    C    D    B    D    F
    # 0   A0   B0   C0   D0  NaN  NaN  NaN
    # 1   A1   B1   C1   D1  NaN  NaN  NaN
    # 2   A2   B2   C2   D2   B2   D2   F2
    # 3   A3   B3   C3   D3   B3   D3   F3
    # 6  NaN  NaN  NaN  NaN   B6   D6   F6
    # 7  NaN  NaN  NaN  NaN   B7   D7   F7

    concatenated = pd.concat([df1, df4], axis=1, join='inner') # join='inner'
    print('\nconcatenated=', concatenated, sep='\n')
    # concatenated=
    #     A   B   C   D   B   D   F
    # 2  A2  B2  C2  D2  B2  D2  F2
    # 3  A3  B3  C3  D3  B3  D3  F3

    # ignoring indexes on the concatenation axis
    concatenated = pd.concat([df1, df4], axis=0, ignore_index=True, sort=False) # join='inner'
    print('\nconcatenated=', concatenated, sep='\n')
    # concatenated=
    #      A   B    C   D    F
    # 0   A0  B0   C0  D0  NaN
    # 1   A1  B1   C1  D1  NaN
    # 2   A2  B2   C2  D2  NaN
    # 3   A3  B3   C3  D3  NaN
    # 4  NaN  B2  NaN  D2   F2
    # 5  NaN  B3  NaN  D3   F3
    # 6  NaN  B6  NaN  D6   F6
    # 7  NaN  B7  NaN  D7   F7

    # concatenating dataframe and series
    s1 = pd.Series(["X0", "X1", "X2", "X3"], name="X")
    concatenated = pd.concat([df1, s1], axis=1)
    print('\nconcatenated=', concatenated, sep='\n')
    # concatenated=
    #     A   B   C   D   X
    # 0  A0  B0  C0  D0  X0
    # 1  A1  B1  C1  D1  X1
    # 2  A2  B2  C2  D2  X2
    # 3  A3  B3  C3  D3  X3


    # passing a dict to concat()
    pieces = {'x': df1, 'y': df2, 'z': df3}
    concatenated = pd.concat(pieces)
    print('\nconcatenated=', concatenated, sep='\n')
    # concatenated=
    #         A    B    C    D
    # x 0    A0   B0   C0   D0
    #   1    A1   B1   C1   D1
    #   2    A2   B2   C2   D2
    #   3    A3   B3   C3   D3
    # y 4    A4   B4   C4   D4
    #   5    A5   B5   C5   D5
    #   6    A6   B6   C6   D6
    #   7    A7   B7   C7   D7
    # z 8    A8   B8   C8   D8
    #   9    A9   B9   C9   D9
    #   10  A10  B10  C10  D10
    #   11  A11  B11  C11  D11

    # appending series rows to a dataframe
    s2 = pd.Series(["X0", "X1", "X2", "X3"], index=["A", "B", "C", "D"])
    print('\ns2=', s2, sep='\n')
    # s2=
    # A    X0
    # B    X1
    # C    X2
    # D    X3
    # dtype: object

    concatenated = pd.concat([df1, s2.to_frame().T], ignore_index=True)
    print('\nconcatenated=', concatenated, sep='\n')
    # concatenated=
    #     A   B   C   D
    # 0  A0  B0  C0  D0
    # 1  A1  B1  C1  D1
    # 2  A2  B2  C2  D2
    # 3  A3  B3  C3  D3
    # 4  X0  X1  X2  X3


if False:
    # ---------------------------------
    # - pandas.merge(
    #       left, right, how='inner', on=None, left_on=None, right_on=None,
    #       left_index=False, right_index=False, sort=False, suffixes=('_x', '_y'),
    #       copy=None, indicator=False, validate=None
    #   )
    # ; merge dataframe or named series objects with a database-style join.
    # ; how: {'left', 'right', 'outer', 'inner', 'cross'}, default 'inner'

    if False:
        left = pd.DataFrame({
            "key": ["K0", "K1", "K2", "K3"],
            "A": ["A0", "A1", "A2", "A3"],
            "B": ["B0", "B1", "B2", "B3"], })
        right = pd.DataFrame({
            "key": ["K0", "K1", "K2", "K3"],
            "C": ["C0", "C1", "C2", "C3"],
            "D": ["D0", "D1", "D2", "D3"],
        })
        print('\nleft=', left, sep='\n')
        print('\nright=', right, sep='\n')
        # left=
        #   key   A   B
        # 0  K0  A0  B0
        # 1  K1  A1  B1
        # 2  K2  A2  B2
        # 3  K3  A3  B3
        # 
        # right=
        #   key   C   D
        # 0  K0  C0  D0
        # 1  K1  C1  D1
        # 2  K2  C2  D2
        # 3  K3  C3  D3

        merged = pd.merge(left, right, on="key")
        print('\nmerged=', merged, sep='\n')
        # merged=
        #   key   A   B   C   D
        # 0  K0  A0  B0  C0  D0
        # 1  K1  A1  B1  C1  D1
        # 2  K2  A2  B2  C2  D2
        # 3  K3  A3  B3  C3  D3

    if True:
        left = pd.DataFrame({
                "key1": ["K0", "K0", "K1", "K2"],
                "key2": ["K0", "K1", "K0", "K1"],
                "A": ["A0", "A1", "A2", "A3"],
                "B": ["B0", "B1", "B2", "B3"],})
        right = pd.DataFrame({
                "key1": ["K0", "K1", "K1", "K2"],
                "key2": ["K0", "K0", "K0", "K0"],
                "C": ["C0", "C1", "C2", "C3"],
                "D": ["D0", "D1", "D2", "D3"],})
        print('\nleft=', left, sep='\n')
        print('\nright=', right, sep='\n')
        # left=
        #   key1 key2   A   B
        # 0   K0   K0  A0  B0
        # 1   K0   K1  A1  B1
        # 2   K1   K0  A2  B2
        # 3   K2   K1  A3  B3
        # 
        # right=
        #   key1 key2   C   D
        # 0   K0   K0  C0  D0
        # 1   K1   K0  C1  D1
        # 2   K1   K0  C2  D2
        # 3   K2   K0  C3  D3

        merged = pd.merge(left, right, how='left', on=["key1", "key2"])
        print('\nmerged(left)=', merged, sep='\n')
        # merged(left)=
        #   key1 key2   A   B    C    D
        # 0   K0   K0  A0  B0   C0   D0
        # 1   K0   K1  A1  B1  NaN  NaN
        # 2   K1   K0  A2  B2   C1   D1
        # 3   K1   K0  A2  B2   C2   D2
        # 4   K2   K1  A3  B3  NaN  NaN

        merged = pd.merge(left, right, how='right', on=["key1", "key2"])
        print('\nmerged(right)=', merged, sep='\n')
        # merged(right)=
        #   key1 key2    A    B   C   D
        # 0   K0   K0   A0   B0  C0  D0
        # 1   K1   K0   A2   B2  C1  D1
        # 2   K1   K0   A2   B2  C2  D2
        # 3   K2   K0  NaN  NaN  C3  D3

        merged = pd.merge(left, right, how='inner', on=["key1", "key2"])
        print('\nmerged(inner)=', merged, sep='\n')
        # merged(inner)=
        #   key1 key2   A   B   C   D
        # 0   K0   K0  A0  B0  C0  D0
        # 1   K1   K0  A2  B2  C1  D1
        # 2   K1   K0  A2  B2  C2  D2

        merged = pd.merge(left, right, how='outer', on=["key1", "key2"])
        print('\nmerged(outer)=', merged, sep='\n')
        # merged(outer)=
        #   key1 key2    A    B    C    D
        # 0   K0   K0   A0   B0   C0   D0
        # 1   K0   K1   A1   B1  NaN  NaN
        # 2   K1   K0   A2   B2   C1   D1
        # 3   K1   K0   A2   B2   C2   D2
        # 4   K2   K1   A3   B3  NaN  NaN
        # 5   K2   K0  NaN  NaN   C3   D3

        merged = pd.merge(left, right, how='cross') # cartesian product
        print('\nmerged(cross)=', merged, sep='\n')
        # merged(cross)=
        #    key1_x key2_x   A   B key1_y key2_y   C   D
        # 0      K0     K0  A0  B0     K0     K0  C0  D0
        # 1      K0     K0  A0  B0     K1     K0  C1  D1
        # 2      K0     K0  A0  B0     K1     K0  C2  D2
        # 3      K0     K0  A0  B0     K2     K0  C3  D3
        # 4      K0     K1  A1  B1     K0     K0  C0  D0
        # 5      K0     K1  A1  B1     K1     K0  C1  D1
        # 6      K0     K1  A1  B1     K1     K0  C2  D2
        # 7      K0     K1  A1  B1     K2     K0  C3  D3
        # 8      K1     K0  A2  B2     K0     K0  C0  D0
        # 9      K1     K0  A2  B2     K1     K0  C1  D1
        # 10     K1     K0  A2  B2     K1     K0  C2  D2
        # 11     K1     K0  A2  B2     K2     K0  C3  D3
        # 12     K2     K1  A3  B3     K0     K0  C0  D0
        # 13     K2     K1  A3  B3     K1     K0  C1  D1
        # 14     K2     K1  A3  B3     K1     K0  C2  D2
        # 15     K2     K1  A3  B3     K2     K0  C3  D3


if False:
    # ---------------------------------
    # - DataFrame.join(
    #       other, on=None, how='left', lsuffix='', rsuffix='', sort=False,
    #       validate=None
    #   )
    # ; join columns of another dataframe.
    # ; on : column or index level name(s) in the caller to join on the index in other
    # ; how{'left', 'right', 'outer', 'inner', 'cross'}, default 'left'

    if False:
        left = pd.DataFrame(
            {"A": ["A0", "A1", "A2"], "B": ["B0", "B1", "B2"]}, index=["K0", "K1", "K2"]
        )
        right = pd.DataFrame(
            {"C": ["C0", "C2", "C3"], "D": ["D0", "D2", "D3"]}, index=["K0", "K2", "K3"]
        )
        print('\nleft=', left, sep='\n')
        print('\nright=', right, sep='\n')
        # left=
        #      A   B
        # K0  A0  B0
        # K1  A1  B1
        # K2  A2  B2
        # 
        # right=
        #      C   D
        # K0  C0  D0
        # K2  C2  D2
        # K3  C3  D3

        joined = left.join(right, how='left')
        print('\njoined(left)=', joined, sep='\n')
        # joined(left)=
        #      A   B    C    D
        # K0  A0  B0   C0   D0
        # K1  A1  B1  NaN  NaN
        # K2  A2  B2   C2   D2

        joined = left.join(right, how='right')
        print('\njoined(right)=', joined, sep='\n')
        # joined(right)=
        #       A    B   C   D
        # K0   A0   B0  C0  D0
        # K2   A2   B2  C2  D2
        # K3  NaN  NaN  C3  D3

        joined = left.join(right, how='inner')
        print('\njoined(inner)=', joined, sep='\n')
        # joined(inner)=
        #      A   B   C   D
        # K0  A0  B0  C0  D0
        # K2  A2  B2  C2  D2

        joined = left.join(right, how='outer')
        print('\njoined(outer)=', joined, sep='\n')
        # joined(outer)=
        #       A    B    C    D
        # K0   A0   B0   C0   D0
        # K1   A1   B1  NaN  NaN
        # K2   A2   B2   C2   D2
        # K3  NaN  NaN   C3   D3

    # joining key columns on an index - (1)
    if False:
        left = pd.DataFrame({
            "A": ["A0", "A1", "A2", "A3"],
            "B": ["B0", "B1", "B2", "B3"],
            "key": ["K0", "K1", "K0", "K1"],
        })
        right = pd.DataFrame({
            "C": ["C0", "C1"], "D": ["D0", "D1"]},
            index=["K0", "K1"]
        )
        print('\nleft=', left, sep='\n')
        print('\nright=', right, sep='\n')
        # left=
        #     A   B key
        # 0  A0  B0  K0
        # 1  A1  B1  K1
        # 2  A2  B2  K0
        # 3  A3  B3  K1
        # 
        # right=
        #      C   D
        # K0  C0  D0
        # K1  C1  D1

        joined = left.join(right, on="key")
        print('\njoined=', joined, sep='\n')
        # joined=
        #     A   B key   C   D
        # 0  A0  B0  K0  C0  D0
        # 1  A1  B1  K1  C1  D1
        # 2  A2  B2  K0  C0  D0
        # 3  A3  B3  K1  C1  D1

    # joining multiple keys columns on an index - (2)
    if True:
        left = pd.DataFrame({
            "A": ["A0", "A1", "A2", "A3"],
            "B": ["B0", "B1", "B2", "B3"],
            "key1": ["K0", "K0", "K1", "K2"],
            "key2": ["K0", "K1", "K0", "K1"],
        })

        index = pd.MultiIndex.from_tuples(
            [("K0", "K0"), ("K1", "K0"), ("K2", "K0"), ("K2", "K1")]
        )

        right = pd.DataFrame({
            "C": ["C0", "C1", "C2", "C3"],
            "D": ["D0", "D1", "D2", "D3"]}, index=index
        )
        print('\nleft=', left, sep='\n')
        print('\nright=', right, sep='\n')
        # left=
        #     A   B key1 key2
        # 0  A0  B0   K0   K0
        # 1  A1  B1   K0   K1
        # 2  A2  B2   K1   K0
        # 3  A3  B3   K2   K1
        # 
        # right=
        #         C   D
        # K0 K0  C0  D0
        # K1 K0  C1  D1
        # K2 K0  C2  D2
        # K2 K1  C3  D3

        joined = left.join(right, on=['key1', 'key2'])
        print('\njoined=', joined, sep='\n')
        # joined=
        #     A   B key1 key2    C    D
        # 0  A0  B0   K0   K0   C0   D0
        # 1  A1  B1   K0   K1  NaN  NaN
        # 2  A2  B2   K1   K0   C1   D1
        # 3  A3  B3   K2   K1   C3   D3


if False:
    # ---------------------------------
    # - DataFrame.compare(
    #       other, align_axis=1, keep_shape=False, keep_equal=False,
    #       result_names=('self', 'other')
    #   )
    # ; compare to another dataframe and show the differences.
    df1 = pd.DataFrame({
        "col1": ["a", "a", "b", "b", "a"],
        "col2": [1.0, 2.0, 3.0, np.nan, 5.0],
        "col3": [1.0, 2.0, 3.0, 4.0, 5.0]},
        columns=["col1", "col2", "col3"],
    )
    df2 = df1.copy()
    df2.loc[0, 'col1'] = 'c'
    df2.loc[2, 'col3'] = 4.0
    print('\ndf1=', df1, sep='\n')
    print('\ndf2=', df2, sep='\n')
    # df1=
    #   col1  col2  col3
    # 0    a   1.0   1.0
    # 1    a   2.0   2.0
    # 2    b   3.0   3.0
    # 3    b   NaN   4.0
    # 4    a   5.0   5.0
    # 
    # df2=
    #   col1  col2  col3
    # 0    c   1.0   1.0
    # 1    a   2.0   2.0
    # 2    b   3.0   4.0
    # 3    b   NaN   4.0
    # 4    a   5.0   5.0

    compared = df1.compare(df2, align_axis=0, result_names=('df1', 'df2'))
    print('\ncompared=', compared, sep='\n')
    # compared=
    #       col1  col3
    # 0 df1    a   NaN
    #   df2    c   NaN
    # 2 df1  NaN   3.0
    #   df2  NaN   4.0

    compared = df1.compare(df2, align_axis=1, result_names=('df1', 'df2'))
    print('\ncompared=', compared, sep='\n')
    # compared=
    #   col1      col3
    #    df1  df2  df1  df2
    # 0    a    c  NaN  NaN
    # 2  NaN  NaN  3.0  4.0

    compared = df1.compare(df2, align_axis=0, keep_shape=True, result_names=('df1', 'df2'))
    print('\ncompared=', compared, sep='\n')
    # compared=
    #       col1  col2  col3
    # 0 df1    a   NaN   NaN
    #   df2    c   NaN   NaN
    # 1 df1  NaN   NaN   NaN
    #   df2  NaN   NaN   NaN
    # 2 df1  NaN   NaN   3.0
    #   df2  NaN   NaN   4.0
    # 3 df1  NaN   NaN   NaN
    #   df2  NaN   NaN   NaN
    # 4 df1  NaN   NaN   NaN
    #   df2  NaN   NaN   NaN

    compared = df1.compare(df2, align_axis=1, keep_shape=True, result_names=('df1', 'df2'))
    print('\ncompared=', compared, sep='\n')
    # compared=
    #   col1      col2     col3
    #    df1  df2  df1 df2  df1  df2
    # 0    a    c  NaN NaN  NaN  NaN
    # 1  NaN  NaN  NaN NaN  NaN  NaN
    # 2  NaN  NaN  NaN NaN  3.0  4.0
    # 3  NaN  NaN  NaN NaN  NaN  NaN
    # 4  NaN  NaN  NaN NaN  NaN  NaN
