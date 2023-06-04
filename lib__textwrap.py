#!/usr/bin/env python
# -*- coding:utf-8 -*-
# vim: ft=python ts=4 sw=4 tw=78 expandtab
# ----------------------------------------------------------------------------
# - file : lib__textwrap.py
# - author : yc0325lee
# - created : 2022-11-26 00:36:07 by yc032
# - modified : 2022-11-26 00:36:07 by yc032
# - description : 
# ----------------------------------------------------------------------------

text = "Look into my eyes, look into my eyes, the eyes, the eyes, \
the eyes, not around the eyes, don't look around the eyes, \
look into my eyes, you're under."

if True:
    print(text, end='\n\n')

import textwrap
print(textwrap.fill(text, 70), end='\n\n')
print(textwrap.fill(text, 40), end='\n\n')
print(textwrap.fill(text, 40, initial_indent='     '), end='\n\n')
print(textwrap.fill(text, 40, subsequent_indent='     '), end='\n\n')

import os
columns = os.get_terminal_size().columns
lines = os.get_terminal_size().lines
print('columns =', columns)
print('lines =', lines)
print(textwrap.fill(text, columns), end='\n\n')
