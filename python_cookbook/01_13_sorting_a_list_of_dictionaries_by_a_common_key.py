#!/usr/bin/env python
# -*- coding:utf-8 -*-
# vim: ft=python ts=4 sw=4 tw=78 expandtab
# ----------------------------------------------------------------------------
# - file : 01_13_sorting_a_list_of_dictionaries_by_a_common_key.py
# - author : yc0325lee
# - created : 2022-11-19 21:55:15 by yc032
# - modified : 2022-11-19 21:55:15 by yc032
# - description : 
# ----------------------------------------------------------------------------

if False:
    # - using lambda expression key
    rows = [
        {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
        {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
        {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
        {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
    ]

    print('\n# sorted by fname')
    for row in sorted(rows, key=lambda k: k['fname']):
        print(row)

    print('\n# sorted by lname')
    for row in sorted(rows, key=lambda k: k['lname']):
        print(row)

    print('\n# sorted by uid')
    for row in sorted(rows, key=lambda k: k['uid']):
        print(row)

if True:
    # - using operator.itemgetter
    # ; itemgetter() typically runs a bit faster
    import operator

    rows = [
        {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
        {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
        {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
        {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
    ]

    print('\n# sorted by fname')
    for row in sorted(rows, key=operator.itemgetter('fname')):
        print(row)

    print('\n# sorted by lname')
    for row in sorted(rows, key=operator.itemgetter('lname')):
        print(row)

    print('\n# sorted by uid')
    for row in sorted(rows, key=operator.itemgetter('uid')):
        print(row)

    print('\nminimum =', min(rows, key=operator.itemgetter('uid')))
    print('\nmaximum =', max(rows, key=operator.itemgetter('uid')))
