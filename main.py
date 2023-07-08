# vim: ft=python ts=4 sw=4 tw=999 expandtab
# ----------------------------------------------------------------------------
# File : main.py
# Author : yc0325lee
# Created : 2022-03-01 13:52:09 by lee2103
# Modified : 2022-03-01 13:52:09 by lee2103
# Description : 
# -*- coding:euc-kr -*-
# -*- coding:utf-8 -*-
# ----------------------------------------------------------------------------
import os, os.path, sys
import pprint
import argparse
import random
import re
import csv
import pickle

parser = argparse.ArgumentParser(
    prog="python main.py",
    description="explanation: template file for starting a new script",
    epilog="----------- end of usage -------------"
)
parser.add_argument("--version", action="version", version="%(prog)s v1.00", help="show program version")
parser.add_argument("infile", type=str, action="store", help="input file name (str)")
group = parser.add_mutually_exclusive_group()
group.add_argument("-v", "--verbose", action="store_true", help="turn on verbose-mode")
group.add_argument("-q", "--quiet", action="store_true", help="turn on quiet-mode")

args = parser.parse_args() # args.infile(str)

# read and write with lineno
# ; usage: python main.py input.txt
if False:
    with open(args.infile, "r", encoding="utf8") as infile:
        for lineno, line in enumerate(infile, 1):
            print("{}: {}".format(lineno, line), end='')


# read
if False:
    infile = open("input.txt", "r", encoding="utf8")
    regex = re.compile(r'\d+/\d+/\d+')
    while True:
        line = infile.readline()
        if line and regex.match(line): # line.startswith('regex')
            print(line, end="")          # line.endswith('regex')
        else:
            break
    infile.close()

# read
if False:
    with open("input.txt", "r", encoding="utf8") as infile:
        lines = (line.strip() for line in infile)
        for line in lines:
            print(line)

if False:
    with open(args.infile, "r", encoding="utf8") as infile:
        for line in infile:
            fields = line.split(',')

if False:
    regex = re.compile(r'\d+-\d+-\d+')
    with open(args.infile, "r", encoding="utf8") as infile:
        for line in infile:
            if line and regex.search(line):
                line = line.rstrip()
                print(line)

if False:
    inside = False # flag
    with open(args.infile, "r", encoding="utf8") as infile:
        for lineno, line in enumerate(infile, 1):
            if line.startswith('# File'):
                inside = True
                continue
            elif line.startswith('amount'):
                inside = False
                continue

            if inside:
                line = line.rstrip()
                print(f'{lineno}: {line}')
