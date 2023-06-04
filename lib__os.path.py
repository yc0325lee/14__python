# vim: ft=python ts=4 sw=4 tw=78 expandtab
# ----------------------------------------------------------------------------
# File : lib__os.path.py
# Author : yc0325lee
# Created : 2022-09-13 00:11:20 by lee2103
# Modified : 2022-09-13 00:11:20 by lee2103
# Description : 
# - common pathname manipulations
# ----------------------------------------------------------------------------
import os.path

if False:
    # os.path.exists(path)
    # ; return true if path refers to an existing path or an open file descriptor
    infile = 'input.txt'
    if os.path.exists(infile):
        print("infile= ", infile)
    else:
        print("[err ] something's wrong!")

if False:
    # os.path.abspath(path)
    # ; return a normalized absolutized version of the pathname path.
    print("abspath=", os.path.abspath('main.py'))
    # abspath= D:\WORK\14__python\main.py

if False:
    # os.path.split(path) -> (dirname, basename)
    # ; split the pathname path into a pair, (head, tail) where tail is the last
    #   pathname component and head is everything leading up to that. 
    # os.path.basename(path)
    # ; return the base name of pathname path
    # os.path.dirname(path)
    # ; return the directory name of pathname path

    path = r"user\hls001\TEMP\project.tcl" # raw-string
    dirname, basename = os.path.split(path)
    print("dirname=", dirname, os.path.dirname(path))
    print("basename=", basename, os.path.basename(path))
    # dirname= user\hls001\TEMP user\hls001\TEMP
    # basename= project.tcl project.tcl

if False:
    # - os.path.splitext(path)
    # ; split the pathname path into a pair (root, ext) such that
    #   root + ext == path
    root, extension = os.path.splitext(__file__)
    print('root=', root)
    print('extension=', extension)
    # root= C:\WORK\14__python\lib__os.path
    # extension= .py
