#!/usr/bin/env python
# -*- coding:utf-8 -*-
# vim: ft=python ts=4 sw=4 tw=78 expandtab
# ----------------------------------------------------------------------------
# - file : lib__fnmatch.py
# - author : yc0325lee
# - created : 2022-11-20 19:27:20 by yc032
# - modified : 2022-11-20 19:27:20 by yc032
# - description : 
# - fnmatch — Unix filename pattern matching
# ; provides support for unix shell-style wildcards, which are not the same as
#   regular expressions
#   +---------+----------------------------------+
#   | Pattern | Meaning                          |
#   +---------+----------------------------------+
#   | *       | matches everything               |
#   | ?       | matches any single character     |
#   | [seq]   | matches any character in seq     |
#   | [!seq]  | matches any character not in seq |
#   +---------+----------------------------------+
#
# ----------------------------------------------------------------------------
import fnmatch
import os

if False:
    # - fnmatch.fnmatch(filename, pattern)
    # ; test whether the filename string matches the pattern string, returning
    #   true or false
    for file in os.listdir('.'):
        if fnmatch.fnmatch(file, 'lib__*.py'):
            print(file)

if False:
    # - fnmatch.fnmatchcase(filename, pattern)
    # ; test whether filename matches pattern, returning true or false; the
    #   comparison is case-sensitive
    pass

if True:
    # - fnmatch.filter(names, pattern)
    # ; construct a list from those elements of the iterable names that match
    #   pattern.
    # ; same as [name for name in names if fnmatch(name, pattern)]
    files = os.listdir('.')
    filtered = fnmatch.filter(files, 'lib__*.py')
    for file in filtered:
        print(file)
