#!/usr/bin/env python
# -*- coding:utf-8 -*-
# vim: ft=python ts=4 sw=4 tw=78 expandtab
# ----------------------------------------------------------------------------
# - file : builtin_variables.py
# - author : yc0325lee
# - created : 2022-11-25 22:35:47 by yc032
# - modified : 2022-11-25 22:35:57 by yc032
# - description : 
# - references
# ; https://docs.python.org/3/reference/datamodel.html
# ----------------------------------------------------------------------------

if True:
    for i, name in enumerate(dir()):
        print("name[{}]= {}".format(i, name))
    # name[0]= __annotations__
    # name[1]= __builtins__
    # name[2]= __cached__
    # name[3]= __doc__
    # name[4]= __file__
    # name[5]= __loader__
    # name[6]= __name__
    # name[7]= __package__
    # name[8]= __spec__

# - __name__
# ; a built-in variable which evaluates to the name of the current module

# - user-defined functions
# ; __doc__
# ; __name__
# ; __qualname__
#   the function’s qualified name.
# ; __module__
#   the name of the module the function was defined in, or none if unavailable.
# ; __defaults__
# ; __code__
# ; __globals__
# ; __dict__
# ; __closure__
# ; __annotations__
# ; __kwdefaults__
