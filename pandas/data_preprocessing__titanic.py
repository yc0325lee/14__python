#!/usr/bin/env python
# -*- coding:utf-8 -*-
# vim: ft=python ts=4 sw=4 tw=78 expandtab
# ----------------------------------------------------------------------------
# - file : data_preprocessing__titanic.py
# - author : yc0325lee
# - created : 2023-04-04 22:43:07 by yc032
# - modified : 2023-04-04 22:43:07 by yc032
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
    # -------------------------------------
    # - dataset
    import seaborn as sns
    dataframe = sns.load_dataset('titanic')
    filename = os.path.join('datasets', 'titanic', 'titanic_in.csv')
    print('[info] writing file {} ...'.format(filename))
    dataframe.to_csv(filename, index=False)


filename = os.path.join('datasets', 'titanic', 'titanic_in.csv')
print('[info] reading file {} ...'.format(filename))
dataframe = pd.read_csv(filename)


if False:
    # -------------------------------------
    # - dataset navigation
    print('\ndataframe.head()=', dataframe.head(), sep='\n')
    # dataframe.head()=
    #    survived  pclass     sex   age  sibsp  parch     fare embarked  class    who  adult_male deck  embark_town alive  alone
    # 0         0       3    male  22.0      1      0   7.2500        S  Third    man        True  NaN  Southampton    no  False
    # 1         1       1  female  38.0      1      0  71.2833        C  First  woman       False    C    Cherbourg   yes  False
    # 2         1       3  female  26.0      0      0   7.9250        S  Third  woman       False  NaN  Southampton   yes   True
    # 3         1       1  female  35.0      1      0  53.1000        S  First  woman       False    C  Southampton   yes  False
    # 4         0       3    male  35.0      0      0   8.0500        S  Third    man        True  NaN  Southampton    no   True

    print('\n# dataframe.index')
    print(dataframe.index)
    # RangeIndex(start=0, stop=891, step=1)

    print('\n# dataframe.columns')
    for pair in enumerate(dataframe.columns): # tutple
        print(pair)
    # - columns
    # (0, 'survived')
    # (1, 'pclass')
    # (2, 'sex')
    # (3, 'age')
    # (4, 'sibsp')
    # (5, 'parch')
    # (6, 'fare')
    # (7, 'embarked')
    # (8, 'class')
    # (9, 'who')
    # (10, 'adult_male')
    # (11, 'deck')
    # (12, 'embark_town')
    # (13, 'alive')
    # (14, 'alone')

    print('\ndataframe.info()=')
    dataframe.info()
    # dataframe.info()=
    # <class 'pandas.core.frame.DataFrame'>
    # RangeIndex: 891 entries, 0 to 890
    # Data columns (total 15 columns):
    #  #   Column       Non-Null Count  Dtype
    # ---  ------       --------------  -----
    #  0   survived     891 non-null    int64
    #  1   pclass       891 non-null    int64
    #  2   sex          891 non-null    object
    #  3   age          714 non-null    float64 *** missing ***
    #  4   sibsp        891 non-null    int64
    #  5   parch        891 non-null    int64
    #  6   fare         891 non-null    float64
    #  7   embarked     889 non-null    object *** missing ***
    #  8   class        891 non-null    object
    #  9   who          891 non-null    object
    #  10  adult_male   891 non-null    bool
    #  11  deck         203 non-null    object *** missing ***
    #  12  embark_town  889 non-null    object *** missing ***
    #  13  alive        891 non-null    object
    #  14  alone        891 non-null    bool
    # dtypes: bool(2), float64(2), int64(4), object(7)
    # memory usage: 92.4+ KB

    print('\ndataframe.describe()=')
    print(dataframe.describe(include='all'))
    print(dataframe.describe())

    # dataframe.describe()=
    #           survived      pclass   sex         age       sibsp       parch        fare embarked  class  who adult_male deck  embark_town alive alone
    # count   891.000000  891.000000   891  714.000000  891.000000  891.000000  891.000000      889    891  891        891  203          889   891   891
    # unique         NaN         NaN     2         NaN         NaN         NaN         NaN        3      3    3          2    7            3     2     2
    # top            NaN         NaN  male         NaN         NaN         NaN         NaN        S  Third  man       True    C  Southampton    no  True
    # freq           NaN         NaN   577         NaN         NaN         NaN         NaN      644    491  537        537   59          644   549   537
    # mean      0.383838    2.308642   NaN   29.699118    0.523008    0.381594   32.204208      NaN    NaN  NaN        NaN  NaN          NaN   NaN   NaN
    # std       0.486592    0.836071   NaN   14.526497    1.102743    0.806057   49.693429      NaN    NaN  NaN        NaN  NaN          NaN   NaN   NaN
    # min       0.000000    1.000000   NaN    0.420000    0.000000    0.000000    0.000000      NaN    NaN  NaN        NaN  NaN          NaN   NaN   NaN
    # 25%       0.000000    2.000000   NaN   20.125000    0.000000    0.000000    7.910400      NaN    NaN  NaN        NaN  NaN          NaN   NaN   NaN
    # 50%       0.000000    3.000000   NaN   28.000000    0.000000    0.000000   14.454200      NaN    NaN  NaN        NaN  NaN          NaN   NaN   NaN
    # 75%       1.000000    3.000000   NaN   38.000000    1.000000    0.000000   31.000000      NaN    NaN  NaN        NaN  NaN          NaN   NaN   NaN
    # max       1.000000    3.000000   NaN   80.000000    8.000000    6.000000  512.329200      NaN    NaN  NaN        NaN  NaN          NaN   NaN   NaN

    # dataframe.describe()=
    #          survived      pclass         age       sibsp       parch        fare
    # count  891.000000  891.000000  714.000000  891.000000  891.000000  891.000000
    # mean     0.383838    2.308642   29.699118    0.523008    0.381594   32.204208
    # std      0.486592    0.836071   14.526497    1.102743    0.806057   49.693429
    # min      0.000000    1.000000    0.420000    0.000000    0.000000    0.000000
    # 25%      0.000000    2.000000   20.125000    0.000000    0.000000    7.910400
    # 50%      0.000000    3.000000   28.000000    0.000000    0.000000   14.454200
    # 75%      1.000000    3.000000   38.000000    1.000000    0.000000   31.000000
    # max      1.000000    3.000000   80.000000    8.000000    6.000000  512.329200


