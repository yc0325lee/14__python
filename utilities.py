# vim: ft=python ts=4 sw=4 tw=999 expandtab
# -*- coding:utf-8 -*-
# ----------------------------------------------------------------------------
# - file : utilities.py
# - author : yc0325lee
# - created : 2022-10-27 23:24:40 by lee2103
# - modified : 2022-10-27 23:24:40 by lee2103
# - description : 
# ----------------------------------------------------------------------------
import inspect
import re

def printv(*args):
    frame = inspect.currentframe().f_back
    captured = inspect.getframeinfo(frame).code_context[0] # let's see what's captured!
    if False: print('[dbg ] captured=', captured.rstrip())
    argstr = re.search(r"\((.*)\)", captured).group(1)
    argstr = re.sub(r'\s+', '', argstr)
    if False: print('[dbg ] argstr=', argstr)
    names = argstr.split(',')
    for i, (var, val) in enumerate(zip(names, args)):
        print(f"{var} = {val}")

def print_mro(cls): 
    print(', '.join(c.__name__ for c in cls.__mro__))
    

if __name__ == '__main__':
    val0 = 3.0
    val1 = list(range(10))
    val2 = tuple(range(10))
    val3 = dict(x = 1, y = 2, z = 3)
    printv(val0)
    printv(val1)
    printv(val2)
    printv(val3)
    printv(   val0,   val1, val2,   val3    ) # all in one
    # -------------------------------------
    # val0 = 3.0
    # val1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    # val2 = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
    # val3 = {'x': 1, 'y': 2, 'z': 3}
    #
    # val0 = 3.0
    # val1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    # val2 = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
    # val3 = {'x': 1, 'y': 2, 'z': 3}
    # -------------------------------------
