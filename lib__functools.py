#!/usr/bin/env python
# -*- coding:utf-8 -*-
# vim: ft=python ts=4 sw=4 tw=78 expandtab
# ----------------------------------------------------------------------------
# File : lib__functools.py
# Author : yc0325lee
# Created : 2022-03-26 20:19:48 by lee2103
# Modified : 2022-03-26 20:19:48 by lee2103
# Description : 
# - the functools module is for higher-order functions: functions that act on or
#   return other functions. in general, any callable object can be treated as a
#   function for the purposes of this module.
# ----------------------------------------------------------------------------
from utilities import printv
import time
import functools

def debug(active=True):
    '''debug() returns a decorator'''
    def debug_inner(func):
        @functools.wraps(func) # func's attributes preserved
        def wrapper(*args, **kwargs):
            arglist = []
            if args:
                arglist.append(', '.join(repr(arg) for arg in args))
            if kwargs:
                pairs = ['%s=%r' % (k, w) for k, w in sorted(kwargs.items())]
                arglist.append(', '.join(pairs))
            arg_str = ', '.join(arglist)
            if active:
                print("[dgb ] {}({}) invoked ...".format(func.__name__, arg_str))
            # ---------------------------------------------
            #start_ = time.perf_counter()
            result = func(*args, **kwargs)
            #end_ = time.perf_counter()
            #elapsed_ = end_ - start_
            #print("[dgb ] {}({}) ends ... elapsed= {:.8f}s"
            #        .format(func.__name__, arg_str, elapsed_))
            # ---------------------------------------------
            return result
        return wrapper # decorated-func
    return debug_inner


if True:
    # - @functools.lru_cache(user_function) ---> maxsize=128(default)
    # - @functools.lru_cache(maxsize=128, typed=False)
    # ; decorator to wrap a function with a memoizing callable that saves up
    #   to the maxsize most recent calls.
    # ; since a dictionary is used to cache results, the positional and
    #   keyword arguments to the function must be hashable.
    # ; if maxsize is set to none, the lru feature is disabled and the cache
    #   can grow without bound.
    # ; if typed is set to true, function arguments of different types will be
    #   cached separately.

    @debug(False)
    def fibonacci_0(n):
        if n < 2:
            return n
        return fibonacci_0(n-2) + fibonacci_0(n-1)

    @functools.lru_cache() # decorator, maxsize=128
    @debug(False)
    def fibonacci_1(n):
        if n < 2:
            return n
        return fibonacci_1(n-2) + fibonacci_1(n-1)

    n = 15

    start = time.perf_counter()
    result = fibonacci_0(n)
    end = time.perf_counter()
    print("fibonacci_0({})=".format(n), result, "elapsed= {:.12f}s".format(end-start))
    # fibonacci_0(32)= 2178309 elapsed= 0.480078400000s

    start = time.perf_counter()
    result = fibonacci_1(n)
    end = time.perf_counter()
    print("fibonacci_1({})=".format(n), result, "elapsed= {:.12f}s".format(end-start))
    # fibonacci_1(32)= 2178309 elapsed= 0.000021500000s


if False:
    # - @functions.singledispatch generic functions
    # ; transform a function into a single-dispatch generic function.
    #   (similar to function overloading in c++)
    # ; to define a generic function, decorate it with the @singledispatch
    #   decorator.
    # ; when defining a function using @singledispatch, note that the dispatch
    #   happens on the type of the first argument
    import sys
    import functools

    @functools.singledispatch
    @debug
    def some_func(arg, verbose=False):
        print('arg=', arg, '(unregistered type)\n') # unregistered type will hit here!

    @some_func.register(int)
    @debug
    def _(arg, verbose=False):
        print('arg=', arg, '(int type)\n') # int type will hit here!
    
    @some_func.register(list)
    @debug
    def _(arg, verbose=False):
        print('arg=', '(int type)') # list type will hit here!
        for i, elem in enumerate(arg):
            print("arg[{}]= {}".format(i, elem))
        print()

    
    some_func(7, verbose=True)
    some_func([3, 4, 5], verbose=True)
    some_func("some_string", verbose=True) # not registered


