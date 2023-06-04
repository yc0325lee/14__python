# vim: ft=python ts=4 sw=4 tw=999 expandtab fileencoding=utf-8
# ----------------------------------------------------------------------------
# File : test.py
# Author : yc0325lee
# Created : 2022-03-05 17:19:01 by lee2103
# Modified : 2022-03-05 17:19:01 by lee2103
# Description : 
# ----------------------------------------------------------------------------
import sys
def test():
    print("[info] running {}.{}() ...".format(__name__, sys._getframe().f_code.co_name))
