# vim: ft=python ts=4 sw=4 tw=999 expandtab
# -*- coding:utf-8 -*-
# ----------------------------------------------------------------------------
# File : data__str.py
# Author : yc0325lee
# Created : 2022-02-27 00:24:08 by lee2103
# Modified : 2022-02-27 00:24:08 by lee2103
# Description : 
# ----------------------------------------------------------------------------


if False:
    # - str.split(sep=None, maxsplit=-1)
    # ; return a list of the words in the string, using sep as the delimiter string. 
    # ; maxsplit=-1 -> no limit on the number of splits

    #line = "aaa:bbb:ccc:ddd:eee" -> line.split(sep=':', maxsplit=5)
    line = " aaa bbb ccc ddd eee "
    tokens = line.split()
    for i, token in enumerate(tokens):
        print("token[%d]= %s" % (i, token))

    lines = """
park 800905-1049118
kim 700905-1059119
shin 680419-2051218
lee 911207-1078074
xxx xxxxxx-xxxxxxx
"""
    for lineno, line in enumerate(lines.split("\n"), 1):
        print(lineno, line)
    print()
    for lineno, line in enumerate(lines.split("\n"), 1):
        if line:
            print(lineno, line)


if False:
    # str.join(iterable)
    # ; return a string which is the concatenation of the strings in iterable. 
    a = 'abcde'
    print('a=', a)
    print(''.join(reversed(a)))

    print('-'.join(str(x) for x in range(10)))
    print('-'.join(str(x) for x in reversed(range(10))))


if False:
    # str.replace(old, new[, count])
    # ; return a copy of the string with all occurrences of substring old replaced by new
    src = "aaa-bbb-ccc-ddd-eee"
    dst = src.replace('-', '.')
    print("src= {}, dst= {}".format(src, dst))
    # src= aaa-bbb-ccc-ddd-eee, dst= aaa.bbb.ccc.ddd.eee

if False:
    src = "aaa - bbb-ccc-ddd-eee"
    if ' - ' in src:
        print("src= ", src)

if False:
    # str.rstrip([chars])
    # ; return a copy of the string with trailing characters removed
    # ; the chars argument is a string specifying the set of characters to be removed
    # ; chars is omitted -> whitespaces!
    src = "aaa - bbb-ccc-ddd-eee"
    if ' - ' in src:
        dst = src.rstrip('-eee')
        print("src=", src)
        print("dst=", dst)

