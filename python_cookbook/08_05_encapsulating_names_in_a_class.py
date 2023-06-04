#!/usr/bin/env python
# -*- coding:utf-8 -*-
# vim: ft=python ts=4 sw=4 tw=78 expandtab
# ----------------------------------------------------------------------------
# - file : 08_05_encapsulating_names_in_a_class.py
# - author : yc0325lee
# - created : 2022-11-22 13:37:08 by yc032
# - modified : 2022-11-22 13:37:08 by yc032
# - description : 
# ----------------------------------------------------------------------------

if False:
    # - single underscore naming convention should be used
    class A:
        def __init__(self):
            self._internal = 0 # An internal attribute
            self.public = 1 # A public attribute
        
        def public_method(self):
            '''
            A public method
            '''
            pass
     
        def _internal_method(self):
            pass


if True:
    # - double-underscored member -> special in python
    class B:
        def __init__(self):
            self.__private = 0 # parent's one

        def __private_method(self):
            print('[dbg ] B.__private_method invoked ...')
     
        def public_method(self):
            print('[dbg ] B.public_method invoked ...')
            self.__private_method()


    class C(B):
        def __init__(self):
            super().__init__()
            self.__private = 1 # does not override B.__private

        # does not override B.__private_method()
        def __private_method(self):
            print('[dbg ] C.__private_method invoked ...')


    c = C()
    print('c.__dict__ =', c.__dict__)
    c.public_method()
    if False:
        c.__private_method() # cannot invoke __method() directly!
    c._C__private_method() # cannot invoke __method() directly!
