#!/usr/bin/env python
# vim: ft=python ts=4 sw=4 tw=78 expandtab
# -*- coding:utf-8 -*-
# ----------------------------------------------------------------------------
# - file : fluent_python_2_data_structures.py
# - author : yc0325lee
# - created : 2022-10-16 00:14:54 by lee2103
# - modified : 2023-06-11 23:40:14 by yc032
# - description : 
# 1. the python data model
# 2. an array of sequences
# 3. dictionaries and sets
# 4. unicode text versus bytes
# 5. data class builders
# 6. object references, mutability, and recycling
# ----------------------------------------------------------------------------

# -------------------------------------
# - basic ideas in python (pythonic)
# ; generic operations on different types of sequence
# ; built-in tuple and mapping types
# ; structure by indentation
# ; strong typing without variable declarations
# ; and more.


# -------------------------------------
# chapter 1: the python data model
# - x[i]
#   ; invokes type(x).__getitem__(x, i)
# - obj[key] -> obj.__getitem__(key) magic(special) method invoked
# - 
# - magic methods are used for
# ; iteration
# ; collections
# ; attribute access
# ; operator overloading
# ; function and method invocation
# ; object creation and destruction
# ; string representation and formatting
# ; managed contexts (i.e., with blocks)
#
# - special methods
# ; magic methods, double-underscore methods, dunder methods, ...
# ; python language reference -> 3.3.2 customizing attribute access
#
# - obj.__new__(cls)
# ; called to create a new instance of class cls
# ; a static method (special-cased so you need not declare it as such) that
#   takes the class of which an instance was requested as its first argument
#
# - obj.__bool__(self)
# ; invoked for truth/falsehood test and bool()
# ; __len__() invoked when not implemented
# ; true when no __bool__ and __len__


if False:
    # -------------------------------------
    # - a pythonic card deck - FrenchDeck
    # ; __getitem__() -> index-ed accessing, iteration, ...
    # ; __len__() -> len(deck)
    import sys
    import collections

    # decorator for debugging
    def debug(func):
        def wrapper(*args):
            #print("[dgb ] {}({}) starts ...".format(func.__name__, list(args[1:])))
            print("[dgb ] {}() starts ...".format(func.__name__))
            decorated = func(*args)
            print("[dgb ] {}() ends ...".format(func.__name__))
            #print("[dgb ] {}({}) ends ...".format(func.__name__, list(args[1:])))
            return decorated
        return wrapper
    
    # the following defines 'Card' type
    Card = collections.namedtuple('Card', ['rank', 'suit'])
    
    class FrenchDeck:
        """
        implementation of __len__ and __getitem__ is important
        for sequence-like behavior!!!
        - iteration and slicing
        - using built-in reversed(), sorted() and random.choice()
        """
        ranks = [str(n) for n in range(2, 11)] + list('JQKA')
        #suits = 'spades diamonds clubs hearts'.split()
        suits = 'clubs diamonds hearts spades'.split() # with priority
        print("ranks=", ranks, "len=", len(ranks))
        print("suits=", suits, "len=", len(suits))
        # ranks= ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'] len= 13
        #          0    1    2    3    4    5    6    7     8    9   10   11   12
        # suits= ['clubs', 'diamonds', 'hearts', 'spades'] len= 4
        
        @debug
        def __init__(self):
            # saved as list!
            self._cards = [Card(rank, suit) for suit in self.suits
                                            for rank in self.ranks]
        @debug
        def __len__(self):
            return len(self._cards)
    
        @debug
        def __getitem__(self, position):
            print('[dbg ] position=', position)
            return self._cards[position] # ':' slicing also supported
        pass

    
    deck = FrenchDeck()
    print("deck=", deck) # __str__ or __repr__ not implemented!
                         # deck= <__main__.FrenchDeck object at 0x0000023103FF8B80>

    if False:
        print("\n# testing deck.__len__()")
        print("len=", len(deck)) # -> deck.__len__()
    
    if False:
        print("\n# element access using []")
        for i in range(len(deck)):
            card = deck[i] # deck[i] -> deck.__getitem__(i)
            print(f"deck[{i:2d}]= {card}")
    
    if False:
        # function input for random.choice()
        # ; __len__() first, __getitem__() second
        import random
        print("\n# input to random.choice() function")
        for i in range(10):
            print("card[{}]= {}".format(i, random.choice(deck)))
            # random.choice(deck) -> deck.__len__() -> deck.__getitem__()
    
    if False:
        # slicing also supported cuz __getitem__() delegates to [] operator
        print("\n# slicing like list or tuple")
        print("deck[:3]=", deck[:3])
        # [dgb ] __getitem__() starts ...
        # [dbg ] position= slice(None, 3, None)
        # [dgb ] __getitem__() ends ...

        print("\n# for card in deck[:4]")
        for card in deck[:4]:
            print(card)

        #print(deck[12::13]) # s[start:end:step]
        print("\n# for card in deck[12::13]")
        for card in deck[12::13]:
            print(card)

    if False:
        # membership(containment) operator 'in'
        # ; no __contains__ method
        #   -> sequential scan with __getitem__
        print("\n# membership(containment) test")
        card = Card('Q', 'hearts')
        if card in deck:
            print(card, "exists in deck!")
        else:
            print(card, "does not exist in deck!")

        card = Card('Q', 'beasts')
        if card in deck:
            print(card, "exists in deck!")
        else:
            print(card, "does not exist in deck!")
        
    if False:
        # - iteration
        # ; __getitem__ required, but __len__ not necessary
        if False:
            print("\n# iteration test")
            for card in deck:
                print(card)
        # [dgb ] __getitem__() starts ...
        # [dbg ] position= 0
        # [dgb ] __getitem__() ends ...
        # Card(rank='2', suit='clubs')
        # [dgb ] __getitem__() starts ...
        # [dbg ] position= 1
        # [dgb ] __getitem__() ends ...
        # Card(rank='3', suit='clubs')
        # ... ...
        # ... ...
        # [dgb ] __getitem__() starts ...
        # [dbg ] position= 50
        # [dgb ] __getitem__() ends ...
        # Card(rank='K', suit='spades')
        # [dgb ] __getitem__() starts ...
        # [dbg ] position= 51
        # [dgb ] __getitem__() ends ...
        # Card(rank='A', suit='spades')

        if False:
            print("# reversed(deck)=", reversed(deck))
            # returns generator object
            # -> reversed(deck)= <reversed object at 0x000002C29B9E8220>
            for card in reversed(deck):
                print(card)
        
    if False:
        # sorting by priority
        suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)
        def get_score(card):
            rank_value = FrenchDeck.ranks.index(card.rank)
            return rank_value * len(suit_values) + suit_values[card.suit] # int
        
        print("\n# sorted") # sorted() returns full list!
        print("type=", type(sorted(deck, key=get_score))) # type= <class 'list'>
        for card in sorted(deck, key=get_score):
            print("card=", card, ", score=", get_score(card))
        # card= Card(rank='2', suit='clubs') , score= 0
        # card= Card(rank='2', suit='diamonds') , score= 1
        # card= Card(rank='2', suit='hearts') , score= 2
        # card= Card(rank='2', suit='spades') , score= 3
        # card= Card(rank='3', suit='clubs') , score= 4
        # card= Card(rank='3', suit='diamonds') , score= 5
        # ... ...
        # ... ...
        # card= Card(rank='K', suit='hearts') , score= 46
        # card= Card(rank='K', suit='spades') , score= 47
        # card= Card(rank='A', suit='clubs') , score= 48
        # card= Card(rank='A', suit='diamonds') , score= 49
        # card= Card(rank='A', suit='hearts') , score= 50
        # card= Card(rank='A', suit='spades') , score= 51


if False:
    # -------------------------------------
    # - euclidean vector class
    # ; emulating numeric types
    # ; string representation of objects
    # ; boolean value of an object
    # ; implementing collections
    import math

    # decorator for debugging
    def debug(func):
        def wrapper(*args):
            print("[dgb ] {}() invoked ...".format(func.__name__))
            decorated = func(*args)
            #print("[dgb ] {}() ends ...".format(func.__name__))
            return decorated
        return wrapper
    

    class Vector:
        @debug
        def __init__(self, x=0, y=0):
            self.x = x
            self.y = y

        @debug
        def __repr__(self):
            #return 'Vector(%r, %r)' % (self.x, self.y) # -> '%r' for classic string formatting
            #return 'Vector({!r}, {!r})'.format(self.x, self.y) # -> '!r' for str.format()
            return f'Vector({self.x!r}, {self.y!r})' # '!r' for new formatted string
            # - special method for repr() and print()
            # ; if no custom __str__() is available, python will call __repr__() instead
            # ; %r : standard representation of object using repr() built-in function
            #   !r used for str.format()
            # ; if __repr__ not implemented -> <Vector object at 0x10e100070>

        # def __str__(self):
        # ; invoked by str() constructor or by print() implicitly
        # ; this invoking will fall back to __repr__ in this case.

        @debug
        def __abs__(self):
            # invoked when abs() used
            # return the euclidean norm, sqrt(sum(x**2 for x in coordinates))
            return math.hypot(self.x, self.y)

        @debug
        def __bool__(self):
            # - boolean value contexts : if, while, and, or, not and bool(x)
            # ; if no __bool__ -> x.__len__() invoked
            # ; if no __bool__ and no __len__ -> the object(instance) is always true(default)
            #return bool(math.hypot(self.x, self.y)) -> not simple
            return bool(abs(self)) # good!
            #return bool(self.x or self.y) # faster, but poorer readability
                                            # -> doesn't need to invoke abs()
        @debug
        def __add__(self, right):
            #print("[info] adding %r and %r ..." % (self, right))
            x = self.x + right.x
            y = self.y + right.y
            return Vector(x, y)

        @debug
        def __mul__(self, scalar):
            return Vector(self.x * scalar, self.y * scalar)


    if False:
        # __add__ for addition
        v1 = Vector(2, 4)
        v2 = Vector(2, 1)
        print("\nv1 = ", v1) # __repr__
        print("v2 = ", v2) # __repr__
        print("v1 + v2 =", v1 + v2) # __add__ -> __init__ -> __repr__
        # v1 = Vector(2, 4)         [dgb ] __repr__() invoked ...
        # v2 = Vector(2, 1)         [dgb ] __repr__() invoked ...
        #                           [dgb ] __add__() invoked ...
        #                           [dgb ] __init__() invoked ...
        # v1 + v2 = Vector(4, 5)    [dgb ] __repr__() invoked ...

    if False:
        # __abs__ for abs()
        v3 = Vector(3, 4)
        v4 = Vector() # Vector(0, 0)
        print("\nv3 = ", v3)
        print("v4 = ", v4)
        print("abs(v3) =", abs(v3)) # __abs__
        # v3 = Vector(3, 4)     [dgb ] __repr__() invoked ...
        # v4 = Vector(0, 0)     [dgb ] __repr__() invoked ...
        #                       [dgb ] __abs__() invoked ...
        # abs(v3) = 5.0

        # __mul__ for multiplication
        print("\nv3 * 3 =", v3 * 3)
        print("abs(v3 * 3) =", abs(v3 * 3)) # __mul__ -> __init__
        #                           [dgb ] __mul__() invoked ...
        #                           [dgb ] __init__() invoked ...
        # v3 * 3 = Vector(9, 12)    [dgb ] __repr__() invoked ...
        #                           [dgb ] __mul__() invoked ...
        #                           [dgb ] __init__() invoked ...
        #                           [dgb ] __abs__() invoked ...
        # abs(v3 * 3) = 15.0

    if False:
        # boolean test
        # ; bool(x), if, while, and, or, not, ...
        # ; object of user-defined class -> true
        # ; but __bool__ or __len__ will change the behavior!
        # ; if __bool__ is not implemented, __len__ will be used for true or false
        # ; if x.__len__() teturns zero, then False. otherwise True
        # ; see "The Python Standard Library" -> Built-in Types -> Truth Value Testing
        print("\nbool(v3) = ", bool(v3)) # True
        print("bool(v4) = ", bool(v4)) # False


