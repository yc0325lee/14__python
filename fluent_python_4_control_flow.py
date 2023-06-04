# vim: ft=python ts=4 sw=4 tw=78 expandtab
# -*- coding:utf-8 -*-
# ----------------------------------------------------------------------------
# - file : fluent_python_5_control_flow.py
# - author : yc0325lee
# - created : 2022-11-06 22:44:10 by yc032
# - modified : 2022-11-06 22:46:51 by yc032
# - description : 
# 17. iterators, generators, and classic coroutines
# 18. with, match, and else blocks
# 19. concurrency models in python
# 20. concurrent executors
# 21. asynchronous programming
# ----------------------------------------------------------------------------
# - iterable vs iterator
# ; objects implementing an __iter__ method returning an iterator are iterable
# ; objects implementing a __getitem__ method that takes 0-based indexes are iterable
# ; iterables have an __iter__ method that instantiates a new iterator every time.
#
# - iterable
# ; any object from which the iter built-in function can obtain an iterator
# ; an object capable of returning its members one at a time.
# ; all sequence types (such as list, str, and tuple)
# ; non-sequence types like dict, file objects, and objects of any classes you
#   define with an __iter__() method or with a __getitem__() method that
#   implements sequence semantics.
#
# - iterator
# ; any object that implements the __next__ no-argument method that returns the
#   next item in a series or raises stopiteration when there are no more items.
# ; python obtains iterators from iterables.
# ; python iterators also implement the __iter__ method so they are iterable as well.
# ; iterators implement the following 2 methods:
#   (1) a __next__ method that returns individual items or raise StopIteration
#   (2) an __iter__ method that returns self.
#       -> allows iterators to be used where an iterable is expected
# ; iterators are also iterable, but iterables are not iterators.
# ; every generator is an iterator
#
# - standard iterator interface must provides:
# (1) __next__() returns the next available item, raising stopiteration when
#     there are no more items.
# (2) __iter__() returns 'self'
#     -> allows an iterator to be used wherever an iterable is required.
#     -> iterator can be used for 'iterable' also!
# ----------------------------------------------------------------------------



# -------------------------------------
# chapter 14: iterables, iterators, and generators


if False:
    # ---------------------------------------------------------------------
    # - sentence take #1: a sequence of words
    # ; example 14-1 shows a sentence class that extracts words from a text by index.
    # ; an object is considered iterable
    #   not only when it implements the special method __iter__,
    #   but also when it implements __getitem__, as long as __getitem__ accepts
    #   int keys starting from 0.
    #
    # - iter(object[, sentinel]) builtin functions
    # ; return an iterator object
    #   (1) calls __iter__ if it exists(implemented)
    #   (2) calls __getitem__ starting from index 0 if it exists(implemented)
    #   (3) else 'TypeError'
    # ---------------------------------------------------------------------
    import re
    import reprlib
    import collections.abc
    RE_WORD = re.compile('\w+')

    class Sentence:
        def __init__(self, text):
            self.text = text
            self.words = RE_WORD.findall(text) # list

        def __getitem__(self, index):
            return self.words[index] 

        #def __len__(self): 
        #    return len(self.words)

        def __repr__(self):
            return 'Sentence(%s)' % reprlib.repr(self.text) 
            #                       ----------------------
            #                       provides a means for producing object representations
            #                       with limits on the size of the resulting strings.
            #                       This limits the generated string to 30 characters.

    sentence = Sentence('"The time has come," the Walrus said,')
    print("sentence=", sentence)
    print("iter(sentence)=", iter(sentence))
    # sentence= Sentence('"The time ha... Walrus said,')
    # iter(sentence)= <iterator object at 0x000001F533E4A8F0>

    # iter() will be used for the following iteration
    for i, word in enumerate(sentence):
        print("word[{}]= {}".format(i, word))

    print("sentence[0]=", sentence[0]) # The
    print("sentence[-1]=", sentence[-1]) # said

    words = list(sentence) # possible because Sentence object is iterable.
    print("words=", words)
    # words= ['The', 'time', 'has', 'come', 'the', 'Walrus', 'said']

    # __len__() is not used here and not necessary

    print('\nissubclass(Sentence, collections.abc.Iterable) =', 
        issubclass(Sentence, collections.abc.Iterable))
    # False becuase __iter__ not implemented, but it's still iterable
    # because it supports __getitem__



