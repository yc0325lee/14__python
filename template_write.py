# vim: ft=python ts=4 sw=4 tw=999 expandtab
# -*- coding:utf-8 -*-
# ----------------------------------------------------------------------------
# File : template_write.py
# Author : yc0325lee
# Created : 2022-10-09 16:42:17 by lee2103
# Modified : 2022-10-09 16:42:17 by lee2103
# Description : 
# ----------------------------------------------------------------------------
import time

def now():
    return time.strftime("%Y%m%d_%H%M%S", time.localtime(time.time()))


def write_header():
    args = {
        'filename' : 'file.txt',
        'title' : 'this file is for test',
        'created' : now(),
    }
    print(
"""# vim: ft=python ts=4 sw=4 tw=999 expandtab
# -*- coding:utf-8 -*-
# ----------------------------------------------------------------------------
# - file : {filename:s}
# - title : {title:s}
# - created : {created:s}
# - description
# ----------------------------------------------------------------------------"""
        .format(**args)
    )


write_header()