if False:
    # -------------------------------------
    # see the "data model" from "the python language reference"
    # ; 3.3 special method names

    # - special method names (operators excluded)
    # +-----------------------------------+-------------------------------------------------------------------+
    # | category                          | method names                                                      |
    # +-----------------------------------+-------------------------------------------------------------------+
    # | string/bytes representation       | __repr__ __str__ __format__ __bytes__                             |
    # +-----------------------------------+-------------------------------------------------------------------+
    # | conversion to number              | __abs__ __bool__ __complex__ __int__ __float__ __hash__ __index__ |
    # +-----------------------------------+-------------------------------------------------------------------+
    # | emulating collections             | __len__ __getitem__ __setitem__ __delitem__ __contains__          |
    # +-----------------------------------+-------------------------------------------------------------------+
    # | iteration                         | __iter__ __reversed__ __next__                                    |
    # +-----------------------------------+-------------------------------------------------------------------+
    # | emulating callables               | __call__                                                          |
    # +-----------------------------------+-------------------------------------------------------------------+
    # | context management                | __enter__ __exit__                                                |
    # +-----------------------------------+-------------------------------------------------------------------+
    # | instance creation and destruction | __new__ __init__ __del__                                          |
    # +-----------------------------------+-------------------------------------------------------------------+
    # | attribute management              | __getattr__ __getattribute__ __setattr__ __delattr__ __dir__      |
    # +-----------------------------------+-------------------------------------------------------------------+
    # | attribute descriptors             | __get__ __set__ __delete__                                        |
    # | class services                    | __prepare__ __instancecheck__ __subclasscheck__                   |
    # +-----------------------------------+-------------------------------------------------------------------+
    # ; built-in types don't have __len__
    #   cpython reads length field from c struct directly


    # - special method names for operators
    # +----------------------------+---------------------------------------------------------+
    # | category                   | method names and related operators                      |
    # +----------------------------+---------------------------------------------------------+
    # | unary numeric operators    | __neg__ __pos__ __abs__                                 |
    # +----------------------------+---------------------------------------------------------+
    # | rich comparison operators  | __lt__ __le__ __eq__ __ne__ __gt__ __ge__               |
    # +----------------------------+---------------------------------------------------------+
    # | arithmetic operators       | __add__ __sub__ __mul__ __truediv__ __floordiv__        |
    # |                            | __mod__ __divmod__ __pow__ __round__                    |
    # +----------------------------+---------------------------------------------------------+
    # | reversed arithmetic        | __radd__ __rsub__ __rmul__ __rtruediv__ __rfloordiv__   |
    # | operators                  | __rmod__ __rdivmod__ __rpow__                           |
    # +----------------------------+---------------------------------------------------------+
    # | augmented assignment       | __iadd__ __isub__ __imul__ __itruediv__                 |
    # | arithmetic operators       | __ifloordiv__ __imod__ __ipow__                         |
    # +----------------------------+---------------------------------------------------------+
    # | bitwise operators          | __invert__ __lshift__ __rshift__ __and__ __or__ __xor__ |
    # +----------------------------+---------------------------------------------------------+
    # | reversed bitwise operators | __rlshift__ __rrshift__ __rand__ __rxor__ __ror__       |
    # +----------------------------+---------------------------------------------------------+
    # | augmented assignment       | __ilshift__ __irshift__ __iand__ __ixor__ __ior__       |
    # | bitwise operators          |                                                         |
    # +----------------------------+---------------------------------------------------------+
    # ; reversed operators
    #   obj1 + obj2
    #   if obj1.__add__(obj2) is not available, obj2.__radd__(obj1) invoked as a fallback!
    # ; augmented assignment
    #   obj1 *= obj2 -> obj1.__imul__(obj2)
    pass


# -------------------------------------
# chapter 2: an array of sequences

# built-in sequences
# - container vs flat
#  ; container sequences : list, tuple, and collections.deque
#    -> can hold items of different(heterogeneous) types.
#  ; flat sequences : str, bytes, bytearray, memoryview, and array.array
#    -> hold items of one(homogeneous) type.
# - mutable vs immutable
#  ; mutable sequences : list, bytearray, array.array, collections.deque, and memoryview
#  ; immutable sequences : tuple, str, and bytes
#
# - sequence inheritance hierarchy
#
#   Container,Iterable,Sized (__contains__,__iter__,__len__)
#             |
#             +---Sequence (__getitem__,__contains__,__iter__,__reversed__,index,count)
#                     |
#                     +---MutableSequence
#                         (__delitem__,__iadd__,__setitem__,append
#                          ,extend,insert,pop,remove,reverse)

if False:
    # - issubclass() test
    import collections
    print(issubclass(tuple, collections.abc.Sequence)) # immutable -> True
    print(issubclass(tuple, collections.abc.MutableSequence)) # immutable -> False
    print(issubclass(list, collections.abc.Sequence)) # mutable -> True
    print(issubclass(list, collections.abc.MutableSequence)) # mutable -> True
    pass

if False:
    # -------------------------------------
    # - list comprehension and readability
    # ; abbr -> listcomps, genexps
    # ; a quick way of building a new list
    # ; a concise way to create lists, simpler codes
    # ; syntax tip
    #   in python code, line breaks are ignored inside pairs of [], {}, or ().
    #   so you can build multiline lists, listcomps, genexps, dictionaries and the like
    #   without using the ugly \ line continuation escape.

    # building a list using conventional loop-ing
    symbols = 'abcdefghijklmnopqrstuvwxyz'
    codes = []
    for symbol in symbols:
        codes.append(ord(symbol))
    print("type(codes)=", type(codes))
    print("codes=", codes)
    # --------------------------------------------------------------------------
    # type(codes)= <class 'list'>
    # codes= [97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110,
    #         111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122]
    # --------------------------------------------------------------------------

    # building a list using list comprehension
    codes = [ord(symbol) for symbol in symbols] # list comprehension -> []
    print("type(codes)=", type(codes))
    print("codes=", codes)
    # --------------------------------------------------------------------------
    # type(codes)= <class 'list'>
    # codes= [97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110,
    #         111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122]
    # --------------------------------------------------------------------------



if False:
    # -------------------------------------
    # building cartesian product using list comprehension
    import collections
    Card = collections.namedtuple('Card', ['rank', 'suit'])

    suits = 'clubs diamonds hearts spades'.split() # priority
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    # suits= ['clubs', 'diamonds', 'hearts', 'spades'], len= 4
    # ranks= ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'], len= 13

    # cartesian product
    cards = [Card(rank, suit) for suit in suits
                              for rank in ranks]

    def point(card):
        rank_index = ranks.index(card.rank)
        return len(ranks) * suits.index(card.suit) + ranks.index(card.rank)
    
    for card in cards:
        print("card= {}".format(card), card.suit, card.rank, "point=", point(card))

    print("\n# reversed using sorted()") # sorted() returns full list!
    for card in sorted(cards, key=point, reverse=True):
        print("card= {}".format(card), card.suit, card.rank, "point=", point(card))


if False:
    # -------------------------------------
    # - cartesian product using list comprehension
    # [note] in python code, line breaks are ignored inside pairs of [], {}, or ()
    colors = ['black', 'white']
    sizes = ['small', 'medium', 'large']
    
    tshirts = [(color, size)
                for color in colors
                for size in sizes]
    #print("tshirts=", tshirts)
    print("# from listcomp")
    for pair in tshirts: print(pair)
    # - from listcomp
    # ('black', 'small')
    # ('black', 'medium')
    # ('black', 'large')
    # ('white', 'small')
    # ('white', 'medium')
    # ('white', 'large')

    # same as the following
    tshirts = []
    for color in colors:
        for size in sizes:
            tshirts.append((color, size))
    print("\n# from nested-loop")
    for pair in tshirts: print(pair)
    # - from nested-loop
    # ('black', 'small')
    # ('black', 'medium')
    # ('black', 'large')
    # ('white', 'small')
    # ('white', 'medium')
    # ('white', 'large')

if False:
    # -------------------------------------
    # - generator expression
    # ; syntax similar to list comprehensions but with parentheses
    #   instead of square brackets
    # ; more memory friendly than equivalent list comprehensions
    #   because it yields items one by one using the iterator protocol
    #   instead of building a whole list just to feed another constructor.
    symbols = 'abcdefghijklmnopqrstuvwxyz'
    codes = (ord(symbol) for symbol in symbols) # generator object
    print("codes=", codes) # %r
    print("type=", type(codes)) # generator object
    # codes= <generator object <genexpr> at 0x00000252453ACF90>
    # type= <class 'generator'>

    print()

    print("sum=", sum(i*i for i in range(10)))
    #                 ----------------------
    #                 sum() requires 'iterable'
    #                 generator expression can be used for iterator
    #                 no need for parentheses in this case! (single argument)

    print()

    colors = ['black', 'white']
    sizes = ['S', 'M', 'L']
    #genexp = (f'{color}-{size}' for color in colors for size in sizes)
    for i, item in enumerate(f'{color}-{size}' for color in colors for size in sizes):
        print("item[{}]= {}".format(i, item))
    # item[0]= black-S
    # item[1]= black-M
    # item[2]= black-L
    # item[3]= white-S
    # item[4]= white-M
    # item[5]= white-L


if False:
    # -------------------------------------
    # array - efficient arrays of numeric values
    # ; an object type which can compactly represent an array of basic values
    #   -> characters, integers, floating point numbers.
    import array
    symbols = 'abcdefghijklmnopqrstuvwxyz'
    codes = array.array('I', (ord(symbol) for symbol in symbols)) # 'I' for unsigned int with 2 bytes
    #                        -----------------------------------
    #                            genexp for iterable argument
    print("type=", type(codes))
    print("array=", codes)
    # array= array('I',
    #     [97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109,
    #     110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122]
    # )

    for i, code in enumerate(codes):
        print("code[{}]= {}".format(i, code))

if False:
    # -------------------------------------
    # - tuples as immutable lists
    a = (10, 'alpha', [1, 2])
    b = (10, 'alpha', [1, 2])
    print("a=", a, id(a))
    print("b=", b, id(b))
    print("a == b:", a == b) # True
    # a= (10, 'alpha', [1, 2]) 2399278954048
    # b= (10, 'alpha', [1, 2]) 2399278953984
    # a == b(before): True

    b[-1].append(99)
    print("a == b:", a == b) # True
    # a == b(after): False

    # testing hashability
    def hashable(a):
        try:
            hash(a)
        except TypeError:
            return False
        return True

    tf = (10, 'alpha', (1, 2)) # hashable
    tm = (10, 'alpha', [1, 2]) # unhashable
    
    print("hashable(tf)=", hashable(tf)) # hashable(tf)= True
    print("hashable(tm)=", hashable(tm)) # hashable(tm)= False

    # - tuples are faster than lists generally!
    # ; Tuples can be constant folded.
    # ; Tuples can be reused instead of copied.
    # ; Tuples are compact and don't over-allocate.
    # ; Tuples directly reference their elements.
    # ; https://stackoverflow.com/questions/68630/are-tuples-more-efficient-than-lists-in-python/22140115#22140115


if False:
    # -------------------------------------
    # list vs. tuple
    # +-------------------------+------------+---------------------------------------------------------------------+
    # | function                | list tuple | description                                                         |
    # +-------------------------+------------+---------------------------------------------------------------------+
    # | s.__add__(s2)           | o    o     | s + s2—concatenation                                                |
    # | s.__iadd__(s2)          | o    x     | s += s2—in-place concatenation                                      |
    # | s.append(x)             | o    x     | append one element after last                                       |
    # | s.clear()               | o    x     | delete all items                                                    |
    # | s.__contains__(x)       | o    o     | x in s                                                              |
    # | s.copy()                | o    x     | shallow copy of the list                                            |
    # | s.count(x)              | o    o     | count occurrences of an element                                     |
    # | s.__delitem__(p)        | o    x     | remove item at position p                                           |
    # | s.extend(it)            | o    x     | append items from iterable it                                       |
    # | s.__getitem__(p)        | o    o     | s[p]—get item at position                                           |
    # | s.__getnewargs__()      | o    x     | support for optimized serialization with pickle                     |
    # | s.index(e)              | o    o     | find position of first occurrence of e                              |
    # | s.insert(p,e)           | o    x     | insert element e before the item at position p                      |
    # | s.__iter__()            | o    o     | get iterator                                                        |
    # | s.__len__()             | o    o     | len(s)—number of items                                              |
    # | s.__mul__(n)            | o    o     | s * n—repeated concatenation                                        |
    # | s.__imul__(n)           | o    x     | s *= n—in-place repeated concatenation                              |
    # | s.__rmul__(n)           | o    o     | n * s—reversed repeated concatenationa                              |
    # | s.pop([p])              | o    x     | remove and return last item or item at optional position p          |
    # | s.remove(x)             | o    x     | remove first occurrence of element x by value                       |
    # | s.reverse()             | o    x     | reverse the order of the items in place                             |
    # | s.__reversed__()        | o    x     | get iterator to scan items from last to first                       |
    # | s.__setitem__(p,e)      | o    x     | s[p] = e—put e in position p  overwriting existing itemb            |
    # | s.sort([key],[reverse]) | o    x     | sort items in place with optional keyword arguments key and reverse |
    # +-------------------------+------------+---------------------------------------------------------------------+
    pass

if False:
    # -------------------------------------
    # tuples are not just immutable lists
    # (1) immutable list
    # (2) records with no field name! tuples as records
    traveler_ids = [('usa', '31195855'), ('bra', 'ce342567'), ('esp', 'xda205856')]
    for passport in sorted(traveler_ids):
        print(passport) # -> tuple

    for passport in sorted(traveler_ids):
        print("%s/%s" % passport)
        #               --------
        #               '%' formatting understands tuples!
        #                (country_code, passport_num)

    # retrieving each field
    # ; unpacking with dummy meaningless varialbe '_'
    # ; '_' is a valid variable name here!
    for country, _ in traveler_ids:
        print(country) # country only
    
if False:
    # -------------------------------------
    # - tuple(iterable) unpacking
    traveler_ids = [('USA', '31195855'), ('BRA', 'CE342567'), ('ESP', 'XDA205856')]

    for pair in traveler_ids:
        print("tuple=", pair)
        print("type=", type(pair))
        country, code = pair # tuple unpacking (1) parallel assignment
        print("country=", country, "code=", code)

    del pair, country, code
    print()

    # let's use unpacking form instead ...
    # ; '_' is a dummy variable (2)
    for country, _ in traveler_ids:
        print("country=", country, "code=", _)

    # swapping without temporary variable
    a = 3
    b = 4
    b, a = a, b # unpacking (3)

    # tuple unpacking for divmod's input and output
    # ; divmod() requires 2 arguments -> divmod(input) doesn't work!
    # ; divmod() returns tuple of (quotient, remainder)
    arguments = (20, 8)
    quotient, remainder = divmod(*arguments) # 2 unpackings here (4)
                                             # - arguments(tuple) unpacking
                                             # - return value(tuple) unpacking

    # os.path.split() returns a tuple of (path, filename)
    _, filename = os.path.split(r"user\hls001\TEMP\project.tcl")
    print("filename=", filename, end='\n\n')

