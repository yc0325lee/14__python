#!/usr/bin/env python
# -*- coding:utf-8 -*-
# vim: ft=python ts=4 sw=4 tw=78 expandtab
# ----------------------------------------------------------------------------
# - file : 01_03_keeping_the_last_n_items.py
# - author : yc0325lee
# - created : 2022-11-19 18:16:28 by yc032
# - modified : 2022-11-19 18:16:28 by yc032
# - description : 
# ----------------------------------------------------------------------------

if True:
    #  keeping the last n items
    import collections

    def search(lines, pattern, history=5): # generator function
        previous_lines = collections.deque(maxlen=history)
        print('[dbg ] ', lines)
        # <_io.TextIOWrapper name='input.txt' mode='r' encoding='utf8'>
        for line in lines:
            if pattern in line:
                yield line, previous_lines
            previous_lines.append(line)

    filename = 'input.txt'
    with open(filename, "r", encoding="utf8") as infile:
        for line, previous in search(infile, 'continu', 5):
            for prev in previous:
                print('<prev>', prev, end='')
            print('<curr>', line)

if False:
    history = 5
    previous = collections.deque(maxlen=history)
    filename = 'input.txt'
    with open(filename, "r", encoding="utf8") as infile:
        for lineno, line in enumerate(infile, 1):
            for item in previous:
                print(item, end='')
            print(str(lineno) + ": " + line, end='\n')
            previous.append(line)