if False:
    # - sentence take #2: a classic iterator pattern
    # ; example 14-4. sentence implemented using the iterator design pattern
    import re
    import reprlib
    RE_WORD = re.compile('\w+')

    # Sentence object is "iterable" because it provides __iter__()
    # ; never act as an iterator (don't implement __next__)
    class Sentence:
        def __init__(self, text):
            self.text = text
            self.words = RE_WORD.findall(text) # list

        def __repr__(self):
            return 'Sentence(%s)' % reprlib.repr(self.text)

        def __iter__(self):
            return SentenceIterator(self.words)

    # SentenceIterator object is a "iterator" because it provides:
    # ; __next__() with StopIteration exception mechanism
    # ; __iter__() that returns self
    class SentenceIterator:
        def __init__(self, words):
            self.words = words # list
            self.index = 0 # from zero

        def __next__(self):
            try:
                word = self.words[self.index]
            except IndexError:
                raise StopIteration()
            self.index += 1
            return word

        def __iter__(self):
            return self


    sentence = Sentence('"The time has come," the Walrus said,')
    print("sentence=", sentence)
    print("iter(sentence)=", iter(sentence))
    # sentence= Sentence('"The time ha... Walrus said,')
    # iter(sentence)= <__main__.SentenceIterator object at 0x00000213FD39F4D0>

    for i, word in enumerate(sentence):
        print("word[{}]= {}".format(i, word))

    from collections import abc
    print("issubclass(Sentence, abc.Iterable)=", issubclass(Sentence, abc.Iterable)) # True
    print("isinstance(sentence, abc.Iterable)=", isinstance(sentence, abc.Iterable)) # True
    print("isinstance(iter(sentence), abc.Iterator)=",
            isinstance(iter(sentence), abc.Iterator)) # True
    print("isinstance(SentenceIterator, abc.Iterator)=",
            isinstance(SentenceIterator, abc.Iterator)) # False! why?
        

if False:
    # - sentence take #3: a generator function
    # ; example 14-5. sentence implemented using a generator function
    # ; generator function replaces the SentenceIterator class
    # ; no 'StopIteration' error raised
    import re
    import reprlib
    RE_WORD = re.compile('\w+')

    class Sentence:
        def __init__(self, text):
            self.text = text
            self.words = RE_WORD.findall(text) # all words are stored in memory.
                                               # -> not efficient?
        def __repr__(self):
            return 'Sentence(%s)' % reprlib.repr(self.text)

        # iter(sentence) returns generator object
        # -> __iter__() is a generator function
        def __iter__(self):
            for word in self.words:
                yield word
            return # None


    sentence = Sentence('"The time has come," the Walrus said,')
    print("sentence=", sentence)
    print("iter(sentence)=", iter(sentence))
    # sentence= Sentence('"The time ha... Walrus said,')
    # iter(sentence)= <generator object Sentence.__iter__ at 0x000001B0FE47CBA0>

    for i, word in enumerate(sentence): # -> this calls __iter__() and __next__()
                                        #    automatically!
        print("word[{}]= {}".format(i, word))


if False:
    # - sentence take #4: a lazy implementation (<-> eager implementation)
    # ; example 14-7. sentence implemented using a generator function calling
    #   the 're.finditer' generator function
    # ; re.findall() vs. re.finditer()
    #   ------------     -------------
    #      eager              lazy
    import re
    import reprlib
    RE_WORD = re.compile('\w+')

    class Sentence:
        def __init__(self, text):
            self.text = text 

        def __repr__(self):
            return 'Sentence(%s)' % reprlib.repr(self.text)

        # __iter__() returns generator object
        def __iter__(self):
            for match in RE_WORD.finditer(self.text): # re.finditer()!
                yield match.group() 


    sentence = Sentence('"The time has come," the Walrus said,')
    print("sentence=", sentence)
    print("iter(sentence)=", iter(sentence))

    for i, word in enumerate(sentence): # this calls __iter__() and __next__() automatically!
        print("word[{}]= {}".format(i, word))


