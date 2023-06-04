#!/usr/bin/env python
# -*- coding:utf-8 -*-
# vim: ft=python ts=4 sw=4 tw=78 expandtab
# ----------------------------------------------------------------------------
# - file : misc__function.py
# - author : yc0325lee
# - created : 2022-11-26 23:41:42 by yc032
# - modified : 2022-11-26 23:41:42 by yc032
# - description : 
# ----------------------------------------------------------------------------
#
# - if no 'return value' statement, 'None' returned
#
# - multiple value return -> function 외부로 tuple이 전달됨
#
# - 'global' keyword to access global variable inside a function
#
# - 매개변수(parameter) vs 인수(arguments)
#
# - parameters
# ; a named entity in a function (or method) definition that specifies an
#   argument (or in some cases, arguments) that the function can accept.
#
# ; positional-or-keyword -> both are allowed
#   def func(foo, bar=None): ...
#            ---  ---
#
# ; positional-only
#   def func(posonly1, posonly2, /, positional_or_keyword): ...
#            --------  --------
#
# ; keyword-only
#   def func(arg, *, kw_only1, kw_only2): ...
#                    --------  --------
#
# ; var-positional
#   variable-length positional arguments
#   an arbitrary sequence of positional arguments can be provided -> *args
#   args becomes a tuple inside function
#   *args can only appear as "the last positional argument" in the function definition
#   def func(*args):
#       ...
#
# ; var-keyword
#   variable-length keyword argument
#   arbitrarily many keyword arguments can be provided -> **kwargs
#   kwargs becomes a dict inside function
#   **kwargs argument can only appear as "the last argument"!
#   def func(**kwargs):
#       ...
#
# - arguments
# ; a value passed to a function (or method) when calling the function.
#
# - keyword arguments
# ; complex(real=3, imag=5)
# ; complex(**{'real': 3, 'imag': 5})
# ; if the syntax **expression appears in the function call, expression must
#   evaluate to a mapping, the contents of which are treated as additional
#   keyword arguments.
#
# - positional arguments
# ; complex(3, 5)
# ; complex(*(3, 5))
# ; if the syntax *expression appears in the function call, expression must
#   evaluate to an iterable. elements from these iterables are treated as if
#   they were additional positional arguments. (unpacking)
#
# ----------------------------------------------------------------------------
import sys

if False:
    # pass placeholder - nothing happens
    # ; just a placeholder when a statement is required syntactically
    def hello():
        pass

if False:
    # function definition with parameters and docstring
    def some_func(name, age, sex):
        "some_func() : prints information of a persion" # docstring
        print(f"name= {name:s}, age= {age:d}, sex= {sex:s}")
        print("name= {:s}, age= {:d}, sex= {:s}".format(name, age, sex))

    some_func("james", 29, "male") # invoking functions with positional arguments
    some_func(sex="male", name="james", age=29) # invoking functions with keyword arguments

if False:
    # with default arguments
    def some_func(name="anonymous", age=20, sex="female"):
        "some_func() : prints information of a persion" # docstring
        print("name= %s, age= %d, sex= %s" % (name, age, sex))

    some_func()
    some_func("sara")
    some_func("sara", 24)
    some_func("james", 29, "male")

if False:
    # ------------------------------------------------------------------------
    # - variable-length arguments with *args
    # ; args becomes a tuple inside function
    # ------------------------------------------------------------------------
    from collections.abc import Sequence
    def some_func(*args):
        thisfunc = sys._getframe().f_code.co_name
        print("[info] {} invoked ...".format(thisfunc))
        print("       type(args)=", type(args)) # tuple
        for i, arg in enumerate(args):
            print("arg[{}]= {}".format(i, arg))
        print()

    for attr in dir(some_func):
        print(attr)

    some_func("sara", 22, "female", [0, 1, 2, 3])
    some_func()
    some_func("arg0")
    some_func("arg0", "arg1")
    some_func("arg0", "arg1", "arg2")
    some_func("arg0", "arg1", "arg2", "arg3")
    some_func("arg0", "arg1", "arg2", "arg3", "arg4")
    
if False:
    # ------------------------------------------------------------------------
    # - variable-length keyword arguments with *args
    # ; args becomes a tuple inside function
    # ------------------------------------------------------------------------
    def some_func(name, age, sex, *hobbies):
        "some_func() : prints information of a persion" # docstring
        thisfunc = sys._getframe().f_code.co_name
        print("[info] {} invoked ...".format(thisfunc))
        print("name= %s, age= %d, sex= %s" % (name, age, sex))
        print("hobbies=", hobbies) # tuple
        for i, hobby in enumerate(hobbies):
            print("    hobby[{0}]= {1}".format(i, hobby))
        print()

    print("some_func.__doc__=", some_func.__doc__) # docstring
    some_func("james", 32, "male", "fishing", "cycling")
    some_func("cathorin", 17, "male", "reading", "fishing", "coding")
    some_func("sara", 22, "female", "coding", "fishing", "reading", "cycling")
    # name= sara, age= 22, sex= female
    # hobbies= ('coding', 'fishing', 'reading', 'cycling')
    #     hobby[0]= coding
    #     hobby[1]= fishing
    #     hobby[2]= reading
    #     hobby[3]= cycling
    
