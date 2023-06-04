# vim: ft=python ts=4 sw=4 tw=999 expandtab
# -*- coding:utf-8 -*-
# ----------------------------------------------------------------------------
# - file : fluent_python_1_prologue.py
# - author : yc0325lee
# - created : 2022-10-11 22:15:49 by lee2103
# - modified : 2022-10-11 22:15:49 by lee2103
# - description : 
# ----------------------------------------------------------------------------

# -------------------------------------
# chapter 1: the python data model
# - x[i]
#   ; invokes type(x).__getitem__(x, i)
# - obj[key] -> obj.__getitem__(key) magic(special) method invoked
# - 
# - magic methods are used for
#   ; iteration
#   ; collections
#   ; attribute access
#   ; operator overloading
#   ; function and method invocation
#   ; object creation and destruction
#   ; string representation and formatting
#   ; managed contexts (i.e., with blocks)
# - special method (magic method or dunder method)
#   ; python language reference -> 3.3.2 customizing attribute access
# - obj.__new__(cls)
# - obj.__bool__(self)
#   ; invoked for truth/falsehood test and bool()
#   ; __len__() invoked when not implemented
#   ; true when no __bool__ and __len__


# a pythonic card deck - FrenchDeck
# ; __getitem__() -> index-ed accessing, iteration, ...
# ; __len__() -> len(deck)
if False:
    import sys
    import collections

    # decorator for debugging
    def debug(func):
        def wrapper(*args):
            #print("[dgb ] {}() starts ...".format(func.__name__))
            decorated = func(*args)
            #print("[dgb ] {}() ends ...".format(func.__name__))
            return decorated
        return wrapper
    
    # the following defines 'Card' type
    Card = collections.namedtuple('Card', ['rank', 'suit'])
    
    class FrenchDeck:
        """
        implementation of __len__ and __getitem__ is important
        for sequence-like behavior!!!
        - iteration and slicing
        - using built-in reversed() and sorted()
        """
        ranks = [str(n) for n in range(2, 11)] + list('JQKA')
        #suits = 'spades diamonds clubs hearts'.split()
        suits = 'clubs diamonds hearts spades'.split() # priority
        print("[info] ranks=", ranks)
        print("[info] suits=", suits)
        print("[info] len(ranks)=", len(ranks))
        print("[info] len(suits)=", len(suits))
        
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
            return self._cards[position] # ':' slicing also supported
        pass

    
    deck = FrenchDeck()
    print("deck=", deck)

    if False:
        print("\n# testing deck.__len__()")
        print("len=", len(deck)) # -> deck.__len__()
    
    if False:
        print("\n# element access using []")
        for i in range(len(deck)):
            print("deck[{}]= {}".format(i, deck[i])) # deck[i] -> deck.__getitem__(i)
    
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
        #print(deck[:3])
        for card in deck[:4]:
            print(card)
        #print(deck[12::13]) # s[start:end:step]
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
        print("\n# iteration test")
        print("reversed(deck)=", reversed(deck))
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
            print("card=", card, "get_score=", get_score(card))


if True:
    # emulating numeric types - Vector
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
            #return 'Vector(%r, %r)' % (self.x, self.y)
            return 'Vector({!r}, {!r})'.format(self.x, self.y)
            # - special method for repr() and print()
            # ; if no custom __str__() is available, python will call __repr__() instead
            # ; %r : standard representation of object using repr() built-in function
            #   !r used for str.format()
            # ; if __repr__ not implemented -> <Vector object at 0x10e100070>

        # def __str__(self):
        # ; invoked by str() constructor or by print() implicitly

        @debug
        def __abs__(self):
            # invoked when abs() used
            # return the euclidean norm, sqrt(sum(x**2 for x in coordinates))
            return math.hypot(self.x, self.y)

        @debug
        def __bool__(self):
            # - boolean value contexts : if, while, and, or, not and bool(x)
            # ; if no __bool__ -> x.__len__() invoked
            # ; if no __bool__ and no __len__ -> the object is always true(default)
            return bool(abs(self))
            #return bool(self.x or self.y) # faster version
                                            # -> doesn't need to invoke abs()
        #@debug
        #def __bool__(self):
        #    return bool(self.x or self.y) # faster version

        @debug
        def __add__(self, right):
            #print("[info] adding %r and %r ..." % (self, right))
            x = self.x + right.x
            y = self.y + right.y
            return Vector(x, y)

        @debug
        def __mul__(self, scalar):
            return Vector(self.x * scalar, self.y * scalar)


    v1 = Vector(2, 4)
    v2 = Vector(2, 1)
    print("\nv1 = ", v1) # __repr__
    print("v2 = ", v2) # __repr__
    print("v1 + v2 =", v1 + v2) # __add__ -> __init__ -> __repr__

    v3 = Vector(3, 4)
    v4 = Vector() # Vector(0, 0)
    print("\nv3 = ", v3)
    print("v4 = ", v4)
    print("abs(v3) =", abs(v3)) # __abs__

    print("\nv3 * 3 =", v3 * 3)
    print("abs(v3 * 3) =", abs(v3 * 3)) # __mul__ -> __init__

    # boolean test
    # ; bool(x), if, while, and, or, not, ...
    # ; object of user-defined class -> true
    # ; but __bool__ or __len__ will change the behavior!
    # ; if __bool__ is not implemented, __len__ will be used for true or false
    # ; if x.__len__() teturns zero, then False. otherwise True
    # ; see "The Python Standard Library" -> Built-in Types -> Truth Value Testing

    print("\nbool(v3) = ", bool(v3)) # True
    print("bool(v4) = ", bool(v4)) # False


# see the "data model" from "the python language reference"

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