if False:
    # - sentence take #5: a generator expression
    # ; the code can be made even shorter with a generator expression
    # ; example 14-9. sentence implemented using a generator expression
    # ; generator expressions are syntactic sugar
    #   can always be replaced by generator function
    import re
    import reprlib
    RE_WORD = re.compile('\w+')

    class Sentence:
        def __init__(self, text):
            self.text = text 

        def __repr__(self):
            return 'Sentence(%s)' % reprlib.repr(self.text)

        def __iter__(self): # returns generator object
            return (match.group() for match in RE_WORD.finditer(self.text))
            #      --------------------------------------------------------
            #                       generator expression


    sentence = Sentence('"The time has come," the Walrus said,')
    print("sentence=", sentence)
    print("iter(sentence)=", iter(sentence))
    # sentence= Sentence('"The time ha... Walrus said,')
    # iter(sentence)= <generator object Sentence.__iter__.<locals>.<genexpr> at 0x000001C857188D40>

    for i, word in enumerate(sentence): # this calls __iter__() and __next__() automatically!
        print("word[{}]= {}".format(i, word))


if False:
    # checking an object if iterable
    from collections.abc import Iterable
    # see 'collections.abc - abstract base classes for containers'


    # (1) __iter__ method check using hasattr()
    # - hasattr(object, name, /)
    # ; the arguments are an object and a string. the result is true if the
    #   string is the name of one of the object’s attributes, false if not.
    obj = list(range(10))
    if hasattr(obj, '__iter__'):
        print("%r is iterable!" % obj)
    else:
        print("%r is not iterable!" % obj)
    # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] is iterable!


    # (2) using the iterable class of collections.abc module
    obj = 127
    if isinstance(obj, Iterable): # collections.abc.Iterable
        print("%r is iterable!" % obj)
    else:
        print("%r is not iterable!" % obj)
    # 127 is not iterable!

    # (3) iter() built-in function
    obj = 127
    try:
        iter(obj) # this will raise a 'TypeError' exception!
        print("%r is iterable!" % obj)
    except Exception as err:
        print("%r is not iterable!" % obj)
        print("(err= {})".format(err))
    # 127 is not iterable!



# -------------------------------------
# arithmetic progression generator

if False:
    # example 14-11. the arithmetic-progression class
    from fractions import Fraction, Decimal
    class ArithmeticProgression:
        debug = False
        def __init__(self, begin, step, end=None): 
            self.begin = begin
            self.step = step
            self.end = end # None -> "infinite" series

        def __iter__(self):
            result = type(self.begin + self.step)(self.begin) 
            #        ----------------------------
            #        numeric coercion rule will control output type

            if __class__.debug:
                print("[debug] type(begin)=", type(self.begin))
                print("[debug] type(step)=", type(self.step))
                print("[debug] type(result)=", type(result))
            forever = self.end is None
            index = 0
            while forever or result < self.end:
                yield result
                index += 1
                result = self.begin + self.step * index
                # -> result re-calculated to minimize the effect of
                #    precision errors.

    ArithmeticProgression.debug = False

    print(list(ArithmeticProgression(0, 1, 3)))
    print(list(ArithmeticProgression(0, 0.5, 3)))
    print(list(ArithmeticProgression(0, 1/3, 1)))
    print(list(ArithmeticProgression(0, Fraction(1, 3), 1)))
    print(list(ArithmeticProgression(0, Decimal('0.1'), 0.3)))
    # [0, 1, 2]
    # [0.0, 0.5, 1.0, 1.5, 2.0, 2.5]
    # [0.0, 0.3333333333333333, 0.6666666666666666]
    # [Fraction(0, 1), Fraction(1, 3), Fraction(2, 3)]
    # [Decimal('0'), Decimal('0.1'), Decimal('0.2')]

    print('\nArithmeticProgression(0.0, 0.3, None)')
    iterator = iter(ArithmeticProgression(0.0, 0.3))
    for i in range(100):
        print("{:10.6f}".format(next(iterator)), end=' ')
        if i > 0 and (i+1) % 5 == 0:
            print()
    

