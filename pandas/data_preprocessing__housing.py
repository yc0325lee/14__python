#!/usr/bin/env python
# -*- coding:utf-8 -*-
# vim: ft=python ts=4 sw=4 tw=78 expandtab
# ----------------------------------------------------------------------------
# - file : 02_end_to_end_demo.py
# - author : yc0325lee
# - created : 2022-12-23 23:06:54 by yc032
# - modified : 2022-12-23 23:06:54 by yc032
# - description :
# ----------------------------------------------------------------------------
import os, os.path, sys
import random
import csv
import pickle
import numpy as np
np.random.seed(42)
import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd


if False:
    # ------------------------------------------------------------------------
    # - class pandas.DataFrame(
    #       data=None, index=None, columns=None, dtype=None, copy=None
    #   )
    # ; two-dimensional, size-mutable, potentially heterogeneous tabular data.
    # ; attributes - data, index, columns, dtype, copy
    #
    # - class pandas.Series(
    #       data=None, index=None, dtype=None, name=None, copy=False,
    #       fastpath=False
    #   )
    # ; one-dimensional ndarray with axis labels (including time series).
    # ------------------------------------------------------------------------
    pass


# -------------------------------------
# - pandas.read_csv()
# ; read a comma-separated values (csv) file into dataframe.
# - DataFrame.to_csv()
# ; write dataframe to a comma-separated values (csv) file.
filename = os.path.join('datasets', 'housing', 'housing_in.csv')
print('[info] reading file {} ...'.format(filename))
dataframe = pd.read_csv(filename)
print(dataframe)
#        longitude  latitude  housing_median_age  total_rooms  total_bedrooms  population  households  median_income  median_house_value ocean_proximity
# 0        -122.23     37.88                41.0        880.0           129.0       322.0       126.0         8.3252            452600.0        NEAR BAY
# 1        -122.22     37.86                21.0       7099.0          1106.0      2401.0      1138.0         8.3014            358500.0        NEAR BAY
# 2        -122.24     37.85                52.0       1467.0           190.0       496.0       177.0         7.2574            352100.0        NEAR BAY
# 3        -122.25     37.85                52.0       1274.0           235.0       558.0       219.0         5.6431            341300.0        NEAR BAY
# 4        -122.25     37.85                52.0       1627.0           280.0       565.0       259.0         3.8462            342200.0        NEAR BAY
# ...          ...       ...                 ...          ...             ...         ...         ...            ...                 ...             ...
# 20635    -121.09     39.48                25.0       1665.0           374.0       845.0       330.0         1.5603             78100.0          INLAND
# 20636    -121.21     39.49                18.0        697.0           150.0       356.0       114.0         2.5568             77100.0          INLAND
# 20637    -121.22     39.43                17.0       2254.0           485.0      1007.0       433.0         1.7000             92300.0          INLAND
# 20638    -121.32     39.43                18.0       1860.0           409.0       741.0       349.0         1.8672             84700.0          INLAND
# 20639    -121.24     39.37                16.0       2785.0           616.0      1387.0       530.0         2.3886             89400.0          INLAND
#
# [20640 rows x 10 columns]

if False:
    filename = 'housing_out.csv'
    print('[info] writing file {} ...'.format(filename))
    dataframe.to_csv(filename, index=False)


if False:
    # -------------------------------------
    # - pandas.read_json()
    # ; convert a json string to pandas object.
    # - DataFrame.to_json()
    # ; convert the object to a json string.
    filename = os.path.join('datasets', 'housing', 'housing_in.json')
    print('[info] reading file {} ...'.format(filename))
    dataframe = pd.read_json(filename, orient='columns')
    print(dataframe)

    filename = 'housing_out.json'
    print('[info] writing file {} ...'.format(filename))
    dataframe.to_json(filename, orient='columns')


if False:
    # -------------------------------------
    # - pandas.read_excel()
    # ; read an excel file into a pandas dataframe.
    # - DataFrame.to_excel()
    # ; convert the object to a json string.
    filename = os.path.join('datasets', 'housing', 'housing_in.xlsx')
    print('[info] reading file {} ...'.format(filename))
    dataframe = pd.read_excel(filename, index_col=None)
    print(dataframe)

    filename = 'housing_out.xlsx'
    print('[info] writing file {} ...'.format(filename))
    dataframe.to_excel(filename, sheet_name='housing', index=False)


