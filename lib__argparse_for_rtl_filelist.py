#!/usr/bin/env python
# -*- coding:utf-8 -*-
# vim: ft=python ts=4 sw=4 tw=78 expandtab
# ----------------------------------------------------------------------------
# - file : lib__argparse_for_rtl_filelist.py
# - author : yc0325lee
# - created : 2023-05-28 20:11:22 by yc032
# - modified : 2023-05-28 20:11:22 by yc032
# - description : 

# -------------------------------------
# - vcs-like parameters
# ; +libext+I<ext>+I<ext>...	libext (I<ext>)
# ; +incdir+I<dir>		incdir (I<dir>)
# ; +define+I<var>=I<value>	define (I<var>,I<value>)
# ; +define+I<var>		define (I<var>,undef)
# ; +librescan		Ignored
# ; -F I<file>		Parse parameters in file relatively
# ; -f I<file>		Parse parameters in file
# ; -v I<file>		library (I<file>)
# ; -y I<dir>		module_dir (I<dir>)
# ; all others		Put in returned list
#
# -------------------------------------
# - gcc-like parameters
# ; -DI<var>=I<value>		define (I<var>,I<value>)
# ; -DI<var>		define (I<var>,undef)
# ; -UI<var>		undefine (I<var>)
# ; -II<dir>		incdir (I<dir>)
# ; -F I<file>		Parse parameters in file relatively
# ; -f I<file>		Parse parameters in file
# ; all others		Put in returned list
#
# ----------------------------------------------------------------------------
import os, os.path, sys
import pprint
import random
import argparse


# -------------------------------------
# - argparser
# ; options with '-' character or filename
# ; parse_known_args() used to filter out known arguments
parser = argparse.ArgumentParser(
    prog=os.path.basename(__file__),
    description="command-line argument handling for reading hdl filelist",
    epilog="----------- end of usage -------------",
    prefix_chars='-',
)
parser.add_argument(
    '-f', '--filelist', action='append', required=False, default=[],
    dest='filelists_abs',
    help="list of files relative to current directory",
)
parser.add_argument(
    '-F', '--FILELIST', action='append', required=False, default=[],
    dest='filelists_rel',
    help="list of files relative to filelist directory",
)
parser.add_argument( # library files
    '-v', '--vfile', action='append', required=False,
    dest='libfiles',
    help="files that contain module information for unresoved modules",
)
parser.add_argument( # library directories
    '-y', '--ydir', action='append', required=False,
    dest='libdirs',
    help="directories that contain module files for unresoved modules",
)
parser.add_argument( # library directories
    '-D', '--DEFILE', action='append', required=False,
    dest='defines',
    help="macro definitions and corresponding values",
)

parser.print_help()


arguements = """
-f vcode.dut.f --filelist vcode.tb.f
-F vcode.cdns.f --FILELIST vcode.snps.f
-v libfile1.v -v libfile2.v -v libfile3.v
-y libdir1 -y libdir2 -y libdir3
-DVERBOSE -DDEBUG=3 --DEFINE WIDTH=4 --DEFINE HEIGHT=16
file1.v file2.v file3.sv file4.vhd
""".split()

args, remainings = parser.parse_known_args(arguements)
print('args=', args)
print('remainings=', remainings)
# args= Namespace(
#     filelists_abs=['vcode.dut.f', 'vcode.tb.f'],
#     filelists_rel=['vcode.cdns.f', 'vcode.snps.f'],
#     libfiles=['libfile1.v', 'libfile2.v', 'libfile3.v'],
#     libdirs=['libdir1', 'libdir2', 'libdir3'],
#     defines=['VERBOSE', 'DEBUG=3']
# )
# remainings= ['--DEFINE', 'WIDTH=4', '--DEFINE', 'HEIGHT=16', 'file1.v', 'file2.v', 'file3.sv', 'file4.vhd']

print("\n# args")
for key, val in vars(args).items():
    print(f"{key} = {val}")
# filelists_abs = ['vcode.dut.f', 'vcode.tb.f']
# filelists_rel = ['vcode.cdns.f', 'vcode.snps.f']
# libfiles = ['libfile1.v', 'libfile2.v', 'libfile3.v']
# libdirs = ['libdir1', 'libdir2', 'libdir3']
# defines = ['VERBOSE', 'DEBUG=3']

print("\n# remainings")
for i, item in enumerate(remainings):
    print(f"item[{i}]= {item}")
# item[0]= --DEFINE
# item[1]= WIDTH=4
# item[2]= --DEFINE
# item[3]= HEIGHT=16
# item[4]= file1.v
# item[5]= file2.v
# item[6]= file3.sv
# item[7]= file4.vhd