if False:
    # example 14-12. the arithmeticprogression using generator-function
    # ; generator factory -> returns generator object
    from fractions import Fraction, Decimal
    def arithmetic_progression(begin, step, end=None):
        result = type(begin + step)(begin)
        forever = end is None
        index = 0
        while forever or result < end:
            yield result
            index += 1
            result = begin + step * index

    print(list(arithmetic_progression(0, 1, 3)))
    print(list(arithmetic_progression(0, 0.5, 3)))
    print(list(arithmetic_progression(0, 1/3, 1)))
    print(list(arithmetic_progression(0, Fraction(1, 3), 1)))
    print(list(arithmetic_progression(0, Decimal('0.1'), 0.3)))

    print('\narithmetic_progression(0.0, 0.3, None)')
    iterator = arithmetic_progression(0.0, 0.3)
    print('iterator=', iterator)
    print('type(iterator)=', type(iterator))
    for i in range(100):
        print("{:10.6f}".format(next(iterator)), end=' ')
        if i > 0 and (i+1) % 5 == 0:
            print()

    
if False:
    # example 14-13. this works like the previous aritprog_gen functions
    # ; there are plenty of ready-to-use generators in the standard library
    # ; using itertools.takewhile() in standard library
    #   -> simpler and shorter implementation
    import itertools
    from fractions import Fraction, Decimal

    # arithmetic_progression() is not a generator factory,
    # but returns a generator object.
    def arithmetic_progression(begin, step, end=None):
        first = type(begin + step)(begin) # need this to implement
                                          # a type-independant one!
        generator = itertools.count(first, step)
        if end is not None:
            generator = itertools.takewhile(lambda n: n < end, generator)
            # another wrapper to limit the maximum
        return generator

    print(list(arithmetic_progression(0, 1, 3)))
    print(list(arithmetic_progression(0, 0.5, 3)))
    print(list(arithmetic_progression(0, 1/3, 1)))
    print(list(arithmetic_progression(0, Fraction(1, 3), 1)))
    print(list(arithmetic_progression(0, Decimal('0.1'), 0.3)))

    print('\narithmetic_progression(0.0, 0.3, None)')
    gen = arithmetic_progression(0.0, 0.3, 30.0)
    print('gen=', gen)
    print('type(gen)=', type(gen))
    for item in gen:
        print("{:10.6f}".format(next(gen)))
    # gen= <itertools.takewhile object at 0x0000017405585B40>
    # type(gen)= <class 'itertools.takewhile'>


# generator functions in the standard library

if False:
    # -------------------------------------------------
    # - example 14-14. filtering generator functions
    # ; itertools.compress(iterable, selectors)
    # ; itertools.dropwhile(predicate, iterable)
    # ; filter(predicate, iterable)
    # ; itertools.filterfalse(predicate, iterable)
    # ; itertools.islice(iterable, stop)
    # ; itertools.islice(iterable, start, stop, step=1)
    # ; itertools.takewhile(predicate, iterable)
    # -------------------------------------------------
    import itertools

    # - filter(function, iterable)
    # ; construct an iterator from those elements of iterable for which function
    #   returns true.
    # ; returns an iterable object(generator)
    print(list(filter(lambda x: x % 2, range(10))))
    # [1, 3, 5, 7, 9]

    # - itertools.filterfalse(predicate, iterable)
    # ; yields item whenever predicate evaluated as false
    print(list(itertools.filterfalse(lambda x: x % 2, range(10))))
    # [0, 2, 4, 6, 8]

    # - itertools.dropwhile(predicate, iterable)
    # ; make an iterator that drops elements from the iterable as long as the
    #   predicate is true; afterwards, returns every element.
    print(list(itertools.dropwhile(lambda x: x < 2, range(10))))
    # [2, 3, 4, 5, 6, 7, 8, 9]
    # -> [0, 1] dropped from the original list

    # - itertools.takewhile(predicate, iterable)
    # ; make an iterator that drops elements from the iterable as long as the
    #   predicate is true; afterwards, returns every element.
    basket = list(range(10))
    basket.extend([0, 1, 2, 3])
    print('basket =', basket)
    print('taken =', end=' ')
    print(list(itertools.takewhile(lambda x: x < 4, range(10))))
    # basket = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3]
    # taken = [0, 1, 2, 3]

    # - itertools.compress(iterable, selectors)
    # ; make an iterator that filters elements from data returning only those
    #   that have a corresponding element in selectors that evaluates to true.
    # iterable = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    # selector = [0, 0, 0, 1, 1, 1, 0, 1, 1, 0]
    print('compressed =', list(itertools.compress(range(10), (0, 0, 0, 1, 1, 1, 0, 1, 1, 0))))
    def compress(iterable, selectors): # same as above!
        return (item for item, sel in zip(iterable, selectors) if sel)
    print('compressed =', list(compress(range(10), (0, 0, 0, 1, 1, 1, 0, 1, 1, 0))))
    #                                                        -  -  -     -  -
    #                                                              Trues

    # - itertools.islice(iterable, stop)
    #   itertools.islice(iterable, start, stop, step=1)
    # ; make an iterator that returns selected elements from the iterable
    # ; same as seq[:stop] or seq[start:stop:step]
    # ; but lazy calculation! -> memory efficient
    print(list(itertools.islice(range(10), 5))) # iterable[:5]
    print(list(itertools.islice(range(10), 5, 10))) # iterable[5:10]
    print(list(itertools.islice(range(10), 5, 10, 2))) # iterable[5:10:2]