if False:
    # -------------------------------------
    # - DataFrame.head([n])
    # ; Return the first n rows.
    # - DataFrame.tail([n])
    # ; Return the last n rows.
    # - DataFrame.info()
    # ; Print a concise summary of a DataFrame.
    print('\ndataframe.head()=')
    print(dataframe.head())
    print('\ndataframe.tail()=')
    print(dataframe.tail())
    print('\ndataframe.info()=')
    dataframe.info()
    # dataframe.head()=
    #    longitude  latitude  housing_median_age  total_rooms  total_bedrooms  population  households  median_income  median_house_value ocean_proximity
    # 0    -122.23     37.88                41.0        880.0           129.0       322.0       126.0         8.3252            452600.0        NEAR BAY
    # 1    -122.22     37.86                21.0       7099.0          1106.0      2401.0      1138.0         8.3014            358500.0        NEAR BAY
    # 2    -122.24     37.85                52.0       1467.0           190.0       496.0       177.0         7.2574            352100.0        NEAR BAY
    # 3    -122.25     37.85                52.0       1274.0           235.0       558.0       219.0         5.6431            341300.0        NEAR BAY
    # 4    -122.25     37.85                52.0       1627.0           280.0       565.0       259.0         3.8462            342200.0        NEAR BAY
    # 
    # dataframe.tail()=
    #        longitude  latitude  housing_median_age  total_rooms  total_bedrooms  population  households  median_income  median_house_value ocean_proximity
    # 20635    -121.09     39.48                25.0       1665.0           374.0       845.0       330.0         1.5603             78100.0          INLAND
    # 20636    -121.21     39.49                18.0        697.0           150.0       356.0       114.0         2.5568             77100.0          INLAND
    # 20637    -121.22     39.43                17.0       2254.0           485.0      1007.0       433.0         1.7000             92300.0          INLAND
    # 20638    -121.32     39.43                18.0       1860.0           409.0       741.0       349.0         1.8672             84700.0          INLAND
    # 20639    -121.24     39.37                16.0       2785.0           616.0      1387.0       530.0         2.3886             89400.0          INLAND
    #
    # dataframe.info()=
    # <class 'pandas.core.frame.DataFrame'>
    # RangeIndex: 20640 entries, 0 to 20639
    # Data columns (total 10 columns):
    #  #   Column              Non-Null Count  Dtype
    # ---  ------              --------------  -----
    #  0   longitude           20640 non-null  float64
    #  1   latitude            20640 non-null  float64
    #  2   housing_median_age  20640 non-null  float64
    #  3   total_rooms         20640 non-null  float64
    #  4   total_bedrooms      20433 non-null  float64 ***
    #  5   population          20640 non-null  float64
    #  6   households          20640 non-null  float64
    #  7   median_income       20640 non-null  float64
    #  8   median_house_value  20640 non-null  float64
    #  9   ocean_proximity     20640 non-null  object  ***
    # dtypes: float64(9), object(1)
    # memory usage: 1.6+ MB


    # - DataFrame.describe(
    #       percentiles=None, include=None, exclude=None, datetime_is_numeric=False
    #   )
    # ; generate descriptive statistics.
    # ; percentiles=None -> default [.25, .5, .75]
    print('\ndataframe.describe()=')
    print(dataframe.describe(), end='\n\n')
    print(dataframe.describe(percentiles=[0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]))
    # dataframe.describe()=
    #           longitude      latitude  dataframe_median_age   total_rooms  total_bedrooms    population    households  median_income  median_house_value
    # count  20640.000000  20640.000000        20640.000000  20640.000000    20433.000000  20640.000000  20640.000000   20640.000000        20640.000000
    # mean    -119.569704     35.631861           28.639486   2635.763081      537.870553   1425.476744    499.539680       3.870671       206855.816909
    # std        2.003532      2.135952           12.585558   2181.615252      421.385070   1132.462122    382.329753       1.899822       115395.615874
    # min     -124.350000     32.540000            1.000000      2.000000        1.000000      3.000000      1.000000       0.499900        14999.000000
    # 25%     -121.800000     33.930000           18.000000   1447.750000      296.000000    787.000000    280.000000       2.563400       119600.000000
    # 50%     -118.490000     34.260000           29.000000   2127.000000      435.000000   1166.000000    409.000000       3.534800       179700.000000
    # 75%     -118.010000     37.710000           37.000000   3148.000000      647.000000   1725.000000    605.000000       4.743250       264725.000000
    # max     -114.310000     41.950000           52.000000  39320.000000     6445.000000  35682.000000   6082.000000      15.000100       500001.000000
    # [8 rows x 9 columns]


