#!/usr/bin/env python
# -*- coding:utf-8 -*-
# vim: ft=python ts=4 sw=4 tw=78 expandtab
# ----------------------------------------------------------------------------
# - file : misc__python_version_check.py
# - author : yc0325lee
# - created : 2023-05-03 23:06:02 by yc032
# - modified : 2023-05-03 23:06:02 by yc032
# - description : 
# ----------------------------------------------------------------------------
import os, os.path, sys

# (1) string
print("\nsys.version=", sys.version)
# sys.version= 3.9.13 (main, Aug 25 2022, 23:51:50) [MSC v.1916 64 bit (AMD64)]

# (2) tuple
print("\nsys.version_info=", type(sys.version_info), sys.version_info, sep='\n')
print("    sys.version_info.major=", sys.version_info.major)
print("    sys.version_info.minor=", sys.version_info.minor)
print("    sys.version_info.micro=", sys.version_info.micro)
print("    sys.version_info.releaselevel=", sys.version_info.releaselevel)
print("    sys.version_info.serial=", sys.version_info.serial)
print()
print("    sys.version_info[0]=", sys.version_info[0]) # major
print("    sys.version_info[1]=", sys.version_info[1]) # minor
print("    sys.version_info[2]=", sys.version_info[2]) # micro
print("    sys.version_info[3]=", sys.version_info[3]) # releaselevel
print("    sys.version_info[4]=", sys.version_info[4]) # serial
# sys.version_info=
# <class 'sys.version_info'>
# sys.version_info(major=3, minor=9, micro=13, releaselevel='final', serial=0)
#
#     sys.version_info.major= 3
#     sys.version_info.minor= 9
#     sys.version_info.micro= 13
#     sys.version_info.releaselevel= final
#     sys.version_info.serial= 0
#
#     sys.version_info[0]= 3
#     sys.version_info[1]= 9
#     sys.version_info[2]= 13
#     sys.version_info[3]= final
#     sys.version_info[4]= 0

# (3) platform
import platform
print("\nplatform.python_version()=", platform.python_version())
print("\nplatform.python_version_tuple()=", platform.python_version_tuple())
major = int(platform.python_version_tuple()[0])
minor = int(platform.python_version_tuple()[1])
micro = int(platform.python_version_tuple()[2])
print(f"\nmajor= {major:d}, minor= {minor:d}, micro= {micro:d}") # formatted string
# platform.python_version()= 3.9.13
# platform.python_version_tuple()= ('3', '9', '13')
# major= 3, minor= 9, micro= 13
