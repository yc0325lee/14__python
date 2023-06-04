#!/usr/bin/env python
# -*- coding:utf-8 -*-
# vim: ft=python ts=4 sw=4 tw=78 expandtab
# ----------------------------------------------------------------------------
# - file : builtin_functions.py
# - author : yc0325lee
# - created : 2022-11-16 22:30:32 by yc032
# - modified : 2022-11-16 22:30:32 by yc032
# - reference
# ; https://docs.python.org/3/library/functions.html
# - description : 
# ----------------------------------------------------------------------------

# +---------------+-------------+--------------+--------------+----------------+
# |                            built-in functions                              |
# +---------------+-------------+--------------+--------------+----------------+
# | abs()         | delattr()   | hash()       | memoryview() | set()          |
# | all()         | dict()      | help()       | min()        | setattr()      |
# | any()         | dir()       | hex()        | next()       | slice()        |
# | ascii()       | divmod()    | id()         | object()     | sorted()       |
# | bin()         | enumerate() | input()      | oct()        | staticmethod() |
# | bool()        | eval()      | int()        | open()       | str()          |
# | breakpoint()  | exec()      | isinstance() | ord()        | sum()          |
# | bytearray()   | filter()    | issubclass() | pow()        | super()        |
# | bytes()       | float()     | iter()       | print()      | tuple()        |
# | callable()    | format()    | len()        | property()   | type()         |
# | chr()         | frozenset() | list()       | range()      | vars()         |
# | classmethod() | getattr()   | locals()     | repr()       | zip()          |
# | compile()     | globals()   | map()        | reversed()   | __import__()   |
# | complex()     | hasattr()   | max()        | round()      |                |
# +---------------+-------------+--------------+--------------+----------------+
from utilities import printv

if False:
    # --------------------------------------------------------------------
    # print()
    # - Syntax: print(value(s), sep=' ', end='\n', file=file, flush=flush)
    # - Parameters: 
    # value(s) : any value, and as many as you like.
    #            will be converted to string before printed 
    #            if __str__ not exists, __repr__ is used
    # sep='separator' : (Optional) Specify how to separate the objects,
    #                   if there is more than one.Default :' ' 
    # end='end': (Optional) Specify what to print at the end.Default : '\n' 
    # file : (Optional) An object with a write method. Default :sys.stdout
    # flush : (Optional) A Boolean, specifying if the output is flushed (True)
    #         or buffered (False). Default: False
    # Returns: It returns output to the screen.
    # --------------------------------------------------------------------
    print( "aaa" "bbb" ) # aaabbb
    print( "aaa" + "bbb" ) # aaabbb
    print( "aaa", "bbb" ) # aaa bbb
    print( "aaa", "bbb", sep="--->" ) # aaa--->bbb
    
    print("aaa", end=" ") # no '\n' character at the end of line
    print()

    a = list(range(10))
    print("a=", end=' ')
    print(*a, sep=', ')
    
    import sys
    print("aaa", file=sys.stdout) # to stdout
    print("aaa", file=sys.stderr) # to stderr

if False:
    # range() - an immutable sequence of numbers
    # - class range(stop)
    # - class range(start, stop[, step])
    # ; rather than being a function, range is actually an immutable sequence type
    a = range(10) # <class 'range'>, immutable sequence
    for i in range(10):
        print("i= {}".format(i))
    
    values = list(range(0, 20, 2))
    print("11 in values: ", 11 in values)
    print("12 in values: ", 12 in values)

    # list of float values
    import numpy
    values = numpy.arange(0.0, 1.05, 0.05)
    for i, val in enumerate(numpy.arange(0.0, 1.05, 0.05)):
        #print('val[{}] = {:.2f}'.format(i, val))
        print('{:.2f}'.format(val))
    # ------------------------------------------------------
    # 0.00 0.05 0.10 0.15 0.20 0.25 0.30 0.35 0.40 0.45
    # 0.50 0.55 0.60 0.65 0.70 0.75 0.80 0.85 0.90 0.95 1.00
    # ------------------------------------------------------