if False:
    # -------------------------------------
    # - Series.value_counts(
    #       normalize=False, sort=True, ascending=False, bins=None,
    #       dropna=True
    #   )
    # ; return a series containing counts of unique values.
    # ; normalize=True will contain the relative frequencies of the unique values.
    series = dataframe['ocean_proximity']
    print("\nseries.value_counts(normalize=False/True)=")
    print(series.value_counts(normalize=False), end='\n\n')
    print(series.value_counts(normalize=True))
    # series.value_counts(normalize=False/True)=
    # <1H OCEAN     9136                    |   <1H OCEAN     0.442636
    # INLAND        6551                    |   INLAND        0.317393
    # NEAR OCEAN    2658                    |   NEAR OCEAN    0.128779
    # NEAR BAY      2290                    |   NEAR BAY      0.110950
    # ISLAND           5                    |   ISLAND        0.000242
    # Name: ocean_proximity, dtype: int64   |   Name: ocean_proximity, dtype: float64


if False:
    # -------------------------------------
    # - DataFrame.hist(
    #       column=None, by=None, grid=True, xlabelsize=None, xrot=None,
    #       ylabelsize=None, yrot=None, ax=None, sharex=False, sharey=False,
    #       figsize=None, layout=None, bins=10, backend=None, legend=False,
    #       **kwargs
    #   )
    # ; make a histogram of the dataframe’s columns.
    # ; calls matplotlib.pyplot.hist(), on each series in the DataFrame, resulting in one histogram per column.
    dataframe.hist(bins=50, figsize=(20,15))
    index = 0
    filename = os.path.splitext(os.path.basename(__file__))[0] + '-{:02d}.png'.format(index)
    print('[info] writing file {} ...'.format(filename))
    plt.savefig(filename, bbox_inches="tight")
    #plt.show()
    plt.close()


if False:
    # -------------------------------------
    # - pandas.cut(
    #       x, bins, right=True, labels=None, retbins=False, precision=3,
    #       include_lowest=False, duplicates='raise', ordered=True
    #   )
    # ; bin values into discrete intervals.
    # ; returns an array-like object representing the respective bin for each value of x
    #
    # - stratified shuffled split
    # ; train/test dataset splitting
    series = dataframe["median_income"]
    series.hist(bins=100)
    index = 1
    filename = os.path.splitext(os.path.basename(__file__))[0] + '-{:02d}.png'.format(index)
    print('[info] writing file {} ...'.format(filename))
    plt.savefig(filename, bbox_inches="tight")
    #plt.show()
    plt.close()

    # categorizing 'median_income'
    categorized = pd.cut(
        dataframe["median_income"], bins=[0., 1.5, 3.0, 4.5, 6., np.inf], labels=[1, 2, 3, 4, 5]
    ) #                                   -----------------------------
    #categorized = pd.cut(
    #    dataframe["median_income"], bins=[0., 1.5, 3.0, 4.5, 6., np.inf], labels=['income1', 'income2', 'income3', 'income4', 'income5']
    #) #                                   -----------------------------
    dataframe['income_cat'] = categorized
    print(dataframe)

    print(categorized.value_counts(normalize=False, sort=False))
    print(categorized.value_counts(normalize=True, sort=False))
    # housing['income_cat'].value_counts()=
    # 1     822                       |  1    0.039826
    # 2    6581                       |  2    0.318847
    # 3    7236                       |  3    0.350581
    # 4    3639                       |  4    0.176308
    # 5    2362                       |  5    0.114438
    # Name: income_cat, dtype: int64  |  Name: income_cat, dtype: float64

    categorized.hist()
    index = 2
    filename = os.path.splitext(os.path.basename(__file__))[0] + '-{:02d}.png'.format(index)
    print('[info] writing file {} ...'.format(filename))
    plt.savefig(filename, bbox_inches="tight")
    #plt.show()
    plt.close()


