#!/usr/bin/env python
# -*- coding:utf-8 -*-
# vim: ft=python ts=4 sw=4 tw=78 expandtab
# ----------------------------------------------------------------------------
# - file : lib__pandas.20_time_series_and_date_functionality.py
# - author : yc0325lee
# - created : 2023-05-06 21:13:47 by yc032
# - modified : 2023-05-06 21:13:47 by yc032
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


if True:
    # -------------------------------------
    # - pandas.date_range(
    #       start=None, end=None, periods=None, freq=None, tz=None,
    #       normalize=False, name=None, inclusive='both', *, unit=None,
    #       **kwargs
    #   )
    # ; return a fixed frequency datetimeindex.
    ranges = pd.date_range("1/1/2023", periods=365)
    scores = pd.DataFrame(
        data=np.random.randint(0, 101, size=len(ranges)*3).reshape(len(ranges), 3),
        index=ranges, columns=['korean', 'english', 'math']
    )
    print("\nscores.info()="); scores.info() # <class 'pandas.core.frame.DataFrame'>
    print("\nscores.describe()=",
        scores.describe(percentiles=[0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]),
        sep='\n'
    )
    print('\nscores=', scores, sep='\n')

    # scores.info()=
    # <class 'pandas.core.frame.DataFrame'>
    # DatetimeIndex: 365 entries, 2023-01-01 to 2023-12-31
    # Freq: D
    # Data columns (total 3 columns):
    #  #   Column   Non-Null Count  Dtype
    # ---  ------   --------------  -----
    #  0   korean   365 non-null    int32
    #  1   english  365 non-null    int32
    #  2   math     365 non-null    int32
    # dtypes: int32(3)
    # memory usage: 7.1 KB
    #
    # scores.describe()=
    #            korean     english        math
    # count  365.000000  365.000000  365.000000
    # mean    49.717808   49.736986   50.441096
    # std     30.915604   29.161484   30.135864
    # min      0.000000    0.000000    0.000000
    # 10%      7.000000   11.000000    8.000000
    # 20%     17.000000   20.000000   20.000000
    # 30%     27.200000   30.200000   29.000000
    # 40%     37.000000   39.600000   40.600000
    # 50%     51.000000   50.000000   51.000000
    # 60%     60.000000   58.400000   61.000000
    # 70%     71.800000   66.000000   69.800000
    # 80%     85.000000   83.200000   81.000000
    # 90%     92.000000   91.000000   93.000000
    # max    100.000000  100.000000  100.000000
    # 
    # scores=
    #             korean  english  math
    # 2023-01-01      51       92    14
    # 2023-01-02      71       60    20
    # 2023-01-03      82       86    74
    # 2023-01-04      74       87    99
    # 2023-01-05      23        2    21
    # ...            ...      ...   ...
    # 2023-12-27      18       83    96
    # 2023-12-28      19       11    46
    # 2023-12-29       0       89    13
    # 2023-12-30      63       37    36
    # 2023-12-31      10       99    76
    # 
    # [365 rows x 3 columns]