if False:
    # -------------------------------------
    # - using '*' to grab excess items like *args
    # ; similar to variable-length arguments in function
    import os

    # (1) using '*' to grab excess items
    a, b, *rest = range(2); print("a=", a, "b=", b, "rest=", rest) # a= 0 b= 1 rest= []       
    a, b, *rest = range(3); print("a=", a, "b=", b, "rest=", rest) # a= 0 b= 1 rest= [2]      
    a, b, *rest = range(4); print("a=", a, "b=", b, "rest=", rest) # a= 0 b= 1 rest= [2, 3]   
    a, b, *rest = range(5); print("a=", a, "b=", b, "rest=", rest) # a= 0 b= 1 rest= [2, 3, 4]
    a, *rest, b = range(5); print("a=", a, "b=", b, "rest=", rest) # a= 0 b= 4 rest= [1, 2, 3]
    *rest, a, b = range(5); print("a=", a, "b=", b, "rest=", rest) # a= 3 b= 4 rest= [0, 1, 2]
    print()

    # (2) using '*' to grab excess arguments
    def func(a, b, *rest):
        print(f'a= {a}, b= {b}, rest= {rest}')

    func(*range(2))
    func(*range(3))
    func(*range(4))
    func(*range(5))
    # a= 0, b= 1, rest= ()
    # a= 0, b= 1, rest= (2,)
    # a= 0, b= 1, rest= (2, 3)
    # a= 0, b= 1, rest= (2, 3, 4)
    #                   ---------
    #                     tuple

if False:
    # -------------------------------------
    # - nested unpacking for tuple
    # tuple = (city, country_code, population, (latitude, longitude))
    #                                           -------------------
    #                                               coordinates
    metro_areas = [
        ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
        ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
        ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
        ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
        ('Sao Paulo', 'BR', 19.649, (-23.547778, -46.635833)),
    ]
    print('{:15} | {:^9} | {:^9}'.format('city', 'lat.', 'long.'))
    fmt = '{:15} | {:9.4f} | {:9.4f}'
    for city, country_code, population, (latitude, longitude) in metro_areas:
        #                                -------------------
        #                                unpacking nested tuple!
        if longitude <= 0:
            print(f'{city:15} | {latitude:9.4f} | {longitude:9.4f}')
            #print(fmt.format(city, latitude, longitude))
            #     ---
            #     fmt-string and args separaed for neat codes!

    # ----------------+-----------+---------- #
    # city            |   lat.    |   long.   #
    # ----------------+-----------+---------- #
    # Mexico City     |   19.4333 |  -99.1333 #
    # New York-Newark |   40.8086 |  -74.0204 #
    # Sao Paulo       |  -23.5478 |  -46.6358 #
    # ----------------+-----------+---------- #


if False:
    # -------------------------------------
    # - pattern matching with sequences
    # ; pep 634—structural pattern matching: specification.
    # ; https://peps.python.org/pep-0634/
    # ; retuires python version >= 3.10
    # ; https://github.com/gvanrossum/patma/blob/3ece6444ef70122876fd9f0099eb9490a2d630df/EXAMPLES.md#case-6-a-very-deep-iterable-and-type-match-with-extraction
    metro_areas = [
        ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
        ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
        ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
        ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
        ('Sao Paulo', 'BR', 19.649, (-23.547778, -46.635833)),
    ]
    print('{:15} | {:^9} | {:^9}'.format('city', 'lat.', 'long.'))
    for record in metro_areas:
        match record:
            case [city, _, _, (latitude, longitude)] if longitude <= 0:
                print(f'{city:15} | {latitude:9.4f} | {longitude:9.4f}')
    # city            |   lat.    |   long.
    # Mexico City     |   19.4333 |  -99.1333
    # New York-Newark |   40.8086 |  -74.0204
    # Sao Paulo       |  -23.5478 |  -46.6358


if False:
    # -------------------------------------
    # - example of lisp command matching
    # ; https://norvig.com/lispy.html -> how to write a (lisp) interpreter (in python)

    # (1) using if-else
    def evaluate(exp: Expression, env: Environment) -> Any:
        "evaluate an expression in an environment."
        if isinstance(exp, Symbol): # variable reference
            return env[exp]
        # ... lines omitted
        elif exp[0] == 'quote': # (quote exp)
            (_, x) = exp
            return x
        elif exp[0] == 'if': # (if test conseq alt)
            (_, test, consequence, alternative) = exp
            if evaluate(test, env):
                return evaluate(consequence, env)
            else:
                return evaluate(alternative, env)
        elif exp[0] == 'lambda': # (lambda (parm…) body…)
            (_, parms, *body) = exp
            return Procedure(parms, body, env)
        elif exp[0] == 'define':
            (_, name, value_exp) = exp
            env[name] = evaluate(value_exp, env)
        # ... more lines omitted

    # (2) using pattern matching with match/case
    def evaluate(exp: Expression, env: Environment) -> Any:
        "evaluate an expression in an environment."
        match exp:
            # ... lines omitted
            case ['quote', x]:
                return x
            case ['if', test, consequence, alternative]:
                if evaluate(test, env):
                    return evaluate(consequence, env)
                else:
                    return evaluate(alternative, env)
            case ['lambda', [*parms], *body] if body:
                return Procedure(parms, body, env)
            case ['define', Symbol() as name, value_exp]:
                env[name] = evaluate(value_exp, env)
            # ... more lines omitted
            case _: 
                raise SyntaxError(lispstr(exp)) # exception handling -> safer!


if False:
    # -------------------------------------
    # - slicing/slice
    # ; range(start, stop, step)
    #   len(range) == stop - start --> straightforward!
    list_ord = list(range(ord('a'), ord('z')+1))
    print(len(list_ord)) # 26
    print(list_ord)
    # [97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122]

    list_chr = [chr(n) for n in list_ord]
    print(list_chr)
    # ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    print(list_chr[:13])
    print(list_chr[13:])
    # ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm']
    # ['n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    subset = list_chr[:13]
    print(subset[::2])
    print(subset[::3])
    print(subset[::-1]) # reversed list
    print(subset[::-2]) # reversed list
    # ['a', 'c', 'e', 'g', 'i', 'k', 'm']
    # ['a', 'd', 'g', 'j', 'm']
    # ['m', 'l', 'k', 'j', 'i', 'h', 'g', 'f', 'e', 'd', 'c', 'b', 'a'] # reversed
    # ['m', 'k', 'i', 'g', 'e', 'c', 'a']

    # slice object
    # ; seq[start:stop:step] ---> invokes seq.__getitem__[slice(start, stop, step)]
    indice = slice(5, 21, 2)
    print(list_chr[indice])
    # ['f', 'h', 'j', 'l', 'n', 'p', 'r', 't']

    # when slice() objects are useful!
    # ; can assign names to slices
    invoice = """
0.....6.................................40........52...55........
1909  Pimoroni PiBrella                     $17.50    3    $52.50
1489  6mm Tactile Switch x20                 $4.95    2     $9.90
1510  Panavise Jr. - PV-201                 $28.00    1    $28.00
1601  PiTFT Mini Kit 320x240                $34.95    1    $34.95
"""
    line_items = invoice.split('\n')[2:]
    sku = slice(0, 6)
    description = slice(6, 40)
    unit_price = slice(40, 50)
    quantity = slice(50, 55)
    item_total = slice(55, None)
    for item in line_items:
        print(item[unit_price], item[description])
    #     $17.50 Pimoroni PiBrella
    #      $4.95 6mm Tactile Switch x20
    #     $28.00 Panavise Jr. - PV-201
    #     $34.95 PiTFT Mini Kit 320x240


if False:
    # -------------------------------------
    # - multidimensional slicing and ellipsis
    # ; a[i, j] ---> invokes a.__getitem__((i, j))
    pass


if False:
    # -------------------------------------
    # - using collections.namedtuple
    # ; more memory-efficient than regular class
    from collections import namedtuple
    City = namedtuple('City', 'name country population location')
    Location = namedtuple('Location', 'latitude longitude')

    print("[dbg] City._fields=", City._fields)
    print("[dbg] Location._fields=", Location._fields)
    # City._fields= ('name', 'country', 'population', 'location')
    # Location._fields= ('latitude', 'longitude')

    # tuple = (name, country_code, population, (latitude, longitude))
    data = [
        ('Tokyo', 'JP', 36.933, Location(35.689722, 139.691667)),
        ('Delhi NCR', 'IN', 21.935, Location(28.613889, 77.208889)),
        ('Mexico City', 'MX', 20.142, Location(19.433333, -99.133333)),
        ('New York-Newark', 'US', 20.104, Location(40.808611, -74.020386)),
        ('Sao Paulo', 'BR', 19.649, Location(-23.547778, -46.635833)),
    ]

    # classmethod somenamedtuple._make(iterable)
    # ; makes a new instance from an existing sequence or iterable
    cities = []
    for datum in data:
        city = City._make(datum)
        cities.append(city)

    # somenamedtuple._asdict()
    # ; return a new built-in dict which maps field names to their corresponding values
    for city in cities:
        for key, val in city._asdict().items():
            if key == "location":
                print("latitude=", val.latitude)
                print("longitude=", val.longitude)
            else:
                print("{}= {}".format(key, val))
        print()
    # name= Tokyo
    # country= JP
    # population= 36.933
    # latitude= 35.689722
    # longitude= 139.691667


if False:
    # -------------------------------------
    # nested list using + and * with sequences
    board = [['_'] * 3 for i in range(3)]
    print(board)
    for row in board:
        print(id(row))
    # [['_', '_', '_'],
    #  ['_', '_', '_'],
    #  ['_', '_', '_']]
    # id= 1780566843200
    # id= 1780566843136
    # id= 1780566842880

    board[1][1] = 'X'
    print(board)
    # [['_', '_', '_'],
    #  ['_', 'X', '_'],
    #  ['_', '_', '_']] -> ok!

    # same as the following
    board = []
    for i in range(3):
        row = ['_'] * 3
        board.append(row)

if False:
    # -------------------------------------
    # strage behavior when building a nest list!
    board = [['_'] * 3] * 3 # be careful!
    #       -----------
    #       this will be repeated!
    #       (reference to the same list is repeated)
    print(board)
    for row in board:
        print(id(row))
    # [['_', '_', '_'],
    #  ['_', '_', '_'],
    #  ['_', '_', '_']]
    # 1932507050176
    # 1932507050176
    # 1932507050176 -> same!

    board[1][2] = 'X'
    print(board)
    # [['_', '_', 'X'], ['_', '_', 'X'], ['_', '_', 'X']] -> no!

    # same as the following
    row = ['_'] * 3
    board = []
    for i in range(3):
        board.append(row)
        # same row is reapeated!

if False:
    # -------------------------------------
    # augmented assignment with sequences
    # ; += -> __iadd__(in-place addition, list built-in type)
    # ; if __iadd__ is not implemented, __add__ used as a fallback(tuple built-int type)
    # ; a += b
    #     mutable sequence -> __iadd__ -> same as a.extend(b)
    #   immutable sequence -> __add__, -> same as a = a + b, returns a new object, less efficient

    l = [1, 2, 3] # list -> __iadd__()
    print("l=", l)
    print("id(l)=", id(l), "\n") # 1779609718592

    l *= 2  # [1, 2, 3, 1, 2, 3]
    print("l=", l)
    print("id(l)=", id(l), "\n") # 1779609718592

    t = (1, 2, 3) # tuple -> __add__
    print("t=", t)
    print("id(t)=", id(t), "\n") # 1779612886848

    t *= 2  # (1, 2, 3, 1, 2, 3) -> inefficient!
    print("t=", t)
    print("id(t)=", id(t), "\n") # 1779610170656 ** different ***


if False:
    # -------------------------------------
    # a += assignment puzzler
    # ; strange behavior an python's corner case but not a problem.
    # ; this thing really happens
    import dis

    t = (1, 2, [30, 40]) # tuple
    print("t=", t)
    print("type(t[2])=", type(t[2]))
    # t= (1, 2, [30, 40])
    # type(t[2])= <class 'list'>

    t[2] += [50, 60] # [question] is it possible to modify an element of tuple?

    #dis.dis('t[2] += [50, 60]') # for debugging
    #  1           0 LOAD_NAME                0 (t)
    #              2 LOAD_CONST               0 (2)
    #              4 DUP_TOP_TWO
    #              6 BINARY_SUBSCR
    #              8 LOAD_CONST               1 (50)
    #             10 LOAD_CONST               2 (60)
    #             12 BUILD_LIST               2
    #             14 INPLACE_ADD
    #             16 ROT_THREE
    #             18 STORE_SUBSCR             *** trying to modify an element of tuple!!! ***
    #             20 LOAD_CONST               3 (None)
    #             22 RETURN_VALUE

    # 'tuple' object does not support item assignment
    # but, what happens here?
    if False:
        try:
            t[2] += [50, 60] # [question] is it possible to modify an element of tuple?
        except Exception as err:
            print(err)

        print("t=", t) # anyway the final result was modified!
        # t= (1, 2, [30, 40, 50, 60])

    # --------------------------------------------------------------
    # 2 things happen here:
    # (1) TypeError: 'tuple' object does not support item assignment
    # (2) modification happens: [30, 40] -> [30, 40, 50, 60]
    # --------------------------------------------------------------

    # - lessons here!
    # ; avoid putting mutiable items in tuples(immutable)


