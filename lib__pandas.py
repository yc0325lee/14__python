#!/usr/bin/env python
# -*- coding:utf-8 -*-
# vim: ft=python ts=4 sw=4 tw=78 expandtab
# ----------------------------------------------------------------------------
# - file : lib__pandas.py
# - author : yc0325lee
# - created : 2022-12-07 23:52:53 by yc032
# - modified : 2022-12-07 23:52:53 by yc032
# - description : 
# - references
# ; https://pandas.pydata.org/docs/index.html
# ----------------------------------------------------------------------------
import os, os.path, sys
import random
import csv
import pickle
import numpy as np
np.random.seed(19680801) # seed-ing
import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd


if False:
    # ------------------------------------------------------------------------
    # - class pandas.Series(
    #       data=None, index=None, dtype=None, name=None, copy=False,
    #       fastpath=False
    #   )
    # ; 1D labeled homogeneously-typed array
    # ; one-dimensional ndarray with axis labels (including time series).
    #
    # - class pandas.DataFrame(
    #       data=None, index=None, columns=None, dtype=None, copy=None
    #   )
    # ; General 2D labeled, size-mutable tabular structure with potentially
    #   heterogeneously-typed column
    # ; two-dimensional, size-mutable, potentially heterogeneous tabular data.
    # ; attributes - data, index, columns, dtype, copy
    # ; axis = 0 -> index, axis =1 -> column
    #
    # - Comments
    # ; DataFrame is a container for Series, and Series is a container for scalars
    # ------------------------------------------------------------------------
    pass


if False:
    # ------------------------------------------------------------------------
    # - Viewing data
    # ; print(dataframe), print(series)
    # ; head(), tail(), info(), describe()
    #
    # - DataFrame.head(n=5)
    # ; Return the first n rows.
    # - DataFrame.tail(n=5)
    # ; Return the last n rows.
    #
    # - DataFrame.describe(percentiles=None, include=None, exclude=None)
    # ; generate descriptive statistics.
    # ; percentiles=[.25, .5, .75]
    #   dataframe.describe(percentiles=[0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9])
    # ------------------------------------------------------------------------
    pass


if False:
    # ------------------------------------------------------------------------
    # - getting column or row
    # ; column = dataframe["age"] # -> series
    #   column = dataframe.age # same as above
    # ; row = dataframe[0:2] # -> dataframe
    #
    # - selection by label
    # ; dataframe.loc()
    #   access a group of rows and columns by label(s) or a boolean array.
    #   single label -> returns the row as a series
    #   list of labels, using [[]] -> returns a dataframe
    # ; dataframe.at()
    #   access a single value for a row/column label pair
    # 
    # - selection by position
    # ; dataframe.iloc()
    #   purely integer-location based indexing for selection by position.
    # ; dataframe.iat()
    #   access a single value for a row/column pair by integer position.
    # ------------------------------------------------------------------------
    pass


if False:
    # ------------------------------------------------------------------------
    # - DataFrame.sort_index(
    #       *, axis=0, level=None, ascending=True, inplace=False,
    #       kind='quicksort', na_position='last', sort_remaining=True,
    #       ignore_index=False, key=None
    #   )
    # ; sort object by labels (along an axis)
    # ; returns a new dataframe sorted by label if inplace argument is false,
    #   otherwise updates the original dataframe and returns none.
    # 
    # - DataFrame.sort_values(
    #       by, *, axis=0, ascending=True, inplace=False, kind='quicksort',
    #       na_position='last', ignore_index=False, key=None
    #   )
    # ; sort by the values along either axis.
    # ------------------------------------------------------------------------
    pass


if False:
    # ------------------------------------------------------------------------
    # - DataFrame.hist(
    #       column=None, by=None, grid=True, xlabelsize=None, xrot=None,
    #       ylabelsize=None, yrot=None, ax=None, sharex=False, sharey=False,
    #       figsize=None, layout=None, bins=10, backend=None, legend=False,
    #       **kwargs
    #   )
    # ; make a histogram of the dataframe’s columns.
    # ------------------------------------------------------------------------
    pass

