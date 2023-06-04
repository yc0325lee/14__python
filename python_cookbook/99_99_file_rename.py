#!/usr/bin/env python
# vim: ft=python ts=4 sw=4 tw=78 expandtab
# -*- coding:utf-8 -*-
# ----------------------------------------------------------------------------
# - file : rename.py
# - author : yc0325lee
# - created : 2022-11-13 22:40:13 by yc032
# - modified : 2022-11-13 22:40:13 by yc032
# - description : 
# ----------------------------------------------------------------------------
import os, os.path
import re
import shutil

if False:
    # 1
    for thing in os.listdir('.'):
        if os.path.isdir(thing):
            oldname = thing
            newname = oldname.replace(' ', '')
            print('[info] {} -> {}'.format(oldname, newname))
            os.rename(oldname, newname)

if False:
    # 2
    for dirpath, dirnames, filenames in os.walk("."):
        #print("dirpath=", dirpath)
        #print("dirnames=", dirnames)
        #print("filenames=", filenames)
        #dirpath = os.path.abspath(dirpath)
        #print(dirpath)
        for filename in filenames:
            oldname = dirpath + '\\' + filename
            newname = re.sub('^(\d)\.', r'0\1.', filename)
            newname = re.sub('\.(\d)\.', r'.0\1.', newname)
            print(filename, '->', newname)
            newname = dirpath + '\\' + newname
            os.rename(oldname, newname)

if False:
    # 3
    for dirpath, dirnames, filenames in os.walk("."):
        for filename in filenames:
            if filename.endswith('ipynb'):
                filename = dirpath + '\\' + filename
                command = 'jupyter nbconvert "' + filename + '" --to python'
                #print('command=', command)
                os.system(command)

if False:
    # 4
    for dirpath, dirnames, filenames in os.walk("."):
        for filename in filenames:
            if filename.endswith('ipynb'):
                filename = dirpath + '\\' + filename
                print('[info] unlinking {} ...'.format(filename))
                os.unlink(filename)

if False:
    # 5
    for dirpath, dirnames, filenames in os.walk("."):
        #print("dirpath=", dirpath)
        #print("dirnames=", dirnames)
        #print("filenames=", filenames, end='\n\n')
        for filename in filenames:
            if 'Chapter' in dirpath and filename.endswith('.py'):
                oldname = dirpath + '\\' + filename
                filename = re.sub('(\d{2})\.(\d{2})\. ', r'\1_\2_', filename.lower())
                newname = re.sub('[,\- ]', '_', filename)
                print('[info] copying {} to {}'.format(oldname, newname))
                shutil.copyfile(oldname, newname)
