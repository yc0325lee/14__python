#!/usr/bin/env python
# -*- coding:utf-8 -*-
# vim: ft=python ts=4 sw=4 tw=999 expandtab
# ----------------------------------------------------------------------------
# File : file_io.py
# Author : yc0325lee
# Created : 2022-03-01 13:42:43 by lee2103
# Modified : 2022-03-01 13:42:43 by lee2103
# Description : 
# - Reference
#   ; The Python Tutorial -> 7.2. Reading and Writing Files
# ----------------------------------------------------------------------------

if False:
    # specifying hier-path for file-name
    filename = "/user/WORK/14__python" # ok!
    #filename = "c:\user\work\14__python" # error!
    filename = "c:\\user\\work\\14__python" # ok!
    filename = r"c:\user\work\14__python" # ok! -> "raw string"


if False:
    # write
    # ; print(..., file=outfile) or outfile.write(...)
    import sys
    outfile = open("temp.txt", "w", encoding="utf8")
    print("[info] writing to temp.txt ...", file=sys.stderr)
    print("0: This is for test!!!", file=outfile)
    print("1:", file=outfile)
    print("2:", file=outfile)
    print("3:", file=outfile)
    print("4:", file=outfile)
    print("5:", file=outfile)
    print("[info] closing temp.txt ...", file=sys.stderr)
    outfile.close()

if False:
    # read
    infile = open("temp.txt", "r", encoding="utf8")
    print( infile.readline(), end="" )
    print( infile.readline(), end="" )
    print( infile.readline(), end="" )
    print( infile.readline(), end="" )
    print( infile.readline(), end="" )
    infile.close()

if False:
    # read
    filename = 'input.txt'
    infile = open(filename, "r", encoding="utf8")
    lineno = 1
    while True:
        line = infile.readline()
        if line:
            line = line.rstrip() # remove newline character
            print(lineno, line)
            lineno += 1
        else:
            break
    infile.close()

if False:
    # read - whole lines
    filename = 'input.txt'
    infile = open(filename, "r", encoding="utf8")
    lines = infile.readlines() # readlines()
    for line in lines:
        print(line, end="")
    infile.close()
    
if True:
    # read using 'with' statement -> simpler and manageable
    filename = 'input.txt'
    with open(filename, "r", encoding="utf8") as infile:
        lines = infile.readlines()
        for line in lines:
            line = line.rstrip()
            print(line)
    
if False:
    # tracing line numbers
    filename = 'input.txt'
    with open(filename, "r", encoding="utf8") as infile:
        lines = infile.readlines()
        for lineno, line in enumerate(lines, 1):
            line = line.rstrip() # remove newline first!
            if line not in (None, ''):
                print(lineno, line)
    
if False:
    # [best]
    filename = 'input.txt'
    with open(filename, "r", encoding="utf8") as infile:
        for lineno, line in enumerate(infile, 1):
            line = line.rstrip() # remove newline first!
            if line not in (None, ''):
                print(lineno, line)

if True:
    # keeping last(recent) n lines
    import collections
    depth = 5
    previous = collections.deque(maxlen=depth)
    filename = 'input.txt'
    with open(filename, "r", encoding="utf8") as infile:
        for lineno, line in enumerate(infile, 1):
            line = line.rstrip()
            for i, prev in enumerate(previous):
                print('[prev-{}] {}'.format(depth-1-(i%depth), prev))
            print(str(lineno) + ':', line)
            previous.append(line)

# -------------------------------------------------------------------
# - inFile.read([n])
# ; Returns the read bytes in form of a string.
# ; Reads n bytes, if no n specified, reads the entire file.
#
# - inFile.readline([n])
# ; reads a line of the file and returns in form of a string.
# ; for specified n, reads at most n bytes.
# ; however, does not reads more than one line,
# ; even if n exceeds the length of the line.
# ; a newline character (\n) is left at the end of the string
#
# - inFile.readlines()
# ; reads all the lines and return them as each line a string element
#   in a list
# -------------------------------------------------------------------