if False:
    # -------------------------------------
    # visualization

    # show the concentration of data
    dataframe.plot(kind="scatter", x="longitude", y="latitude")
    plt.grid(visible=True, linestyle='dotted')
    index = 3
    filename = os.path.splitext(os.path.basename(__file__))[0] + '-{:02d}.png'.format(index)
    print('[info] writing file {} ...'.format(filename))
    plt.savefig(filename, bbox_inches="tight")
    #plt.show()
    plt.close()

    # - DataFrame.drop(
    #       labels=None, *, axis=0, index=None, columns=None, level=None,
    #       inplace=False, errors='raise'
    #   )
    # ; drop specified labels from rows or columns.
    # ; if inplace=False, return a copy.
    #   otherwise, do operation inplace and return none.
    interested = dataframe.drop(['median_house_value', 'ocean_proximity'], axis=1, inplace=False)
    print('\ninterested.head()=')
    print(interested.head())

    # correlation_matrix
    # - DataFrame.corr(
    #       method='pearson', min_periods=1, numeric_only=_NoDefault.no_default
    #   )
    # ; compute pairwise correlation of columns, excluding na/null values.
    corr_matrix = interested.corr()
    print('\ncorr_matrix=')
    print(corr_matrix)
    # corr_matrix=
    #                     longitude  latitude  housing_median_age  total_rooms  total_bedrooms  population  households  median_income
    # longitude            1.000000 -0.924664           -0.108197     0.044568        0.069608    0.099773    0.055310      -0.015176
    # latitude            -0.924664  1.000000            0.011173    -0.036100       -0.066983   -0.108785   -0.071035      -0.079809
    # housing_median_age  -0.108197  0.011173            1.000000    -0.361262       -0.320451   -0.296244   -0.302916      -0.119034
    # total_rooms          0.044568 -0.036100           -0.361262     1.000000        0.930380    0.857126    0.918484       0.198050
    # total_bedrooms       0.069608 -0.066983           -0.320451     0.930380        1.000000    0.877747    0.979728      -0.007723
    # population           0.099773 -0.108785           -0.296244     0.857126        0.877747    1.000000    0.907222       0.004834
    # households           0.055310 -0.071035           -0.302916     0.918484        0.979728    0.907222    1.000000       0.013033
    # median_income       -0.015176 -0.079809           -0.119034     0.198050       -0.007723    0.004834    0.013033       1.000000

    # - pandas.plotting.scatter_matrix(
    #       frame, alpha=0.5, figsize=None, ax=None, grid=False,
    #       diagonal='hist', marker='.', density_kwds=None, hist_kwds=None,
    #       range_padding=0.05, **kwargs
    #   )
    # ; draw a matrix of scatter plots.
    from pandas.plotting import scatter_matrix
    attributes = ["median_house_value", "median_income", "total_rooms", "housing_median_age"]
    scatter_matrix(dataframe[attributes], figsize=(15, 10), grid=True, hist_kwds=dict(bins=100))
    plt.grid(visible=True, linestyle='dotted')
    index = 4
    filename = os.path.splitext(os.path.basename(__file__))[0] + '-{:02d}-scatter_matrix.png'.format(index)
    print('[info] writing file {} ...'.format(filename))
    plt.savefig(filename, bbox_inches="tight")
    #plt.show()
    plt.close()


if False:
    # -------------------------------------
    # visualizing core attributes
    core_attrs = [
        'median_income', 'rooms_per_household', 'total_rooms',
        'housing_median_age', 'latitude', 'bedrooms_per_room'
    ]

    # adding new attributes
    dataframe["rooms_per_household"] = dataframe["total_rooms"] / dataframe["households"]
    dataframe["bedrooms_per_room"] = dataframe["total_bedrooms"] / dataframe["total_rooms"]

    print('\ndataframe.head()=')
    print(dataframe.head())

    for attr in core_attrs:
        dataframe.plot(kind="scatter", x=attr, y="median_house_value", alpha=0.2)
        plt.grid(visible=True, linestyle='dotted')
        index = 5
        filename = os.path.splitext(os.path.basename(__file__))[0] + '-{:02d}-{}.png'.format(index, attr)
        print('[info] writing file {} ...'.format(filename))
        plt.savefig(filename, bbox_inches="tight")
        #plt.show()
        plt.close()