if False:
    # ------------------------------------------------------------------------
    # - variable-length keyword arguments with **kwargs
    # ; kwargs becomes a dict inside function
    # ------------------------------------------------------------------------
    def some_func(**kwargs):
        #thisfunc = sys._getframe().f_code.co_name
        print("\n[info] {}() invoked ...".format(some_func.__name__))
        print('[dbg ] sys._getframe().f_code.co_name =', sys._getframe().f_code.co_name)
        print('[dbg ] some_func.__name__ =', some_func.__name__)
        print('[dbg ] some_func.__qualname__ =', some_func.__qualname__)
        print("[dbg ] type(kwargs)=", type(kwargs)) # dict
        for key, value in kwargs.items():
            print("{0} = {1}".format(key, value))

    some_func(name="sara", age=22, sex="female")
    some_func(name="sara", age=22, sex="female", hobby="reading")
    some_func(name="sara", age=22, sex="female", hobby="reading", occupation="student")

    #some_func("james", 32, "male")
    # TypeError: some_func() takes 0 positional arguments, but 3 were given

if False:
    # ---------------------------------------------------------------
    # def some_func(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):
    #               --+-------     -+--------     -----+----
    #                 |             |                  |
    #                 |        positional or keyword   |
    #                 |                                - keyword only
    #                 +-- positional only
    #
    # some_func(1, 2, 3, kwd1=4, kwd2=5)
    # some_func(1, 2, pos_or_kwd=3, kwd1=4, kwd2=5)
    # -> only these 2 styles are allowed!
    # ---------------------------------------------------------------
    def some_func(name, /, age=17, sex="male", **kwargs):
        thisfunc = sys._getframe().f_code.co_name
        print("\n[info] {} invoked ...".format(thisfunc))
        print("name= %s, age= %d, sex= %s" % (name, age, sex))
        for key in kwargs:
            print("{}={}".format(key, kwargs[key]))

    some_func("james", 32, "male", fld1="aaa", fld2="bbb", fld3="ccc") # ok
    some_func("james", age=32, sex="male", fld1="aaa", fld2="bbb", fld3="ccc") # ok
    some_func("james", fld1="aaa", fld2="bbb", fld3="ccc", age=32, sex="male") # ok
    some_func("james", fld1="aaa", fld2="bbb", fld3="ccc") # ok

    #some_func("james", name="xxx", fld1="aaa", fld2="bbb", fld3="ccc") # error!
    #                   ---------
    #                      ???


if False:
    def some_func(*args, **kwargs):
    #              -+--    --+---
    #               |        |
    #               |        keyworded arguments
    #               positional argument
        thisfunc = some_func.__name__
        print("\n[info] {} invoked ...".format(thisfunc))
        arg_lst = []
        if args:
            arg_lst.append(', '.join(repr(arg) for arg in args))
        if kwargs:
            pairs = ['%s=%r' % (key, val) for key, val in sorted(kwargs.items())]
            arg_lst.append(', '.join(pairs))
        arg_str = ', '.join(arg_lst)
        print("%s(%s)" % (thisfunc, arg_str))

    some_func(0, 1, 2, 3)
    some_func(0, 1, 2, d=3)
    some_func(0, 1, c=2, d=3)
    some_func(0, b=1, c=2, d=3)
    some_func(a=0, b=1, c=2, d=3)

    some_func(0, 1, c=2, d=3)
    #         -+--  ---+----
    #          |       |
    #          |       kwargs = dict(c=2, d=3)
    #          args = [0, 1]

    # - the following is not allowed!
    # some_func(a=0, b=1, 2, 3)
    # SyntaxError: positional argument follows keyword argument


if False:
    # unpacking function arguments from a list or dictionary

    # - positional argument
    # ; complex(3, 5)
    # ; complex(*(3, 5))
    # ; if the syntax *expression appears in the function call, expression must
    #   evaluate to an iterable. elements from these iterables are treated as if
    #   they were additional positional arguments.
    args = [3, 6] # a list!
    #list(range(args)) # error! -> unpacking required
    list(range(*args)) # ok
    #          --+--
    #            |
    # unpacked into positional arguments

    # - keyword argument
    # ; complex(real=3, imag=5)
    # ; complex(**{'real': 3, 'imag': 5})
    # ; if the syntax **expression appears in the function call, expression must
    #   evaluate to a mapping, the contents of which are treated as additional
    #   keyword arguments.
    def some_func(name, age, sex):
        print("name= %s, age= %d, sex= %s" % (name, age, sex))

    kwargs = dict(name="james", age=23, sex="male")
    #some_func(kwargs) # error! -> unpacking required
    some_func(**kwargs) # ok
    #         ----+---
    #             |
    # unpacked into keyword arguments


