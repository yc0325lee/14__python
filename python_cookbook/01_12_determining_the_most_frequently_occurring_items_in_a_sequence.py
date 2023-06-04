#!/usr/bin/env python
# vim: ft=python ts=4 sw=4 tw=78 expandtab
# -*- coding:utf-8 -*-
# ----------------------------------------------------------------------------
# - file : 01_12_determining_the_most_frequently_occurring_items_in_a_sequence.py
# - author : yc0325lee
# - created : 2022-11-15 23:42:04 by yc032
# - modified : 2022-11-15 23:42:04 by yc032
# - description : 
# ----------------------------------------------------------------------------
from collections import Counter

if False:
    # - class collections.Counter([iterable-or-mapping])
    # ; a counter is a dict subclass for counting hashable objects. it is a
    #   collection where elements are stored as dictionary keys and their counts
    #   are stored as dictionary values.
    words = [
        'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
        'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
        'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
        'my', 'eyes', "you're", 'under'
    ]
    counted = Counter(words)
    #print('counted =', counted)
    for word in counted:
        print('{} = {}'.format(word, counted[word]))

    print('\ntotal =', counted.total())

    top_three = counted.most_common(3)
    print('top_three =', top_three)

    morewords = ['why','are','you','not','looking','in','my','eyes']

    # updating more - (1)
    for word in morewords:
        counted[word] += 1

    # updating more - (2)
    counted.update(morewords)

    # combining counts using '+'
    a = Counter(words)
    b = Counter(morewords)
    combined = a + b
    print('\ncombined =', combined)
