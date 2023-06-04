#!/usr/bin/env python
# -*- coding:utf-8 -*-
# vim: ft=python ts=4 sw=4 tw=78 expandtab
# ----------------------------------------------------------------------------
# - file : 08_02_customizing_string_formatting.py
# - author : yc0325lee
# - created : 2022-11-20 21:15:23 by yc032
# - modified : 2022-11-20 21:15:23 by yc032
# - description : 
# ----------------------------------------------------------------------------


if False:
    _formats = {
        'ymd' : '{d.year}-{d.month}-{d.day}',
        'mdy' : '{d.month}/{d.day}/{d.year}',
        'dmy' : '{d.day}/{d.month}/{d.year}'
    }

    class Date:
        def __init__(self, year, month, day):
            self.year = year
            self.month = month
            self.day = day
        
        def __format__(self, code):
            if code == '':
                code = 'ymd'
            fmt = _formats[code]
            return fmt.format(d=self)

    d = Date(2012, 12, 21)
    print(format(d))        # 2012-12-21
    print(format(d, 'ymd')) # 2012-12-21
    print(format(d, 'mdy')) # 12/21/2012
    print(format(d, 'dmy')) # 21/12/2012


if True:
    import datetime
    d = datetime.date(2012, 12, 21)
    print(d)
    print(format(d))
    print(format(d,'%A, %B %d, %Y'))
    print('The end is {:%d %b %Y}. Goodbye'.format(d))
    # 2012-12-21
    # 2012-12-21
    # Friday, December 21, 2012
    # The end is 21 Dec 2012. Goodbye