if False:
    # - function introspection
    # ; listing attributes of functions that don't exist in plain instances
    # - dir()
    class Temp:
        pass
    obj = Temp()

    def func():
        pass

    print("# function-only attributes")
    for attr in sorted(set(dir(func)) - set(dir(obj))):
        print("attr=", attr)
    # function-only attributes
    # attr= __annotations__
    # attr= __call__
    # attr= __closure__
    # attr= __code__
    # attr= __defaults__
    # attr= __get__
    # attr= __globals__
    # attr= __kwdefaults__
    # attr= __name__
    # attr= __qualname__

    # +-----------------+---------------------------------------------------------------------------------------+
    # | attr            | description                                                                           |
    # +-----------------+---------------------------------------------------------------------------------------+
    # | __annotations__ | dict parameter and return annotations                                                 |
    # | __call__        | method-wrapper implementation of the () operator; a.k.a. the callable object protocol |
    # | __closure__     | tuple the function closure. i.e. bindings for free variables (often is none)          |
    # | __code__        | code function metadata and function body compiled into bytecode                       |
    # | __defaults__    | tuple default values for the formal parameters                                        |
    # | __get__         | method-wrapper implementation of the read-only descriptor protocol                    |
    # | __globals__     | dict global variables of the module where the function is defined                     |
    # | __kwdefaults__  | dict default values for the keyword-only formal parameters                            |
    # | __name__        | str the function name                                                                 |
    # | __qualname__    | str the qualified function name                                                       |
    # +-----------------+---------------------------------------------------------------------------------------+


if False:
    # - function is a first-class object(citizen)
    # ; created at runtime
    # ; assigned to a variable or element in a data structure
    # ; passed as an argument to a function
    # ; returned as the result of a function
    # ; integers, strings, lists and dictionaries are first-class objects.
    print("issubclass(int,object)=", issubclass(int, object))
    # issubclass(int,object)= True
    
    def some_func():
        pass
    
    print("some_func.__class__=", some_func.__class__)
    print("issubclass(some_func,object)=", issubclass(some_func.__class__, object))
    # some_func.__class__= <class 'function'>
    # issubclass(some_func,object)= True


if False:
    # closure
    def outer():
        x = 1
        def inner():
            print(x)
        return inner

    foo = outer()
    print(foo)
    #print(foo.func_closure)
    print(foo.__closure__)


if False:
    # extracting information about the function arguments (1)
    # ; from function attributes
    def some_func(name, /, age=17, sex="male", **kwargs):
        thisfunc = sys._getframe().f_code.co_name
        print("\n[info] {} invoked ...".format(thisfunc))
        print("name= %s, age= %d, sex= %s" % (name, age, sex))
        for key in kwargs:
            print("{}={}".format(key, kwargs[key]))

    print("some_func.__defaults__=", some_func.__defaults__)
    print("some_func.__code__.co_varnames=", some_func.__code__.co_varnames)
    print("some_func.__code__.co_argcount=", some_func.__code__.co_argcount, end='\n\n')
    # some_func.__defaults__= (17, 'male')
    # some_func.__code__.co_varnames= ('name', 'age', 'sex', 'kwargs', 'thisfunc', 'key')
    # some_func.__code__.co_argcount= 3
    # -> does not include any variable arguments prefixed with * or **

    # extracting information about the function arguments (2)
    # ; using 'inspect' module's signature function
    import inspect
    sig = inspect.signature(some_func)
    print("sig=", sig)
    print("str(sig)=", str(sig))
    for name, param in sig.parameters.items():
        print(param.kind, ':', name, '=', param.default)
    # -------------------------------------------------
    # sig= (name, /, age=17, sex='male', **kwargs)
    # str(sig)= (name, /, age=17, sex='male', **kwargs)
    #
    # POSITIONAL_ONLY : name = <class 'inspect._empty'>
    # POSITIONAL_OR_KEYWORD : age = 17
    # POSITIONAL_OR_KEYWORD : sex = male
    # VAR_KEYWORD : kwargs = <class 'inspect._empty'>
    # -------------------------------------------------


if True:
    import inspect
    # function annotations
    # ; just saved in function.__annotations__
    # ; nothing else is done, like no checks, enforcement, validation
    def add(a:'int > 0', b:'int > 0') -> int:
        return a + b

    print("add(3, 4) =", add(3, 4))
    print("add.__annotations__=", add.__annotations__)
    print("add(-3, 4) =", add(-3, 4)) # nothing is checked!
    # add(3, 4) = 7
    # add.__annotations__= {'a': 'int > 0', 'b': 'int > 0', 'return': <class 'int'>}
    # add(-3, 4) = 1

    print()

    sig = inspect.signature(add)
    print("sig=", sig)
    print("str(sig)=", str(sig))
    for name, param in sig.parameters.items():
        print(param.kind, ':', name, '=', param.default)