if False:
    # - single-dispatch generic functions - (1) using register() function
    # ; transform a function into a single-dispatch generic function.
    # ; this looks like function overloading or template
    import sys
    from functools import singledispatch

    @singledispatch
    def some_func(arg, verbose=False):
        if verbose:
            print("[info] {}<default>() invoked ...".format(some_func.__name__))
        print("       arg=", arg) # unregistered type will hit here!

    @some_func.register(int)
    def _(arg, verbose=False):
        if verbose:
            print("[info] {}<int>() invoked ...".format(some_func.__name__))
        print("       arg=", arg) # int type will hit here!
    
    @some_func.register(list)
    def _(arg, verbose=False):
        if verbose:
            print("[info] {}<list>() invoked ...".format(some_func.__name__))
        for i, item in enumerate(arg): # list type will hit here!
            print("       arg[{}]= {}".format(i, item))

    @some_func.register(complex)
    def _(arg, verbose=False):
        if verbose:
            print("[info] {}<complex>() invoked ...".format(some_func.__name__))
        print("       arg= {}".format(arg)) # complex type will hit here!
    
    
    some_func(7, verbose=True)
    some_func([3, 4, 5], verbose=True)
    some_func("some_string", verbose=True) # not registered
    some_func(complex(3.0, 4.0), verbose=True) # not registered


if False:
    # - single-dispatch generic functions - (2) using type annotation
    # ; transform a function into a single-dispatch generic function.
    # ; this looks like function overloading or template
    import sys
    from functools import singledispatch

    @singledispatch
    def some_func(arg, verbose=False):
        if verbose:
            print("[info] {}<default>() invoked ...".format(some_func.__name__))
        print("       arg=", arg) # unregistered type will hit here!

    @some_func.register
    def _(arg: int, verbose=False):
        if verbose:
            print("[info] {}<int>() invoked ...".format(some_func.__name__))
        print("       arg=", arg) # int type will hit here!
    
    @some_func.register
    def _(arg: list, verbose=False):
        if verbose:
            print("[info] {}<list>() invoked ...".format(some_func.__name__))
        for i, item in enumerate(arg): # list type will hit here!
            print("       arg[{}]= {}".format(i, item))

    @some_func.register
    def _(arg: complex, verbose=False):
        if verbose:
            print("[info] {}<complex>() invoked ...".format(some_func.__name__))
        print("       arg= {}".format(arg)) # complex type will hit here!
    
    
    some_func(7, verbose=True)
    some_func([3, 4, 5], verbose=True)
    some_func("some_string", verbose=True) # not registered
    some_func(complex(3.0, 4.0), verbose=True) # not registered


if False:
    # - @functools.wraps(wrapped, assigned=WRAPPER_ASSIGNMENTS, updated=WRAPPER_UPDATES)
    # ; name and docstring attributes of original function are maintained
    #   when decorating a function
    pass

if False:
    # - functools.reduce(function, iterable[, initializer])
    # ; apply function of two arguments cumulatively to the items of iterable,
    #   from left to right, so as to reduce the iterable to a single value.
    # ; examples of reducing functions -> sum, any, all, functools.reduce, ...
    import functools
    values = list(range(1, 10))

    result1 = functools.reduce(lambda x, y: x + y, values, 0)
    #                                                      | init = 0

    result2 = functools.reduce(lambda x, y: x * y, values, 1)
    #                                                      | init = 1

    printv(values, result1, result2)
    # values = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    # result1 = 45
    # result2 = 362880


if False:
    # ------------------------------------------------------------------------
    # - functools.partial(func, /, *args, **keywords)
    # ; return a new partial object which when called will behave like func
    #   called with the positional arguments args and keyword arguments
    #   keywords.
    # ; the partial() is used for partial function application which "freezes"
    #   some portion of a function’s arguments and/or keywords resulting in a
    #   new object with a simplified signature.
    # ------------------------------------------------------------------------
    pass