if False:
    # enumerate(iterable, start=0)
    a = ["aaa", "bbb", "ccc", "ddd"]
    for i, val in enumerate(a): # (0,'aaa'), (1,'bbb'), (2,'ccc'), (3,'ddd')
        print("i= {}, val= {}".format(i, val))
    print()
    for i, val in enumerate(a, start=1): # (1,'aaa'), (2,'bbb'), (3,'ccc'), (4,'ddd')
        print("i= {}, val= {}".format(i, val))
    print()

if False:
    # len()
    # ; Return the length (the number of items) of an object.
    # ; The argument may be a sequence (such as a string, bytes, tuple, list, or range)
    #   or a collection (such as a dictionary, set, or frozen set).
    a = ["aaa", "bbb", "ccc", "ddd"]
    b = range(10)
    c = "this is a string"
    print("len(a)= %d" % len(a)) # 4
    print("len(b)= %d" % len(b)) # 10
    print("len(c)= %d" % len(c)) # 16

if False:
    # id(object)
    # ; Return the "identity of an object. This is an integer
    #   which is guaranteed to be unique and constant for this object during its lifetime.
    # ; the memory address where object is stored
    a = ["aaa", "bbb", "ccc", "ddd"]
    print("a=", a)
    print("type(a)=", type(a))
    print("type(a).__name__=", type(a).__name__)
    print("repr(a)=", repr(a))
    print("str(a)=", str(a))
    print(id(a))

if False:
    # input([prompt])
    # ; 
    val = input("Input a string --> ")
    print("type(val)=", type(val))
    print("val=", val)

if False:
    # ----------------------------------------------------------------------------
    # - map(function, iterable, ...)
    # ; return an iterator that applies function to every item of iterable,
    #   yielding the results.
    # ; 'map' applies a function to every element of a sequence
    #    and returns an iterator
    # ; if additional iterable arguments are passed, function must take that
    #   many arguments and is applied to the items from all iterables in parallel.
    # ----------------------------------------------------------------------------
    simpsons = ['homer', 'marge', 'bart']
    mapped = map(len, simpsons) # returns [5, 5, 4]
    print("mapped=", mapped)
    print(type(mapped))
    for i, item in enumerate(mapped):
        print("item[{}]= {}".format(i, item))

    # equivalent list comprehension
    mapped = [len(word) for word in simpsons]
    print("mapped=", mapped)
    print(type(mapped))

    def square(x, y):
        return x**2 + y**2

    x = list(range(0, 10, 2)) # [0, 2, 4, 6, 8]
    y = list(range(1, 10, 2)) # [1, 3, 5, 7, 9]
    for i, squared in enumerate(map(square, x, y)):
        #                                   |  |
        #                                   |  iterable2
        #                                   iterable1
        print(f"i= {i:1d}, squared= {squared:3d}")

if False:
    # --------------------------------------------------------------------------
    # - filter(function, iterable)
    # ; construct an iterator from those elements of iterable for which function
    #   returns true.
    # ; returns an iterable object(generator)
    # --------------------------------------------------------------------------
    nums = range(10)
    filtered = filter(lambda x: x % 2 == 0, nums)
    print("filtered=", filtered)
    print('type(filtered)', type(filtered))
    # filtered= <filter object at 0x0000018B8B40EA00>
    # <class 'filter'>
    # -> iterable

    for i, item in enumerate(filtered):
        print("item[{}]= {}".format(i, item))

    print()

    # equivalent list comprehension
    # ; list returned
    filtered = [num for num in nums if num % 2 == 0]
    print("filtered=", filtered)
    print('type(filtered)', type(filtered))
    # filtered= [0, 2, 4, 6, 8]
    # type(filtered) <class 'list'>

if False:
    # -----------------------------------------------------------------------------
    # locals()
    # ; update and return a dictionary representing the current local symbol table.
    # globals()
    # ; return the dictionary implementing the current module namespace
    # -----------------------------------------------------------------------------
    print()
    table = dict(globals()) # current snapshot required
    for key in table.keys():
        print(key)

    print()
    table = dict(locals())
    for key in table.keys():
        print(key)

    print()
    varname = [key for key, val in locals().items() if val == table][0]; # list comprehension
    print("varname=", varname)


