#!/usr/bin/env python
# -*- coding:utf-8 -*-
# vim: ft=python ts=4 sw=4 tw=78 expandtab
# ----------------------------------------------------------------------------
# - file : 02_03_matching_strings_using_shell_wildcard_patterns.py
# - author : yc0325lee
# - created : 2022-11-20 19:24:47 by yc032
# - modified : 2022-11-20 19:24:47 by yc032
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

if False:
    # - fnmatch.filter(names, pattern)
    # ; construct a list from those elements of the iterable names that match
    #   pattern.
    # ; same as [name for name in names if fnmatch(name, pattern)]
    files = os.listdir('.')
    filtered = fnmatch.filter(files, 'lib__*.py')
    for file in filtered:
        print(file)


if False:
    files = ['Dat1.csv','Dat2.csv','config.ini','foo.py']
    print [name for name in names if fnmatch.fnmatch(name,'Dat*.csv')]
    print [name for name in names if not fnmatch.fnmatch(name,'*.py')]


    addresses = [
        '5412 N CLARK ST',
        '1060 W ADDISON ST',
        '1039 W GRANVILLE AVE',
        '2122 N CLARK ST',
        '4802 N BROADWAY'
    ]

    from fnmatch import fnmatchcase
    filtered = [addr for addr in addresses if fnmatch.fnmatchcase(addr,'* ST')]
    filtered = [addr for addr in addresses if fnmatch.fnmatchcase(addr,'54[0-9][0-9] *CLARK*')]
