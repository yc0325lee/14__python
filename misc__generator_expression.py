# vim: ft=python ts=4 sw=4 tw=78 expandtab
# -*- coding:utf-8 -*-
# ----------------------------------------------------------------------------
# - file : misc__generator_expression.py
# - author : yc0325lee
# - created : 2022-11-08 22:43:22 by yc032
# - modified : 2022-11-08 22:43:22 by yc032
# - references
# ; https://docs.python.org/3/tutorial/classes.html#iterators
# ; https://docs.python.org/3/tutorial/classes.html#generators
# ; https://docs.python.org/3/tutorial/classes.html#generator-expressions
# - description : 
# ----------------------------------------------------------------------------
if True:
    # - simple generator function
    # ; a function that contains the yield keyword in the body
    def gen_123():
        yield 1
        yield 2
        yield 3
        # when the body of the function completes,
        # the generator object raises a 'StopIteration'
        # (this conforms to the Iterator protocol!)

    print('gen_123 =', gen_123) # -> function object
    # gen_123 = <function gen_123 at 0x000002172A628E00>

    thing = gen_123() # function call -> returns generator object (iterator)
    print('thing =', thing)
    print('type(thing) =', type(thing))
    # thing = <generator object gen_123 at 0x00000182DFD68B40>
    # type(thing) = <class 'generator'>

    print(next(thing)) # -> 1
    print(next(thing)) # -> 2
    print(next(thing)) # -> 3
    #print(next(thing)) # -> StopIteration!

    for val in gen_123():
        print('val =', val)
        # -----------------------------------------------------------
        # does the followings:
        # (1) g = iter(gen_123())
        # (2) next(g) invoked until the end of function body
        # (3) 'StopIteration' will be raised upon the end of function
        # (4) for-looop will catch the exception and stop the loop
        # -----------------------------------------------------------

    print('\n# list comprehension')
    vals = [x*3 for x in gen_123()]
    print('type(vals) =', type(vals))
    print('vals =', vals)
    for val in vals:
        print(val, end=' ')

    print('\n# generator expression')
    vals = (x*3 for x in gen_123())
    print('type(vals) =', type(vals))
    print('vals =', vals)
    for val in vals:
        print(val, end=' ')


if False:
    # - 4.3. creating new iteration patterns with generator functions
    # ; generator function
    #   -> 'yield' statement in the body
    #   -> generator factory
    #   -> function call returns generator object
    #      __next__() and __iter__() are created automatically
    # ; each time next() is called on it, the generator resumes where it left
    #   off (it remembers all the data values and which statement was last
    #   executed
    def some_range(start, stop, incr):
        val = start
        while val < stop:
            yield val # generator!
            val += incr

    print("some_range=", some_range)
    # function object
    # some_range= <function some_range at 0x00000188986CE040>

    for value in some_range(0.0, 4.0, 0.5):
    #            -------------------------
    #                generator object
        print("item=", value)

    print()
    
    #iterator = iter(some_range(0.0, 4.0, 0.5)) # returns self!
    iterator = some_range(0.0, 4.0, 0.5) # returns generator object
    print("iterator=", iterator)
    print("type=", type(iterator))
    # iterator= <generator object some_range at 0x0000020F7F4A0D60>
    # type= <class 'generator'>

    while True:
        item = next(iterator, None) # None -> sentinel
        if item is None:            # instead of 'StopIteration' exception!
            break
        print("item=", item)

    print()
    
    iterator = some_range(0.0, 4.0, 0.5)
    while True:
        item = next(iterator)
        print("item=", item)
        # 'StopIteration' will be raised when exhausted
    
    # -------------------------------------------------------------
    # [note]
    # - range() is not an iterator -> iter() required
    # - list() is not an iterator -> iter() required
    # - generator object is an iterator -> iter() not required
    # -------------------------------------------------------------

    # ----------------------------------------------------------------------------
    # next(iterator[, default])
    # - Retrieve the next item from the iterator by calling its __next__() method.
    # - If default is given, it is returned if the iterator is exhausted,
    #    otherwise 'StopIteration' exception is raised.
    # ----------------------------------------------------------------------------

if False:
    # - generator expression
    # ; syntax similar to list comprehensions but with parentheses
    #   instead of square brackets
    # ; more memory friendly than equivalent list comprehensions
    #   because it yields items one by one using the iterator protocol
    #   instead of building a whole list just to feed another constructor.

    print('\nsum of squares')
    print('sum(i*i for i in range(10)) =', sum(i*i for i in range(10)))

    print('\ndot product - zipping 2 vectors')
    xvals = [10, 20, 30]
    yvals = [ 7,  5,  3]
    print('sum(x*y for x, y in zip(xvals, yvals)) =',
            sum(x*y for x, y in zip(xvals, yvals)))


    symbols = 'abcdefghijklmnopqrstuvwxyz'
    codes = (ord(symbol) for symbol in symbols) # generator object
    print("codes=", codes)

    for Upper, Lower in ((ord(symbol)-32, ord(symbol)) for symbol in symbols):
        print("upper= {}, lower= {}".format(Upper, Lower))

    print("sum=", sum(code-32 for code in codes))
    
    #colors = ['black', 'white']
    #sizes = ['small', 'medium', 'arge'] # cartesian product
    #items = [color + '-' + size for color in colors for size in sizes]
    #print("items=", items)


