# vim: ft=python ts=4 sw=4 tw=78 expandtab
# -*- coding:utf-8 -*-
# ----------------------------------------------------------------------------
# - file : lib__os.py
# - author : yc0325lee
# - created : 2022-11-10 15:52:26 by yc032
# - modified : 2022-11-10 15:52:26 by yc032
# - description : 
# ----------------------------------------------------------------------------
import os
import os.path

# os.environ
if False:
    for key, value in os.environ.items():
        print("key= {}, value= {}".format(key, value))
        if key == "PATH":
            paths = value.split(';')
            for i, path in enumerate(paths):
                print("    path[{}]= {}".format(i, path))

# os.getcwd()
if False:
    print("[info] os.getcwd()=", os.getcwd())

# os.chdir()

if True:
    # - os.system(command)
    # ; execute the command (a string) in a subshell. this is implemented by
    #   calling the standard c function system(), and has the same limitations
    pass

# os.popen()
if False:
    inFile = os.popen("ls -1")
    while True:
        line = inFile.readline()
        if line:
            line = line.strip() # remove newline character
            print("file=", line)
        else:
            break
if False:
    inFile = os.popen("ls -1")
    for i, name in enumerate(inFile, 1):
        print(i, name, end='')

# os.mkdir("some_path")
# os.rmdir("some_path")
# os.unlink("some_path")
# os.rename("from.txt", "to.txt")
# os.path.splitext()

if False:
    # - os.rename("from.txt", "to.txt")
    # - os.rename(src, dst, *, src_dir_fd=None, dst_dir_fd=None)
    # ; rename the file or directory src to dst.
    # ; if dst exists, the operation will fail with an exception.
    pass

if False:
    # - os.unlink(path, *, dir_fd=None)
    # ; remove (delete) the file path. this function is semantically identical
    #   to remove(); 
    pass


if False:
    # - os.listdir(path='.')
    # ; return a list containing the names of the entries in the directory
    #   given by path. 
    files = [name for name in os.listdir(".") if os.path.isfile(name)] # files
    dirs = [name for name in os.listdir(".") if os.path.isdir(name)] # directories
    for item in os.listdir("."):
        if os.path.isfile(item):
            print("[file]", item)
        elif os.path.isdir(item):
            print("[dir ]", item)
        else:
            print("[unkn]", item) # unknown


if False:
    # - os.walk(top, topdown=True, onerror=None, followlinks=False)
    # ; generate the file names in a directory tree by walking the tree either
    #   top-down or bottom-up. 
    # ; output - 3-tuple (dirpath, dirnames, filenames)
    # - os.path.abspath(path)
    # ; return a normalized absolutized version of the pathname path
    print("[info] testing os.walk() ...")
    for dirpath, dirnames, filenames in os.walk("."):
        #print("dirpath=", dirpath)
        #print("dirnames=", dirnames)
        #print("filenames=", filenames)
        dirpath = os.path.abspath(dirpath)
        for filename in filenames:
            print(dirpath + '\\' + filename)
        print()

# 5.11. manipulating pathnames
if False:
    import os

    path = '/users/beazley/Data/data.csv'
    print("path=", path)
    print("basename=", os.path.basename(path))
    print("dirname=", os.path.dirname(path))
    print("joined=", os.path.join(r'\user', 'yclee03', os.path.basename(path)))
    print("splitext=", os.path.splitext(path))
    # path= /users/beazley/Data/data.csv
    # basename= data.csv
    # dirname= /users/beazley/Data
    # joined= \user\yclee03\data.csv
    # splitext= ('/users/beazley/Data/data', '.csv')

    path = '~/Data/data.csv'
    print("expanded=", os.path.expanduser(path))
    # expanded= C:\Users\lee2103/Data/data.csv


