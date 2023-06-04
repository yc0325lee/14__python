#!/usr/bin/env python
# -*- coding:utf-8 -*-
# vim: ft=python ts=4 sw=4 tw=78 expandtab
# ----------------------------------------------------------------------------
# - file : 01_15_grouping_records_together_based_on_a_field.py
# - author : yc0325lee
# - created : 2022-11-19 22:48:08 by yc032
# - modified : 2022-11-19 22:48:08 by yc032
# - description : 
# ----------------------------------------------------------------------------

if False:
    # - itertools.groupby(iterable, key=None)
    # ; make an iterator that returns consecutive keys and groups from the
    #   iterable. the key is a function computing a key value for each element.
    import operator
    import itertools

    rows = [
        {'address': '5412 N CLARK', 'date': '07/01/2012'},
        {'address': '5148 N CLARK', 'date': '07/04/2012'},
        {'address': '5800 E 58TH', 'date': '07/02/2012'},
        {'address': '2122 N CLARK', 'date': '07/03/2012'},
        {'address': '5645 N RAVENSWOOD', 'date': '07/02/2012'},
        {'address': '1060 W ADDISON', 'date': '07/02/2012'},
        {'address': '4801 N BROADWAY', 'date': '07/01/2012'},
        {'address': '1039 W GRANVILLE', 'date': '07/04/2012'},
    ]
    print('\n# unsorted')
    for row in rows:
        print(row)

    # (1) sorting first
    rows.sort(key=operator.itemgetter('date'))
    print('\n# sorted')
    for row in rows:
        print(row)

    for date, items in itertools.groupby(rows, key=operator.itemgetter('date')):
        print('date =', date)
        for item in items:
            print('   ', item)
    

if True:
    # - using collections.defaultdict
    import collections

    rows = [
        {'address': '5412 N CLARK', 'date': '07/01/2012'},
        {'address': '5148 N CLARK', 'date': '07/04/2012'},
        {'address': '5800 E 58TH', 'date': '07/02/2012'},
        {'address': '2122 N CLARK', 'date': '07/03/2012'},
        {'address': '5645 N RAVENSWOOD', 'date': '07/02/2012'},
        {'address': '1060 W ADDISON', 'date': '07/02/2012'},
        {'address': '4801 N BROADWAY', 'date': '07/01/2012'},
        {'address': '1039 W GRANVILLE', 'date': '07/04/2012'},
    ]

    rows_by_date = collections.defaultdict(list)
    for row in rows:
        rows_by_date[row['date']].append(row)

    for date in sorted(rows_by_date.keys()):
        print('date =', date)
        for item in rows_by_date[date]:
            print('   ', item)