if False:
    # ---------------------------------------------------------
    # - example 14-16. mapping generator function
    # ; itertools.accumulate(iterable[, func, *, initial=None])
    # ; enumerate(iterable, start=0)
    # ; map(function, iterable, /, *iterables)
    # ; itertools.starmap(function, iterable)
    # ---------------------------------------------------------
    import itertools
    import operator

    samples = [5, 4, 2, 8, 7, 6, 3, 0, 9, 1]
    print(list(itertools.accumulate(samples))) # running sum
    print(list(itertools.accumulate(samples, min))) # running minimum
    print(list(itertools.accumulate(samples, max))) # running maximum
    print(list(itertools.accumulate(samples, operator.mul))) # running product

    print(list(enumerate('abcde'))) # enumerate -> 2-element tuple of (index, item)
    print(list(enumerate('abcde', 1))) # enumerate -> 2-element tuple of (index, item)
    # [(0, 'a'), (1, 'b'), (2, 'c'), (3, 'd'), (4, 'e')]
    # [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd'), (5, 'e')]

    print(list(map(operator.mul, range(1, 17, 3), [2, 4, 8])))
    #                            -------+-------  ---------
    #                                   |
    #                               [1, 4, 7]
    #                               stop when the shortest iterable ends.

    print(list(map(lambda a, b: (a, b), range(5), range(4, -1, -1))))
    #                                   ---+----  --------+-------
    #                                      |              |
    #                                      |              [4, 3, 2, 1, 0]
    #                                      [0, 1, 2, 3, 4]
    #
    # [(0, 4), (1, 3), (2, 2), (3, 1), (4, 0)]

if False:
    # ---------------------------------------------------------
    # - example 14-17.  Generator functions that merge multiple input
    #   iterables
    # ; itertools.chain(it0, it1, it2, ...)
    # ; itertools.chain.from_iterable(iterable)
    # ; itertools.product(it0, it1, it2, ..., repeat=1)
    # ; zip(it0, it1, it2, ..., strict=False)
    # ; itertools.zip_longest(it0, it1, ..., fillvalue=None)
    import itertools

    # - itertools.chain(*iterables)
    #   itertools.chain(iterable0, iterable1, iterable2, ...)
    # ; make an iterator that returns elements from the first iterable until
    #   it is exhausted, then proceeds to the next iterable, until all of the
    #   iterables are exhausted.
    cont0 = list(range(0, 10))
    cont1 = list(range(10, 20))
    print(list(itertools.chain(cont0, cont1)))
    # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
    # -> chained

    print(
        list(
            zip('abc', range(5), [10, 20, 30, 40, 50])
        ))#     -----
          #    shortest

    # [('a', 0, 10), ('b', 1, 20), ('c', 2, 30)]

    print(
        list(
            itertools.zip_longest('abc', range(5), [10, 20, 30, 40, 50], fillvalue='?')
        )) #                      -----
           #                     shortest

    # [('a', 0, 10), ('b', 1, 20), ('c', 2, 30), ('?', 3, 40), ('?', 4, 50)]


    # - itertools.product(*iterables, repeat=1)
    # ; cartesian product of input iterables.
    # ; cartesian product of two sets A and B, denoted A × B, is the set of
    #   all ordered pairs (a, b) where a is in A and b is in B.
    # ; product(A, B) returns the same as ((x,y) for x in A for y in B)

    # deck of cards
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'clubs diamonds hearts spades'.split()
    #deck = ((suit, rank) for suit in suits for rank in ranks)
    deck = itertools.product(suits, ranks)
    print('deck =', deck)
    for card in deck:
        print(card)

    # coordinate system
    vals = [0, 1]
    vectors = itertools.product(vals, repeat=3)
    for vector in vectors:
        print(vector)


