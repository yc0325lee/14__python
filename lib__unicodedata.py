# vim: ft=python ts=4 sw=4 tw=999 expandtab
# ----------------------------------------------------------------------------
# File : lib__unicodedata.py
# Author : yc0325lee
# Created : 2022-03-19 23:47:28 by lee2103
# Modified : 2022-03-19 23:47:28 by lee2103
# Description : 
# ----------------------------------------------------------------------------

# name()
if True:
    from unicodedata import name
    for i in range(32, 256):
        if 'SIGN' in name(chr(i), ''):
            print("i= {}, name={}".format(i, name(chr(i),'')))