if False:
    # ------------------------------------------------------------------------
    # - Series.value_counts(
    #       normalize=False, sort=True, ascending=False, bins=None,
    #       dropna=True
    #   )
    # ; return a series containing counts of unique values.
    # ------------------------------------------------------------------------
    size = 128
    dataframe = pd.DataFrame(
        {'col0': [chr(random.randint(97, 106)) for _ in range(size)],
         'col1': [chr(random.randint(97, 106)) for _ in range(size)],
         'col2': [chr(random.randint(97, 106)) for _ in range(size)],
         'col3': [chr(random.randint(97, 106)) for _ in range(size)]},
        index=range(size)
    )
    print("\ndataframe=", dataframe, sep='\n')

    print("\ncol0_counts=", dataframe.value_counts("col0").sort_index(), sep='\n')
    print("\ncol1_counts=", dataframe.value_counts("col1").sort_index(), sep='\n')
    print("\ncol2_counts=", dataframe.value_counts("col2").sort_index(), sep='\n')
    print("\ncol3_counts=", dataframe.value_counts("col3").sort_index(), sep='\n')
    # col0_counts=
    # col0
    # a     9
    # b    19
    # c    10
    # d    12
    # e    13
    # f    10
    # g    16
    # h    11
    # i    18
    # j    10
    # dtype: int64
    pass

if False:
    # ------------------------------------------------------------------------
    # - descriptive statistics
    #   +------------+----------------------------------------------+
    #   | function   | description                                  |
    #   +------------+----------------------------------------------+
    #   |  count     |  number of non-na observations               |
    #   |  sum       |  sum of values                               |
    #   |  mean      |  mean of values                              | -> average
    #   |  median    |  arithmetic median of values                 | -> median value
    #   |  min       |  minimum                                     |
    #   |  max       |  maximum                                     |
    #   |  mode      |  mode                                        |
    #   |  abs       |  absolute value                              |
    #   |  prod      |  product of values                           |
    #   |  std       |  bessel-corrected sample standard deviation  |
    #   |  var       |  unbiased variance                           |
    #   |  sem       |  standard error of the mean                  |
    #   |  skew      |  sample skewness (3rd moment)                |
    #   |  kurt      |  sample kurtosis (4th moment)                |
    #   |  quantile  |  sample quantile (value at %)                |
    #   |  cumsum    |  cumulative sum                              |
    #   |  cumprod   |  cumulative product                          |
    #   |  cummax    |  cumulative maximum                          |
    #   |  cummin    |  cumulative minimum                          |
    #   +------------+----------------------------------------------+
    #
    # - DataFrame.mean(axis=0, skipna=True, numeric_only=True, **kwargs)
    # ; return the mean of the values over the requested axis.
    # ; axis{'index' (0), 'columns' (1)}
    # ------------------------------------------------------------------------
    size = 16
    dataframe = pd.DataFrame(
        {'col0': [chr(random.randint(97, 122)) for _ in range(size)],
         'col1': [chr(random.randint(97, 122)) for _ in range(size)],
         'col2': [chr(random.randint(97, 122)) for _ in range(size)],
         'col3': [chr(random.randint(97, 122)) for _ in range(size)]},
        index=range(size)
    )
    print("\ndataframe=", dataframe, sep='\n')

    print("\nmin(axis=0)=", dataframe.min(axis=0), sep='\n')
    print("\nmax(axis=0)=", dataframe.max(axis=0), sep='\n')
    # min(axis=0)=     max(axis=0)=  
    # col0    a        col0    z     
    # col1    c        col1    y     
    # col2    a        col2    y     
    # col3    b        col3    z     
    # dtype: object    dtype: object 

    print("\nmin(axis=1)=", dataframe.min(axis=1), sep='\n')
    print("\nmax(axis=1)=", dataframe.max(axis=1), sep='\n')
    # min(axis=1)=     max(axis=1)= 
    # 0     a          0     s      
    # 1     h          1     u      
    # 2     m          2     z      
    # 3     b          3     y      
    # 4     c          4     s      
    # 5     e          5     v      
    # 6     e          6     r      
    # 7     a          7     y      
    # 8     d          8     x      
    # 9     b          9     z      
    # 10    g          10    w      
    # 11    i          11    u      
    # 12    g          12    v      
    # 13    g          13    y      
    # 14    c          14    y      
    # 15    c          15    s      
    # dtype: object    dtype: object
    pass