if False:
    # -------------------------------------
    # - handling missing data
    # ; fillna() or dropna()

    # - DataFrame.dropna(
    #       *, axis=0, how=_NoDefault.no_default,
    #       thresh=_NoDefault.no_default, subset=None, inplace=False
    #   )
    # ; remove missing values.
    dropped_0 = dataframe.dropna(axis='index', how='any', subset=['age', 'deck']).reset_index(drop=True)
    print('\ndropped_0.info()=')
    dropped_0.info()
    print('\ndropped_0.head()=', dropped_0.head(), sep='\n')
    print('\ndropped_0=', dropped_0, sep='\n')
    # dropped_0=
    #      survived  pclass     sex   age  sibsp  parch     fare embarked  class    who  adult_male deck  embark_town alive  alone
    # 0           1       1  female  38.0      1      0  71.2833        C  First  woman       False    C    Cherbourg   yes  False
    # 1           1       1  female  35.0      1      0  53.1000        S  First  woman       False    C  Southampton   yes  False
    # 2           0       1    male  54.0      0      0  51.8625        S  First    man        True    E  Southampton    no   True
    # 3           1       3  female   4.0      1      1  16.7000        S  Third  child       False    G  Southampton   yes  False
    # 4           1       1  female  58.0      0      0  26.5500        S  First  woman       False    C  Southampton   yes   True
    # ..        ...     ...     ...   ...    ...    ...      ...      ...    ...    ...         ...  ...          ...   ...    ...
    # 179         1       1  female  47.0      1      1  52.5542        S  First  woman       False    D  Southampton   yes  False
    # 180         0       1    male  33.0      0      0   5.0000        S  First    man        True    B  Southampton    no   True
    # 181         1       1  female  56.0      0      1  83.1583        C  First  woman       False    C    Cherbourg   yes  False
    # 182         1       1  female  19.0      0      0  30.0000        S  First  woman       False    B  Southampton   yes   True
    # 183         1       1    male  26.0      0      0  30.0000        C  First    man        True    C    Cherbourg   yes   True

    # - using boolean index
    dropped_1 = dataframe[dataframe[['age', 'deck']].notna().all(axis='columns')].reset_index(drop=True)
    print('\ndropped_1.info()=')
    dropped_1.info()
    print('\ndropped_1.head()=', dropped_1.head(), sep='\n')
    print('\ndropped_1=', dropped_1, sep='\n')
    # dropped_1=
    #      survived  pclass     sex   age  sibsp  parch     fare embarked  class    who  adult_male deck  embark_town alive  alone
    # 0           1       1  female  38.0      1      0  71.2833        C  First  woman       False    C    Cherbourg   yes  False
    # 1           1       1  female  35.0      1      0  53.1000        S  First  woman       False    C  Southampton   yes  False
    # 2           0       1    male  54.0      0      0  51.8625        S  First    man        True    E  Southampton    no   True
    # 3           1       3  female   4.0      1      1  16.7000        S  Third  child       False    G  Southampton   yes  False
    # 4           1       1  female  58.0      0      0  26.5500        S  First  woman       False    C  Southampton   yes   True
    # ..        ...     ...     ...   ...    ...    ...      ...      ...    ...    ...         ...  ...          ...   ...    ...
    # 179         1       1  female  47.0      1      1  52.5542        S  First  woman       False    D  Southampton   yes  False
    # 180         0       1    male  33.0      0      0   5.0000        S  First    man        True    B  Southampton    no   True
    # 181         1       1  female  56.0      0      1  83.1583        C  First  woman       False    C    Cherbourg   yes  False
    # 182         1       1  female  19.0      0      0  30.0000        S  First  woman       False    B  Southampton   yes   True
    # 183         1       1    male  26.0      0      0  30.0000        C  First    man        True    C    Cherbourg   yes   True


    # - DataFrame.fillna(
    #       value=None, *, method=None, axis=None, inplace=False, limit=None,
    #       downcast=None
    #   )
    # ; fill na/nan values using the specified method.
    # ; value to use to fill holes (e.g. 0), alternately a dict/series/dataframe
    #   of values specifying which value to use for each index (for a series)
    #   or column (for a dataframe).
    fill_values = {
        'age' : dataframe['age'].median(),
        'embarked' : 'X',
        'deck' : 'X',
        'embark_town' : 'Unknown',
    }
    print("\nfill_values=", fill_values)
    # fill_values= {'age': 28.0, 'embarked': 'X', 'deck': 'X', 'embark_town': 'Unknown'}

    filled = dataframe.fillna(value=fill_values)
    print('\nfilled.info()=')
    filled.info()
    print('\nfilled.head()=', filled.head(), sep='\n')
    print('\nfilled=', filled, sep='\n')
    # filled.info()=
    # <class 'pandas.core.frame.DataFrame'>
    # RangeIndex: 891 entries, 0 to 890
    # Data columns (total 15 columns):
    #  #   Column       Non-Null Count  Dtype
    # ---  ------       --------------  -----
    #  0   survived     891 non-null    int64
    #  1   pclass       891 non-null    int64
    #  2   sex          891 non-null    object
    #  3   age          891 non-null    float64
    #  4   sibsp        891 non-null    int64
    #  5   parch        891 non-null    int64
    #  6   fare         891 non-null    float64
    #  7   embarked     891 non-null    object
    #  8   class        891 non-null    object
    #  9   who          891 non-null    object
    #  10  adult_male   891 non-null    bool
    #  11  deck         891 non-null    object
    #  12  embark_town  891 non-null    object
    #  13  alive        891 non-null    object
    #  14  alone        891 non-null    bool
    # dtypes: bool(2), float64(2), int64(4), object(7)
    # memory usage: 92.4+ KB
    # 
    # filled.head()=
    #    survived  pclass     sex   age  sibsp  parch     fare embarked  class    who  adult_male deck  embark_town alive  alone
    # 0         0       3    male  22.0      1      0   7.2500        S  Third    man        True    X  Southampton    no  False
    # 1         1       1  female  38.0      1      0  71.2833        C  First  woman       False    C    Cherbourg   yes  False
    # 2         1       3  female  26.0      0      0   7.9250        S  Third  woman       False    X  Southampton   yes   True
    # 3         1       1  female  35.0      1      0  53.1000        S  First  woman       False    C  Southampton   yes  False
    # 4         0       3    male  35.0      0      0   8.0500        S  Third    man        True    X  Southampton    no   True
    # 
    # filled=
    #      survived  pclass     sex   age  sibsp  parch     fare embarked   class    who  adult_male deck  embark_town alive  alone
    # 0           0       3    male  22.0      1      0   7.2500        S   Third    man        True    X  Southampton    no  False
    # 1           1       1  female  38.0      1      0  71.2833        C   First  woman       False    C    Cherbourg   yes  False
    # 2           1       3  female  26.0      0      0   7.9250        S   Third  woman       False    X  Southampton   yes   True
    # 3           1       1  female  35.0      1      0  53.1000        S   First  woman       False    C  Southampton   yes  False
    # 4           0       3    male  35.0      0      0   8.0500        S   Third    man        True    X  Southampton    no   True
    # ..        ...     ...     ...   ...    ...    ...      ...      ...     ...    ...         ...  ...          ...   ...    ...
    # 886         0       2    male  27.0      0      0  13.0000        S  Second    man        True    X  Southampton    no   True
    # 887         1       1  female  19.0      0      0  30.0000        S   First  woman       False    B  Southampton   yes   True
    # 888         0       3  female  28.0      1      2  23.4500        S   Third  woman       False    X  Southampton    no  False
    # 889         1       1    male  26.0      0      0  30.0000        C   First    man        True    C    Cherbourg   yes   True
    # 890         0       3    male  32.0      0      0   7.7500        Q   Third    man        True    X   Queenstown    no   True
    # 
    # [891 rows x 15 columns]
    pass


