# vim: ft=python ts=4 sw=4 tw=78 expandtab
# -*- coding:utf-8 -*-
# ----------------------------------------------------------------------------
# - file : lib__glob.py
# - author : yc0325lee
# - created : 2022-11-03 22:10:05 by lee2103
# - modified : 2022-11-03 22:10:05 by lee2103
# - description : 
# ; unix style pathname pattern expansion
# ; the glob module finds all the pathnames matching a specified pattern
#   according to the rules used by the unix shell, although results are returned
#   in arbitrary order.
# ----------------------------------------------------------------------------
import glob

if False:
    # - glob.glob(pathname, *, root_dir=None, dir_fd=None, recursive=False, include_hidden=False)
    # ; return a possibly empty list of path names that match pathname, which
    #   must be a string containing a path specification
    files = glob.glob("lib__*.py") # returns list
    for i, file in enumerate(files):
        print(f"file[{i}]= {file}")

if True:
    # - glob.iglob(pathname, *, root_dir=None, dir_fd=None, recursive=False, include_hidden=False)
    # ; return an iterator which yields the same values as glob() without
    # actually storing them all simultaneously.
    items = glob.iglob("lib__*.py") # generator-expr
    for i, item in enumerate(items):
        print(f"file[{i}]= {item}")
