#!/usr/bin/env python
# -*- coding:utf-8 -*-
# vim: ft=python ts=4 sw=4 tw=78 expandtab
# ----------------------------------------------------------------------------
# - file : 02_15_interpolating_variables_in_strings.py
# - author : yc0325lee
# - created : 2022-11-25 23:46:12 by yc032
# - modified : 2022-11-25 23:46:12 by yc032
# - description : 
# ----------------------------------------------------------------------------

if False:
    # - using str.format()
    s = '{name} has {n} messages.'
    interpolated = s.format(name='Guido', n = 37)
    print('interpolated =', interpolated)
    # interpolated = Guido has 37 messages.

    d = dict(
        name = 'Guido',
        n = 37
    )
    interpolated = s.format(**d) # unpack dict
    print('interpolated =', interpolated)
    # interpolated = Guido has 37 messages.


if True:
    # - str.format_map(mapping)
    # ; similar to str.format(**mapping), except that mapping is used directly
    #   and not copied to a dict
    s = '{name} has {n} messages.'
    name = 'Guido'
    n = 37
    interpolated = s.format_map(vars())
    print('interpolated =', interpolated)
    # interpolated = Guido has 37 messages.


    class Info:
        def __init__(self, name, n):
            self.name = name
            self.n = n

    info = Info('Guido',37)
    interpolated = s.format_map(vars(info))
    print('interpolated =', interpolated)
    # interpolated = Guido has 37 messages.


    # dealing with missing values
    class dict2(dict):
        # returns key string upon KeyError
        def __missing__(self, key):
            return '{' + key + '}'

    del n
    interpolated = s.format_map(dict2(vars()))
    print('interpolated =', interpolated)
    # interpolated = Guido has {n} messages.

    import sys
    # - sys._getframe(1) returns the stack frame of the caller
    def sub(text):
        return text.format_map(dict2(sys._getframe(1).f_locals))

    name = 'Guido'
    n = 37
    print(sub('Hello {name}'))
    print(sub('You have {n} messages.'))
    print(sub('Your favorite color is {color}'))