if True:
    # -------------------------------------
    # - data purification
    # ; fillna() or dropna()
    fill_values = {
        'age' : dataframe['age'].median(),
        'embarked' : 'X',
        'deck' : 'X',
        'embark_town' : 'Unknown',
    }
    dataframe.fillna(value=fill_values, inplace=True)

    print("\nlen(dataframe)=", len(dataframe))
    print("\nlen(dataframe.iloc[3])=", len(dataframe.iloc[3]))
    print("\ndataframe.size=", dataframe.size)
    print("\ndataframe.shape=", dataframe.shape)
    print("\ndataframe.index=", dataframe.index, len(dataframe.index))
    print("\ndataframe.columns=", dataframe.columns, len(dataframe.columns))
    print("\ndataframe.dtypes=", dataframe.dtypes, sep='\n')

    print('\ndataframe.info()=')
    dataframe.info()
    # dataframe.info()=
    # <class 'pandas.core.frame.DataFrame'>
    # RangeIndex: 891 entries, 0 to 890
    # Data columns (total 15 columns):
    #  #   Column       Non-Null Count  Dtype
    # ---  ------       --------------  -----
    #  0   survived     891 non-null    int64
    #  1   pclass       891 non-null    int64
    #  2   sex          891 non-null    object
    #  3   age          891 non-null    float64
    #  4   sibsp        891 non-null    int64
    #  5   parch        891 non-null    int64
    #  6   fare         891 non-null    float64
    #  7   embarked     891 non-null    object
    #  8   class        891 non-null    object
    #  9   who          891 non-null    object
    #  10  adult_male   891 non-null    bool
    #  11  deck         891 non-null    object
    #  12  embark_town  891 non-null    object
    #  13  alive        891 non-null    object
    #  14  alone        891 non-null    bool
    # dtypes: bool(2), float64(2), int64(4), object(7)
    # memory usage: 92.4+ KB

    print('\ndataframe.describe()=',
        dataframe.describe(percentiles=[0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]),
        sep='\n'
    )
    # dataframe.describe()=
    #          survived      pclass         age       sibsp       parch        fare
    # count  891.000000  891.000000  891.000000  891.000000  891.000000  891.000000
    # mean     0.383838    2.308642   29.361582    0.523008    0.381594   32.204208
    # std      0.486592    0.836071   13.019697    1.102743    0.806057   49.693429
    # min      0.000000    1.000000    0.420000    0.000000    0.000000    0.000000
    # 10%      0.000000    1.000000   16.000000    0.000000    0.000000    7.550000
    # 20%      0.000000    1.000000   20.000000    0.000000    0.000000    7.854200
    # 30%      0.000000    2.000000   24.000000    0.000000    0.000000    8.050000
    # 40%      0.000000    2.000000   28.000000    0.000000    0.000000   10.500000
    # 50%      0.000000    3.000000   28.000000    0.000000    0.000000   14.454200
    # 60%      0.000000    3.000000   28.000000    0.000000    0.000000   21.679200
    # 70%      1.000000    3.000000   32.500000    1.000000    0.000000   27.000000
    # 80%      1.000000    3.000000   38.000000    1.000000    1.000000   39.687500
    # 90%      1.000000    3.000000   47.000000    1.000000    2.000000   77.958300
    # max      1.000000    3.000000   80.000000    8.000000    6.000000  512.329200


if False:
    # -------------------------------------
    # - data selection
    # ; column
    series = dataframe["age"] # selecting a single column -> series
                              # same as dataframe.age
    print("\nseries=", series, sep='\n')

    print('\nseries.info()=')
    series.info()
    # series.info()=
    # <class 'pandas.core.series.Series'>
    # RangeIndex: 891 entries, 0 to 890
    # Series name: age
    # Non-Null Count  Dtype
    # --------------  -----
    # 891 non-null    float64
    # dtypes: float64(1)
    # memory usage: 7.1 KB

    print("\nseries.name=", series.name) # age
    print("\nseries.shape=", series.shape) # (891,)
    print("\nseries.describe()=", series.describe(), sep='\n')
    # series.describe()=
    # count    891.000000
    # mean      29.361582
    # std       13.019697
    # min        0.420000
    # 25%       22.000000
    # 50%       28.000000
    # 75%       35.000000
    # max       80.000000
    # Name: age, dtype: float64

    dataframe_0 = dataframe[["age"]] # -> brackets!
    print('\ndataframe_0.info()=')
    dataframe_0.info()
    # dataframe_0.info()=
    # <class 'pandas.core.frame.DataFrame'>
    # RangeIndex: 891 entries, 0 to 890
    # Data columns (total 1 columns):
    #  #   Column  Non-Null Count  Dtype
    # ---  ------  --------------  -----
    #  0   age     891 non-null    float64
    # dtypes: float64(1)
    # memory usage: 7.1 KB
    
    print("\ndataframe_0.describe()=", dataframe_0.describe(), sep='\n')
    # dataframe_0.describe()=
    #               age
    # count  891.000000
    # mean    29.361582
    # std     13.019697
    # min      0.420000
    # 25%     22.000000
    # 50%     28.000000
    # 75%     35.000000
    # max     80.000000


if False:
    # -------------------------------------
    # - data selection
    # ; row by range selection
    subset = dataframe[0:1]
    #print("\nsubset.info()="); subset.info()
    print("\nsubset(0)="); print(subset)
    # subset(0)=
    #    survived  pclass   sex   age  sibsp  parch  fare embarked  class  who  adult_male deck  embark_town alive  alone
    # 0         0       3  male  22.0      1      0  7.25        S  Third  man        True    X  Southampton    no  False

    subset = dataframe[0:5]
    #print("\nsubset.info()="); subset.info()
    print("\nsubset(1)="); print(subset)
    # subset(1)=
    #    survived  pclass     sex   age  sibsp  parch     fare embarked  class    who  adult_male deck  embark_town alive  alone
    # 0         0       3    male  22.0      1      0   7.2500        S  Third    man        True    X  Southampton    no  False
    # 1         1       1  female  38.0      1      0  71.2833        C  First  woman       False    C    Cherbourg   yes  False
    # 2         1       3  female  26.0      0      0   7.9250        S  Third  woman       False    X  Southampton   yes   True
    # 3         1       1  female  35.0      1      0  53.1000        S  First  woman       False    C  Southampton   yes  False
    # 4         0       3    male  35.0      0      0   8.0500        S  Third    man        True    X  Southampton    no   True