if False:
    # ------------------------------------------------------------------------
    # - list.sort() and the sorted() built-in function
    # ; functions or methods that change an object in place should return None
    # - list.sort(*, key=None, reverse=False)
    # ; sorts the list in place, using only < comparisons between items
    # ; returns None
    # ; random.shuffle(s) does a similar thing(in-place modification)
    #
    # - sorted(iterable, /, *, key=None, reverse=False)
    # ; built-in function
    # ; return a new sorted 'list' from the items in iterable(not an iterator)
    # ------------------------------------------------------------------------
    fruits = ['grape', 'raspberry', 'apple', 'banana']
    print("fruits=", fruits)
    # fruits= ['grape', 'raspberry', 'apple', 'banana']

    print("sorted=", sorted(fruits))
    # sorted= ['apple', 'banana', 'grape', 'raspberry']

    print("sorted=", sorted(fruits, reverse=True))
    # sorted= ['raspberry', 'grape', 'banana', 'apple']

    print("sorted=", sorted(fruits, key=len))
    # sorted= ['grape', 'apple', 'banana', 'raspberry'] -> stable sorting!(order preserved)

    print("sorted=", sorted(fruits, key=len, reverse=True))
    # sorted= ['raspberry', 'banana', 'grape', 'apple']

    fruits.sort() # in-place modification & returns None
    print("fruits=", fruits)
    # fruits= ['apple', 'banana', 'grape', 'raspberry']


if False:
    # ------------------------------------------------------------------------
    # - bisect — array bisection algorithm
    # ; provides support for maintaining a list in sorted order without having
    #   to sort the list after each insertion
    # ; searching with bisect
    # ------------------------------------------------------------------------
    import bisect # array bisection algorithm

    haystack = [1, 4, 5, 6, 8, 12, 15, 20, 21, 23, 23, 26, 29, 30]
    needles = [0, 1, 2, 5, 8, 10, 22, 23, 29, 30, 31]

    ROW_FMT = '{0:02d} @ {1:2d} {2}{0:<2d}'
    #          ---+---   --+--- -+----+---
    #             |        |     |    |
    #             |        |     |    needle
    #             |        |     offset
    #             |        position
    #             needle

    def demo(bisect_fn):
        for needle in reversed(needles):
            position = bisect_fn(haystack, needle)
            offset = '      ' + position * ' | '
            print(ROW_FMT.format(needle, position, offset))

    # bisect_right : target position after
    # bisect_left : target position before
    for bisect_fn in [bisect.bisect_left, bisect.bisect]:
        print('\ndemo:', bisect_fn.__name__)
        print("len(haystack)=", len(haystack))
        print('haystack ->  ', ' '.join('%02d'.format(n) for n in haystack))
        demo(bisect_fn)

    # demo: bisect_left
    # len(haystack)= 14
    # haystack ->   01 04 05 06 08 12 15 20 21 23 23 26 29 30
    # 31 @ 14        |  |  |  |  |  |  |  |  |  |  |  |  |  | 31
    # 30 @ 13        |  |  |  |  |  |  |  |  |  |  |  |  | 30
    # 29 @ 12        |  |  |  |  |  |  |  |  |  |  |  | 29
    # 23 @  9        |  |  |  |  |  |  |  |  | 23
    # 22 @  9        |  |  |  |  |  |  |  |  | 22
    # 10 @  5        |  |  |  |  | 10
    # 08 @  4        |  |  |  | 8
    # 05 @  2        |  | 5
    # 02 @  1        | 2
    # 01 @  0       1
    # 00 @  0       0
    # 
    # demo: bisect_right
    # len(haystack)= 14
    # haystack ->   01 04 05 06 08 12 15 20 21 23 23 26 29 30
    # 31 @ 14        |  |  |  |  |  |  |  |  |  |  |  |  |  | 31
    # 30 @ 14        |  |  |  |  |  |  |  |  |  |  |  |  |  | 30
    # 29 @ 13        |  |  |  |  |  |  |  |  |  |  |  |  | 29
    # 23 @ 11        |  |  |  |  |  |  |  |  |  |  | 23
    # 22 @  9        |  |  |  |  |  |  |  |  | 22
    # 10 @  5        |  |  |  |  | 10
    # 08 @  5        |  |  |  |  | 8
    # 05 @  3        |  |  | 5
    # 02 @  1        | 2
    # 01 @  1        | 1
    # 00 @  0       0


if False:
    # -------------------------------------
    # - example 2-18. given a test score,
    #   grade returns the corresponding letter grade
    import bisect # array bisection algorithm

    def grade(score, breakpoints=[60, 70, 80, 90], grades='FDCBA'):
        i = bisect.bisect(breakpoints, score)
        return grades[i]

    scores = [33, 99, 77, 70, 89, 90, 100]
    grades = [grade(score) for score in scores]
    print('----- -----')
    print('score grade')
    print('----- -----')
    fmt = '{:5d} {:>5s}'
    for score, grade in zip(scores, grades):
        #print('{:3d} ---> {}'.format(score, grade))
        print(fmt.format(score, grade))
    print('----- -----')
    # ----- -----
    # score grade
    # ----- -----
    #    33     F
    #    99     A
    #    77     C
    #    70     C
    #    89     B
    #    90     A
    #   100     A
    # ----- -----

if False:
    # -------------------------------------
    # - inserting with bisect.insort
    # ; insort(seq, item) inserts item into seq so as to keep seq
    #   in ascending order.
    import bisect
    import random

    SIZE = 7
    random.seed(1729)

    bucket = []
    for i in range(SIZE):
        item = random.randrange(SIZE*2)
        bisect.insort(bucket, item)
        print('%2d inserted, bucket ->' % item, bucket)
    # ----------------------------------------------
    # *** sorted order maintained ***
    # 10 inserted, bucket -> [10]
    #  0 inserted, bucket -> [0, 10]
    #  6 inserted, bucket -> [0, 6, 10]
    #  8 inserted, bucket -> [0, 6, 8, 10]
    #  7 inserted, bucket -> [0, 6, 7, 8, 10]
    #  2 inserted, bucket -> [0, 2, 6, 7, 8, 10]
    # 10 inserted, bucket -> [0, 2, 6, 7, 8, 10, 10]
    # ----------------------------------------------

if False:
    # -------------------------------------
    # - use proper data type according to your specific purpose
    # ; list - flexible
    # ; array.array - memory efficient
    # ; deque - fifo operations(push/pop)
    # ; set - fast membership checking
    pass

if False:
    # -------------------------------------
    # - class array.array(typecode[, initializer])
    # ; efficient arrays of numeric values
    # ; an object type which can compactly represent an array of basic values
    #   -> characters, integers, floating point numbers
    # ; use this special container if something special is required
    # - random.random()
    # ; return the next random floating point number in the range [0.0, 1.0)
    import array
    import random; random.seed(1729)
    SIZE = 16

    doubles_0 = array.array('d', (random.random() for i in range(SIZE)))
    #                            --------------------------------------
    #                                     generator expression

    print('\n- doubles_0')
    for i, value in enumerate(doubles_0):
        print("value[{}]= {}".format(i, value))
    # - doubles_0
    # value[0]= 0.9963723767827669
    # value[1]= 0.8848200965298146
    # value[2]= 0.4107983745731689
    # value[3]= 0.45771949119610766
    # value[4]= 0.6672344063086454
    # value[5]= 0.18251911452417136
    # value[6]= 0.29217588543820794
    # value[7]= 0.3630932932632249
    # value[8]= 0.8671459725962595
    # value[9]= 0.2076513315470634
    # value[10]= 0.8289947875089807
    # value[11]= 0.15602920092468964
    # value[12]= 0.7308024134384177
    # value[13]= 0.4997260049413905
    # value[14]= 0.6133376468495829
    # value[15]= 0.3703879594514147
    

    # writing to a file
    filename = "doubles.dat"
    with open(filename, 'wb') as outfile:
        print("\n[info] writing {} ...".format(filename))
        doubles_0.tofile(outfile)

    # reading from a file
    doubles_1 = array.array('d')
    with open(filename, 'rb') as infile:
        print("\n[info] reading {} ...".format(filename))
        doubles_1.fromfile(infile, SIZE) # fast!

    print('\n- doubles_1')
    for i, value in enumerate(doubles_1):
        print("value[{}]= {}".format(i, value))
    # - doubles_1
    # value[0]= 0.9963723767827669
    # value[1]= 0.8848200965298146
    # value[2]= 0.4107983745731689
    # value[3]= 0.45771949119610766
    # value[4]= 0.6672344063086454
    # value[5]= 0.18251911452417136
    # value[6]= 0.29217588543820794
    # value[7]= 0.3630932932632249
    # value[8]= 0.8671459725962595
    # value[9]= 0.2076513315470634
    # value[10]= 0.8289947875089807
    # value[11]= 0.15602920092468964
    # value[12]= 0.7308024134384177
    # value[13]= 0.4997260049413905
    # value[14]= 0.6133376468495829
    # value[15]= 0.3703879594514147

    print("\n[info] doubles_0 == doubles_1 -->", doubles_0 == doubles_1) # True
    print("\n[info] doubles_0.typecode =", doubles_0.typecode) # d (double)

    # sorting
    doubles_2 = array.array(doubles_1.typecode, sorted(doubles_1))
    print('\n- sorted(doubles_1)')
    for i, value in enumerate(doubles_2):
        print("value[{:2d}] = {}".format(i, value))
    # - sorted(doubles_1)
    # value[ 0] = 0.15602920092468964
    # value[ 1] = 0.18251911452417136
    # value[ 2] = 0.2076513315470634
    # value[ 3] = 0.29217588543820794
    # value[ 4] = 0.3630932932632249
    # value[ 5] = 0.3703879594514147
    # value[ 6] = 0.4107983745731689
    # value[ 7] = 0.45771949119610766
    # value[ 8] = 0.4997260049413905
    # value[ 9] = 0.6133376468495829
    # value[10] = 0.6672344063086454
    # value[11] = 0.7308024134384177
    # value[12] = 0.8289947875089807
    # value[13] = 0.8671459725962595
    # value[14] = 0.8848200965298146
    # value[15] = 0.9963723767827669


if False:
    # -------------------------------------
    # - memoryview
    # ; built-in core library
    # ; memoryview objects allow python code to access the internal data of
    #   an object that supports the buffer protocol without copying.
    #
    # - class memoryview(object)
    # ; return a "memory view" object created from the given argument
    import array
    octets = array.array('B', range(6))
    print("\noctets=", octets)
    # octets= array('B', [0, 1, 2, 3, 4, 5])

    m1 = memoryview(octets) 
    m1.tolist()
    print("\nm1=", m1)
    print("len(m1)=", len(m1))
    print("m1.format=", m1.format)
    print("m1.itemsize=", m1.itemsize)
    print("m1.tolist()=", m1.tolist())
    # m1= <memory at 0x0000022727E56500>
    # len(m1)= 6
    # m1.format= B
    # m1.itemsize= 1
    # m1.tolist()= [0, 1, 2, 3, 4, 5]

    m2 = m1.cast('B', [2, 3]) 
    print("\nm2=", m2)
    print("len(m2)=", len(m2))
    print("m2.format=", m2.format)
    print("m2.itemsize=", m2.itemsize)
    print("m2.tolist()=", m2.tolist())
    # m2= <memory at 0x00000257D396C790>
    # len(m2)= 2
    # m2.format= B
    # m2.itemsize= 1
    # m2.tolist()= [[0, 1, 2],
    #               [3, 4, 5]]

    m3 = m1.cast('B', [3, 2]) 
    print("\nm3=", m3)
    print("len(m3)=", len(m3))
    print("m3.format=", m3.format)
    print("m3.itemsize=", m3.itemsize)
    print("m3.tolist()=", m3.tolist())
    # m3= <memory at 0x0000019CD986A5A0>
    # len(m3)= 3
    # m3.format= B
    # m3.itemsize= 1
    # m3.tolist()= [[0, 1],
    #               [2, 3],
    #               [4, 5]]

    # memories are shared amoing octets, m1, m2 and m3!
    m2[1,1] = 22 # 4 -> 22
    m3[1,1] = 33 # 3 -> 33

    print("\noctets=", octets)
    # octets= array('B', [0, 1, 2, 33, 22, 5])


if False:
    # -------------------------------------
    # - memoryview example
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
    #                                            |

    byteview[5] = 4 # [note] this will modify 'numbers'!
    print("numbers=", numbers)
    # numbers= array('h', [-2, -1, 1024, 1, 2])

    for item in byteview:
        print(f'{item:08b}')


