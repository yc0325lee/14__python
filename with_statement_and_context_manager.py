#!/usr/bin/env python
# vim: ft=python ts=4 sw=4 tw=78 expandtab
# -*- coding:utf-8 -*-
# ----------------------------------------------------------------------------
# - file : with_statement.py
# - author : yc0325lee
# - created : 2022-11-14 23:25:57 by yc032
# - modified : 2022-11-14 23:25:57 by yc032
# - references
# ; https://realpython.com/python-with-statement/
# - description : 
# ; simplifies the management of common resources like file streams
# ----------------------------------------------------------------------------

# - usage
# with <expression> as <variable>:
#     <block>
#
# ; __enter__() and __exit__() is invoked implicitly
#
# - benefits
# ; makes resource management safer than its equivalent try ... finally
#   statements
# ; encapsulates standard uses of try ... finally statements in context managers
# ; allows reusing the code that automatically manages the setup and teardown
#   phases of a given operation
# ; helps avoid resource leaks


if False:
    # (1) file open/close handling directly
    filename = 'input.txt'
    infile = open(filename, 'r')
    contents = infile.read()
    infile.close() # no close() possible upon error
                   # in the middle of read()!

    # (2) try-finally
    # ; ensures file-closing upon exception
    #   but code is not simple & cumbersome
    filename = 'input.txt'
    infile = open(filename, 'r')
    try:
        contents = infile.read()
    finally:
        infile.close()

    # (3) with statement
    # ; no need to call infile.close()! -> simpler
    # ; with statement itself ensures proper acquisition and release of resources
    filename = 'input.txt'
    with open(filename, 'r') as infile:
        contents = infile.read()
        # __exit__() can be invoked thru 'infile' object
        # __exit__() will invoke file.close() implicitly


# - 'with' structure and magic method
# ; 'with'를 class와 함께 사용하기 위해서는 class의 member로 magic method들을 정의해야 함
# ; magic methods in class -> __enter__(), __exit__()


if False:
    # - "with" statement for user defined objects
    # ; 'with'를 class와 함께 사용하기 위해서는 class의 member로 magic
    #   method들을 정의해야 함
    # ; magic methods in class -> __enter__(), __exit__()

    # decorator for debugging
    def trace(func):
        def wrapper(*args):
            print("[dgb ] {}() invoked ...".format(func.__name__))
            decorated = func(*args)
            return decorated
        return wrapper
     
    class MessageWriter(object):
        def __init__(self, filename):
            self.filename = filename
          
        @trace
        def __enter__(self):
            self.outfile = open(self.filename, 'w')
            return self.outfile
      
        @trace
        def __exit__(self, exc_type, exc_value, traceback):
            self.outfile.close()
            if True:
                print('[dbg ] exc_type =', exc_type)
                print('[dbg ] exc_value =', exc_value)
                print('[dbg ] traceback =', traceback)
  
    # using with statement with MessageWriter
    filename = 'outfile.txt'
    with MessageWriter(filename) as outfile:
        outfile.write('hello world!')
        # __enter__ and __exit__ invoked implicitly

    # [dgb ] __enter__() invoked ...
    # [dgb ] __exit__() invoked ...
    # [dbg ] exc_type = None
    # [dbg ] exc_value = None
    # [dbg ] traceback = None

if False:
    import os
    with os.scandir('.') as entries:
        for entry in entries:
            print(entry.name, "->", entry.stat().st_size, "bytes")