if False:
    # -------------------------------------
    # - data selection
    # ; using dataframe.loc() & dataframe.at()
    subset = dataframe.loc[0] # returns a series!
    print("\nsubset.info()="); subset.info()
    # subset.info()=
    # <class 'pandas.core.series.Series'>
    # Index: 15 entries, survived to alone
    # Series name: 0
    # Non-Null Count  Dtype
    # --------------  -----
    # 15 non-null     object
    # dtypes: object(1)
    # memory usage: 796.0+ bytes

    print("\nsubset(0)="); print(subset)
    # subset(0)=
    # survived                 0
    # pclass                   3
    # sex                   male
    # age                   22.0
    # sibsp                    1
    # parch                    0
    # fare                  7.25
    # embarked                 S
    # class                Third
    # who                    man
    # adult_male            True
    # deck                     X
    # embark_town    Southampton
    # alive                   no
    # alone                False
    # Name: 0, dtype: object


    subset = dataframe.loc[[0]] # returns a dataframe!
    print("\nsubset.info()="); subset.info()
    # subset.info()=
    # <class 'pandas.core.frame.DataFrame'>
    # Int64Index: 1 entries, 0 to 0
    # Data columns (total 15 columns):
    #  #   Column       Non-Null Count  Dtype
    # ---  ------       --------------  -----
    #  0   survived     1 non-null      int64
    #  1   pclass       1 non-null      int64
    #  2   sex          1 non-null      object
    #  3   age          1 non-null      float64
    #  4   sibsp        1 non-null      int64
    #  5   parch        1 non-null      int64
    #  6   fare         1 non-null      float64
    #  7   embarked     1 non-null      object
    #  8   class        1 non-null      object
    #  9   who          1 non-null      object
    #  10  adult_male   1 non-null      bool
    #  11  deck         1 non-null      object
    #  12  embark_town  1 non-null      object
    #  13  alive        1 non-null      object
    #  14  alone        1 non-null      bool
    # dtypes: bool(2), float64(2), int64(4), object(7)
    # memory usage: 114.0+ bytes

    print("\nsubset(1)="); print(subset)
    # subset(1)=
    #    survived  pclass   sex   age  sibsp  parch  fare embarked  class  who  adult_male deck  embark_town alive  alone
    # 0         0       3  male  22.0      1      0  7.25        S  Third  man        True    X  Southampton    no  False


    subset = dataframe.loc[:10, ['age', 'class', 'fare']]
    print("\nsubset.info()="); subset.info()
    print("\nsubset(2)="); print(subset)
    # subset(2)=
    #      age   class     fare
    # 0   22.0   Third   7.2500
    # 1   38.0   First  71.2833
    # 2   26.0   Third   7.9250
    # 3   35.0   First  53.1000
    # 4   35.0   Third   8.0500
    # 5   28.0   Third   8.4583
    # 6   54.0   First  51.8625
    # 7    2.0   Third  21.0750
    # 8   27.0   Third  11.1333
    # 9   14.0  Second  30.0708
    # 10   4.0   Third  16.7000

    # access a single value for a row/column label pair
    print("\nvalue=", dataframe.at[4, "age"])
    # value= 35.0


if False:
    # -------------------------------------
    # - data selection
    # ; using dataframe.iloc() & dataframe.iat()
    subset = dataframe.iloc[3] # returns a series!
    subset.info() # <class 'pandas.core.series.Series'>
    print("\nsubset(0)=", subset, sep='\n')
    # subset(0)=
    # survived                 1
    # pclass                   1
    # sex                 female
    # age                   35.0
    # sibsp                    1
    # parch                    0
    # fare                  53.1
    # embarked                 S
    # class                First
    # who                  woman
    # adult_male           False
    # deck                     C
    # embark_town    Southampton
    # alive                  yes
    # alone                False
    # Name: 3, dtype: object

    subset = dataframe.iloc[[3]] # returns a dataframe!
    print("\nsubset.info()="); subset.info() # <class 'pandas.core.frame.DataFrame'>
    print("\nsubset(1)=", subset, sep='\n')
    # subset(1)=
    #    survived  pclass     sex   age  sibsp  parch  fare embarked  class    who  adult_male deck  embark_town alive  alone
    # 3         1       1  female  35.0      1      0  53.1        S  First  woman       False    C  Southampton   yes  False

    subset = dataframe.iloc[5:10, [3, 6, 8]]
    print("\nsubset.info()="); subset.info()
    print("\nsubset(2)="); print(subset)
    # subset(2)=
    #     age     fare   class
    # 5  28.0   8.4583   Third
    # 6  54.0  51.8625   First
    # 7   2.0  21.0750   Third
    # 8  27.0  11.1333   Third
    # 9  14.0  30.0708  Second

    # access a single value for a row/column label pair
    print("\nvalue=", dataframe.iat[4, 3])
    # value= 35.0


if False:
    # - boolean indexing
    boolean = dataframe["age"] > 29.36
    print("\nboolean=", boolean, sep='\n')
    # boolean=
    # 0      False
    # 1       True
    # 2      False
    # 3       True
    # 4       True
    #        ...
    # 886    False
    # 887    False
    # 888    False
    # 889    False
    # 890     True
    # Name: age, Length: 891, dtype: bool

    subset = dataframe[dataframe["age"] > 29.36].reset_index(drop=True)
    print("\nsubset(4)="); print(subset) # series
    # subset(4)=
    #      survived  pclass     sex   age  sibsp  parch     fare embarked  class    who  adult_male deck  embark_town alive  alone
    # 1           1       1  female  38.0      1      0  71.2833        C  First  woman       False    C    Cherbourg   yes  False
    # 3           1       1  female  35.0      1      0  53.1000        S  First  woman       False    C  Southampton   yes  False
    # 4           0       3    male  35.0      0      0   8.0500        S  Third    man        True    X  Southampton    no   True
    # 6           0       1    male  54.0      0      0  51.8625        S  First    man        True    E  Southampton    no   True
    # 11          1       1  female  58.0      0      0  26.5500        S  First  woman       False    C  Southampton   yes   True
    # ..        ...     ...     ...   ...    ...    ...      ...      ...    ...    ...         ...  ...          ...   ...    ...
    # 873         0       3    male  47.0      0      0   9.0000        S  Third    man        True    X  Southampton    no   True
    # 879         1       1  female  56.0      0      1  83.1583        C  First  woman       False    C    Cherbourg   yes  False
    # 881         0       3    male  33.0      0      0   7.8958        S  Third    man        True    X  Southampton    no   True
    # 885         0       3  female  39.0      0      5  29.1250        Q  Third  woman       False    X   Queenstown    no  False
    # 890         0       3    male  32.0      0      0   7.7500        Q  Third    man        True    X   Queenstown    no   True