if False:
    # - example 14-21 rearranging generator functions
    # ; yield all items in the input iterables, but rearranged in some way
    # ; itertools.groupby(iterable, key=None)
    # ; reversed(seq, /)
    # ; 
    # ; make an iterator that returns consecutive keys and groups from the iterable
    import itertools

    # - itertools.groupby(iterable, key=None)
    # ; make an iterator that returns consecutive keys and groups from the
    #   iterable. the key is a function computing a key value for each element.
    print('\n# itertools.groupby(iterable, key=None)')
    animals = ['duck', 'eagle', 'rat', 'giraffe', 'bear', 'bat', 'dolphin', 'shark', 'lion']
    animals.sort(key=len) # sort first!
    print('animals =', animals)

    for length, group in itertools.groupby(animals, len):
        print(length, '->', list(group))
    # animals = [
    #     'rat', 'bat', 'duck', 'bear', 'lion', 'eagle', 'shark', 'giraffe', 'dolphin'
    # ]
    # 3 -> ['rat', 'bat']
    # 4 -> ['duck', 'bear', 'lion']
    # 5 -> ['eagle', 'shark']
    # 7 -> ['giraffe', 'dolphin']

    # - itertools.tee(iterable, n=2)
    # ; return n independent iterators from a single iterable.
    # ; yields a tuple of ngenerators, each yielding the items of the input
    #   iterable independently
    print('\n# itertools.tee(iterable, n=2)')
    g0, g1, g2 = itertools.tee('abcde', 3)
    print('list(g0) =', list(g0))
    print('list(g1) =', list(g1))
    print('list(g2) =', list(g2))
    g0, g1, g2 = itertools.tee('abcde', 3) # reset generators
    next(g0)
    next(g1)
    next(g1)
    print('list(g0) =', list(g0))
    print('list(g1) =', list(g1))
    print('list(g2) =', list(g2))


if False:
    # - example 14-23 iterable reducing functions
    # ; all(iterable, /)
    # ; any(iterable, /)
    # ; min(iterable, /, *, key=None)
    # ; functools.reduce(function, iterable[, initializer])
    # ; max(iterable, /, *, key=None)
    # ; sum(iterable, /, start=0)

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

    # values = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    # result1 = 45
    # result2 = 362880


if False:
    # - a closer look at the iter function
    # ; python calls iter(x) when it needs to iterate over an object x
    # - iter(object[, sentinel])
    # ; return an iterator object
    #   (1) calls __iter__ if it exists(implemented)
    #   (2) calls __getitem__ starting from index 0 if it exists(implemented)
    #   (3) else 'TypeError'
    # ; 2 usages
    #   (1) iter(object)
    #       -> raise StopIteration when exhausted
    #   (2) iter(object, sentinel)
    #       -> raise StopIteration when meets sentinel

    # example of iter(object, sentinel)
    with open('input.txt') as infile:
        for line in iter(infile.readline, ''): # sentinel
            line = line.rstrip()
            print(line)


# -------------------------------------
# chapter 15: context managers and else blocks
# - the with statement and context managers
# - the else clause in for, while, and try statements

if False:
    # - else blocks

    # - for-else block
    # ; the else block will run only if and when the for loop runs to completion
    #   (i.e., not if the for is aborted with a break)
    
    # - while-else block
    # ; the else block will run only if and when the while loop exits because the
    #   condition became falsy (i.e., not when the while is aborted with a break).
    
    # - try-else block
    # ; the else block will only run if no exception is raised in the try block.
    pass

if False:
    # - example 15-1. demonstration of a file object as a context manager
    # ; __enter__ and __exit__ methods are invoked implicitly
    # ; (1) __enter__ is invoked on the context manager object
    # ; (2) __exit__ on the context manager object is invoked implicitly
    #       at the end of the with block
    with open("input.txt", "r", encoding="utf8") as infile:
        for lineno, line in enumerate(infile, 1):
            print(lineno + ": " + line, end="")
        # no need to close the opened file here! -> convenient!
