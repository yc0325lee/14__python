# vim: ft=python ts=4 sw=4 tw=80 expandtab
# -*- coding:utf-8 -*-
# ----------------------------------------------------------------------------
# - file : misc__exotic_syntax.py
# - author : yc0325lee
# - created : 2022-10-13 00:05:37 by lee2103
# - modified : 2022-10-13 00:05:37 by lee2103
# - description : 
# ----------------------------------------------------------------------------

# python ideas
# - generic operations on sequences
# ; built-in tuple and mapping types
# ; structure by indentation
# ; strong typing without variable declarations
# ; and more.

# variables are all handles that referencing some data in the memory

# line break
# ; in python code, line breaks are ignored inside pairs of [], {}, or ().
# ; so you can build multiline lists, listcomps, genexps, dictionaries and the
#   like without using the ugly \ line continuation escape.


if False:
    # normal strings vs. raw strings(r' quoting)
    print('first line\nsecond line') # normal strings allow escaped characters
    print(r'first line\nfirst line') # raw strings treat backslashes as literal characters

# sorted() vs reversed()
# ; sorted() -> return a new sorted list from the items in iterable
# ; reversed() -> return a reverse iterator