if False:
    # -------------------------------------
    # - DataFrame.mean(axis=0, skipna=True, numeric_only=True, **kwargs)
    # ; return the mean of the values over the requested axis.
    # ; numeric_only by default
    means = dataframe.mean(axis=0, numeric_only=True)
    print("\nmeans=", means, sep='\n')
    # means=
    # survived       0.383838
    # pclass         2.308642
    # age           29.361582
    # sibsp          0.523008
    # parch          0.381594
    # fare          32.204208
    # adult_male     0.602694
    # alone          0.602694
    # dtype: float64


if False:
    # - finding min/max rows
    idxmin = dataframe['age'].idxmin(axis=0)
    print('\nidxmin=', idxmin)
    print('min=', dataframe.loc[[idxmin]], sep='\n')
    # idxmin= 803
    # min=
    #      survived  pclass   sex   age  sibsp  parch    fare embarked  class    who  adult_male deck embark_town alive  alone
    # 803         1       3  male  0.42      0      1  8.5167        C  Third  child       False    X   Cherbourg   yes  False

    idxmax = dataframe['age'].idxmax(axis=0)
    print('\nidxmax=', idxmax)
    print('max=', dataframe.loc[[idxmax]], sep='\n')
    # idxmax= 630
    # max=
    #      survived  pclass   sex   age  sibsp  parch  fare embarked  class  who  adult_male deck  embark_town alive  alone
    # 630         1       1  male  80.0      0      0  30.0        S  First  man        True    A  Southampton   yes   True


if False:
    # -------------------------------------
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
    dataframe_sorted = dataframe.sort_index(axis=1, ascending=True, inplace=False)
    print("\ndataframe_sorted.head()=")
    print(dataframe_sorted.head())
    # dataframe_sorted.head()=
    #    adult_male   age alive  alone  class deck  embark_town embarked     fare  parch  pclass     sex  sibsp  survived    who
    # 0        True  22.0    no  False  Third    X  Southampton        S   7.2500      0       3    male      1         0    man
    # 1       False  38.0   yes  False  First    C    Cherbourg        C  71.2833      0       1  female      1         1  woman
    # 2       False  26.0   yes   True  Third    X  Southampton        S   7.9250      0       3  female      0         1  woman
    # 3       False  35.0   yes  False  First    C  Southampton        S  53.1000      0       1  female      1         1  woman
    # 4        True  35.0    no   True  Third    X  Southampton        S   8.0500      0       3    male      0         0    man

    dataframe_sorted = dataframe.sort_values(by="age", ascending=True, inplace=False)
    print("\ndataframe_sorted.head()=")
    print(dataframe_sorted.head())
    # dataframe_sorted.head()=
    #      survived  pclass     sex   age  sibsp  parch     fare embarked   class    who  adult_male deck  embark_town alive  alone
    # 803         1       3    male  0.42      0      1   8.5167        C   Third  child       False    X    Cherbourg   yes  False
    # 755         1       2    male  0.67      1      1  14.5000        S  Second  child       False    X  Southampton   yes  False
    # 644         1       3  female  0.75      2      1  19.2583        C   Third  child       False    X    Cherbourg   yes  False
    # 469         1       3  female  0.75      2      1  19.2583        C   Third  child       False    X    Cherbourg   yes  False
    # 831         1       2    male  0.83      1      1  18.7500        S  Second  child       False    X  Southampton   yes  False


if False:
    # -------------------------------------
    # - DataFrame.nlargest(n, columns, keep='first')
    # ; return the first n rows ordered by columns in descending order.
    # ; equivalent to dataframe.sort_values(columns, ascending=False).head(n),
    #   but more performant.
    # - DataFrame.nsmallest(n, columns, keep='first')
    # ; return the first n rows ordered by columns in ascending order.
    # ; equivalent to dataframe.sort_values(columns, ascending=True).head(n),
    #   but more performant.
    largest_age_10 = dataframe.nlargest(10, 'age')
    print('\nlargest_age_10=', largest_age_10, sep='\n')
    # largest_age_10=
    #      survived  pclass   sex   age  sibsp  parch     fare embarked   class  who  adult_male deck  embark_town alive  alone
    # 630         1       1  male  80.0      0      0  30.0000        S   First  man        True    A  Southampton   yes   True
    # 851         0       3  male  74.0      0      0   7.7750        S   Third  man        True    X  Southampton    no   True
    # 96          0       1  male  71.0      0      0  34.6542        C   First  man        True    A    Cherbourg    no   True
    # 493         0       1  male  71.0      0      0  49.5042        C   First  man        True    X    Cherbourg    no   True
    # 116         0       3  male  70.5      0      0   7.7500        Q   Third  man        True    X   Queenstown    no   True
    # 672         0       2  male  70.0      0      0  10.5000        S  Second  man        True    X  Southampton    no   True
    # 745         0       1  male  70.0      1      1  71.0000        S   First  man        True    B  Southampton    no  False
    # 33          0       2  male  66.0      0      0  10.5000        S  Second  man        True    X  Southampton    no   True
    # 54          0       1  male  65.0      0      1  61.9792        C   First  man        True    B    Cherbourg    no  False
    # 280         0       3  male  65.0      0      0   7.7500        Q   Third  man        True    X   Queenstown    no   True

    largest_fare_10 = dataframe.nlargest(10, 'fare')
    print('\nlargest_fare_10=', largest_fare_10, sep='\n')
    # largest_fare_10=
    #      survived  pclass     sex   age  sibsp  parch      fare embarked  class    who  adult_male deck  embark_town alive  alone
    # 258         1       1  female  35.0      0      0  512.3292        C  First  woman       False    X    Cherbourg   yes   True
    # 679         1       1    male  36.0      0      1  512.3292        C  First    man        True    B    Cherbourg   yes  False
    # 737         1       1    male  35.0      0      0  512.3292        C  First    man        True    B    Cherbourg   yes   True
    # 27          0       1    male  19.0      3      2  263.0000        S  First    man        True    C  Southampton    no  False
    # 88          1       1  female  23.0      3      2  263.0000        S  First  woman       False    C  Southampton   yes  False
    # 341         1       1  female  24.0      3      2  263.0000        S  First  woman       False    C  Southampton   yes  False
    # 438         0       1    male  64.0      1      4  263.0000        S  First    man        True    C  Southampton    no  False
    # 311         1       1  female  18.0      2      2  262.3750        C  First  woman       False    B    Cherbourg   yes  False
    # 742         1       1  female  21.0      2      2  262.3750        C  First  woman       False    B    Cherbourg   yes  False
    # 118         0       1    male  24.0      0      1  247.5208        C  First    man        True    B    Cherbourg    no  False


