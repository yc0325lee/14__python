#!/usr/bin/env python
# -*- coding:utf-8 -*-
# vim: ft=python ts=4 sw=4 tw=78 expandtab
# ----------------------------------------------------------------------------
# - file : raw_string.py
# - author : yc0325lee
# - created : 2023-01-09 22:49:49 by yc032
# - modified : 2023-01-09 22:49:49 by yc032
# - description : 
# ----------------------------------------------------------------------------

# - raw string r"pattern" or r'pattern'
# ; every backslash ('\') in a regular expression doesn't need to be prefixed
#   with another one to escape it.
# ; re.match("\\W(.)\\1\\W", " ff ")
# ; re.match(r"\W(.)\1\W", " ff ")
