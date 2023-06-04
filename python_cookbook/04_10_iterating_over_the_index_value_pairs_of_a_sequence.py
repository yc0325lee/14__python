#!/usr/bin/env python
# -*- coding:utf-8 -*-
# vim: ft=python ts=4 sw=4 tw=78 expandtab
# ----------------------------------------------------------------------------
# - file : 04_10_iterating_over_the_index_value_pairs_of_a_sequence.py
# - author : yc0325lee
# - created : 2022-11-17 23:02:15 by yc032
# - modified : 2022-11-17 23:15:37 by yc032
# - description : 
# ----------------------------------------------------------------------------

if True:
    # using 'enumerate' built-in
    basket = ['a', 'b', 'c', 'd', 'e']
    for idx, val in enumerate(basket): # start=0
        print(idx, val)
    # 0 a
    # 1 b
    # 2 c
    # 3 d
    # 4 e

    for idx, val in enumerate(basket, 1): # start=1
        print(idx, val)
    # 1 a
    # 2 b
    # 3 c
    # 4 d
    # 5 e


if False:
    # tracking line numbers in files
    filename = 'input.txt'
    accumulated = 0
    with open(filename, "r", encoding="utf8") as infile:
        for lineno, line in enumerate(infile, 1):
            if line:
                fields = line.split()
                try:
                    count = int(fields[1])
                    accumulated += count
                except ValueError as err:
                    print('[err ] line {}: parse error {}'.format(lineno, err))


if False:
    import collections
    word_summary = collections.defaultdict(list)

    filename = 'input.txt'
    with open(filename, "r", encoding="utf8") as infile:
        lines = infile.readlines()

    for idx, line in enumerate(lines):
        # create a list of words in current line
        words = [word.strip().lower() for word in line.split()]
        for word in words:
            word_summary[word].append(idx)

if False:
    # handling a sequence of tuple
    data = [(1, 2), (3, 4), (5, 6), (7, 8)]
    for i, (x, y) in enumerate(data):
        print("[{}] {}, {}".format(i, x, y))