if False:
    # -------------------------------------
    # - DataFrame.filter(
    #       items=None, like=None, regex=None, axis=None
    #   )
    # ; subset the dataframe rows or columns according to the specified index labels.

    dataframe_0 = dataframe.filter(items=['fare', 'survived', 'age'], axis=1)
    print('\ndataframe_0.head()=')
    print(dataframe_0.head())
    # dataframe.head()=
    #       fare  survived   age
    # 0   7.2500         0  22.0
    # 1  71.2833         1  38.0
    # 2   7.9250         1  26.0
    # 3  53.1000         1  35.0
    # 4   8.0500         0  35.0

    dataframe_1 = dataframe.filter(regex='^embark', axis=1)
    print('\ndataframe_1.head()=')
    print(dataframe_1.head())
    # dataframe_1.head()=
    #   embarked  embark_town
    # 0        S  Southampton
    # 1        C    Cherbourg
    # 2        S  Southampton
    # 3        S  Southampton
    # 4        S  Southampton

    dataframe_2 = dataframe.filter(like='class', axis=1)
    print('\ndataframe_2.head()=')
    print(dataframe_2.head())
    # dataframe_2.head()=
    #    pclass  class
    # 0       3  Third
    # 1       1  First
    # 2       3  Third
    # 3       1  First
    # 4       3  Third


if False:
    # -------------------------------------
    # - Series.apply(func, convert_dtype=True, args=(), **kwargs)
    # ; invoke function on values of series.
    def _convert(value):
        if value is False:
            return 'no'
        else:
            return 'yes'

    print('\ndataframe.head()= <before>')
    print(dataframe.head())
    # dataframe.head()= <before>
    #    survived  pclass     sex   age  sibsp  parch     fare embarked  class    who  adult_male deck  embark_town alive  alone
    # 0         0       3    male  22.0      1      0   7.2500        S  Third    man        True    X  Southampton    no  False
    # 1         1       1  female  38.0      1      0  71.2833        C  First  woman       False    C    Cherbourg   yes  False
    # 2         1       3  female  26.0      0      0   7.9250        S  Third  woman       False    X  Southampton   yes   True
    # 3         1       1  female  35.0      1      0  53.1000        S  First  woman       False    C  Southampton   yes  False
    # 4         0       3    male  35.0      0      0   8.0500        S  Third    man        True    X  Southampton    no   True

    series = dataframe['alone']
    dataframe['alone'] = series.apply(_convert)

    print('\ndataframe.head()= <after>')
    print(dataframe.head())
    # dataframe.head()= <after>
    #    survived  pclass     sex   age  sibsp  parch     fare embarked  class    who  adult_male deck  embark_town alive alone
    # 0         0       3    male  22.0      1      0   7.2500        S  Third    man        True    X  Southampton    no    no
    # 1         1       1  female  38.0      1      0  71.2833        C  First  woman       False    C    Cherbourg   yes    no
    # 2         1       3  female  26.0      0      0   7.9250        S  Third  woman       False    X  Southampton   yes   yes
    # 3         1       1  female  35.0      1      0  53.1000        S  First  woman       False    C  Southampton   yes    no
    # 4         0       3    male  35.0      0      0   8.0500        S  Third    man        True    X  Southampton    no   yes

    cumulative_sum = dataframe[['age', 'fare']].apply(np.cumsum)
    cumulative_sum.columns = ['age_cumul', 'fare_cumul']
    print('\ncumulative_sum=', cumulative_sum, sep='\n')

    dataframe = pd.concat([dataframe, cumulative_sum], axis=1)
    print('\ndataframe=', dataframe, sep='\n')
    # dataframe=
    #      survived  pclass     sex   age  sibsp  parch     fare embarked   class    who  adult_male deck  embark_town alive alone  age_cumul  fare_cumul
    # 0           0       3    male  22.0      1      0   7.2500        S   Third    man        True    X  Southampton    no    no      22.00      7.2500
    # 1           1       1  female  38.0      1      0  71.2833        C   First  woman       False    C    Cherbourg   yes    no      60.00     78.5333
    # 2           1       3  female  26.0      0      0   7.9250        S   Third  woman       False    X  Southampton   yes   yes      86.00     86.4583
    # 3           1       1  female  35.0      1      0  53.1000        S   First  woman       False    C  Southampton   yes    no     121.00    139.5583
    # 4           0       3    male  35.0      0      0   8.0500        S   Third    man        True    X  Southampton    no   yes     156.00    147.6083
    # ..        ...     ...     ...   ...    ...    ...      ...      ...     ...    ...         ...  ...          ...   ...   ...        ...         ...
    # 886         0       2    male  27.0      0      0  13.0000        S  Second    man        True    X  Southampton    no   yes   26056.17  28602.7493
    # 887         1       1  female  19.0      0      0  30.0000        S   First  woman       False    B  Southampton   yes   yes   26075.17  28632.7493
    # 888         0       3  female  28.0      1      2  23.4500        S   Third  woman       False    X  Southampton    no    no   26103.17  28656.1993
    # 889         1       1    male  26.0      0      0  30.0000        C   First    man        True    C    Cherbourg   yes   yes   26129.17  28686.1993
    # 890         0       3    male  32.0      0      0   7.7500        Q   Third    man        True    X   Queenstown    no   yes   26161.17  28693.9493
    # 
    # [891 rows x 17 columns]


if False:
    # -------------------------------------
    # - DataFrame.groupby(
    #       by=None, axis=0, level=None, as_index=True, sort=True,
    #       group_keys=True, observed=False, dropna=True
    #   )
    # ; group dataframe using a mapper or by a series of columns.
    grouped = dataframe[['class', 'fare', 'age']].groupby(['class'])
    print('\nmean=', grouped.mean(), sep='\n')
    print('\nmedian=', grouped.median(), sep='\n')
    print('\nmin=', grouped.min(), sep='\n')
    print('\nmax=', grouped.max(), sep='\n')
    # mean=        fare        age
    # class
    # First   84.154687  36.812130
    # Second  20.662183  29.765380
    # Third   13.675550  25.932627
    # 
    # median=    fare   age
    # class
    # First   60.2875  35.0
    # Second  14.2500  28.0
    # Third    8.0500  28.0
    # 
    # min=    fare   age
    # class
    # First    0.0  0.92
    # Second   0.0  0.67
    # Third    0.0  0.42
    # 
    # max=        fare   age
    # class
    # First   512.3292  80.0
    # Second   73.5000  70.0
    # Third    69.5500  74.0


