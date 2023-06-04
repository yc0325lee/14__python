# vim: ft=python ts=4 sw=4 tw=999 expandtab
# ----------------------------------------------------------------------------
# File : lib__shutil.py
# Author : yc0325lee
# Created : 2022-03-05 19:19:58 by lee2103
# Modified : 2022-03-05 19:19:58 by lee2103
# Description : 
# Reference
# - https://docs.python.org/3/library/shutil.html#module-shutil
# ----------------------------------------------------------------------------
import os
import shutil

if True:
    # shutil.disk_usage(path)
    # ; return disk usage statistics about the given path
    cwd = os.getcwd()
    print("# diskusage for {}".format(cwd))
    print(shutil.disk_usage(cwd))



# shutil.copyfile(src, dst, *, follow_symlinks=True)
# shutil.copy(src, dst, *, follow_symlinks=True)
# shutil.copytree(src, dst, symlinks=False, ignore=None, copy_function=copy2, ignore_dangling_symlinks=False, dirs_exist_ok=False)
# shutil.rmtree(path, ignore_errors=False, onerror=None)
# shutil.move(src, dst, copy_function=copy2)
# shutil.disk_usage(path)
# shutil.chown(path, user=None, group=None)
# shutil.which(cmd, mode=os.F_OK | os.X_OK, path=None)