if False:
    # -------------------------------------
    # - deques and other queues
    # the following is ok, but very inefficient on pop(0).
    # don't implement queue using 'list' built-in type.
    queue = list(); print("queue=", queue)
    queue.append(0); print("queue=", queue)
    queue.append(1); print("queue=", queue)
    queue.append(2); print("queue=", queue)
    queue.append(3); print("queue=", queue)
    queue.append(4); print("queue=", queue)
    queue.pop(0); print("queue=", queue)
    queue.pop(0); print("queue=", queue) # --------------------------------------
    queue.pop(0); print("queue=", queue) # inserting and removing from the head
    queue.pop(0); print("queue=", queue) # of a list (the 0-index end) is costly!
    queue.pop(0); print("queue=", queue) # --------------------------------------
    # queue= []
    # queue= [0]
    # queue= [0, 1]
    # queue= [0, 1, 2]
    # queue= [0, 1, 2, 3]
    # queue= [0, 1, 2, 3, 4]
    # queue= [1, 2, 3, 4]
    # queue= [2, 3, 4]
    # queue= [3, 4]
    # queue= [4]
    # queue= []

    print()

    # -------------------------------------
    # - class collections.deque([iterable[, maxlen]])
    # ; list-like container with fast appends and pops on either end
    #   (doubly-linked-list)
    # ; returns a new deque object initialized left-to-right (using append())
    #   with data from iterable.
    # ; if iterable is not specified, the new deque is empty.
    # ; if maxlen is not specified or is none, deques may grow to an arbitrary length.
    #   otherwise, the deque is bounded to the specified maximum length.
    # ; when new items are added and the queue is full, the oldest item is
    #   automatically removed(when maxlen is specified)
    # ; problem of built-in list
    #   -> inserting and removing from the left of a list is costly(not efficient)
    #     (the 0-index end using pop(0))
    # ; double-ended queue (doubly linked-list)
    # ; append(x) and appendleft(x)
    #   add x to the right(left) side of the deque.
    # ; extend(iterable) and extendleft(iterable)
    #   extend the right side of the deque by appending elements from the iterable argument.
    # ; pop() and popleft()
    #   remove and return an element from the right(left) side of the deque.
    import collections
    queue = collections.deque(range(10), maxlen=10); print("queue=", queue) # fixed-size
    # queue= deque([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], maxlen=10)

    queue.rotate(3); print("queue=", queue)
    # queue= deque([7, 8, 9, 0, 1, 2, 3, 4, 5, 6], maxlen=10)

    queue.rotate(-4); print("queue=", queue)
    # queue= deque([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], maxlen=10)

    queue.appendleft(-1); print("queue=", queue)
    # queue= deque([-1, 1, 2, 3, 4, 5, 6, 7, 8, 9], maxlen=10)

    queue.extend([11, 22, 33]); print("queue=", queue)
    # queue= deque([3, 4, 5, 6, 7, 8, 9, 11, 22, 33], maxlen=10)

    queue.extendleft([10, 20, 30, 40]); print("queue=", queue)
    # queue= deque([40, 30, 20, 10, 3, 4, 5, 6, 7, 8], maxlen=10)


if False:
    # ------------------------------------------------------------------------
    # - numpy
    # ; implements multi-dimensional, homogeneous arrays and matrix types that
    #   hold not only numbers but also user-defined records, and provides
    #   efficient elementwise operations.
    # - scipy
    # ; written on top of NumPy, offering many scientific computing algorithms
    #   from linear algebra, numerical calculus, and statistics
    # ------------------------------------------------------------------------
    pass


# -------------------------------------
# chapter 3: dictionaries and sets
#
# - mapping type inheritance hierarchy
#
#   MutableMapping (__setitem__, __delitem__, clear, pop
#             |              popitem, setdefault, update)
#             |
#             +--- Mapping (__getitem__, __contains__, __eq__, __ne__,
#                     |                      get, items, keys, values)
#                     |
#                     +--- Container (__contains__)
#                     |
#                     +--- Iterable (__iter__)
#                     |
#                     +--- Container (__len__)
#
#   MutableSet (__ior__, __iand__, __ixor__, __isub__
#          |         add, discard, remove, pop, clear)
#          |
#          +--- Set (__le__, __lt__, __gt__, __ge__, __eq__, __ne__
#                |    __and__, __or__, __sub__, __xor__, isdisjoint)
#                |
#                +--- Container (__contains__)
#                |
#                +--- Iterable (__iter__)
#                |
#                +--- Container (__len__)
#
# - common mapping types
# ; dict, collections.defaultdict, collections.OrderedDict


if False:
    # -------------------------------------
    # - dictcomp(dict comprehension)
    # ; curly-braces used
    import pprint
    dial_codes = [
        (86, 'China'),
        (91, 'India'),
        (1, 'United States'),
        (62, 'Indonesia'),
        (55, 'Brazil'),
        (92, 'Pakistan'),
        (880, 'Bangladesh'),
        (234, 'Nigeria'),
        (7, 'Russia'),
        (81, 'Japan'),
    ] # -> list of tuples

    table = {country: code for code, country in dial_codes}
    print("\ntype(table)=", type(table)) # type(key)=str
    print("table=")
    pprint.pprint(table)
    # table=
    # {'Bangladesh': 880,
    #  'Brazil': 55,
    #  'China': 86,
    #  'India': 91,
    #  'Indonesia': 62,
    #  'Japan': 81,
    #  'Nigeria': 234,
    #  'Pakistan': 92,
    #  'Russia': 7,
    #  'United States': 1}

    if 'Brazil' in table: # containment(membership) test
        print("\nBrazil found")
    else:
        print("\nBrazil not found")
    # Brazil found

    if 'Korea' in table: # containment(membership) test
        print("\nKorea found")
    else:
        print("\nKorea not found")
    # Korea not found

    # dictcomp with conditional filtering
    table = {code: country.upper()
                for country, code in sorted(table.items()) if code < 66}
    print("\ntype(table)=", type(table)) # type(key)=int
    print("table=")
    pprint.pprint(table)
    # {1: 'UNITED STATES', 7: 'RUSSIA', 55: 'BRAZIL', 62: 'INDONESIA'}


if False:
    # -------------------------------------
    # - unpacking mappings
    # ; references
    #   4.8.4. arbitrary argument lists
    #   4.8.5. unpacking argument lists
    def dump(**kwargs):
        print("\ntype(kwargs)=", type(kwargs))
        print("kwargs=", kwargs)

    dump(**{'x': 1}, y=2, **{'z': 3})
    # type(kwargs)= <class 'dict'>
    # kwargs= {'x': 1, 'y': 2, 'z': 3}

    table = {'a': 0, **{'x': 1}, 'y': 2, **{'z': 3, 'x': 4}}
    #                ----------          ------------------
    #                unpacking                unpacking

    print("\ntable=", table)
    # table= {'a': 0, 'x': 4, 'y': 2, 'z': 3}
    #                 ------
    #             duplicate item -> later one overrides!


if False:
    # -------------------------------------
    # - merging mappings(dict) with '|' or '|='
    d1= {'dwzca': 50, 'cwjxm': 91, 'iexon': 75, 'ymnae': 57, 'gisnx': 36}
    d2= {'bsyrc': 34, 'swqid': 57, 'uqubh': 78, 'pfsxn': 30, 'spiea': 98}
    print("\nd1=", d1)
    print("d2=", d2)
    # d1= {'dwzca': 50, 'cwjxm': 91, 'iexon': 75, 'ymnae': 57, 'gisnx': 36}
    # d2= {'bsyrc': 34, 'swqid': 57, 'uqubh': 78, 'pfsxn': 30, 'spiea': 98}
    
    if False:
        # -------------------------------------
        # 1) crude(brute-force) way
        combined = dict()
        for key, val in d1.items():
            combined[key] = val
        for key, val in d2.items():
            combined[key] = val
    
        print("\ncombined=", len(combined))
        pprint.pprint(combined)
        # combined= 10
        # {'bsyrc': 34,
        #  'cwjxm': 91,
        #  'dwzca': 50,
        #  'gisnx': 36,
        #  'iexon': 75,
        #  'pfsxn': 30,
        #  'spiea': 98,
        #  'swqid': 57,
        #  'uqubh': 78,
        #  'ymnae': 57}
    
    if False:
        # -------------------------------------
        # 2) using itertools.chain()
        import itertools
        combined = dict()
        for key, val in itertools.chain(d1.items(), d2.items()):
            combined[key] = val
    
        print("\ncombined=", len(combined))
        pprint.pprint(combined)
        # combined= 10
        # {'bsyrc': 34,
        #  'cwjxm': 91,
        #  'dwzca': 50,
        #  'gisnx': 36,
        #  'iexon': 75,
        #  'pfsxn': 30,
        #  'spiea': 98,
        #  'swqid': 57,
        #  'uqubh': 78,
        #  'ymnae': 57}
    
    if False:
        # -------------------------------------
        # 3) using dict.update() method
        # - update([other])
        # ; update the dictionary with the key/value pairs from other,
        #   overwriting existing keys. return none.
        combined = d1.copy() # shallow copy
        combined.update(d2)
    
        print("\ncombined=", len(combined))
        pprint.pprint(combined)
        # combined= 10
        # {'bsyrc': 34,
        #  'cwjxm': 91,
        #  'dwzca': 50,
        #  'gisnx': 36,
        #  'iexon': 75,
        #  'pfsxn': 30,
        #  'spiea': 98,
        #  'swqid': 57,
        #  'uqubh': 78,
        #  'ymnae': 57}
    
    if False:
        # -------------------------------------
        # 4) using unpacking operator **
        combined = { **d1, **d2 }
    
        print("\ncombined=", len(combined))
        pprint.pprint(combined)
        # combined= 10
        # {'bsyrc': 34,
        #  'cwjxm': 91,
        #  'dwzca': 50,
        #  'gisnx': 36,
        #  'iexon': 75,
        #  'pfsxn': 30,
        #  'spiea': 98,
        #  'swqid': 57,
        #  'uqubh': 78,
        #  'ymnae': 57}
    
    if False:
        # -------------------------------------
        # 5) using collections.ChainMap
        # - class collections.ChainMap(*maps)
        # ; a ChainMap groups multiple dicts or other mappings together to create
        #   a single, updateable view.
        import collections
        combined = dict(collections.ChainMap(d1, d2))
        #               ----------------------------
        #                     ChainMap object
    
        print("\ncombined=", len(combined))
        pprint.pprint(combined)
        # combined= 10
        # {'bsyrc': 34,
        #  'cwjxm': 91,
        #  'dwzca': 50,
        #  'gisnx': 36,
        #  'iexon': 75,
        #  'pfsxn': 30,
        #  'spiea': 98,
        #  'swqid': 57,
        #  'uqubh': 78,
        #  'ymnae': 57}
    
    if False:
        # -------------------------------------
        # 5) unpacking the 2nd dict
        # ; works only when the key of 2nd dict are string!
        combined = dict(d1, **d2)
    
        print("\ncombined=", len(combined))
        pprint.pprint(combined)
        # combined= 10
        # {'bsyrc': 34,
        #  'cwjxm': 91,
        #  'dwzca': 50,
        #  'gisnx': 36,
        #  'iexon': 75,
        #  'pfsxn': 30,
        #  'spiea': 98,
        #  'swqid': 57,
        #  'uqubh': 78,
        #  'ymnae': 57}
    
    if False:
        # -------------------------------------
        # 5) using the merge operator '|' or '|='
        # ; similar to union operation of set
        combined = d1.copy()
        combined |= d2
    
        print("\ncombined=", len(combined))
        pprint.pprint(combined)
        # combined= 10
        # {'bsyrc': 34,
        #  'cwjxm': 91,
        #  'dwzca': 50,
        #  'gisnx': 36,
        #  'iexon': 75,
        #  'pfsxn': 30,
        #  'spiea': 98,
        #  'swqid': 57,
        #  'uqubh': 78,
        #  'ymnae': 57}


if False:
    # -------------------------------------
    # - pattern matching with mappings
    # ; match instances of any actual or virtual subclass of
    #   collections.abc.Mapping
    # ; the order of the keys in the patterns is irrelevant!
    # ; mapping patterns succeed on partial matches
    def get_creators(record: dict) -> list:
        match record:
            case {'type': 'book', 'api': 2, 'authors': [*names]}:
                return names
            case {'type': 'book', 'api': 1, 'author': name}:
                return [name]
            case {'type': 'book'}:
                raise ValueError(f"Invalid 'book' record: {record!r}")
            case {'type': 'movie', 'director': name}:
                return [name]
            case _:
                raise ValueError(f'Invalid record: {record!r}')

    b1 = dict(api=1, author='Douglas Hofstadter', type='book', title='Gödel, Escher, Bach')
    result = get_creators(b1)
    print("result(1)=", result)
    # result(1)= ['Douglas Hofstadter']

    from collections import OrderedDict
    b2 = OrderedDict(
        api=2, type='book', title='Python in a Nutshell',
        authors='Martelli Ravenscroft Holden'.split())
    result = get_creators(b2)
    print("result(2)=", result)
    # result(2)= ['Martelli', 'Ravenscroft', 'Holden']

    b3 = {'type': 'book', 'pages': 770}
    try:
        result = get_creators(b3)
    except Exception as err:
        print("[err ] something's wrong!")
        print(" message= ", err)
    else:
        print("result(3)=", result)
    # [err ] something's wrong!
    # message=  Invalid 'book' record: {'type': 'book', 'pages': 770}

    b4 = 'Spam, spam, spam'
    try:
        result = get_creators(b4)
    except Exception as err:
        print("[err ] something's wrong!")
        print(" message= ", err)
    else:
        print("result(4)=", result)
    # [err ] something's wrong!
    # message=  Invalid record: 'Spam, spam, spam'

    # - capturing extra key-value pairs!
    def get_creators(record: dict) -> list:
        match record:
            case {'type': 'book', 'api': 2, 'authors': [*names]}:
                return names
            case {'type': 'book', 'api': 1, 'author': name}:
                return [name]
            case {'type': 'book'}:
                raise ValueError(f"Invalid 'book' record: {record!r}")
            case {'type': 'movie', 'director': name}:
                return [name]
            case _:
                raise ValueError(f'Invalid record: {record!r}')