if False:
    # -------------------------------------------------------------------------
    # - ord()
    # ; return an integer representing the unicode code point of that character
    # - chr()
    # ; return the string representing a character whose unicode code point is
    #   the integer
    # -------------------------------------------------------------------------
    print(ord('A')) # 65
    print(ord('Z')) # 90
    print(ord('a')) # 97
    print(ord('z')) # 122

    chars = [chr(n) for n in range(65, 91, 1)]
    print("\nchars=", chars)

    nums = [ord(c) for c in chars]
    print("\nnums=", nums)

if False:
    # ------------------------------------------------------------------------------
    # - repr()
    #  ; return a string containing a printable representation of an object
    #  ; a class can control what this function returns for its instances by
    #    defining a __repr__() method.
    #  ; return a string representing the object as the 'developer' wants to see it.
    # - str()
    #  ; str(object) returns object.__str__(), which is the 'informal' or nicely
    #    printable string representation of object.
    #  ; if object does not have a __str__() method, then str() falls back to
    #    returning repr(object).
    #  ; return a string representing the object as the user wants to see it.
    #    [note] 대부분의 경우  __str__이 없을 경우 __repr__이 대신 호출된다.
    # ------------------------------------------------------------------------------
    from math import hypot

    class Vector:
        def __init__(self, x=0, y=0):
            self.x = x
            self.y = y

        def __repr__(self):
            return 'Vector(%r, %r)' % (self.x, self.y)
            # if no custom __str__() is available, python will call __repr__() instead

        def __str__(self):
            return "(x= {}, y= {})".format(self.x, self.y)

    vector = Vector(3, 4)
    print("vector=", vector) # if __str__() is not provided, print() will invoke
                             # __repr__() magic method.

if False:
    # ---------------------------------------------------------------------------------
    # - dir() or dir(object)
    # ; without arguments, return the list of names in the current local scope.
    # ; with an argument, attempt to return a list of valid attributes for that object.
    # ---------------------------------------------------------------------------------
    print("# attrs in dir()")
    i = 0
    for attr in dir():
        print("attr[{}]= {} -> {}".format(i, attr, type(attr)))
        i = i + 1
    print()

    print("# attrs in dir(list())")
    i = 0
    for attr in dir([1, 2, 3, 4]):
        if "__" not in attr:
            print("attr[{}]= {} -> {}".format(i, attr, type(attr)))
            i = i + 1
    print()

if False:
    # --------------------------------------------------------------------------
    # class super([type[, object-or-type]])
    # ; return a proxy object that delegates method calls to a parent or sibling
    #   class of type.
    # ; this is useful for accessing inherited methods that have been overridden
    #   in a class.
    # --------------------------------------------------------------------------
    pass

if False:
    # -------------------------------------------------------------------
    # format(value[, format_spec])
    # ; convert a value to a "formatted" representation, as controlled by
    #   format_spec.
    # ; format_spec='' -> same as str(val)
    # ; will invoke implemented __format__ method implicitly
    # -------------------------------------------------------------------
    print(format(511, '010b'))
    print(format(2/3, '0.6%'))

if False:
    # -------------------------------------------------------------------
    # hash(object)
    # ; return the hash value of the object (if it has one).
    # ; hash values are integers.
    # ; will invoke '__hash__()' magic method
    # ; returns TypeError exception upon unhashable
    # -------------------------------------------------------------------
    def hashable(a):
        try:
            hash(a)
        except TypeError:
            return False
        return True

    tf = (10, 'alpha', (1, 2)) # hashable
    tm = (10, 'alpha', [1, 2]) # unhashable
    pass