if False:
    # -------------------------------------
    # purifying data

    # adding new attributes
    dataframe["rooms_per_household"] = dataframe["total_rooms"] / dataframe["households"]
    dataframe["bedrooms_per_room"] = dataframe["total_bedrooms"] / dataframe["total_rooms"]

    # DataFrame.isna() - detect missing values
    # DataFrame.isnull() - DataFrame.isnull is an alias for DataFrame.isna
    defected_rows = dataframe[dataframe.isnull().any(axis=1)]
    print('\ndefected_rows=')
    print(defected_rows)
    # defected_rows=
    #        longitude  latitude  housing_median_age  total_rooms  total_bedrooms  population  households  median_income  median_house_value ocean_proximity
    # 290      -122.16     37.77                47.0       1256.0             NaN       570.0       218.0         4.3750            161900.0        NEAR BAY
    # 341      -122.17     37.75                38.0        992.0             NaN       732.0       259.0         1.6196             85100.0        NEAR BAY
    # 538      -122.28     37.78                29.0       5154.0             NaN      3741.0      1273.0         2.5762            173400.0        NEAR BAY
    # 563      -122.24     37.75                45.0        891.0             NaN       384.0       146.0         4.9489            247100.0        NEAR BAY
    # 696      -122.10     37.69                41.0        746.0             NaN       387.0       161.0         3.9063            178400.0        NEAR BAY
    # ...          ...       ...                 ...          ...             ...         ...         ...            ...                 ...             ...
    # 20267    -119.19     34.20                18.0       3620.0             NaN      3171.0       779.0         3.3409            220500.0      NEAR OCEAN
    # 20268    -119.18     34.19                19.0       2393.0             NaN      1938.0       762.0         1.6953            167400.0      NEAR OCEAN
    # 20372    -118.88     34.17                15.0       4260.0             NaN      1701.0       669.0         5.1033            410700.0       <1H OCEAN
    # 20460    -118.75     34.29                17.0       5512.0             NaN      2734.0       814.0         6.6073            258100.0       <1H OCEAN
    # 20484    -118.72     34.28                17.0       3051.0             NaN      1705.0       495.0         5.7376            218600.0       <1H OCEAN
    # 
    # [207 rows x 10 columns]


    # (1) dropping all rows with n/a value
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
    dataframe_dropna = dataframe.dropna(subset=['total_bedrooms'])
    print('\ndataframe_dropna=')
    print(dataframe_dropna)


    # (2) dropping whole columns with Nan values
    dataframe_drop = dataframe.drop(columns=['total_bedrooms', 'bedrooms_per_room'], axis=1)
    print('\ndataframe_drop=')
    print(dataframe_drop)
    # dataframe_drop=
    #        longitude  latitude  housing_median_age  total_rooms  population  households  median_income  median_house_value ocean_proximity  rooms_per_household
    # 0        -122.23     37.88                41.0        880.0       322.0       126.0         8.3252            452600.0        NEAR BAY             6.984127
    # 1        -122.22     37.86                21.0       7099.0      2401.0      1138.0         8.3014            358500.0        NEAR BAY             6.238137
    # 2        -122.24     37.85                52.0       1467.0       496.0       177.0         7.2574            352100.0        NEAR BAY             8.288136
    # 3        -122.25     37.85                52.0       1274.0       558.0       219.0         5.6431            341300.0        NEAR BAY             5.817352
    # 4        -122.25     37.85                52.0       1627.0       565.0       259.0         3.8462            342200.0        NEAR BAY             6.281853
    # ...          ...       ...                 ...          ...         ...         ...            ...                 ...             ...                  ...
    # 20635    -121.09     39.48                25.0       1665.0       845.0       330.0         1.5603             78100.0          INLAND             5.045455
    # 20636    -121.21     39.49                18.0        697.0       356.0       114.0         2.5568             77100.0          INLAND             6.114035
    # 20637    -121.22     39.43                17.0       2254.0      1007.0       433.0         1.7000             92300.0          INLAND             5.205543
    # 20638    -121.32     39.43                18.0       1860.0       741.0       349.0         1.8672             84700.0          INLAND             5.329513
    # 20639    -121.24     39.37                16.0       2785.0      1387.0       530.0         2.3886             89400.0          INLAND             5.254717
    # 
    # [20640 rows x 10 columns]


    # (3) filling n/a cells with some values(zero, mean, median, etc)
    medians = { # median values
        'total_bedrooms' : dataframe['total_bedrooms'].median(),
        'bedrooms_per_room' : dataframe['bedrooms_per_room'].median(),
    }
    print('medians=', medians)
    # medians= {'total_bedrooms': 435.0, 'bedrooms_per_room': 0.20316243411595591}

    dataframe_filled = dataframe.copy()
    dataframe_filled.fillna(value=medians, inplace=True)
    print('\ndataframe_filled=')
    print(dataframe_filled)
    # dataframe_filled=
    #        longitude  latitude  housing_median_age  total_rooms  total_bedrooms  population  households  median_income  median_house_value ocean_proximity  rooms_per_household  bedrooms_per_room
    # 0        -122.23     37.88                41.0        880.0           129.0       322.0       126.0         8.3252            452600.0        NEAR BAY             6.984127           0.146591
    # 1        -122.22     37.86                21.0       7099.0          1106.0      2401.0      1138.0         8.3014            358500.0        NEAR BAY             6.238137           0.155797
    # 2        -122.24     37.85                52.0       1467.0           190.0       496.0       177.0         7.2574            352100.0        NEAR BAY             8.288136           0.129516
    # 3        -122.25     37.85                52.0       1274.0           235.0       558.0       219.0         5.6431            341300.0        NEAR BAY             5.817352           0.184458
    # 4        -122.25     37.85                52.0       1627.0           280.0       565.0       259.0         3.8462            342200.0        NEAR BAY             6.281853           0.172096
    # ...          ...       ...                 ...          ...             ...         ...         ...            ...                 ...             ...                  ...                ...
    # 20635    -121.09     39.48                25.0       1665.0           374.0       845.0       330.0         1.5603             78100.0          INLAND             5.045455           0.224625
    # 20636    -121.21     39.49                18.0        697.0           150.0       356.0       114.0         2.5568             77100.0          INLAND             6.114035           0.215208
    # 20637    -121.22     39.43                17.0       2254.0           485.0      1007.0       433.0         1.7000             92300.0          INLAND             5.205543           0.215173
    # 20638    -121.32     39.43                18.0       1860.0           409.0       741.0       349.0         1.8672             84700.0          INLAND             5.329513           0.219892
    # 20639    -121.24     39.37                16.0       2785.0           616.0      1387.0       530.0         2.3886             89400.0          INLAND             5.254717           0.221185
    # 
    # [20640 rows x 12 columns]


