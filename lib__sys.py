#!/usr/bin/env python
# -*- coding:utf-8 -*-
# vim: ft=python ts=4 sw=4 tw=78 expandtab
# ----------------------------------------------------------------------------
# File : lib__sys.py
# Author : yc0325lee
# Created : 2022-03-05 18:54:25 by lee2103
# Modified : 2022-03-05 18:54:25 by lee2103
# Description : 
# ----------------------------------------------------------------------------
import sys

# sys.argv - command line arguments
if False:
    args = sys.argv[1:]
    for i, arg in enumerate(args):
        print("arg[%d]= %s" % (i, arg))

# sys.exit()

if True:
    # sys.path
    sys.path.append(r"D:\WORK\14__python\temp")
    sys.path.insert(0, r"D:\WORK\14__python\package_example")
    for i, path in enumerate(sys.path):
        print("path[{}]= {}".format(i, path))

# file encoding information
if False:
    print("encoding=", sys.getfilesystemencoding()) # default= utf-8

if False:
    # sys._getframe()
    thisFunc = sys._getframe().f_code.co_name