if False:
    # ----------------------------------------------------------------------------
    # reversed(seq)
    # ; only sequences are allowed for arguments, not iterable
    # ; return a reverse iterator. seq must be an object which has a
    #   __reversed__() method or supports the sequence protocol (the __len__()
    #   method and the __getitem__() method with integer arguments starting at 0).
    # - sorted() vs reversed()
    # ; sorted() -> return a new sorted list from the items in iterable
    # ; reversed() -> return a reverse iterator
    # ----------------------------------------------------------------------------
    a = list(range(10))
    print("reversed(a)=", reversed(a))
    print([x for x in reversed(a)])

if False:
    # ----------------------------------------------------------------------
    # - zip(*iterables, strict=False)
    # ; iterate over several iterables in parallel, producing tuples with an
    #   item from each one.
    # ; pairing 2 lists with zip()
    # ----------------------------------------------------------------------
    questions = ['name', 'quest', 'favorite color']
    answers = ['lancelot', 'the holy grail', 'blue']

    for question, answer in zip(questions, answers):
        print('What is your {0}?  It is {1}.'.format(question, answer))

    print()

    for question, answer in zip(questions, answers):
        print(f'What is your {question}?  It is {answer}.')

if False:
    # ---------------------------------------------------------------------
    # - memoryview
    # ; memoryview objects allow Python code to access the internal data of
    #   an object that supports the buffer protocol without copying.
    # ; 
    # - class memoryview(object)
    # ; return a "memory view" object created from the given argument
    # ; attributes
    #   itemsize, ndim, shape, format
    # ---------------------------------------------------------------------
    import array
    numbers = array.array('h', [-2, -1, 0, 1, 2]) # 'h' -> signed short(2 bytes)
    print("numbers=", numbers)
    # numbers= array('h', [-2, -1, 0, 1, 2])

    memview = memoryview(numbers)
    print("\nmemview=", memview)
    print("len(memview)=", len(memview))
    print("memview.format=", memview.format)
    print("memview.itemsize=", memview.itemsize)
    print("memview.tolist()=", memview.tolist())
    # memview= <memory at 0x000001EAA0F96680>
    # len(memview)= 5
    # memview.format= h
    # memview.itemsize= 2
    # memview.tolist()= [-2, -1, 0, 1, 2]


    byteview = memview.cast('B') # unsigned char, 0 ~ 255
    print("\nbyteview=", byteview)
    print("len(byteview)=", len(byteview))
    print("byteview.format=", byteview.format)
    print("byteview.itemsize=", byteview.itemsize)
    print("byteview.tolist()=", byteview.tolist())
    # byteview= <memory at 0x000002391ED86980>
    # len(byteview)= 10
    # byteview.format= B
    # byteview.itemsize= 1
    # byteview.tolist()= [254, 255, 255, 255, 0, 0, 1, 0, 2, 0]

    for item in byteview:
        print(f'{item:08b}')

    byteview[5] = 4 # [note] this will modify 'numbers'!
    print("numbers=", numbers)


if False:
    # --------------------------------------------------------------------
    # - isinstance(object, classinfo)
    # ; return true if the object argument is an instance of the classinfo
    #   argument, or of a (direct, indirect, or virtual) subclass thereof.
    # ; if classinfo is a tuple of type objects (or recursively, other such
    #   tuples) or a union type of multiple types, return true if object is
    #   an instance of any of the types.
    #
    # - issubclass(class, classinfo)
    # ; return true if class is a subclass (direct, indirect, or virtual)
    #   of classinfo.
    # --------------------------------------------------------------------
    class Base:
        pass
    class Derived_0(Base):
        pass
    class Derived_1:
        pass

    obj0 = Derived_0()
    obj1 = Derived_1()

    print("isinstance(obj0, Base)=", isinstance(obj0, Base))
    print("isinstance(obj1, Base)=", isinstance(obj1, Base))
    print("issubclass(Derived_0, Base)=", issubclass(Derived_0, Base))
    print("issubclass(Derived_1, Base)=", issubclass(Derived_1, Base))
    # isinstance(obj0, Base)= True
    # isinstance(obj1, Base)= False
    # issubclass(Derived_0, Base)= True
    # issubclass(Derived_1, Base)= False

    def validate_numeric_value(value):
        if isinstance(value, (int, float, complex)):
            print(value, '-> ok!')
        else:
            raise TypeError(
                f"numeric value expected, but has got {type(value).__name__} type!"
            )

    validate_numeric_value(3) # int
    validate_numeric_value(3.14) # float
    validate_numeric_value(complex('1.0+2.0j')) # complex
    validate_numeric_value('abc') # str
    # 3 -> ok!
    # 3.14 -> ok!
    # (1+2j) -> ok!
    # TypeError: numeric value expected, but has got str type!