if True:
    # ------------------------------------------------------------------------
    # - DataFrame.isin(values)
    # ; whether each element in the dataframe is contained in values.
    # ; values : iterable, Series, DataFrame or dict
    # ------------------------------------------------------------------------
    size = 8
    dataframe = pd.DataFrame(
        {'col0': [chr(random.randint(97, 122)) for _ in range(size)],
         'col1': [chr(random.randint(97, 122)) for _ in range(size)],
         'col2': [chr(random.randint(97, 122)) for _ in range(size)],
         'col3': [chr(random.randint(97, 122)) for _ in range(size)]},
        index=range(size)
    )
    print("\ndataframe=", dataframe, sep='\n')
    # dataframe=
    #   col0 col1 col2 col3
    # 0    a    u    u    h
    # 1    l    f    s    q
    # 2    b    q    j    g
    # 3    v    c    q    i
    # 4    l    u    m    e
    # 5    q    s    d    r
    # 6    j    g    d    a
    # 7    j    u    l    f

    within = dataframe.isin(['a', 'e', 'i', 'o', 'u'])
    print("\nwithin=", within, sep='\n')
    # within=
    #     col0   col1   col2   col3
    # 0   True   True   True  False
    # 1  False  False  False  False
    # 2  False  False  False  False
    # 3  False  False  False   True
    # 4  False   True  False   True
    # 5  False  False  False  False
    # 6  False  False  False   True
    # 7  False   True  False  False

    pass

if False:
    # ------------------------------------------------------------------------
    # - DataFrame.isnull()
    # ; dataframe.isnull is an alias for dataframe.isna.
    # - DataFrame.isna()
    # ; detect missing values.
    # ; return a boolean same-sized object indicating if the values are na. 
    # ------------------------------------------------------------------------
    pass

if False:
    # ------------------------------------------------------------------------
    # - DataFrame.groupby(
    #       by=None, axis=0, level=None, as_index=True, sort=True,
    #       group_keys=True, observed=False, dropna=True
    #   )
    # ; group dataframe using a mapper or by a series of columns.
    # ------------------------------------------------------------------------
    pass


if False:
    # ------------------------------------------------------------------------
    # - DataFrame.all(axis=0, bool_only=None, skipna=True, **kwargs)
    # ; return whether all elements are true, potentially over an axis.
    #
    # - DataFrame.any(
    #       *, axis=0, bool_only=None, skipna=True, level=None, **kwargs
    #   )
    # ; return whether any element is true, potentially over an axis.
    # ; axis=0
    #   0 / ‘index’ : reduce the index, return a Series whose index is the
    #   original column labels.
    # ; 1 / ‘columns’ : reduce the columns, return a Series whose index is the
    #   original index.
    #   None : reduce all axes, return a scalar.
    # ------------------------------------------------------------------------
    dataframe = pd.DataFrame(
        {'col0': [True, True, True],
         'col1': [True, True, False],
         'col2': [True, False, False],
         'col3': [False, False, False]},
        index=[0, 1, 2]
    )
    print("\ndataframe=", dataframe, sep='\n')
    # dataframe=
    #    col0   col1   col2   col3
    # 0  True   True   True  False
    # 1  True   True  False  False
    # 2  True  False  False  False

    #print(dataframe.all()) # axis='index'(default)
    #print(dataframe.any()) # axis='index'(default)
    #         "all"    "any"
    # col0     True     True
    # col1    False     True
    # col2    False     True
    # col3    False    False

    print(dataframe.all(axis=1)) # axis='columns'
    print(dataframe.any(axis=1)) # axis='columns'
    #      "all"    "any"
    # 0    False    True
    # 1    False    True
    # 2    False    True

if False:
    # ------------------------------------------------------------------------
    # - DataFrame.dropna(
    #       *, axis=0, how=_NoDefault.no_default,
    #       thresh=_NoDefault.no_default, subset=None, inplace=False
    #   )
    # ; remove missing values.
    # ; axis=0
    #   0 or 'index', 1 or 'columns'
    # ; subset=None
    #   column label or sequence of labels, optional
    #   labels along other axis to consider, e.g. if you are dropping rows
    #   these would be a list of columns to include.
    #
    # - DataFrame.fillna(
    #       value=None, *, method=None, axis=None, inplace=False, limit=None,
    #       downcast=None
    #   )
    # ; fill na/nan values using the specified method.
    # ; value to use to fill holes (e.g. 0), alternately a dict/series/dataframe
    #   of values specifying which value to use for each index (for a series)
    #   or column (for a dataframe).
    # ------------------------------------------------------------------------
    pass

