#!/usr/bin/env python
# -*- coding:utf-8 -*-
# vim: ft=python ts=4 sw=4 tw=78 expandtab
# ----------------------------------------------------------------------------
# - file : function_registry.py
# - author : yc0325lee
# - created : 2022-10-17 23:57:18 by lee2103
# - modified : 2022-10-30 19:33:55 by lee2103
# - description : 
# ; registered at 'import time', not run-time
# ----------------------------------------------------------------------------
registry = [] 

def register(func): 
    print('[info] running register(%s)' % func) 
    registry.append(func) 
    return func 

@register 
def f1():
    print('[info] running f1()')

@register
def f2():
    print('[info] running f2()')

def f3(): 
    print('[info] running f3()')

def main(): 
    print('[info] running main()')
    print('       registry ->', registry)
    f1()
    f2()
    f3()


if __name__=='__main__':
    main() 

# [info] running register(<function f1 at 0x00000198CC9A8FE0>)
# [info] running register(<function f2 at 0x00000198CC9A8F40>)
# [info] running main()
#        registry -> [
#                <function f1 at 0x00000198CC9A8FE0>,
#                <function f2 at 0x00000198CC9A8F40>
#            ]
# [info] running f1()
# [info] running f2()
# [info] running f3()
