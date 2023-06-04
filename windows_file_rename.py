# vim: ft=python ts=4 sw=4 tw=999 expandtab
# -*- coding:euc-kr -*-
# ----------------------------------------------------------------------------
# File : rename.py
# Author : yc0325lee
# Created : 2022-09-12 21:16:46 by lee2103
# Modified : 2022-09-12 21:16:46 by lee2103
# Description : 
# -*- coding:utf-8 -*-
# ----------------------------------------------------------------------------
import os
import os.path
import glob
import re

if False:
    for src in glob.glob("*.mp3"):
        dst = "나미 - " + src.replace('-', '.', 1)
        print("[info] renaming {} -> {} ...".format(src, dst))
        os.rename(src, dst)

if False:
    for thing in os.listdir('.'):
        if os.path.isdir(thing):
            index = int(thing)
            oldname = thing
            newname = 'chapter' + '{:02d}'.format(index)
            print('[info] {} -> {}'.format(oldname, newname))
            os.rename(oldname, newname)

if False:
    for src in glob.glob("*.mp3"):
        dst = re.sub('^[0-9]{3} ', '', src)
        print("[info] renaming {} -> {} ...".format(src, dst))
        os.rename(src, dst)
