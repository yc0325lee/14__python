#!/usr/bin/env python
# -*- coding:utf-8 -*-
# vim: ft=python ts=4 sw=4 tw=78 expandtab
# ----------------------------------------------------------------------------
# - file : lib__typing.py
# - author : yc0325lee
# - created : 2023-06-11 23:31:51 by yc032
# - modified : 2023-06-11 23:31:51 by yc032
# - description : 
# ; provides runtime support for type hints
# ; suport of types Any, Union, Callable, TypeVar, and Generic
# ----------------------------------------------------------------------------
import typing

if False:
    # -------------------------------------
    # - type annotation
    def greeting_0(name: str) -> str:
        return 'hello, ' + name
    def greeting_1(name: str) -> str:
        return f'hello, {name}'

    print('message=', greeting_0('james'))
    print('message=', greeting_1('james'))
    print('message=', greeting_1(4)) # no type checking, but just a hint!
    pass