if False:
    # -------------------------------------
    # - handling text and categorical attributes
    medians = { # median values
        'total_bedrooms' : dataframe['total_bedrooms'].median(),
    }
    dataframe.fillna(value=medians, inplace=True)

    numericals = dataframe.drop('ocean_proximity', axis=1)
    categoricals = dataframe[['ocean_proximity']].copy()
    print('\nnumericals.head(10)=')
    print(numericals.head(10))
    print('\ncategoricals.head(10)=')
    print(categoricals.head(10))

    print(categoricals.value_counts(normalize=False, sort=False))
    print(categoricals.value_counts(normalize=True, sort=False))
    # ocean_proximity
    # <1H OCEAN          9136   0.442636
    # INLAND             6551   0.317393
    # ISLAND                5   0.000242
    # NEAR BAY           2290   0.110950
    # NEAR OCEAN         2658   0.128779
    # dtype: int64

    categorized = pd.cut(
        dataframe['ocean_proximity'], bins=['<1H OCEAN', 'INLAND', 'ISLAND', 'NEAR BAY', 'NEAR OCEAN'], labels=[1, 2, 3, 4, 5]
    )

    categorized.hist()
    index = 6
    filename = os.path.splitext(os.path.basename(__file__))[0] + '-{:02d}.png'.format(index)
    print('[info] writing file {} ...'.format(filename))
    plt.savefig(filename, bbox_inches="tight")
    #plt.show()
    plt.close()
