# vim: ft=python ts=4 sw=4 tw=78 expandtab
# -*- coding:utf-8 -*-
# ----------------------------------------------------------------------------
# - file : lib__itertools.py
# - author : yc0325lee
# - created : 2022-11-10 13:15:07 by yc032
# - modified : 2022-11-10 13:15:07 by yc032
# - description : 
# ; provides functions creating iterators for efficient looping
# ----------------------------------------------------------------------------
import itertools

if False:
    # - itertools.takewhile(predicate, iterable)
    # ; make an iterator that returns elements from the iterable as long as
    #   the predicate is true
    # ; produces a generator that consumes another generator and stops when a
    #   given predicate evaluates to False.
    # - itertools.count(start=0, step=1)
    # ; make an iterator that returns evenly spaced values starting with
    #   number start.
    limit = 5.0

    print('\n# using itertools.takewhile')
    thing = itertools.takewhile(lambda n: n < limit, itertools.count(1, 0.3))
    #                           --------------------------------------------
    #                                      generator expression

    print('thing =', thing)
    print('type(thing) =', type(thing))
    print('iter(thing) =', iter(thing)) # returns self

    print("val=", next(thing))
    print("val=", next(thing))
    for val in thing:
        print(val)
    # - using itertools.takewhile
    # thing = <itertools.takewhile object at 0x000002521CE47FC0>
    # type(thing) = <class 'itertools.takewhile'>
    # iter(thing) = <itertools.takewhile object at 0x000002521CE47FC0>
    # val= 1
    # val= 1.3
    # 1.6
    # 1.9000000000000001
    # 2.2
    # 2.5
    # 2.8
    # 3.0999999999999996
    # 3.3999999999999995
    # 3.6999999999999993
    # 3.999999999999999
    # 4.299999999999999
    # 4.599999999999999
    # 4.899999999999999

    print('\n# using generator function takewhile - equivalent implementation')
    def takewhile(predicate, iterable):
        for x in iterable:
            if predicate(x):
                yield x
            else:
                break

    thing = takewhile(lambda n: n < limit, itertools.count(1, 0.3))

    print('thing =', thing)
    print('type(thing) =', type(thing))
    print('iter(thing) =', iter(thing)) # returns self

    print("val=", next(thing))
    print("val=", next(thing))
    for val in thing:
        print(val)
    # - using generator function takewhile - equivalent implementation
    # thing = <generator object takewhile at 0x000002521CDC0D60>
    # type(thing) = <class 'generator'>
    # iter(thing) = <generator object takewhile at 0x000002521CDC0D60>
    # val= 1
    # val= 1.3
    # 1.6
    # 1.9000000000000001
    # 2.2
    # 2.5
    # 2.8
    # 3.0999999999999996
    # 3.3999999999999995
    # 3.6999999999999993
    # 3.999999999999999
    # 4.299999999999999
    # 4.599999999999999
    # 4.899999999999999


if False:
    # -------------------------------------
    # - itertools.chain(*iterables)
    #   itertools.chain(iterable0, iterable1, iterable2, ...)
    # ; make an iterator that returns elements from the first iterable until
    #   it is exhausted, then proceeds to the next iterable, until all of the
    #   iterables are exhausted.
    a = [1, 2, 3, 4]
    b = ['x', 'y', 'z']

    for x in itertools.chain(a, b):
        print(x)

    # inefficent
    for x in a + b:
        print(x)

    # better
    for x in chain(a, b):
        print(x)

    # - classmethod chain.from_iterable(iterable)
    # ; alternate constructor for chain(). gets chained inputs from a single
    #   iterable argument that is evaluated lazily. roughly equivalent to
    pass


if False:
    # - itertools.product(*iterables, repeat=1)
    # ; cartesian product of input iterables.
    # ; cartesian product of two sets A and B, denoted A × B, is the set of
    #   all ordered pairs (a, b) where a is in A and b is in B.
    # ; product(A, B) returns the same as ((x,y) for x in A for y in B)

    # deck of cards
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'clubs diamonds hearts spades'.split()
    deck = ((suit, rank) for suit in suits
                         for rank in ranks)
    print('deck =', deck)
    print('type(deck) =', type(deck))
    for card in deck:
        print(card)

    # 2-dimensional coordinate system
    xvals = range(-2, 3)
    yvals = range(-2, 3)
    #coordinates = ((x, y) for y in yvals
    #                      for x in xvals)
    coordinates = itertools.product(xvals, yvals)
    for coordinate in coordinates:
        print(coordinate)

    print()

    vals = range(-5, 6)
    coordinates = itertools.product(vals, repeat=2)
    for coordinate in coordinates:
        print(coordinate)


if False:
    # - itertools.zip_longest(*iterables, fillvalue=None)
    # ; make an iterator that aggregates elements from each of the iterables.
    #   if the iterables are of uneven length, missing values are filled-in with
    #   fillvalue. iteration continues until the longest iterable is exhausted.
    pass

if False:
    # - itertools.groupby(iterable, key=None)
    # ; make an iterator that returns consecutive keys and groups from the
    #   iterable. the key is a function computing a key value for each element.
    pass

if False:
    # - itertools.compress(data, selectors)
    # ; make an iterator that filters elements from data returning only those
    #   that have a corresponding element in selectors that evaluates to true.
    #   stops when either the data or selectors iterables has been exhausted.
    pass