if False:
    # -------------------------------------
    # - isinstance(object, classinfo)
    # - checking if a data satisfies the criteria for mapping type
    # ; return true if the object argument is an instance of the classinfo
    #   argument, or of a (direct, indirect, or virtual) subclass thereof.
    # ; if classinfo is a tuple of type objects (or recursively, other such
    #   tuples) or a union type of multiple types, return true if object is
    #   an instance of any of the types.
    import collections.abc
    data = {'dwzca': 50, 'cwjxm': 91, 'iexon': 75, 'ymnae': 57, 'gisnx': 36}

    if isinstance(data, collections.abc.Mapping):
        print("data is a collections.abc.Mapping!")
    # data is a collections.abc.Mapping!

    if isinstance(data, collections.abc.MutableMapping):
        print("data is a collections.abc.MutableMapping!")
    # data is a collections.abc.MutableMapping!


if False:
    # -------------------------------------
    # - hashable
    # ; an object is hashable
    #   (1) if it has a hash value which never changes during its lifetime
    #       (it needs a __hash__() method)
    #   (2) can be compared to other objects (it needs an __eq__() method)
    #   (3) hashable objects which compare equal must have the same hash value.
    #       'if a == b' -> hash(a) == hash(b)
    # ; the atomic immutable types (str, bytes, numeric types) are all hashable. a
    #   frozen set is always hashable, because its elements must be hashable by
    #   definition.
    # ; a tuple is hashable only if all its items are hashable.
    # ; user-defined types are hashable by default because
    #   (1) hash(obj) returns id(obj)
    #   (2) __eq__() is inherited from 'object' class
    tt = (1, 2, (30, 40))
    try:
        hval = hash(tt)
    except Exception as err:
        print("[err ] something's wrong!")
        print(" message= ", err)
    else:
        print("hval(1)=", hval)
    # hval(1)= -3907003130834322577

    tl = (1, 2, [30, 40])
    try:
        hval = hash(tl)
    except Exception as err:
        print("[err ] something's wrong!")
        print(" message= ", err)
    else:
        print("hval(2)=", hval)
    # [err ] something's wrong!
    #  message=  unhashable type: 'list'

    tf = (1, 2, frozenset([30, 40]))
    try:
        hval = hash(tf)
    except Exception as err:
        print("[err ] something's wrong!")
        print(" message= ", err)
    else:
        print("hval(3)=", hval)
    # hval(3)= 5149391500123939311


if False:
    # ---------------------------------------------------------------------
    # - handling missing keys
    # (1) d[key]
    # ; return the item of d with key key.
    # ; raises a KeyError if key is not in the map.
    # (2) get(key[, default])
    # ; return the value for key if key is in the dictionary, else default.
    # ; if default is not given, it defaults to None,
    #   so that this method never raises a KeyError.
    # ---------------------------------------------------------------------
    table = dict(aaa = 0, bbb = 1, ccc = 2, ddd = 3, eee = 4)

    # dict.get() method
    print("table.get('aaa',None)=", table.get('aaa',None))
    print("table.get('bbb',None)=", table.get('bbb',None))
    print("table.get('fff',None)=", table.get('fff',None)) # None
    # table.get('aaa',None)= 0
    # table.get('bbb',None)= 1
    # table.get('fff',None)= None


if False:
    # ---------------------------------------------------------------------
    # - handling missing key with dict.get()
    # - get(key[, default])
    # ; return the value for key if key is in the dictionary, else default.
    # ; if default is not given, it defaults to none,
    #   so that this method never raises a KeyError.
    # ---------------------------------------------------------------------
    import re

    lookup_table = {}
    filename = "input.txt"
    with open(filename, 'r', encoding='utf-8') as infile:
        print(f"[info] reading {filename} ...")
        for lineno, line in enumerate(infile, 1):
            print("reading line", lineno)
            if not line: continue
            if line.isspace(): continue
            if line.startswith('#'): continue

            for match in re.finditer('\w+', line):
                word = match.group()
                location = (lineno, match.start()+1)
                #           lineno      column
                occurrences = lookup_table.get(word, []) # missing -> empty list
                occurrences.append(location)
                lookup_table[word] = occurrences
            #   ------------------
            #   entails a second search! not efficient?

    for word in sorted(lookup_table, key=str.upper):
        print("word=", word, "location=", lookup_table[word])

if False:
    # ----------------------------------------------------------------
    # - handling missing key in a dictionary using dict.setdefault()
    # - dict.setdefault(key[, default])
    # ; if key is in the dictionary, return its value.
    # ; if not, insert key with a value of default and return default.
    # ; default defaults to None.
    # ----------------------------------------------------------------
    import re

    lookup_table = {} # built-in dict
    fileName = "input.txt"
    with open(fileName, 'r', encoding='utf-8') as inFile:
        print("[info] reading", fileName, "...")
        for lineno, line in enumerate(inFile, 1):
            print("reading line", lineno)
            if not line: continue
            if line.isspace(): continue
            if line.startswith('#'): continue

            for match in re.finditer('\w+', line):
                word = match.group()
                location = (lineno, match.start()+1)
                lookup_table.setdefault(word, []).append(location)
                # -----------------------------------
                # *** same as the following ***
                # if word not in lookup_table:
                #     lookup_table[word] = []
                # lookup_table[word].append(location)
                # -----------------------------------

    for word in sorted(lookup_table, key=str.upper):
        print("word=", word, "location=", lookup_table[word])


if False:
    # -------------------------------------------------------------------------
    # - automatic handling of missing keys - (1)
    # ; handling missing key in a dictionary using collections.defaultdict
    # ; 'defaultdict.__missing__' will take care of everything upon missing
    #   key for d[k]
    # - class collections.defaultdict(default_factory=None, /[, ...])
    # ; dict subclass that calls a factory function to supply missing values
    # ; default_factory
    #   a callable
    #   this attribute is used by the __missing__() method; it is initialized
    #   from the first argument to the constructor, if present, or to none, if
    #   absent.
    # ; [important] handling missing key happens for only __getitem__! <-- data[key]
    #   'data.get[key]' and 'key in data' don't invoke __getitem__!!!
    # -------------------------------------------------------------------------
    import collections
    import re
    regex = re.compile('\w+') # regular expression

    lookup_table = collections.defaultdict(list)
    #                                      ----
    #                                      callable object(function)
    #                                      that produces default value
    #                                      (default_factory=list)
    fileName = "input.txt"
    with open(fileName, 'r', encoding='utf-8') as inFile:
        print("[info] reading", fileName, "...")
        for lineno, line in enumerate(inFile, 1):
            print("reading line", lineno)
            if not line: continue
            if line.isspace(): continue
            if line.startswith('#'): continue

            for match in re.finditer('\w+', line):
                word = match.group()
                location = (lineno, match.start()+1)
                lookup_table[word].append(location) # simpler!

    for word in sorted(lookup_table, key=str.upper):
        print("word=", word, "location=", lookup_table[word])

if False:
    # --------------------------------------------------------------------
    # - automatic handling of missing keys - (2)
    # ; __missing__() method
    # ; inherited from built-in 'dict'
    # ; standard dict.__getitem__ will call __missing__ whenever a key is
    #   not found, instead of raising KeyError.
    # ; the following StrKeyDict0 will support both str and int keys.
    # --------------------------------------------------------------------
    class StrKeyDict0(dict):

        def __missing__(self, key):
            """
            dict.__getitem__() will invoke this
            upon missing key"""
            if isinstance(key, str):
                raise KeyError(key)
                # ; 'key' not exists really!
                # ; handle as usual if the key is 'str' type,
                #   else convert non-str key to str key
                # ; infinite recursion happens without this test

            return self[str(key)]
            # this will raise exception upon non-existing key!

        def get(self, key, default=None):
            try:
                return self[key]
                # -> delegates to __getitem__
                # not found -> __missing__() -> KeyError can be raised
            except KeyError:
                return default

        def __contains__(self, key):
            """
            'key in data' doesn't fall back to __missing__!
            without this, integer indexing doesn't work!
            """
            return key in self.keys() or str(key) in self.keys()

    table = StrKeyDict0([('2', 'two'), ('4', 'four')])
    table['3'] = 'three' # ok
    table[5] = 'five' # ok

    print("table=", table)
    # table= {'2': 'two', '4': 'four', '3': 'three', 5: 'five'}

    print(table['2']) # two
    print(table[4]) # four

    # testing 'in' operator
    print("2 in table :", 2 in table)
    print("1 in table :", 1 in table)
    # 2 in table : True
    # 1 in table : False

    print("table.get(1)=", table.get(1)) # using StrKeyDict0.get()
    # table.get(1)= None

    # using StrKeyDict0.__getitem__ & __missing__
    print("table[1]=", table[1])
    # raise KeyError(key) -> KeyError: '1'


if False:
    # ------------------------------------------------------------------
    # - subclassing(inheriting) 'collections.UserDict'
    # ; can handle missing key using both d[k] and d.get(k)
    #   ('d[k] = val' invokes __setitem__)
    # ; inheriting 'dict' directly requires several methods overriding
    #   -> cumbersome!
    # ; 'collections.UserDict' is more convenient
    # ; UserDict does not inherit from 'dict' (different implementation)
    # ; 'data' member for another dict implementation
    # ; full-fledged mapping type inheritted from MutableMapping ABC
    # ;  __missing__ method
    #    can customize what happens when a key is not found when using the
    #    d[k] syntax that invokes __getitem__
    # - reference
    # ; https://github.com/fluentpython/example-code-2e/blob/master/03-dict-set/missing.py
    # ------------------------------------------------------------------
    import collections

    #for i, attr in enumerate(sorted(dir(collections.UserDict))):
    #    print(f'attr[{i}]= {attr}')

    class StrKeyDict(collections.UserDict):
        def __missing__(self, key): # same missing key handling
            if isinstance(key, str):
                raise KeyError(key)
            return self[str(key)]

        def __contains__(self, key):
            return str(key) in self.data # simpler

        def __setitem__(self, key, item):
            self.data[str(key)] = item
            #         --------
            #         guarantees all keys are string!

    table = StrKeyDict([('2', 'two'), ('4', 'four')])
    table['3'] = 'three' # ok
    table[5] = 'five' # ok

    print("type(table.data)=", type(table.data))
    # type(table.data)= <class 'dict'>

    print("table=", table)
    # table= {'2': 'two', '4': 'four', '3': 'three', '5': 'five'}

    print(table['2']) # two
    print(table[4]) # four

    # testing 'in' operator
    print("2 in table :", 2 in table) # True
    print("1 in table :", 1 in table) # False

    # using StrKeyDict0.get()
    print("table.get(1)=", table.get(1)) # None

    # using StrKeyDict0.__getitem__ --> __missing__
    print("table[1]=", table[1])
    # raise KeyError(key) -> KeyError: '1'


if False:
    # -------------------------------------
    # - collections.OrderedDict
    # ; key orders are kept in 'dict' since python 3.6
    # ; only good for handling frequent reordering operations
    # ; no reason to use collections.OrderedDict except for backward
    #   compatibility!
    pass


if False:
    # -------------------------------------
    # - class collections.ChainMap(*maps)
    # ; a ChainMap groups multiple dicts or other mappings together to create
    #   a single, updateable view.
    import collections
    import pprint

    d1 = {'dwzca': 50, 'cwjxm': 91, 'iexon': 75, 'ymnae': 57, 'gisnx': 36}
    d2 = {'bsyrc': 34, 'swqid': 57, 'uqubh': 78, 'pfsxn': 30, 'spiea': 98}

    combined_view = collections.ChainMap(d1, d2)
    print("\ncombined_view=")
    pprint.pprint(combined_view)
    # combined_view=
    # ChainMap({'cwjxm': 91, 'dwzca': 50, 'gisnx': 36, 'iexon': 75, 'ymnae': 57},
    #          {'bsyrc': 34, 'pfsxn': 30, 'spiea': 98, 'swqid': 57, 'uqubh': 78})

    for i, (key, val) in enumerate(combined_view.items()):
        print(f"[{i}]: key= {key}, value= {val}")
    # [0]: key= bsyrc, value= 34
    # [1]: key= swqid, value= 57
    # [2]: key= uqubh, value= 78
    # [3]: key= pfsxn, value= 30
    # [4]: key= spiea, value= 98
    # [5]: key= dwzca, value= 50
    # [6]: key= cwjxm, value= 91
    # [7]: key= iexon, value= 75
    # [8]: key= ymnae, value= 57
    # [9]: key= gisnx, value= 36

    combined_view['uqubh'] = -999 # modifiying view affects the first one!

    print("\ncombined_view=")
    pprint.pprint(combined_view)
    # combined_view=
    # ChainMap({'cwjxm': 91, 'dwzca': 50, 'gisnx': 36, 'iexon': 75, 'uqubh': -999, 'ymnae': 57},
    #          {'bsyrc': 34, 'pfsxn': 30, 'spiea': 98, 'swqid': 57, 'uqubh': 78})
    #
    # [note]
    # updates or insertions to a chainmap only affect the first input mapping!

    for i, (key, val) in enumerate(combined_view.items()):
        print(f"[{i}]: key= {key}, value= {val}")
    # [0]: key= bsyrc, value= 34
    # [1]: key= swqid, value= 57
    # [2]: key= uqubh, value= -999
    # [3]: key= pfsxn, value= 30
    # [4]: key= spiea, value= 98
    # [5]: key= dwzca, value= 50
    # [6]: key= cwjxm, value= 91
    # [7]: key= iexon, value= 75
    # [8]: key= ymnae, value= 57
    # [9]: key= gisnx, value= 36