if False:
    # -------------------------------------
    # - categoricals
    # ; infant = 0-1 year.
    # ; toddler = 2-4 yrs.
    # ; child = 5-12 yrs.
    # ; teenager = 13-19 yrs.
    # ; adult = 20-39 yrs.
    # ; middle = 40-59 yrs.
    # ; senior = 60+
    def age2stage(age):
        if age < 2.0: return '1.infant'
        elif age < 5: return '2.toddler'
        elif age < 13: return '3.child'
        elif age < 20: return '4.teenager'
        elif age < 40: return '5.adult'
        elif age < 60: return '6.middle' # middle-aged
        else: return '7.senior'

    series = dataframe['age']
    dataframe['age_stage'] = series.apply(age2stage)
    print("\ndataframe.info()="); dataframe.info() # <class 'pandas.core.frame.DataFrame'>
    print('\ndataframe=', dataframe, sep='\n')
    # dataframe=
    #      survived  pclass     sex   age  sibsp  parch     fare embarked   class    who  adult_male deck  embark_town alive  alone   age_stage
    # 0           0       3    male  22.0      1      0   7.2500        S   Third    man        True    X  Southampton    no  False     5.adult
    # 1           1       1  female  38.0      1      0  71.2833        C   First  woman       False    C    Cherbourg   yes  False     5.adult
    # 2           1       3  female  26.0      0      0   7.9250        S   Third  woman       False    X  Southampton   yes   True     5.adult
    # 3           1       1  female  35.0      1      0  53.1000        S   First  woman       False    C  Southampton   yes  False     5.adult
    # 4           0       3    male  35.0      0      0   8.0500        S   Third    man        True    X  Southampton    no   True     5.adult
    # ..        ...     ...     ...   ...    ...    ...      ...      ...     ...    ...         ...  ...          ...   ...    ...         ...
    # 886         0       2    male  27.0      0      0  13.0000        S  Second    man        True    X  Southampton    no   True     5.adult
    # 887         1       1  female  19.0      0      0  30.0000        S   First  woman       False    B  Southampton   yes   True  4.teenager
    # 888         0       3  female  28.0      1      2  23.4500        S   Third  woman       False    X  Southampton    no  False     5.adult
    # 889         1       1    male  26.0      0      0  30.0000        C   First    man        True    C    Cherbourg   yes   True     5.adult
    # 890         0       3    male  32.0      0      0   7.7500        Q   Third    man        True    X   Queenstown    no   True     5.adult
    # [891 rows x 16 columns]

    # - Series.value_counts(
    #       normalize=False, sort=True, ascending=False, bins=None,
    #       dropna=True
    #   )
    # ; return a series containing counts of unique values.
    #print(dataframe['age_stage'].value_counts(normalize=False, sort=False).sort_index(axis=0, ascending=True))
    #print(dataframe['age_stage'].value_counts(normalize=True, sort=False).sort_index(axis=0, ascending=True))

    value_counts = pd.DataFrame(
        {'normalized_x': dataframe['age_stage'].value_counts(normalize=False, sort=False).sort_index(axis=0, ascending=True),
         'normalized_o': dataframe['age_stage'].value_counts(normalize=True,  sort=False).sort_index(axis=0, ascending=True)}
    )
    print("\nvalue_counts.info()="); value_counts.info() # <class 'pandas.core.frame.DataFrame'>
    print('\nvalue_counts=', value_counts, sep='\n')
    # value_counts=
    #             normalized_x  normalized_o
    # 1.infant              14      0.015713
    # 2.toddler             26      0.029181
    # 3.child               29      0.032548
    # 4.teenager            95      0.106622
    # 5.adult              564      0.632997
    # 6.middle             137      0.153760
    # 7.senior              26      0.029181


if False:
    # -------------------------------------
    # - pandas.cut(
    #       x, bins, right=True, labels=None, retbins=False, precision=3,
    #       include_lowest=False, duplicates='raise', ordered=True
    #   )
    # ; bin values into discrete intervals.
    # ; returns an array-like object representing the respective bin for each value of x

    # continuous to discrete
    bins = list(range(0, 101, 10))
    labels = ["{0}-{1}".format(i, i+9) for i in range(0, 100, 10)]
    print("\nbins=", bins)
    print("labels=", labels)
    # bins= [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    # labels= ['0-9', '10-19', '20-29', '30-39', '40-49', '50-59', '60-69', '70-79', '80-89', '90-99']

    digitized = pd.cut(
        dataframe["age"], bins=bins,
        labels=labels
    )
    dataframe['age_step'] = digitized

    print('\ndataframe.head()= <after>')
    print(dataframe.head())
    # dataframe.head()= <after>
    #    survived  pclass     sex   age  sibsp  parch     fare embarked  class    who  adult_male deck  embark_town alive  alone age_step
    # 0         0       3    male  22.0      1      0   7.2500        S  Third    man        True    X  Southampton    no  False    20-29
    # 1         1       1  female  38.0      1      0  71.2833        C  First  woman       False    C    Cherbourg   yes  False    30-39
    # 2         1       3  female  26.0      0      0   7.9250        S  Third  woman       False    X  Southampton   yes   True    20-29
    # 3         1       1  female  35.0      1      0  53.1000        S  First  woman       False    C  Southampton   yes  False    30-39
    # 4         0       3    male  35.0      0      0   8.0500        S  Third    man        True    X  Southampton    no   True    30-39

    value_counts = pd.DataFrame(
        {'normalized_x': dataframe['age_step'].value_counts(normalize=False, sort=False),
         'normalized_o': dataframe['age_step'].value_counts(normalize=True,  sort=False)}
    )
    print("\nvalue_counts.info()="); value_counts.info() # <class 'pandas.core.frame.DataFrame'>
    print('\nvalue_counts=', value_counts, sep='\n')
    # value_counts=
    #        normalized_x  normalized_o
    # 0-9              64      0.071829
    # 10-19           115      0.129068
    # 20-29           407      0.456790
    # 30-39           155      0.173962
    # 40-49            86      0.096521
    # 50-59            42      0.047138
    # 60-69            17      0.019080
    # 70-79             5      0.005612
    # 80-89             0      0.000000
    # 90-99             0      0.000000

    # - drawing histogram
    digitized.hist(bins=10)
    index = 0
    filename = os.path.splitext(os.path.basename(__file__))[0] + '-{:02d}.png'.format(index)
    print('[info] writing file {} ...'.format(filename))
    plt.savefig(filename, bbox_inches="tight")
    #plt.show()
    plt.close()