if False:
    # ------------------------------------------------------------------------
    # - DataFrame.drop(
    #       labels=None, *, axis=0, index=None, columns=None, level=None,
    #       inplace=False, errors='raise'
    #   )
    # ; drop specified labels from rows or columns.
    # ; if inplace=False, return a copy.
    #   otherwise, do operation inplace and return none.
    # ------------------------------------------------------------------------
    pass

if False:
    # ------------------------------------------------------------------------
    # - pandas.concat(
    #       objs, *, axis=0, join='outer', ignore_index=False, keys=None,
    #       levels=None, names=None, verify_integrity=False, sort=False,
    #       copy=True
    #   )
    # ; concatenate pandas objects along a particular axis.
    # ------------------------------------------------------------------------
    df1 = pd.DataFrame([['a', 1], ['b', 2]], columns=['letter', 'number'])
    df2 = pd.DataFrame([['c', 3], ['d', 4]], columns=['letter', 'number'])
    print('df1=', df1, sep='\n')
    print('df2=', df2, sep='\n')
    # df1=
    #   letter  number
    # 0      a       1
    # 1      b       2
    #
    # df2=
    #   letter  number
    # 0      c       3
    # 1      d       4

    df3 = pd.concat([df1, df2], axis=0, ignore_index=True)
    print('df3='); print(df3)
    # df3=
    #   letter  number
    # 0      a       1
    # 1      b       2
    # 2      c       3
    # 3      d       4

    df1 = pd.DataFrame([['a', 1], ['b', 2]], columns=['letter', 'number'])
    df2 = pd.DataFrame([['c', 3], ['d', 4]], columns=['column3', 'column4'])
    print('df1='); print(df1)
    print('df2='); print(df2)
    # df1=
    #   letter  number
    # 0      a       1
    # 1      b       2
    #
    # df2=
    #   letter  number
    # 0      c       3
    # 1      d       4

    df3 = pd.concat([df1, df2], axis=1)
    print('df3='); print(df3)
    # df3=
    #   letter  number column3  column4
    # 0      a       1       c        3
    # 1      b       2       d        4

if False:
    # - pandas.plotting.scatter_matrix(
    #       frame, alpha=0.5, figsize=None, ax=None, grid=False,
    #       diagonal='hist', marker='.', density_kwds=None, hist_kwds=None,
    #       range_padding=0.05, **kwargs
    #   )
    # ; draw a matrix of scatter plots.
    pass

if False:
    # ------------------------------------------------------------------------
    # - DataFrame.to_csv(
    #       path_or_buf=None, sep=',', na_rep='', float_format=None,
    #       columns=None, header=True, index=True, index_label=None, mode='w',
    #       encoding=None, compression='infer', quoting=None, quotechar='"',
    #       lineterminator=None, chunksize=None, date_format=None,
    #       doublequote=True, escapechar=None, decimal='.', errors='strict',
    #       storage_options=None
    #   )
    # ; write object to a comma-separated values (csv) file.
    # ------------------------------------------------------------------------
    pass

if False:
    # ------------------------------------------------------------------------
    # - pandas.cut(
    #       x, bins, right=True, labels=None, retbins=False, precision=3,
    #       include_lowest=False, duplicates='raise', ordered=True
    #   )
    # ; bin values into discrete intervals.
    # ; returns an array-like object representing the respective bin for each value of x
    # ------------------------------------------------------------------------
    pass


if False:
    # ------------------------------------------------------------------------
    # - DataFrame.nlargest(n, columns, keep='first')
    # ; return the first n rows ordered by columns in descending order.
    # ; equivalent to dataframe.sort_values(columns, ascending=False).head(n),
    #   but more performant.
    #
    # - DataFrame.nsmallest(n, columns, keep='first')
    # ; return the first n rows ordered by columns in ascending order.
    # ; equivalent to dataframe.sort_values(columns, ascending=True).head(n),
    #   but more performant.
    # ------------------------------------------------------------------------
    pass