if False:
    # -------------------------------------
    # - example of using ChainMap
    import collections
    import builtins
    import pprint
    lookup = collections.ChainMap(locals(), globals(), vars(builtins))
    pprint.pprint(lookup)


if False:
    # -------------------------------------
    # - class collections.Counter([iterable-or-mapping])
    # ; a counter is a dict subclass for counting hashable objects. it is a
    #   collection where elements are stored as dictionary keys and their counts
    #   are stored as dictionary values.
    # ; can be used for a multiset with item counts
    import collections
    counter = collections.Counter('abracadabra')
    print("counter=", counter)
    # counter= Counter({'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1})

    counter.update('aaaaazzz')

    print("counter=", counter)
    # counter= Counter({'a': 10, 'z': 3, 'b': 2, 'r': 2, 'c': 1, 'd': 1})

    print("most_common(3)=", counter.most_common(3))
    # most_common(3)= [('a', 10), ('z', 3), ('b', 2)]

    print("list(elements())=", list(counter.elements()))
    # list(elements())= ['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'b', 'b', 'r', 'r', ' c', 'd', 'z', 'z', 'z']

    print("total()=", counter.total())
    # total()= 19


if False:
    # -------------------------------------
    # - shelve — python object persistence
    # ; a "shelf" is a persistent, dictionary-like object. the difference with
    #   "dbm" databases is that the values (not the keys!) in a shelf can be
    #   essentially arbitrary python objects
    pass


if False:
    # -------------------------------------
    # - class types.MappingProxyType(mapping)
    # ; read-only proxy of a mapping. it provides a dynamic view on the
    #   mapping's entries, which means that when the mapping changes, the view
    #   reflects these changes.
    import types
    import pprint

    lookup = {
        'dwzca': 50, 'cwjxm': 91, 'iexon': 75, 'ymnae': 57, 'gisnx': 36,
        'bsyrc': 34, 'swqid': 57, 'uqubh': 78, 'pfsxn': 30, 'spiea': 98
    }
    print("lookup=")
    pprint.pprint(lookup)
    # lookup=
    # {'bsyrc': 34, 'cwjxm': 91, 'dwzca': 50, 'gisnx': 36, 'iexon': 75,
    #  'pfsxn': 30, 'spiea': 98, 'swqid': 57, 'uqubh': 78, 'ymnae': 57}

    proxy = types.MappingProxyType(lookup)
    print("proxy=")
    pprint.pprint(proxy)
    # proxy=
    # mappingproxy({'bsyrc': 34, 'cwjxm': 91, 'dwzca': 50, 'gisnx': 36, 'iexon': 75,
    #               'pfsxn': 30, 'spiea': 98, 'swqid': 57, 'uqubh': 78, 'ymnae': 57})

    lookup['xxxxx'] = 99
    pprint.pprint(proxy)
    # mappingproxy({'bsyrc': 34, 'cwjxm': 91, 'dwzca': 50, 'gisnx': 36, 'iexon': 75,
    #               'pfsxn': 30, 'spiea': 98, 'swqid': 57, 'uqubh': 78, 'xxxxx': 99,
    #               'ymnae': 57})

    proxy['yyyyy'] = 99
    # TypeError: 'mappingproxy' object does not support item assignment


if False:
    # -------------------------------------
    # - dictionary views
    # ; the objects returned by dict.keys(), dict.values() and dict.items()
    #   are view objects.
    lookup = {
        'dwzca': 50, 'cwjxm': 91, 'iexon': 75, 'ymnae': 57, 'gisnx': 36,
        'bsyrc': 34, 'swqid': 57, 'uqubh': 78, 'pfsxn': 30, 'spiea': 98
    }

    # view objects
    dict_keys = lookup.keys()
    dict_values = lookup.values()
    dict_items = lookup.items()

    print("\nbefore")
    print("dict_keys=", dict_keys, type(dict_keys))
    print("dict_values=", dict_values, type(dict_values))
    print("dict_items=", dict_items, type(dict_items))
    # dict_keys= dict_keys(
    #   ['dwzca', 'cwjxm', 'iexon', 'ymnae', 'gisnx', 'bsyrc', 'swqid',
    #   'uqubh', 'pfsxn', 'spiea']
    # )
    # dict_values= dict_values(
    #   [50, 91, 75, 57, 36, 34, 57, 78, 30, 98]
    # )
    # dict_items= dict_items(
    #   [('dwzca', 50), ('cwjxm', 91), ('iexon', 75), ('ymnae', 57), ('gisnx', 36),
    #    ('bsyrc', 34), ('swqid', 57), ('uqubh', 78), ('pfsxn', 30), ('spiea', 98)]
    # )

    lookup['xxxxx'] = 11
    lookup['yyyyy'] = 99

    print("\nafter")
    print("dict_keys=", dict_keys, type(dict_keys))
    print("dict_values=", dict_values, type(dict_values))
    print("dict_items=", dict_items, type(dict_items))
    # dict_keys= dict_keys(
    #   ['dwzca', 'cwjxm', 'iexon', 'ymnae', 'gisnx', 'bsyrc', 'swqid',
    #   'uqubh', 'pfsxn', 'spiea', 'xxxxx', 'yyyyy']
    # )
    # dict_values= dict_values(
    #   [50, 91, 75, 57, 36, 34, 57, 78, 30, 98, 11, 99]
    # )
    # dict_items= dict_items(
    #   [('dwzca', 50), ('cwjxm', 91), ('iexon', 75), ('ymnae', 57), ('gisnx', 36),
    #    ('bsyrc', 34), ('swqid', 57), ('uqubh', 78), ('pfsxn', 30), ('spiea', 98),
    #    ('xxxxx', 11), ('yyyyy', 99)]
    # )


if False:
    # --------------------------------------------------------------
    # - set & frozenset
    # ; unordered collection of distinct hashable objects
    # ; membership testing, removing duplicates from a sequence
    # ; computing mathematical operations
    # ; operations
    #   -> x in set, x not in set, len(set), for x in set
    #   -> intersection, union, difference, and symmetric difference
    #   -> left.isdisjoint(right)
    #   -> left <= right, left < right
    #   -> left >= right, left > right
    #   -> left | right, left.union(*right)
    #   -> left & right, left.intersection(*right)
    #   -> left - right, left.difference(*right)
    #   -> left ^ right, left.symmetric_difference(right)
    # - set
    # ; mutable -> add(), remove(), discard(), pop(), clear()
    # ; not hashable
    # - frozenset
    # ; immutable and hashable
    # ; only immutable operations are allowed
    # --------------------------------------------------------------
    import random
    import pprint
    haystack = [chr(random.randint(97, 122)) for _ in range(128)]
    needles = [chr(random.randint(97, 122)) for _ in range(17)]

    print("haystack=", len(haystack))
    pprint.pprint(haystack)
    print("needles=", len(needles))
    pprint.pprint(needles)
    # haystack= 128
    # ['u', 'a', 'u', 'g', 'k', 'i', 'r', 'm', 'u', 'x',
    #  'd', 'f', 'o', 'b', 'j', 'u', 'h', 'l', 'g', 'v',
    #  'q', 'b', 'l', 'f', 'a', 'd', 'k', 'z', 'n', 'h',
    #  'w', 'k', 'l', 'g', 'g', 't', 'k', 's', 'l', 'o',
    #  'a', 'j', 't', 'w', 'h', 'd', 'q', 'd', 'f', 'a',
    #  'a', 'g', 'f', 'i', 'n', 'w', 's', 'p', 'l', 'b',
    #  'w', 'd', 'h', 'o', 'p', 'h', 'f', 'x', 'u', 'o',
    #  'c', 'a', 'c', 'r', 'y', 's', 'b', 't', 'r', 'i',
    #  'l', 'm', 'b', 'o', 'm', 'f', 'j', 'i', 'k', 's',
    #  'b', 't', 'j', 'g', 'r', 'z', 'z', 'f', 'x', 'u',
    #  'y', 'f', 'x', 'h', 'o', 'f', 'h', 'x', 't', 'u',
    #  'n', 'w', 'y', 'j', 'b', 'd', 'm', 'r', 'l', 'r',
    #  'j', 'h', 'h', 'b', 'u', 't', 'a', 'r']
    #
    # needles= 17
    # ['h', 'l', 'p', 'd', 't', 'z', 'r', 'b', 's', 'm',
    #  'u', 'b', 'h', 't', 'g', 'v', 'z']

    # brute-force way
    found = 0
    for n in needles:
        if n in haystack:
            found += 1
            continue
    print("found=", found) # 17

    # using set operation - simpler
    intersection = set(needles) & set(haystack)
    found = len(intersection)
    print("intersection=", intersection, "found=", found)
    # intersection= {'s', 'y', 'n', 'd', 'q', 'l', 'm', 'a', 'k', 'c', 'u', 'j', 'z'}
    # found= 13


if False:
    # set comprehensions
    import random
    a = {chr(random.randint(97, 105)) for _ in range(128)}
    #   --------------------------------------------------
    #                   set comprehension

    print("set=", a, "len=", len(a))
    print("type=", type(a))
    # set= {'f', 'a', 'd', 'i', 'b', 'e', 'h', 'g', 'c'} len= 9
    # type= <class 'set'>


# -------------------------------------
# chapter 5: data class builders
# - data classes
# ; (1) classical data-holding class
# ; (2) collections.namedtuple
# ; (3) typing.NamedTuple
# ; (4) @dataclasses.dataclass

if False:
    # -------------------------------------
    # - (1) basic data-holding class
    # ; poor __repr__ -> not helpful
    # ; '==' operation --> id(obj1) == id(obj2)
    #   requires more functionalities
    class Coordinate:
        def __init__(self, lat, lon):
            self.lat = lat # latitude
            self.lon = lon # longitude

    moscow = Coordinate(55.76, 37.62)
    print(moscow)
    # <__main__.Coordinate object at 0x000001E205328350>

    somewhere = Coordinate(55.76, 37.62)
    print(somewhere)
    # <__main__.Coordinate object at 0x000001E205328290>

    print("somewhere == moscow", somewhere == moscow) # False
    print(
        "(somewhere.lat, somewhere.lon) == (moscow.lat, moscow.lon)", 
        (somewhere.lat, somewhere.lon) == (moscow.lat, moscow.lon)) # True


if False:
    # -------------------------------------
    # - (2) using collections.namedtuple
    # ; factory function for creating tuple subclasses with named fields
    # ; more memory-efficient than regular class
    # ; more useful __repr__
    # ; meaningful __eq__
    import collections
    Coordinate = collections.namedtuple('Coordinate', 'lat lon')

    #moscow = Coordinate(55.76, 37.62)
    moscow = Coordinate(lat=55.76, lon=37.62)
    print(moscow)
    # Coordinate(lat=55.76, lon=37.62)

    somewhere = Coordinate(55.76, 37.62)
    print(somewhere)
    # Coordinate(lat=55.76, lon=37.62)

    print("somewhere == moscow", somewhere == moscow) # True


if False:
    # -------------------------------------
    # - (3) using typing.NamedTuple - 1st style
    # ; with type annotations
    import typing
    if False:
        Coordinate = typing.NamedTuple('Coordinate', lat=float, lon=float)
    else:
        Coordinate = typing.NamedTuple('Coordinate', [('lat', float), ('lon', float)])

    moscow = Coordinate(55.76, 37.62)
    print(moscow)
    # Coordinate(lat=55.76, lon=37.62)

    somewhere = Coordinate(55.76, 37.62)
    print(somewhere)
    # Coordinate(lat=55.76, lon=37.62)

    print("somewhere == moscow", somewhere == moscow) # True

    print(issubclass(Coordinate, tuple)) # True
    print(issubclass(Coordinate, dict)) # False
    print(
        typing.get_type_hints(Coordinate)
    )
    # {'lat': <class 'float'>, 'lon': <class 'float'>}


if False:
    # -------------------------------------
    # - (3) using typing.NamedTuple - 2nd style
    # ; with type annotations
    import typing
    class Coordinate(typing.NamedTuple):
        lat: float
        lon: float

        def __str__(self):
            """print() uses this!"""
            ns = 'N' if self.lat >= 0 else 'S' # north or south
            we = 'E' if self.lon >= 0 else 'W' # west or east
            return f'{abs(self.lat):.1f}°{ns}, {abs(self.lon):.1f}°{we}'

    print("Coordinate.__annotations__=", Coordinate.__annotations__)
    print("Coordinate.__doc__=", Coordinate.__doc__)
    print("Coordinate.lat=", Coordinate.lat) # -> returns getter!
    print("Coordinate.lon=", Coordinate.lon) #
    # Coordinate.__annotations__= {'lat': <class 'float'>, 'lon': <class 'float'>}
    # Coordinate.__doc__= Coordinate(lat: float, lon: float)
    # Coordinate.lat= _tuplegetter(0, 'Alias for field number 0')
    # Coordinate.lon= _tuplegetter(1, 'Alias for field number 1')

    moscow = Coordinate(55.76, 37.62)
    print(moscow)
    # 55.8°N, 37.6°E

    somewhere = Coordinate(55.76, 37.62)
    print(somewhere)
    # 55.8°N, 37.6°E

    print("somewhere == moscow", somewhere == moscow) # True

    print(issubclass(Coordinate, tuple)) # True
    print(issubclass(Coordinate, dict)) # False
    print(
        typing.get_type_hints(Coordinate)
    )
    # {'lat': <class 'float'>, 'lon': <class 'float'>}