if False:
    # -------------------------------------
    # - histogram for fare
    dataframe.hist(bins=50, figsize=(20,15))
    index = 1
    filename = os.path.splitext(os.path.basename(__file__))[0] + '-{:02d}.png'.format(index)
    print('[info] writing file {} ...'.format(filename))
    plt.savefig(filename, bbox_inches="tight")
    #plt.show()
    plt.close()

    expensive = dataframe[ dataframe['fare'] > 200.0 ]
    print('expensive=', expensive, sep='\n')
    # expensive=
    #      survived  pclass     sex   age  sibsp  parch      fare embarked  class    who  adult_male deck  embark_town alive  alone
    # 27          0       1    male  19.0      3      2  263.0000        S  First    man        True    C  Southampton    no  False
    # 88          1       1  female  23.0      3      2  263.0000        S  First  woman       False    C  Southampton   yes  False
    # 118         0       1    male  24.0      0      1  247.5208        C  First    man        True    B    Cherbourg    no  False
    # 258         1       1  female  35.0      0      0  512.3292        C  First  woman       False  NaN    Cherbourg   yes   True
    # 299         1       1  female  50.0      0      1  247.5208        C  First  woman       False    B    Cherbourg   yes  False
    # 311         1       1  female  18.0      2      2  262.3750        C  First  woman       False    B    Cherbourg   yes  False
    # 341         1       1  female  24.0      3      2  263.0000        S  First  woman       False    C  Southampton   yes  False
    # 377         0       1    male  27.0      0      2  211.5000        C  First    man        True    C    Cherbourg    no  False
    # 380         1       1  female  42.0      0      0  227.5250        C  First  woman       False  NaN    Cherbourg   yes   True
    # 438         0       1    male  64.0      1      4  263.0000        S  First    man        True    C  Southampton    no  False
    # 527         0       1    male   NaN      0      0  221.7792        S  First    man        True    C  Southampton    no   True
    # 557         0       1    male   NaN      0      0  227.5250        C  First    man        True  NaN    Cherbourg    no   True
    # 679         1       1    male  36.0      0      1  512.3292        C  First    man        True    B    Cherbourg   yes  False
    # 689         1       1  female  15.0      0      1  211.3375        S  First  child       False    B  Southampton   yes  False
    # 700         1       1  female  18.0      1      0  227.5250        C  First  woman       False    C    Cherbourg   yes  False
    # 716         1       1  female  38.0      0      0  227.5250        C  First  woman       False    C    Cherbourg   yes   True
    # 730         1       1  female  29.0      0      0  211.3375        S  First  woman       False    B  Southampton   yes   True
    # 737         1       1    male  35.0      0      0  512.3292        C  First    man        True    B    Cherbourg   yes   True
    # 742         1       1  female  21.0      2      2  262.3750        C  First  woman       False    B    Cherbourg   yes  False
    # 779         1       1  female  43.0      0      1  211.3375        S  First  woman       False    B  Southampton   yes  False

    print(expensive['survived'].value_counts())
    # 1    14
    # 0     6


if False:
    # -------------------------------------
    # - pandas.pivot_table(
    #       data, values=None, index=None, columns=None, aggfunc='mean',
    #       fill_value=None, margins=False, dropna=True, margins_name='All',
    #       observed=False, sort=True
    #   )
    # ; create a spreadsheet-style pivot table as a dataframe.
    dataframe = dataframe[['age','sex','class','fare','survived']]
    print("\ndataframe.info()="); dataframe.info()
    print('\ndataframe.head()=', dataframe.head(), sep='\n')
    # dataframe.head()=
    #     age     sex  class     fare  survived
    # 0  22.0    male  Third   7.2500         0
    # 1  38.0  female  First  71.2833         1
    # 2  26.0  female  Third   7.9250         1
    # 3  35.0  female  First  53.1000         1
    # 4  35.0    male  Third   8.0500         0

    fill_value = dataframe['age'].mean()
    print('\nfill_value=', fill_value)
    # fill_value= 29.69911764705882
    pivot_table = pd.pivot_table(
        dataframe, index='class', columns='sex', values='age',
        aggfunc=np.mean, fill_value=fill_value
    )
    print('\npivot_table[0]=', pivot_table, sep='\n')
    # pivot_table[0]=
    # sex        female       male
    # class
    # First   34.611765  41.281386
    # Second  28.722973  30.740707
    # Third   21.750000  26.507589

    pivot_table = pd.pivot_table(
        dataframe, index='class', columns='sex', values='survived',
        aggfunc=['mean', 'sum'], fill_value=0
    )
    print('\npivot_table[1]=', pivot_table, sep='\n')
    # pivot_table[1]=
    # --------+----------------------+------------
    #         |      mean            |    sum
    # sex     |    female      male  | female male
    # --------+----------------------+------------
    # class   |                      |
    # First   |  0.968085  0.368852  |     91   45
    # Second  |  0.921053  0.157407  |     70   17
    # Third   |  0.500000  0.135447  |     72   47
    # --------+----------------------+------------

    #print(dataframe['class'].value_counts())


if False:
    # -------------------------------------
    # - time series
    ranges = pd.date_range("1/1/2023", periods=365)
    scores = pd.DataFrame(
        data=np.random.randint(0, 101, size=len(ranges)*3).reshape(len(ranges), 3),
        index=ranges, columns=['korean', 'english', 'math']
    )
    print("\nscores.info()="); scores.info() # <class 'pandas.core.frame.DataFrame'>
    print("\nscores.describe()=", scores.describe(), sep='\n')
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


if False:
    # -------------------------------------
    # - DataFrame.rename(
    #       mapper=None, *, index=None, columns=None, axis=None, copy=None,
    #       inplace=False, level=None, errors='ignore'
    #   )
    # ; rename columns or index labels.
    ranges = pd.date_range("1/1/2023", periods=10)
    scores = pd.DataFrame(
        data=np.random.randint(0, 101, size=len(ranges)*3).reshape(len(ranges), 3),
        index=ranges, columns=['korean', 'english', 'math']
    )
    print('\nscores=', scores, sep='\n')
    # scores=
    #             korean  english  math
    # 2023-01-01      51       92    14
    # 2023-01-02      71       60    20
    # 2023-01-03      82       86    74
    # 2023-01-04      74       87    99
    # 2023-01-05      23        2    21
    # 2023-01-06      52        1    87
    # 2023-01-07      29       37     1
    # 2023-01-08      63       59    20
    # 2023-01-09      32       75    57
    # 2023-01-10      21       88    48

    scores.rename(columns={'korean':'KOR', 'english':'ENG', 'math':'MATH'}, inplace=True)
    print('\nscores=', scores, sep='\n')
    # scores=
    #             KOR  ENG  MATH
    # 2023-01-01   51   92    14
    # 2023-01-02   71   60    20
    # 2023-01-03   82   86    74
    # 2023-01-04   74   87    99
    # 2023-01-05   23    2    21
    # 2023-01-06   52    1    87
    # 2023-01-07   29   37     1
    # 2023-01-08   63   59    20
    # 2023-01-09   32   75    57
    # 2023-01-10   21   88    48