if False:
    # -------------------------------------------------------------------
    # callable(object)
    # ; return true if the object argument appears callable, false if not
    # ; classes are callable (calling a class returns a new instance)
    # ; instances are callable if their class has a __call__() method
    # -------------------------------------------------------------------
    pass

if False:
    # ---------------------------------------------------------------------
    # - iter(object[, sentinel])
    # ; return an iterator object
    # (1) calls __iter__ if it exists(implemented)
    # (2) calls __getitem__ starting from index 0 if it exists(implemented)
    # (3) else 'TypeError'
    # ---------------------------------------------------------------------
    pass

if False:
    # --------------------------------------------------------------------
    # - next(iterator, /)
    # - next(iterator, default, /)
    # ; retrieve the next item from the iterator by calling its __next__()
    #   method.
    # ; if default is given, it is returned if the iterator is exhausted,
    #   otherwise stopiteration is raised.
    # --------------------------------------------------------------------
    pass

if False:
    # ----------------------------------------------------------------------
    # - sorted(iterable, /, *, key=None, reverse=False)
    # ; return a new sorted list from the items in iterable
    # ; key specifies a function of one argument that is used to extract a
    #   comparison key from each element in iterable
    # ; reverse is set to True, then the list elements are sorted as if each
    #   comparison were reversed
    # - sorted() vs reversed()
    # ; sorted() -> return a new sorted list from the items in iterable
    # ; reversed() -> return a reverse iterator
    # ----------------------------------------------------------------------
    pass

if False:
    # -------------------------------------
    # - all(iterable, /)
    # ; return true if all elements of the iterable are true
    #   (or if the iterable is empty -> woops!)
    basket = [True, True, True]
    print('all(basket) =', all(basket)) # True
    print('all([]) =', all([])) # True!!!

    # -------------------------------------
    # - any(iterable, /)
    # ; return true if any element of the iterable is true.
    # ; if the iterable is empty, return false.

    # -------------------------------------
    # - min(iterable, /, *, key=None)
    # - min(iterable, /, *, default, key=None)
    # - min(arg1, arg2, /, *args, key=None)
    # ; return the smallest item in an iterable or the smallest of two or more
    #   arguments.

    # -------------------------------------
    # - max(iterable, /, *, key=None)
    # - max(iterable, /, *, default, key=None)
    # - max(arg1, arg2, /, *args, key=None)
    # ; return the largest item in an iterable or the largest of two or more
    #   arguments.

    # -------------------------------------
    # - sum(iterable, /, start=0)
    # ; sums start and the items of an iterable from left to right and returns
    #   the total.
    pass

if False:
    # -------------------------------------
    # - round(number, ndigits=None)
    # ; return number rounded to ndigits precision after the decimal point.
    # ; if ndigits is omitted or is none, it returns the nearest integer to its input.
    print('round(1.23, 1) =', round(1.23, 1)) # 1.2
    print('round(1.27, 1) =', round(1.27, 1)) # 1.3
    print('round(-1.27, 1) =', round(-1.27, 1)) # -1.3
    print('round(1.5) =', round(1.5)) # 2 <- to the nearest even number!
    print('round(2.5) =', round(2.5)) # 2 <- to the nearest even number!
    pass

if False:
    # -------------------------------------
    # - vars() or vars(object)
    # ; return the __dict__ attribute for a module, class, instance, or any
    #   other object with a __dict__ attribute.
    # ; without an argument, vars() acts like locals()
    pass