if False:
    # -------------------------------------
    # - (4) using dataclasses.dataclass decorator
    # ; frozen=True/False
    #   -> controls get() & set() availabilities
    import dataclasses

    @dataclasses.dataclass(frozen=True)
    class Coordinate:
        lat: float = 0.0
        lon: float = 0.0 # defaut!

        def __str__(self):
            """print() uses this!"""
            ns = 'N' if self.lat >= 0 else 'S' # north or south
            we = 'E' if self.lon >= 0 else 'W' # west or east
            return f'{abs(self.lat):.1f}°{ns}, {abs(self.lon):.1f}°{we}'

    print("Coordinate.__annotations__=", Coordinate.__annotations__)
    print("Coordinate.__doc__=", Coordinate.__doc__)
    print("Coordinate.lat=", Coordinate.lat) # -> error.
    print("Coordinate.lon=", Coordinate.lon) #    not a class-member!
    # Coordinate.__annotations__= {'lat': <class 'float'>, 'lon': <class 'float'>}
    # Coordinate.__doc__= Coordinate(lat: float, lon: float)
    # Coordinate.lat= 0.0
    # Coordinate.lon= 0.0

    moscow = Coordinate(55.76, 37.62)
    print(moscow)
    # 55.8°N, 37.6°E

    somewhere = Coordinate(55.76, 37.62)
    print(somewhere)
    # 55.8°N, 37.6°E

    print("somewhere == moscow", somewhere == moscow) # True

    print(issubclass(Coordinate, tuple)) # False
    print(issubclass(Coordinate, dict)) # False
    # {'lat': <class 'float'>, 'lon': <class 'float'>}


if False:
    # -------------------------------------
    # - collections.namedtuple details
    # ; factory function for creating tuple subclasses with named fields
    # ; more memory-efficient than regular class
    # ; more useful __repr__
    # ; meaningful __eq__
    import collections
    import pprint
    City = collections.namedtuple('City', 'name country population coordinates')
    Location = collections.namedtuple('Location', 'lat lon')

    print("[dbg] City._fields=", City._fields)
    print("[dbg] Location._fields=", Location._fields)
    # City._fields= ('name', 'country', 'population', 'location')
    # Location._fields= ('lat', 'lon')

    # tuple = (name, country_code, population, (lat, lon))
    data = [
        ('Tokyo', 'JP', 36.933, Location(35.689722, 139.691667)),
        ('Delhi NCR', 'IN', 21.935, Location(28.613889, 77.208889)),
        ('Mexico City', 'MX', 20.142, Location(19.433333, -99.133333)),
        ('New York-Newark', 'US', 20.104, Location(40.808611, -74.020386)),
        ('Sao Paulo', 'BR', 19.649, Location(-23.547778, -46.635833)),
    ]

    # classmethod somenamedtuple._make(iterable)
    # ; makes a new instance from an existing sequence or iterable
    cities = []
    for datum in data:
        city = City._make(datum)
        cities.append(city)
    pprint.pprint(cities)
    # [
    #  City(name='Tokyo', country='JP', population=36.933, coordinates=Location(lat=35.689722, lon=139.691667)),
    #  City(name='Delhi NCR', country='IN', population=21.935, coordinates=Location(lat=28.613889, lon=77.208889)),
    #  City(name='Mexico City', country='MX', population=20.142, coordinates=Location(lat=19.433333, lon=-99.133333)),
    #  City(name='New York-Newark', country='US', population=20.104, coordinates=Location(lat=40.808611, lon=-74.020386)),
    #  City(name='Sao Paulo', country='BR', population=19.649, coordinates=Location(lat=-23.547778, lon=-46.635833))
    # ]

    # somenamedtuple._asdict()
    # ; return a new built-in dict which maps field names to their corresponding values
    for city in cities:
        for key, val in city._asdict().items():
            if key == "coordinates":
                print("lat=", val.lat)
                print("lon=", val.lon)
            else:
                print("{}= {}".format(key, val))
        print()
    # name= Tokyo
    # country= JP
    # population= 36.933
    # lat= 35.689722
    # lon= 139.691667


if False:
    # -------------------------------------
    # - collections.namedtuple details
    # ; construction using kwargs
    import collections
    import pprint
    City = collections.namedtuple('City', 'name country population coordinates')
    Location = collections.namedtuple('Location', 'lat lon')

    print("[dbg] City._fields=", City._fields)
    print("[dbg] Location._fields=", Location._fields)
    # City._fields= ('name', 'country', 'population', 'location')
    # Location._fields= ('lat', 'lon')

    # dict = {name, country_code, population, coordinates}
    data = [
        dict( name='Tokyo',           country='JP', population=36.933, coordinates=Location( 35.689722, 139.691667) ),
        dict( name='Delhi NCR',       country='IN', population=21.935, coordinates=Location( 28.613889,  77.208889) ),
        dict( name='Mexico City',     country='MX', population=20.142, coordinates=Location( 19.433333, -99.133333) ),
        dict( name='New York-Newark', country='US', population=20.104, coordinates=Location( 40.808611, -74.020386) ),
        dict( name='Sao Paulo',       country='BR', population=19.649, coordinates=Location(-23.547778, -46.635833) ),
    ]
    print("\ndata=")
    pprint.pprint(data)

    # classmethod somenamedtuple._make(iterable)
    # ; makes a new instance from an existing sequence or iterable
    cities = []
    for datum in data:
        city = City(**datum)
        cities.append(city)
    print("\ncities=")
    pprint.pprint(cities)
    # [
    #  City(name='Tokyo', country='JP', population=36.933, coordinates=Location(lat=35.689722, lon=139.691667)),
    #  City(name='Delhi NCR', country='IN', population=21.935, coordinates=Location(lat=28.613889, lon=77.208889)),
    #  City(name='Mexico City', country='MX', population=20.142, coordinates=Location(lat=19.433333, lon=-99.133333)),
    #  City(name='New York-Newark', country='US', population=20.104, coordinates=Location(lat=40.808611, lon=-74.020386)),
    #  City(name='Sao Paulo', country='BR', population=19.649, coordinates=Location(lat=-23.547778, lon=-46.635833))
    # ]


if False:
    # -------------------------------------
    # - adding attributes and injecting a method in a collections.namedtuple
    # ; this is a hack! (not recommended)
    # ; class implementation is recommended
    import collections
    import pprint

    class FrenchDeck:
        ranks = [str(n) for n in range(2, 11)] + list('JQKA')
        suits = 'clubs diamonds hearts spades'.split() # with priority
        # ranks= ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'] len= 13
        #          0    1    2    3    4    5    6    7     8    9   10   11   12
        # suits= ['clubs', 'diamonds', 'hearts', 'spades'] len= 4
        
        def __init__(self):
            self._cards = [Card(rank, suit) for suit in self.suits
                                            for rank in self.ranks]
        def __len__(self):
            return len(self._cards)
    
        def __getitem__(self, position):
            return self._cards[position] # ':' slicing also supported

    Card = collections.namedtuple('Card', ['rank', 'suit'])
    Card.suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)

    def get_score(card):
        rank_value = FrenchDeck.ranks.index(card.rank)
        suit_value = card.suit_values[card.suit]
        return rank_value * len(card.suit_values) + suit_value

    Card.get_score = get_score # injecting a member function

    lowest = Card('2', 'clubs')
    highest = Card('A', 'spades')

    print("lowest.get_score()=", lowest.get_score())
    print("highest.get_score()=", highest.get_score())
    # lowest.get_score()= 0
    # highest.get_score()= 51
    # -> this works! but poor readability!


if False:
    # -------------------------------------
    # - typing.NamedTuple details
    # ; typed version of collections.namedtuple().
    # ; nothing different from collections.namedtuple except for __annotations__
    #   (class attribute, ignored during runtime)
    # ; type hints - PEP 484
    #   (1) no runtime effect
    #   (2) no type checking at runtime
    import typing
    class Coordinate(typing.NamedTuple): #
        lat: float                       #
        lon: float                       # variable annotation syntax
        reference: str = 'wsg84'         # type with default

        def __str__(self):
            """print() uses this!"""
            ns = 'N' if self.lat >= 0 else 'S' # north or south
            we = 'E' if self.lon >= 0 else 'W' # west or east
            return f'{abs(self.lat):.1f}°{ns}, {abs(self.lon):.1f}°{we}, {self.reference}'

    # class attributes
    print(Coordinate.__doc__) # custom docstring
    print(Coordinate.__annotations__)
    print(Coordinate.lat)
    print(Coordinate.lon)
    print(Coordinate.reference)
    # Coordinate(lat, lon, reference)
    # {'lat': <class 'float'>, 'lon': <class 'float'>, 'reference': <class 'str'>}
    # _tuplegetter(0, 'Alias for field number 0') |
    # _tuplegetter(1, 'Alias for field number 1') |
    # _tuplegetter(2, 'Alias for field number 2') +--> property getter for
    #                                                  read-only attributes


    moscow = Coordinate(55.76, 37.62)
    print(id(moscow), moscow, sep=', ') # 1836726154912, 55.8°N, 37.6°E, wsg84

    somewhere = Coordinate(55.76, 37.62)
    print(id(somewhere), somewhere, sep=', ') # 1836726154992, 55.8°N, 37.6°E, wsg84

    wrong = Coordinate(55.76, 37.62, 44.53)
    print(id(wrong), wrong, sep=', ')
    # 1836726155072, 55.8°N, 37.6°E, 44.53
    #                                --+--
    #                                  |
    #                                  no type check!

    print("somewhere is moscow:", somewhere is moscow) # False
    print("somewhere == moscow:", somewhere == moscow) # True, __eq__ supported

    print(issubclass(Coordinate, tuple)) # True
    print(issubclass(Coordinate, dict)) # False -> not a mapping type

    # - getting type hints
    # ; from __annotations__
    # ; from typing.get_type_hints()
    print(
        typing.get_type_hints(Coordinate)
    )
    # {'lat': <class 'float'>, 'lon': <class 'float'>, 'reference': <class 'str'>}


if False:
    # -------------------------------------
    # - @dataclasses.dataclass(
    #       *, init=True, repr=True, eq=True, order=False, unsafe_hash=False,
    #       frozen=False, match_args=True, kw_only=False, slots=False,
    #       weakref_slot=False
    #   )
    # ; this function is a decorator that is used to add generated special
    #   methods to classes
    # ; keyword-argument only! <--- '*'
    #
    # - @dataclasses.dataclass decorator details
    # ; this module provides a decorator and functions for automatically
    #   adding generated special methods such as __init__() and __repr__() to
    #   user-defined classes.
    # ; no type checking at runtime
    # ; mutable by default (frozen=False)
    # ; eq=True & frozen=True -> __hash__ generated, hashable
    #   -> no setter will be available
    # ; can implement user-defined __init__, __repr__, __eq__
    import dataclasses

    @dataclasses.dataclass(frozen=True) # frozen= True(immutable) or False(mutable)
    class Coordinate:
        lat: float
        lon: float # not a class attribute, but instance attribute
                   # -> fields become parameters of __init__

        def __str__(self):
            """print() uses this!"""
            ns = 'N' if self.lat >= 0 else 'S' # north or south
            we = 'E' if self.lon >= 0 else 'W' # west or east
            return f'{abs(self.lat):.1f}°{ns}, {abs(self.lon):.1f}°{we}'

    # class attributes
    print(Coordinate.__doc__) # custom docstring
    print(Coordinate.__annotations__)
    #print(Coordinate.lat) -> not exists as class attribues
    #print(Coordinate.lon) -> not exists as class attribues
    # Coordinate(lat: float, lon: float)
    # {'lat': <class 'float'>, 'lon': <class 'float'>}

    moscow = Coordinate(55.76, 37.62)
    print(moscow)
    # 55.8°N, 37.6°E

    somewhere = Coordinate(55.76, 37.62)
    print(somewhere)
    # 55.8°N, 37.6°E

    print("somewhere == moscow", somewhere == moscow) # True

    print(issubclass(Coordinate, tuple)) # False
    print(issubclass(Coordinate, dict)) # False
    # {'lat': <class 'float'>, 'lon': <class 'float'>}


if False:
    # -------------------------------------
    # - default values must be immutable!
    # ; or any factory pattern
    import dataclasses
    @dataclasses.dataclass
    class ClubMember:
        name: str
        #guests: list = [] # error! <- mutable
        #guests: list = dataclasses.field(default_factory=list)
        guests: list[str] = dataclasses.field(default_factory=list)
        #       ---------                                     ----
        #       list of string                                function
        athlete: bool = dataclasses.field(default=False, repr=True)

    cm0 = ClubMember("aaa", [0, 1, 2])
    cm1 = ClubMember("bbb", ['a', 'b', 'c'])
    print(cm0)
    print(cm1)
    # ClubMember(name='aaa', guests=[0, 1, 2]) # 'str' is just a type hint!
    # ClubMember(name='bbb', guests=['a', 'b', 'c'])


if True:
    # -------------------------------------
    # - __post_init__ method for HackerClubMember
    # ;
    import dataclasses
    @dataclasses.dataclass
    class ClubMember:
        name: str
        #guests: list = [] # error! <- mutable
        #guests: list = dataclasses.field(default_factory=list)
        guests: list[str] = dataclasses.field(default_factory=list)
        #       ---------                                     ----
        #       list of string                                function


    @dataclasses.dataclass
    class HackerClubMember(ClubMember):
        all_handles = set()
        handle: str = ''

        def __post_init__(self):
            cls = s
