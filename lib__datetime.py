# vim: ft=python ts=4 sw=4 tw=999 expandtab
# -*- coding:utf-8 -*-
# ----------------------------------------------------------------------------
# - file : lib__datetime.py
# - author : yc0325lee
# - created : 2022-10-10 19:22:15 by lee2103
# - modified : 2022-10-10 19:22:15 by lee2103
# - description : 
# ----------------------------------------------------------------------------
from datetime import datetime

if True:
    now = datetime.now()
    print("now=", now)
    print("now=", format(now, '%H:%M:%S'))
    print("now=", format(now, '%y%m%d_%H%M%S'))
