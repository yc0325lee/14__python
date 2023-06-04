#!/usr/bin/env python
# -*- coding:utf-8 -*-
# vim: ft=python ts=4 sw=4 tw=78 expandtab
# ----------------------------------------------------------------------------
# - file : fluent_python_4_object_oriented_idioms.py
# - author : yc0325lee
# - created : 2022-11-06 22:43:41 by yc032
# - modified : 2022-12-04 19:36:22 by yc032
# - description : 
# 11. a pythonic object
# 12. special methods for sequences
# 13. interfaces, protocols, and abcs
# 14. inheritance: for better or for worse
# 15. more about type hints
# 16. operator overloading
# ----------------------------------------------------------------------------
from utilities import printv

# -------------------------------------
# chapter 8: object references, mutability, and recycling

# - variables in python is a handle
# ; with reference variables, it makes much more sense to say that the variable
#   is assigned to an object, and not the other way around.
# ; '==' operator and 'is' operator are different!
# ; use 'is' operator for equality instead of id() function
#
# - identity operators - special
# +--------+----------------------------------------+
# | is     | True if the operands are identical     |
# +--------+----------------------------------------+
# | is not | True if the operands are not identical |
# +--------+----------------------------------------+
# - equality operator (==) compares the values of both the operands and checks
#   for value equality.
# - the 'is' operator checks whether both the operands refer to the same object or not.
# ; same as 'id(a) == id(b)'

if False:
    t1 = (1, 2, [30, 40])
    t2 = (1, 2, [30, 40])
    print(t1 == t2) # True
    print(t1 is t2) # False

if False:
    l1 = [3, [55, 44], (7, 8, 9)]
    l2 = list(l1) 
    print(l1 == l2) # True
    print(l1 is l2) # False
    print(id(l1[-1]), id(l2[-1])) # 2079220420992 2079220420992 -> same!

if False:
    l1 = [3, [66, 55, 44], (7, 8, 9)]
    l2 = list(l1) # shallow copy
    l1.append(100) #
    l1[1].remove(55) # 
    print('l1:', l1)
    print('l2:', l2)
    l2[1] += [33, 22] # 
    l2[2] += (10, 11) # 
    print('l1:', l1)
    print('l2:', l2)

if False:
    # ------------------------------------
    # - copy.copy(x) - shallow copy
    # - copy.deepcopy(x[, memo]) - deep copy
    # ; does not copy immutable container
    # ------------------------------------
    import copy
    l1 = [3, [66, 55, 44], (7, 8, 9)]
    print("\n# l1:")
    for i, item in enumerate(l1):
        print("id(item[{}])= {}, {}".format(i, id(item), item))

    l2 = copy.copy(l1)
    l2[1][1] += 1
    print("\n# l1:")
    for i, item in enumerate(l1):
        print("id(item[{}])= {}, {}".format(i, id(item), item))
    print("\n# l2:")
    for i, item in enumerate(l2):
        print("id(item[{}])= {}, {}".format(i, id(item), item))

    l2 = copy.deepcopy(l1)
    l2[1][1] += 1
    print("\n# l1:")
    for i, item in enumerate(l1):
        print("id(item[{}])= {}, {}".format(i, id(item), item))
    print("\n# l2:")
    for i, item in enumerate(l2):
        print("id(item[{}])= {}, {}".format(i, id(item), item))
    pass
    
if False:
    # ------------------------------------
    # - copy.copy(x) - shallow copy
    # - copy.deepcopy(x[, memo]) - deep copy
    # ; does not copy immutable container
    # ------------------------------------
    from copy import copy, deepcopy
    class Bus:
        def __init__(self, passengers=None):
            if passengers is None:
                self.passengers = []
            else:
                self.passengers = list(passengers)
    
        def __repr__(self):
            return "Bus({})".format(self.passengers)
            # if no custom __str__() is available,
            # python will call __repr__() instead!
    
        def pick(self, name):
            self.passengers.append(name)
    
        def drop(self, name):
            self.passengers.remove(name)
    
        pass

    bus1 = Bus(['alice', 'bill', 'claire', 'david'])
    bus2 = copy(bus1)
    bus3 = deepcopy(bus1)
    # bus1= Bus(['alice', 'bill', 'claire', 'david'])
    # bus2= Bus(['alice', 'bill', 'claire', 'david'])
    # bus3= Bus(['alice', 'bill', 'claire', 'david'])

    bus1.drop('bill') # will affect bus2 also!
    # bus1= Bus(['alice', 'claire', 'david'])
    # bus2= Bus(['alice', 'claire', 'david'])
    # bus3= Bus(['alice', 'bill', 'claire', 'david'])

if False:
    # cyclic references
    from copy import copy, deepcopy

    a = [10, 20]
    b = [a, 30]
    print("a=", a, "b=", b)

    a.append(b)
    print("a=", a, "b=", b)

    c = deepcopy(a)
    print("c=", c)

if False:
    # function parameters as references
    def f(a, b):
        a += b # a = a + b
        return a

    # scalar
    x, y = 1, 2
    z = f(x, y)
    print("x=", x, "y=", y, "z=", z)
    # x= 1 y= 2 z= 3 -> 'x' unchanged

    # list
    x = [1, 2]
    y = [3, 4]
    z = f(x, y)
    print("x=", x, "y=", y, "z=", z)
    # x= [1, 2, 3, 4] y= [3, 4] z= [1, 2, 3, 4] -> 'x' changed

    # tuple
    x = (1, 2)
    y = (3, 4)
    z = f(x, y)
    print("x=", x, "y=", y, "z=", z)
    # x= (1, 2) y= (3, 4) z= (1, 2, 3, 4) -> 'x' unchanged
    # [note] list and tuple show different behavior,
    #        because '+=' operation is different

if False:
    # mutable types as parameter defaults -> bad idea!
    # -> eerie(strange,mysterious) behavior!
    # -> default list is evaluated when '__init__' is defined!
    # -> use 'None' instead of mutable value for parameter
    class HauntedBus:
        def __init__(self, passengers=[]):
            self.passengers = passengers # default= empty-list
                                         # but always the same list object!
    
        def __repr__(self):
            return "HauntedBus({})".format(self.passengers)
            # if no custom __str__() is available,
            # python will call __repr__() instead!
    
        def pick(self, name):
            self.passengers.append(name)
    
        def drop(self, name):
            self.passengers.remove(name)
    
        pass


    bus1 = HauntedBus(['alice', 'bill'])
    print("bus1=", bus1)
    bus1.pick('charlie')
    bus1.drop('alice')
    print("bus1=", bus1)

    bus2 = HauntedBus()
    bus2.pick('carrie')
    print("bus2=", bus2)

    bus3 = HauntedBus()
    print("bus3=", bus3)
    bus3.pick('dave')
    print("bus3=", bus3)

    # what happens to bus2 is?
    print("bus2=", bus2)
    print("HauntedBus.__init__.__defaults__=", HauntedBus.__init__.__defaults__)
    print(HauntedBus.__init__.__defaults__[0] is bus2.passengers)
    print(id(HauntedBus.__init__.__defaults__[0]), id(bus2.passengers))
    

if False:
    import weakref
    def bye():
        print("[info] object is being destroyed ...")

    s1 = {1, 2, 3}
    s2 = s1

    ender = weakref.finalize(s1, bye)
    if ender.alive:
        print("[info] object is still alive ...")

    del s1
    if ender.alive:
        print("[info] object is still alive ...")

    s2 = [1, 2, 3] # 's2' refers to another object,
                   # so '{1, 2, 3}' should be garbage collected.
    print("[info] end of program ...")


if False:
    # ----------------------------------------------------------------------
    # class weakref.ref(object[, callback])
    # ; return a weak reference to object.
    # ; the original object can be retrieved by calling the reference object
    #   if the referent is still alive
    # ; if the referent is no longer alive, calling the reference object
    #   will cause 'None' to be returned.
    # ----------------------------------------------------------------------
    import weakref
    def bye(ref):
        print("[info] object referred by {} is being destroyed ...".format(ref))

    a = {0, 1}
    weak = weakref.ref(a, bye)
    print("weak=", weak)
    print("weak()=", weak())
    # weak= <weakref at 0x000001FD577D7C70; to 'set' at 0x000001FD577DC820>
    # weak()= {0, 1}                        ------------------------------
    #                                                  alive!

    a = {2, 3, 4} # '{0, 1}' is destroyed and bye() is invoked
    print("weak=", weak) # dead referent
    print("weak()=", weak()) # None
    # weak= <weakref at 0x000001FD577D7C70; dead>
    # weak()= None                          ----
    #                                       not alive!


if False:
    # the WeakValueDictionary skit
    import weakref
    class Cheese:
        def __init__(self, kind):
            self.kind = kind
        def __repr__(self):
            return 'Cheese(%r)' % self.kind

    catalog = [
        Cheese('Red Leicester'), Cheese('Tilsit'),
        Cheese('Brie'), Cheese('Parmesan')
    ]

    stock = weakref.WeakValueDictionary()

    for cheese in catalog:
        stock[cheese.kind] = cheese
        # stock holds weak references to each cheese

    print("catalog=", catalog)
    for key, val in stock.items():
        print("stock[{}]= {}".format(key, val))

    del catalog # delete all!
    print("[info] catalog deleted!")

    #print("catalog=", catalog)
    for key, val in stock.items():
        print("stock[{}]= {}".format(key, val))
    # 'val' is holding the last cheese!

    for attr in dir():
        if '__' not in attr:
            print(attr) # 'cheese' still exists!


# -------------------------------------
# chapter 9: pythonic object

if False:
    # object representations
    # - built-in : repr(), str()
    # - magic method to support representations
    # ; repr()   -> __repr__()
    # ; str()    -> __str__()
    # ; format() -> __format__()
    # ; bytes()  -> __bytes__()
    from array import array
    import math
    
    # decorator for debugging
    def debug(func):
        def wrapper(*args):
            print("[dgb ] {}() invoked ...".format(func.__name__))
            decorated = func(*args)
            return decorated
        return wrapper
    
    class Vector2d:
        typecode = 'd' # class attribute
    
        @debug
        def __init__(self, x, y):
            self.x = float(x)
            self.y = float(y)
    
        @debug
        @classmethod
        def frombytes(cls, octets):
            # for alternative constructor
            typecode = chr(octets[0])
            memv = memoryview(octets[1:]).cast(typecode)
            return cls(*memv)
    
        @debug
        def __iter__(self):
            return (i for i in (self.x, self.y)) # comprehension
    
        @debug
        def __repr__(self):
            class_name = type(self).__name__ # for safer inheritance!
            return '{}({!r}, {!r})'.format(class_name, *self)
    
        @debug
        def __str__(self):
            return str(tuple(self))
    
        @debug
        def __format__(self, fmt_spec=''):
            # -----------------------------------------
            # fmt_spec ends with 'c' : cartesian format
            # fmt_spec ends with 'p' : polar format
            # -----------------------------------------
            if fmt_spec.endswith('p'):
                fmt_spec = fmt_spec[:-1]
                coords = (abs(self), self.angle()) # tuple
                outer_fmt = '<{}, {}>'
            else:
                if fmt_spec.endswith('c'):
                    fmt_spec = fmt_spec[:-1]
                coords = self
                outer_fmt = '({}, {})'
    
            components = (format(c, fmt_spec) for c in coords) # generator expr
            return outer_fmt.format(*components)
    
        @debug
        def __bytes__(self):
            # self.typecode -> __class__.typecode (default)
            return (bytes([ord(self.typecode)]) +
                    bytes(array(self.typecode, self)))
    
        @debug
        def __eq__(self, other):
            return tuple(self) == tuple(other)
        #                ----           -----
        #               Vector()        this works when other is not
        #                               of type 'Vector2d'!
        #                               any iterable will be ok.
        #                               Vector(3, 4) == [3, 4] --> True!
    
        @debug
        def __hash__(self):
            return hash(self.x) ^ hash(self.y)
    
        @debug
        def __abs__(self):
            return math.hypot(self.x, self.y)
    
        @debug
        def __bool__(self):
            return bool(abs(self)) 
    
        @debug
        def angle(self):
            return math.atan2(self.y, self.x)
    
        pass


    print('\n# __init__')
    v1 = Vector2d(3, 4)

    print('\n# __str__ -> __iter__')
    print(v1) # str(v1) -> __str__(v1) -> (3.0, 4.0)

    print('\n# __format__ -> __iter__')
    print(format(v1)) # no __format__() -> str(v1) invoked!

    print('\n# __repr__ -> __iter__')
    print(repr(v1)) # __repr__()
    
    # formatted display
    print('\n# __format__ -> __iter__')
    print(format(v1, '.6f'))  # default
    print(format(v1, '.6e'))  # default
    print(format(v1, '.6fc')) # cartesian
    print(format(v1, '.6ec')) # cartesian
    print(format(v1, '.6fp')) # polar
    print(format(v1, '.6ep')) # polar
    
    # a hashable Vector2d - 2 requirements
    # 1. immutable object required, but not mandatory
    #  (1) double underscores -> private attributes
    #  (2) @property decorators for getter method
    #  (3) self.__x -> x() getter
    # 2. __hash__() and __eq__() required
    #  (1) objects that compare equal should have the same hash value
    print('\n# __hash__')
    v2 = Vector2d(3, 4)
    v3 = Vector2d(3.1, 4.2)
    print("hash(v2)=", hash(v2))
    print("hash(v3)=", hash(v3))

    print('\n# __eq__ -> __iter__')
    print('v2 == v3 ->', v2 == v3)
    print('v2 == [3, 4] ->', v2 == [3, 4])

    # private attribute names are "mangled" by prefixing the _ and the class name
    # '__attr' -> do not use this! special
    # '_attr' -> use this by naming convention
    
    # saving space with the '__slots__' class attribute
    # (3.3.2.4. __slots__)
    # ; these are all the instance attributes in this class.
    # ; __slots__ allow us to explicitly declare data members (like properties)
    #   and deny the creation of __dict__ and __weakref__ (unless explicitly
    #   declared in __slots__ or available in a parent.)
    
    # overriding class attributes - (1)
    print('\n# __bytes__ -> __iter__')
    dumped = bytes(v3) # __class__.typecode
    print("dumped=", dumped, "len(dumped)=", len(dumped))
    
    v3.typecode = 'f' # overrides 'Vector2d.typecode'
    dumped = bytes(v3) # self.typecode
    print("dumped=", dumped, "len(dumped)=", len(dumped))
    
    del v3.typecode # recover the default
    dumped = bytes(v3) # __class__.typecode
    print("dumped=", dumped, "len(dumped)=", len(dumped))
    # dumped= b'd\xcd\xcc\xcc\xcc\xcc\xcc\x08@\xcd\xcc\xcc\xcc\xcc\xcc\x10@' len(dumped)= 17
    # dumped= b'fffF@ff\x86@' len(dumped)= 9
    # dumped= b'd\xcd\xcc\xcc\xcc\xcc\xcc\x08@\xcd\xcc\xcc\xcc\xcc\xcc\x10@' len(dumped)= 17
    
    print('\n# inheritance -> Vector2d_Short')
    # overriding class attributes - (2)
    # ; inheritance
    # ; fancier way by customizing class data in derived classes
    class Vector2d_Short(Vector2d):
        typecode = 'f'
    
    v4 = Vector2d_Short(3.3, 4.4)
    print("v4=")
    print(v4) # __str__
    dumped = bytes(v4)
    print("dumped=", dumped, "len(dumped)=", len(dumped), end='\n\n')



# -------------------------------------
# chapter 10: sequence hacking, hashing, and slicing

if False:
    # - vector take #1: vector2d compatible
    # ; a user-defined sequence type
    # ;
    from array import array
    import reprlib # to produce limited-length representations,
    import math

    class Vector:
        typecode = 'd' # double, 'f' -> float

        def __init__(self, components):
            self._components = array(self.typecode, components) 
            #                                       ----------
            #                                       a sequence(iterable),
            #                                       not multiple args

        @classmethod
        def frombytes(cls, octets):
            typecode = chr(octets[0])
            memv = memoryview(octets[1:]).cast(typecode)
            return cls(memv)

        def __iter__(self):
            # iter() will invoke this!
            return iter(self._components)

        def __repr__(self):
            components = reprlib.repr(self._components) # -> str
            components = components[components.find('['):-1] 
            return 'Vector({})'.format(components)
            # -----------------------------------------------
            # array('d', [0.0, 1.0, 2.0, 3.0, 4.0, ...])
            #            ------------------------------
            #                      sub-string
            # Vector([0.0, 1.0, 2.0, 3.0, 4.0, ...])
            # -> can be used for Vector construction
            # -----------------------------------------------

        def __str__(self):
            return str(tuple(self))
            # (0.0, 1.0, 2.0, 3.0, 4.0, ...)

        def __bytes__(self):
            return (bytes([ord(self.typecode)]) + bytes(self._components))
            #                                     -----------------------
            #                                     invokes array's __repr__ 

        def __eq__(self, other):
            return tuple(self) == tuple(other)
            #      -----------
            #      invokes __iter__()

        def __abs__(self):
            return math.sqrt(sum(x * x for x in self)) # x**2

        def __bool__(self):
            return bool(abs(self))

        pass


    print(repr(Vector([3.1, 4.2])))
    print(repr(Vector([3.0, 4.0, 5.0])))
    print(repr(Vector(range(10))))
    # Vector([3.1, 4.2])
    # Vector([3.0, 4.0, 5.0])
    # Vector([0.0, 1.0, 2.0, 3.0, 4.0, ...])


if False:
    # - protocols and duck typing
    # ; sequence protocol requires __len__ and __getitem__
    # - a pythonic card deck - FrenchDeck
    # ; __getitem__() -> index-ed accessing, iteration, ...
    # ; __len__() -> len(deck)
    class FrenchDeck:
        """
        implementation of __len__ and __getitem__ is important
        for sequence-like behavior!!!
        - iteration and slicing
        - used for built-in reversed() and sorted()
        """
        ranks = [str(n) for n in range(2, 11)] + list('JQKA')
        suits = 'clubs diamonds hearts spades'.split() # priority
        
        def __init__(self): # list comprehension
            self._cards = [Card(rank, suit) for suit in self.suits
                                            for rank in self.ranks]
        def __len__(self):
            return len(self._cards)
            #          -----------
            #              list
    
        def __getitem__(self, position):
            return self._cards[position] # ':' slicing also supported
        pass


if False:
    # - vector take #2: a sliceable sequence
    # ; a user-defined sequence type
    # ; for pythonic objects like FrenchDeck
    #   __getitem__() -> index-ed accessing v[3], iteration, ...
    #   __len__() -> len(deck)
    from array import array
    import reprlib # to produce limited-length representations,
    import math

    class Vector:
        typecode = 'd' # double, 'f' -> float

        def __init__(self, components):
            self._components = array(self.typecode, components) 
            #                                       ----------
            #                                       a sequence(iterable),
            #                                       not multiple args

        @classmethod
        def frombytes(cls, octets):
            typecode = chr(octets[0])
            memv = memoryview(octets[1:]).cast(typecode)
            return cls(memv)

        def __iter__(self):
            # iter() will invoke this!
            return iter(self._components)

        def __repr__(self):
            components = reprlib.repr(self._components) # -> str
            components = components[components.find('['):-1] 
            return 'Vector({})'.format(components)
            # -----------------------------------------------
            # array('d', [0.0, 1.0, 2.0, 3.0, 4.0, ...])
            #            ------------------------------
            #                      sub-string
            # Vector([0.0, 1.0, 2.0, 3.0, 4.0, ...])
            # -> can be used for Vector construction
            # -----------------------------------------------

        def __str__(self):
            return str(tuple(self))
            # (0.0, 1.0, 2.0, 3.0, 4.0, ...)

        def __bytes__(self):
            return (bytes([ord(self.typecode)]) + bytes(self._components))
            #                                     -----------------------
            #                                     invokes array's __repr__ 

        def __eq__(self, other):
            return tuple(self) == tuple(other)
            #      -----------
            #      invokes __iter__()

        def __abs__(self):
            return math.sqrt(sum(x * x for x in self)) # x**2

        def __bool__(self):
            return bool(abs(self))

        def __len__(self): # for len(obj)
            return len(self._components)

        def __getitem__(self, index): # indexing & iteration
            return self._components[index]

        pass

    v3 = Vector([3.0, 4.0, 5.0])
    print('v3=', repr(v3))
    print('len(v1)=', len(v3)) # len()
    print('v3[1]=', v3[1]) # indexing
    print('v3[-1]=', v3[-1])

    v7 = Vector(range(7))
    print('v7=', repr(v7))
    print('v7[1:4]=', v7[1:4]) # slicing
    # v7= Vector([0.0, 1.0, 2.0, 3.0, 4.0, ...])
    # v7[1:4]= array('d', [1.0, 2.0, 3.0])
    # -> we should do more!


if False:
    # - vector take #2: a sliceable sequence
    # ; slice-aware __getitem__
    from array import array
    import reprlib # to produce limited-length representations,
    import math
    import numbers

    class Vector:
        typecode = 'd' # double, 'f' -> float

        def __init__(self, components):
            self._components = array(self.typecode, components) 
            #                                       ----------
            #                                       a sequence(iterable),
            #                                       not multiple args

        @classmethod
        def frombytes(cls, octets):
            typecode = chr(octets[0])
            memv = memoryview(octets[1:]).cast(typecode)
            return cls(memv)

        def __iter__(self):
            # iter() will invoke this!
            return iter(self._components)

        def __repr__(self):
            components = reprlib.repr(self._components) # -> str
            components = components[components.find('['):-1] 
            return 'Vector({})'.format(components)
            # -----------------------------------------------
            # array('d', [0.0, 1.0, 2.0, 3.0, 4.0, ...])
            #            ------------------------------
            #                      sub-string
            # Vector([0.0, 1.0, 2.0, 3.0, 4.0, ...])
            # -> can be used for Vector construction
            # -----------------------------------------------

        def __str__(self):
            return str(tuple(self))
            # (0.0, 1.0, 2.0, 3.0, 4.0, ...)

        def __bytes__(self):
            return (bytes([ord(self.typecode)]) + bytes(self._components))
            #                                     -----------------------
            #                                     invokes array's __repr__ 

        def __eq__(self, other):
            return tuple(self) == tuple(other)
            #      -----------
            #      invokes __iter__()

        def __abs__(self):
            return math.sqrt(sum(x * x for x in self)) # x**2

        def __bool__(self):
            return bool(abs(self))

        def __len__(self): # for len(obj)
            return len(self._components)

        def __getitem__(self, index): # indexing & iteration
            cls = type(self)
            if isinstance(index, slice): # 'slice' type can be used for indexing!
                return cls(self._components[index]) # returns a new Vector object(sub-array)
            elif isinstance(index, numbers.Integral):
                return self._components[index]
            else:
                message = '{cls.__name__} indices must be integers'
                raise TypeError(message.format(cls=cls))

        pass

    v3 = Vector([3.0, 4.0, 5.0])
    printv(v3) # __str__
    printv(repr(v3)) # __repr__
    printv(len(v3)) # __len__
    printv(v3[1]) # indexing
    printv(v3[-1])
    # v3 = (3.0, 4.0, 5.0)
    # repr(v3) = Vector([3.0, 4.0, 5.0])
    # len(v3) = 3
    # v3[1] = 4.0
    # v3[-1] = 5.0

    print()

    v7 = Vector(range(7))
    printv(v7)
    printv(repr(v7))
    printv(repr(v7[1:4])) # slicing
    printv(repr(v7[-1:])) # slicing
    # v7 = (0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0)
    # repr(v7) = Vector([0.0, 1.0, 2.0, 3.0, 4.0, ...])
    # repr(v7[1:4]) = Vector([1.0, 2.0, 3.0])
    # repr(v7[-1:]) = Vector([6.0])

    if False:
        printv(v7[1,2]) # illegal slicing
        # TypeError: Vector indices must be integers


if False:
    # - vector take #3: dynamic attribute access
    # ; need to get access to vector components by name
    #   v.x, v.y, v.z, v.t -> 4-dimension only
    # ; __getattr__ would be implemented for this
    # ; the __getattr__ method is invoked by the interpreter
    #   when attribute lookup fails.
    # ; when 'obj.x' expr is given
    #   (1) check if obj.x exists
    #   (2) check obj.__class__ and its base-classes for 'x' class attribute
    #   (3) self.__getattr__('x') is invoked
    from array import array
    import reprlib # to produce limited-length representations,
    import math
    import numbers

    class Vector:
        typecode = 'd' # double, 'f' -> float

        def __init__(self, components):
            self._components = array(self.typecode, components) 
            #                                       ----------
            #                                       a sequence(iterable),
            #                                       not multiple args

        @classmethod
        def frombytes(cls, octets):
            typecode = chr(octets[0])
            memv = memoryview(octets[1:]).cast(typecode)
            return cls(memv)

        def __iter__(self):
            # iter() will invoke this!
            return iter(self._components)

        def __repr__(self):
            components = reprlib.repr(self._components) # -> str
            components = components[components.find('['):-1] 
            return 'Vector({})'.format(components)
            # -----------------------------------------------
            # array('d', [0.0, 1.0, 2.0, 3.0, 4.0, ...])
            #            ------------------------------
            #                      sub-string
            # Vector([0.0, 1.0, 2.0, 3.0, 4.0, ...])
            # -> can be used for Vector construction
            # -----------------------------------------------

        def __str__(self):
            return str(tuple(self))
            # (0.0, 1.0, 2.0, 3.0, 4.0, ...)

        def __bytes__(self):
            return (bytes([ord(self.typecode)]) + bytes(self._components))
            #                                     -----------------------
            #                                     invokes array's __repr__ 

        def __eq__(self, other):
            return tuple(self) == tuple(other)
            #      -----------
            #      invokes __iter__()

        def __abs__(self):
            return math.sqrt(sum(x * x for x in self)) # x**2

        def __bool__(self):
            return bool(abs(self))

        def __len__(self): # for len(obj)
            return len(self._components)

        def __getitem__(self, index): # indexing & iteration
            cls = type(self)
            if isinstance(index, slice): # 'slice' type can be used for indexing!
                return cls(self._components[index]) # returns a new Vector object(sub-array)
            elif isinstance(index, numbers.Integral):
                return self._components[index]
            else:
                message = '{cls.__name__} indices must be integers'
                raise TypeError(message.format(cls=cls))

        shortcut_names = 'xyzt'

        def __getattr__(self, name):
            cls = type(self) 
            if len(name) == 1: 
                pos = cls.shortcut_names.find(name) 
                if 0 <= pos < len(self._components): 
                    return self._components[pos]
            # 2 exceptions
            # ; vector is too short for accessing
            # ; wrong attribute name
            msg = '{.__name__!r} object has no attribute {!r}' 
            raise AttributeError(msg.format(cls, name))

        def __setattr__(self, name, value):
            "settattr not allowed for immutability(hashable)"
            cls = type(self)
            if len(name) == 1: 
                if name in cls.shortcut_names: 
                    error = 'readonly attribute {attr_name!r}'
                elif name.islower(): 
                    error = "can't set attributes 'a' to 'z' in {cls_name!r}"
                else:
                    error = '' 

                if error: 
                    msg = error.format(cls_name=cls.__name__, attr_name=name)
                    raise AttributeError(msg)
            super().__setattr__(name, value)

        pass

    print('\n# - vector take #1: vector2d compatible')
    v3 = Vector([3.0, 4.0, 5.0])
    printv(v3) # __str__
    printv(repr(v3)) # __repr__
    printv(len(v3)) # __len__
    printv(v3[1]) # indexing
    printv(v3[-1])
    # v3 = (3.0, 4.0, 5.0)
    # repr(v3) = Vector([3.0, 4.0, 5.0])
    # len(v3) = 3
    # v3[1] = 4.0
    # v3[-1] = 5.0

    print('\n# - vector take #2: a sliceable sequence')

    v7 = Vector(range(7))
    printv(v7)
    printv(repr(v7))
    printv(repr(v7[1:4])) # slicing
    printv(repr(v7[-1:])) # slicing
    # v7 = (0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0)
    # repr(v7) = Vector([0.0, 1.0, 2.0, 3.0, 4.0, ...])
    # repr(v7[1:4]) = Vector([1.0, 2.0, 3.0])
    # repr(v7[-1:]) = Vector([6.0])

    if False:
        printv(v7[1,2]) # illegal slicing
        # TypeError: Vector indices must be integers

    print('\n# - vector take #3: dynamic attribute access with names')
    print('v7.x =', v7.x)
    print('v7.y =', v7.y)
    print('v7.z =', v7.z)
    print('v7.t =', v7.t)

    if False:
        # the followings are not allowed
        v7.x = 10.0 # AttributeError: readonly attribute 'x'
        v7.p = 10.0 # AttributeError: can't set attributes 'a'
                    #                 to 'z' in 'Vector'

    # hashing
    # print(hash(v7))
    # -> TypeError: unhashable type: 'Vector'


if False:
    # - vector take #4: hashing and a faster ==
    # ; implementing __hash__ to make objects hashable
    # ; __eq__ improved for efficiency
    # ; Vector([1.0, 2.0]) == (1, 2) -> True
    from array import array
    import reprlib # to produce limited-length representations,
    import math
    import numbers
    import operator # xor
    import functools # reduce

    class Vector:
        typecode = 'd' # double, 'f' -> float

        def __init__(self, components):
            self._components = array(self.typecode, components) 
            #                                       ----------
            #                                       a sequence(iterable),
            #                                       not multiple args

        @classmethod
        def frombytes(cls, octets):
            typecode = chr(octets[0])
            memv = memoryview(octets[1:]).cast(typecode)
            return cls(memv)

        def __iter__(self):
            # iter() will invoke this!
            return iter(self._components)

        def __repr__(self):
            components = reprlib.repr(self._components) # -> str
            components = components[components.find('['):-1] 
            return 'Vector({})'.format(components)
            # -----------------------------------------------
            # array('d', [0.0, 1.0, 2.0, 3.0, 4.0, ...])
            #            ------------------------------
            #                      sub-string
            # Vector([0.0, 1.0, 2.0, 3.0, 4.0, ...])
            # -> can be used for Vector construction
            # -----------------------------------------------

        def __str__(self):
            return str(tuple(self))
            # (0.0, 1.0, 2.0, 3.0, 4.0, ...)

        def __bytes__(self):
            return (bytes([ord(self.typecode)]) + bytes(self._components))
            #                                     -----------------------
            #                                     invokes array's __repr__ 

        #def __eq__(self, other):
        #    return tuple(self) == tuple(other)
        #def __eq__(self, other):
        #    if len(self) != len(other):
        #        return False
        #    # len(self) == len(other) now
        #    for a, b in zip(self, other):
        #        if a != b:
        #            return False
        #    return True
        # -> simpler coding follows:
        def __eq__(self, other):
            return len(self) == len(other) and all(a == b for a, b in zip(self, other))

        #def __hash__(self):
        #    hashes = map(hash, self._components) # map() also returns a generator
        #    return functools.reduce(operator.xor, hashes)
        def __hash__(self):
            hashes = (hash(x) for x in self._components) # generator expr -> lazy computation
            return functools.reduce(operator.xor, hashes, 0)
            #                                             |
            #                                    deal with empty vector

        def __abs__(self):
            return math.sqrt(sum(x * x for x in self)) # x**2

        def __bool__(self):
            return bool(abs(self))

        def __len__(self): # for len(obj)
            return len(self._components)

        def __getitem__(self, index): # indexing & iteration
            cls = type(self)
            if isinstance(index, slice): # 'slice' type can be used for indexing!
                return cls(self._components[index]) # returns a new Vector object(sub-array)
            elif isinstance(index, numbers.Integral):
                return self._components[index]
            else:
                message = '{cls.__name__} indices must be integers'
                raise TypeError(message.format(cls=cls))

        shortcut_names = 'xyzt'

        def __getattr__(self, name):
            cls = type(self) 
            if len(name) == 1: 
                pos = cls.shortcut_names.find(name) 
                if 0 <= pos < len(self._components): 
                    return self._components[pos]
            # 2 exceptions
            # ; vector is too short for accessing
            # ; wrong attribute name
            msg = '{.__name__!r} object has no attribute {!r}' 
            raise AttributeError(msg.format(cls, name))

        def __setattr__(self, name, value):
            "settattr not allowed for immutability(hashable)"
            cls = type(self)
            if len(name) == 1: 
                if name in cls.shortcut_names: 
                    error = 'readonly attribute {attr_name!r}'
                elif name.islower(): 
                    error = "can't set attributes 'a' to 'z' in {cls_name!r}"
                else:
                    error = '' 

                if error: 
                    msg = error.format(cls_name=cls.__name__, attr_name=name)
                    raise AttributeError(msg)
            super().__setattr__(name, value)

        pass

    print('\n# - vector take #1: vector2d compatible')
    v3 = Vector([3.0, 4.0, 5.0])
    printv(v3) # __str__
    printv(repr(v3)) # __repr__
    printv(len(v3)) # __len__
    printv(v3[1]) # indexing
    printv(v3[-1])
    # v3 = (3.0, 4.0, 5.0)
    # repr(v3) = Vector([3.0, 4.0, 5.0])
    # len(v3) = 3
    # v3[1] = 4.0
    # v3[-1] = 5.0

    print('\n# - vector take #2: a sliceable sequence')

    v7 = Vector(range(7))
    printv(v7)
    printv(repr(v7))
    printv(repr(v7[1:4])) # slicing
    printv(repr(v7[-1:])) # slicing
    # v7 = (0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0)
    # repr(v7) = Vector([0.0, 1.0, 2.0, 3.0, 4.0, ...])
    # repr(v7[1:4]) = Vector([1.0, 2.0, 3.0])
    # repr(v7[-1:]) = Vector([6.0])

    if False:
        printv(v7[1,2]) # illegal slicing
        # TypeError: Vector indices must be integers

    print('\n# - vector take #3: dynamic attribute access with names')
    print('v7.x =', v7.x)
    print('v7.y =', v7.y)
    print('v7.z =', v7.z)
    print('v7.t =', v7.t)

    if False:
        # the followings are not allowed
        v7.x = 10.0 # AttributeError: readonly attribute 'x'
        v7.p = 10.0 # AttributeError: can't set attributes 'a'
                    #                 to 'z' in 'Vector'

    print('\n# - vector take #4: hashing and a faster ==')
    print('hash(v7) =', hash(v7))

    import random
    container = set()
    for i in range(100):
        dims = random.randint(1, 9)
        container.add(Vector((random.random() for _ in range(dims))))
    if hash(container.pop()):
        print('now vector object is hashable ...')
    print('len(container set) =', len(container))


if False:
    # - vector take #5: formatting
    # ; __format__ method implemented for format()
    # ; https://en.wikipedia.org/wiki/N-sphere
    from array import array
    import reprlib # to produce limited-length representations,
    import math
    import numbers
    import operator # xor
    import functools # reduce
    import itertools

    class Vector:
        typecode = 'd' # double, 'f' -> float

        def __init__(self, components):
            self._components = array(self.typecode, components) 
            #                                       ----------
            #                                       a sequence(iterable),
            #                                       not multiple args

        @classmethod
        def frombytes(cls, octets):
            typecode = chr(octets[0])
            memv = memoryview(octets[1:]).cast(typecode)
            return cls(memv)

        def __iter__(self):
            # iter() will invoke this!
            return iter(self._components)

        def __repr__(self):
            components = reprlib.repr(self._components) # -> str
            components = components[components.find('['):-1] 
            return 'Vector({})'.format(components)
            # -----------------------------------------------
            # array('d', [0.0, 1.0, 2.0, 3.0, 4.0, ...])
            #            ------------------------------
            #                      sub-string
            # Vector([0.0, 1.0, 2.0, 3.0, 4.0, ...])
            # -> can be used for Vector construction
            # -----------------------------------------------

        def __str__(self):
            return str(tuple(self))
            # (0.0, 1.0, 2.0, 3.0, 4.0, ...)

        def __bytes__(self):
            return (bytes([ord(self.typecode)]) + bytes(self._components))
            #                                     -----------------------
            #                                     invokes array's __repr__ 

        #def __eq__(self, other):
        #    return tuple(self) == tuple(other)
        #def __eq__(self, other):
        #    if len(self) != len(other):
        #        return False
        #    # len(self) == len(other) now
        #    for a, b in zip(self, other):
        #        if a != b:
        #            return False
        #    return True
        # -> simpler coding follows:
        def __eq__(self, other):
            return len(self) == len(other) and all(a == b for a, b in zip(self, other))

        #def __hash__(self):
        #    hashes = map(hash, self._components) # map() also returns a generator
        #    return functools.reduce(operator.xor, hashes)
        def __hash__(self):
            hashes = (hash(x) for x in self._components) # generator expr -> lazy computation
            return functools.reduce(operator.xor, hashes, 0)
            #                                             |
            #                                    deal with empty vector

        def __abs__(self):
            return math.sqrt(sum(x * x for x in self)) # x**2

        def __bool__(self):
            return bool(abs(self))

        def __len__(self): # for len(obj)
            return len(self._components)

        def __getitem__(self, index): # indexing & iteration
            cls = type(self)
            if isinstance(index, slice): # 'slice' type can be used for indexing!
                return cls(self._components[index]) # returns a new Vector object(sub-array)
            elif isinstance(index, numbers.Integral):
                return self._components[index]
            else:
                message = '{cls.__name__} indices must be integers'
                raise TypeError(message.format(cls=cls))

        shortcut_names = 'xyzt'

        def __getattr__(self, name):
            cls = type(self) 
            if len(name) == 1: 
                pos = cls.shortcut_names.find(name) 
                if 0 <= pos < len(self._components): 
                    return self._components[pos]
            # 2 exceptions
            # ; vector is too short for accessing
            # ; wrong attribute name
            msg = '{.__name__!r} object has no attribute {!r}' 
            raise AttributeError(msg.format(cls, name))

        def __setattr__(self, name, value):
            "settattr not allowed for immutability(hashable)"
            cls = type(self)
            if len(name) == 1: 
                if name in cls.shortcut_names: 
                    error = 'readonly attribute {attr_name!r}'
                elif name.islower(): 
                    error = "can't set attributes 'a' to 'z' in {cls_name!r}"
                else:
                    error = '' 

                if error: 
                    msg = error.format(cls_name=cls.__name__, attr_name=name)
                    raise AttributeError(msg)
            super().__setattr__(name, value)

        def angle(self, n): 
            r = math.sqrt(sum(x * x for x in self[n:]))
            a = math.atan2(r, self[n-1])
            if (n == len(self) - 1) and (self[-1] < 0):
                return math.pi * 2 - a
            else:
                return a

        def angles(self): 
            return (self.angle(n) for n in range(1, len(self)))

        def __format__(self, fmt_spec=''):
            if fmt_spec.endswith('h'): # hyperspherical coordinates
                fmt_spec = fmt_spec[:-1]
                coords = itertools.chain([abs(self)], self.angles()) 
                outer_fmt = '<{}>' 
            else:
                coords = self
                outer_fmt = '({})' 
            components = (format(c, fmt_spec) for c in coords)
            return outer_fmt.format(', '.join(components))

        pass

    print('\n# - vector take #1: vector2d compatible')
    v3 = Vector([3.0, 4.0, 5.0])
    printv(v3) # __str__
    printv(repr(v3)) # __repr__
    printv(len(v3)) # __len__
    printv(v3[1]) # indexing
    printv(v3[-1])
    # v3 = (3.0, 4.0, 5.0)
    # repr(v3) = Vector([3.0, 4.0, 5.0])
    # len(v3) = 3
    # v3[1] = 4.0
    # v3[-1] = 5.0

    print('\n# - vector take #2: a sliceable sequence')

    v7 = Vector(range(7))
    printv(v7)
    printv(repr(v7))
    printv(repr(v7[1:4])) # slicing
    printv(repr(v7[-1:])) # slicing
    # v7 = (0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0)
    # repr(v7) = Vector([0.0, 1.0, 2.0, 3.0, 4.0, ...])
    # repr(v7[1:4]) = Vector([1.0, 2.0, 3.0])
    # repr(v7[-1:]) = Vector([6.0])

    if False:
        printv(v7[1,2]) # illegal slicing
        # TypeError: Vector indices must be integers

    print('\n# - vector take #3: dynamic attribute access with names')
    print('v7.x =', v7.x)
    print('v7.y =', v7.y)
    print('v7.z =', v7.z)
    print('v7.t =', v7.t)

    if False:
        # the followings are not allowed
        v7.x = 10.0 # AttributeError: readonly attribute 'x'
        v7.p = 10.0 # AttributeError: can't set attributes 'a'
                    #                 to 'z' in 'Vector'

    print('\n# - vector take #4: hashing and a faster ==')
    print('hash(v7) =', hash(v7))

    import random
    container = set()
    for i in range(100):
        dims = random.randint(1, 9)
        container.add(Vector((random.random() for _ in range(dims))))
    if hash(container.pop()):
        print('now vector object is hashable ...')
    print('len(container set) =', len(container))

    print('\n# - vector take #5: formatting')
    print('- testing format() with cartesian coordinates in 2d')
    print(format(Vector([3, 4])))
    print(format(Vector([3, 4]), '.2f'))
    print(format(Vector([3, 4]), '.3e'))
    # - testing format() with cartesian coordinates in 2d
    # (3.0, 4.0)
    # (3.00, 4.00)
    # (3.000e+00, 4.000e+00)

    print('- testing format() with cartesian coordinates in 3d and 7d')
    print(format(Vector([3, 4, 5])))
    print(format(Vector(range(7))))
    # - testing format() with cartesian coordinates in 3d and 7d
    # (3.0, 4.0, 5.0)
    # (0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0)

    print('- testing format() with spherical coordinates in 2d, 3d and 4d')
    print(format(Vector([1, 1]), 'h'))
    print(format(Vector([1, 1]), '.3eh'))
    print(format(Vector([1, 1]), '0.5fh'))
    print(format(Vector([1, 1, 1]), 'h'))
    print(format(Vector([2, 2, 2]), '.3eh'))
    print(format(Vector([0, 0, 0]), '0.5fh'))
    print(format(Vector([-1, -1, -1, -1]), 'h'))
    print(format(Vector([2, 2, 2, 2]), '.3eh'))
    print(format(Vector([0, 1, 0, 0]), '0.5fh'))
    # - testing format() with spherical coordinates in 2d, 3d and 4d
    # <1.4142135623730951, 0.7853981633974483>
    # <1.414e+00, 7.854e-01>
    # <1.41421, 0.78540>
    # <1.7320508075688772, 0.9553166181245093, 0.7853981633974483>
    # <3.464e+00, 9.553e-01, 7.854e-01>
    # <0.00000, 0.00000, 0.00000>
    # <2.0, 2.0943951023931957, 2.186276035465284, 3.9269908169872414>
    # <4.000e+00, 1.047e+00, 9.553e-01, 7.854e-01>
    # <1.00000, 1.57080, 0.00000, 0.00000>



# -------------------------------------
# chapter 11: interfaces: from protocols to abcs
# ; abc -> abstract base class

# - interface
# ; the subset of an object¡¯s public methods that enable it to play a
#   specific role in the system
# ; protocol -> an informal wording
# ; x-like object, x protocol and x interface

if False:
    # - monkey-patching to implement a protocol at runtime
    # ; __getitem__ and __len__ -> enough to sequence-like behavior
    # ; but cannot be shuffled because it's not mutable (immutable)
    # ; monkey patching to support shuffling (container-like behavior)
    #   changing a class or module at runtime, without touching the source code
    # ; __setitem__ required
    # ; duck typing
    #   operating with objects regardless of their types is possible,
    #   as long as they implement certain protocols
    # - monkey patch
    # ; a technique used to dynamically update the behavior of code at run-time.
    # ; https://en.wikipedia.org/wiki/Monkey_patch
    import collections
    import functools
    from random import choice, shuffle

    # decorator for debugging
    def debug(func):
        def wrapper(*args):
            print("[dgb ] {}() invoked ...".format(func.__name__))
            decorated = func(*args)
            return decorated
        return wrapper
    
    # the following defines 'Card' type
    Card = collections.namedtuple('Card', ['rank', 'suit'])
    
    class FrenchDeck:
        """
        - implementation of __len__ and __getitem__ is important
        for sequence-like behavior!!!
        ; iteration and slicing
        ; used for built-in reversed() and sorted()
        """
        ranks = [str(n) for n in range(2, 11)] + list('JQKA')
        suits = 'spades diamonds clubs hearts'.split()
        if False:
            print("[info] ranks=", ranks)
            print("[info] suits=", suits)
            print("[info] len(ranks)=", len(ranks))
            print("[info] len(suits)=", len(suits))
        
        #@debug
        def __init__(self):
            # underlying data structure -> list
            self._cards = [Card(rank, suit) for suit in self.suits
                                            for rank in self.ranks]
        #@debug
        def __len__(self):
            return len(self._cards)
    
        #@debug
        def __getitem__(self, position):
            return self._cards[position] # ':' slicing also supported

        #@debug
        def __str__(self):
            cards = []
            for i, card in enumerate(self):
                cards.append('card[{:2d}] = {}'.format(i, card))
            return '\n'.join(cards)
        pass

    cards = FrenchDeck()
    print("\n# len(cards) =", len(cards))
    print(cards) # __str__

    print("\n# suffling without __setitem__")
    print("TypeError: 'FrenchDeck' object does not support item assignment")
    if False:
        shuffle(cards)

    print("\n# suffling with __setitem__")
    def set_card(deck, position, card):
        deck._cards[position] = card
    FrenchDeck.__setitem__ = set_card # monkey-patch!
    shuffle(cards)
    print(cards) # __str__
    # random.shuffle doesn't care what type of argument it gets, but
    # needs the object to implement part of the mutable sequence protocol
    # -> should be mutable with __setitem__

if False:
    # - subclassing an ABC
    # ; all the necessary methods must be implemented
    # ; 'TypeError' if not provided
    import collections
    import functools
    from random import choice, shuffle

    # the following defines 'Card' type
    Card = collections.namedtuple('Card', ['rank', 'suit'])
    
    class FrenchDeck(collections.MutableSequence):
        """
        FrenchDeck is derived from 'collections.MutableSequence'
        """
        ranks = [str(n) for n in range(2, 11)] + list('JQKA')
        suits = 'spades diamonds clubs hearts'.split()
        if False:
            print("[info] ranks=", ranks, "len=", len(ranks))
            print("[info] suits=", suits, "len=", len(suits))
        
        def __init__(self):
            # underlying data structure -> list
            self._cards = [Card(rank, suit) for suit in self.suits
                                            for rank in self.ranks]
        pass

    cards = FrenchDeck()
    # --------------------------------------------------------------------
    # TypeError: Can't instantiate abstract class FrenchDeck with abstract
    # methods __delitem__, __getitem__, __len__, __setitem__, insert
    # -> this will be checked at run-time, not import-time!
    # --------------------------------------------------------------------

if False:
    # - subclassing an ABC
    # ; all the necessary methods must be implemented
    # ; 'TypeError' if not provided
    import collections.abc
    import functools
    from random import choice, shuffle

    # the following defines 'Card' type
    Card = collections.namedtuple('Card', ['rank', 'suit'])
    
    class FrenchDeck(collections.abc.MutableSequence):
        """
        FrenchDeck is derived from 'collections.MutableSequence'
        """
        ranks = [str(n) for n in range(2, 11)] + list('JQKA')
        suits = 'spades diamonds clubs hearts'.split()
        if False:
            print("[info] ranks=", ranks, "len=", len(ranks))
            print("[info] suits=", suits, "len=", len(suits))
        
        def __init__(self):
            # underlying data structure -> list
            self._cards = [Card(rank, suit) for suit in self.suits
                                            for rank in self.ranks]
        def __delitem__(self, position):
            del self._cards[position]

        def __getitem__(self, position):
            return self._cards[position] # ':' slicing also supported
    
        def __len__(self):
            return len(self._cards)
    
        def __setitem__(self, position, value):
            self._cards[position] = value

        def insert(self, position, value):
            self._cards.insert(position, value)

        pass

    cards = FrenchDeck()
    print("\n# len(cards) =", len(cards))
    print(cards) # no __str__, __repr__ will be invoked

    print("\n# suffling with __setitem__")
    shuffle(cards)
    print(cards) # __str__, __repr__ will be invoked
    # random.shuffle doesn't care what type of argument it gets, but
    # needs the object to implement part of the mutable sequence protocol
    # -> should be mutable with __setitem__

    print('\n# implementing __str__ with monky-patch')
    def dump_deck(self):
        cards = []
        for i, card in enumerate(self):
            cards.append('card[{}] = {}'.format(i, card))
        return '\n'.join(cards)
    FrenchDeck.__str__ = dump_deck
    print(cards)

    print('\n# printing __mro__')
    from utilities import print_mro
    print_mro(FrenchDeck)
    # printing __mro__
    # FrenchDeck, MutableSequence, Sequence, Reversible, Collection, Sized,
    # Iterable, Container, object


# -------------------------------------
# chapter 12: inheritance: for good or for worse
# ; the pitfalls of subclassing from built-in types
# ; multiple inheritance and the method resolution order

if False:
    # ------------------------------------------------------------------------
    # - subclassing built-in types is tricky
    # ; the code of the built-ins (written in C) does not call special methods
    #   overridden by user-defined classes
    #   -> might be surprising
    # ; so don't override ready-made methods when subclassing built-in type
    # - [note]
    # ; subclassing built-in types like dict or list or str directly is
    #   error-prone because the built-in methods mostly ignore user-defined
    #   overrides.
    # ; instead of subclassing the built-ins, derive your classes from the
    #   collections module using UserDict, UserList, and UserString, which are
    #   designed to be easily extended.
    # ------------------------------------------------------------------------
    pass

if False:
    # - multiple inheritance and method resolution order
    # ; diamond problem
    #   language implementing multiple inheritance needs to deal with potential
    #   naming conflicts when unrelated ancestor classes implement a method by
    #   the same name.
    # ; MRO(Method Resolution Order) of D
    class A:
        def ping(self):
            print('ping(A):', self)

    class B(A):
        def pong(self):
            print('pong(B):', self)

    class C(A):
        def pong(self):
            print('pong(C):', self)

    class D(B, C):
        def ping(self):
            super().ping() # will invoke A.ping(self)
            print('ping(D):', self)

        def pingpong(self):
            # ping test - which one?
            self.ping()
            super().ping()

            print()

            # pong test - which one?
            self.pong()    # B.pong(self)
            super().pong() # B.pong(self)
            C.pong(self)   # C.pong(self) -> ignore __mro__!


    d = D() # D's object

    d.pong()
    # (1) pong(B): <__main__.D object at 0x00000247E4227F70>
    # ; same as B.pong(d)
    # ; resoved because Python follows a specific order when traversing the
    #   inheritance graph -> MRO

    print('D.__mro__ =', D.__mro__) # MRO information
    # D.__mro__ = (
    #   <class '__main__.D'>, <class '__main__.B'>,
    #   <class '__main__.C'>, <class '__main__.A'>,
    #   <class 'object'>
    # )

    C.pong(d)
    # (2) pong(C): <__main__.D object at 0x0000027843687F70>
    # -> with explicit arguement self=d

    print('\n# invoking ping()')
    d.ping()
    # ping(A): <__main__.D object at 0x00000277FD3E7F70>
    # ping(D): <__main__.D object at 0x00000277FD3E7F70>

    print('\n# invoking pingpong()')
    d.pingpong()
    # ping(A): <__main__.D object at 0x00000277FD3E7F70>
    # ping(D): <__main__.D object at 0x00000277FD3E7F70>
    # ping(A): <__main__.D object at 0x00000277FD3E7F70>
    # 
    # pong(B): <__main__.D object at 0x00000277FD3E7F70>
    # pong(B): <__main__.D object at 0x00000277FD3E7F70>
    # pong(C): <__main__.D object at 0x00000277FD3E7F70> -> __mro__ ignored!

    print('\n# printing __mro__')
    from utilities import print_mro
    import numbers
    import io
    print_mro(bool)
    print_mro(numbers.Integral)
    print_mro(io.BytesIO)
    print_mro(io.TextIOWrapper)
    # bool, int, object
    # Integral, Rational, Real, Complex, Number, object
    # BytesIO, _BufferedIOBase, _IOBase, object
    # TextIOWrapper, _TextIOBase, _IOBase, object


# -------------------------------------
# chapter 13: operator overloading: doing it right
# - problems of previous vector class
#   Vector(3, 4) == [3, 4] --> True!
# - limitations of python's operator overloading
# ; cannot overload operators for the built-in types.
# ; cannot create new operators, only overload existing ones.
# ; a few operators can't be overloaded: is, and, or, not 


if False:
    # - vector take #6: operator overloadiing
    from array import array
    import reprlib # to produce limited-length representations,
    import math
    import numbers
    import operator # xor
    import functools # reduce
    import itertools
    import numbers

    # decorator for debugging
    def trace(func):
        def wrapper(*args):
            print("[dgb ] {}() invoked ...".format(func.__name__))
            decorated = func(*args)
            return decorated
        return wrapper
    

    class Vector:
        typecode = 'd' # double, 'f' -> float

        def __init__(self, components):
            self._components = array(self.typecode, components) 
            #                                       ----------
            #                                       a sequence(iterable),
            #                                       not multiple args

        @classmethod
        def frombytes(cls, octets):
            typecode = chr(octets[0])
            memv = memoryview(octets[1:]).cast(typecode)
            return cls(memv)

        def __iter__(self):
            # iter() will invoke this!
            return iter(self._components)

        def __repr__(self):
            components = reprlib.repr(self._components) # -> str
            components = components[components.find('['):-1] 
            return 'Vector({})'.format(components)
            # -----------------------------------------------
            # array('d', [0.0, 1.0, 2.0, 3.0, 4.0, ...])
            #            ------------------------------
            #                      sub-string
            # Vector([0.0, 1.0, 2.0, 3.0, 4.0, ...])
            # -> can be used for Vector construction
            # -----------------------------------------------

        def __str__(self):
            return str(tuple(self))
            # (0.0, 1.0, 2.0, 3.0, 4.0, ...)

        def __bytes__(self):
            return (bytes([ord(self.typecode)]) + bytes(self._components))
            #                                     -----------------------
            #                                     invokes array's __repr__ 

        #def __hash__(self):
        #    hashes = map(hash, self._components) # map() also returns a generator
        #    return functools.reduce(operator.xor, hashes)
        def __hash__(self):
            hashes = (hash(x) for x in self._components) # generator expr -> lazy computation
            return functools.reduce(operator.xor, hashes, 0)
            #                                             |
            #                                    deal with empty vector

        def __len__(self): # for len(obj)
            return len(self._components)

        def __getitem__(self, index): # indexing & iteration
            cls = type(self)
            if isinstance(index, slice): # 'slice' type can be used for indexing!
                return cls(self._components[index]) # returns a new Vector object(sub-array)
            elif isinstance(index, numbers.Integral):
                return self._components[index]
            else:
                message = '{cls.__name__} indices must be integers'
                raise TypeError(message.format(cls=cls))

        shortcut_names = 'xyzt'

        def __getattr__(self, name):
            cls = type(self) 
            if len(name) == 1: 
                pos = cls.shortcut_names.find(name) 
                if 0 <= pos < len(self._components): 
                    return self._components[pos]
            # 2 exceptions
            # ; vector is too short for accessing
            # ; wrong attribute name
            msg = '{.__name__!r} object has no attribute {!r}' 
            raise AttributeError(msg.format(cls, name))

        def __setattr__(self, name, value):
            "settattr not allowed for immutability(hashable)"
            cls = type(self)
            if len(name) == 1: 
                if name in cls.shortcut_names: 
                    error = 'readonly attribute {attr_name!r}'
                elif name.islower(): 
                    error = "can't set attributes 'a' to 'z' in {cls_name!r}"
                else:
                    error = '' 

                if error: 
                    msg = error.format(cls_name=cls.__name__, attr_name=name)
                    raise AttributeError(msg)
            super().__setattr__(name, value)

        def angle(self, n): 
            r = math.sqrt(sum(x * x for x in self[n:]))
            a = math.atan2(r, self[n-1])
            if (n == len(self) - 1) and (self[-1] < 0):
                return math.pi * 2 - a
            else:
                return a

        def angles(self): 
            return (self.angle(n) for n in range(1, len(self)))

        def __format__(self, fmt_spec=''):
            if fmt_spec.endswith('h'): # hyperspherical coordinates
                fmt_spec = fmt_spec[:-1]
                coords = itertools.chain([abs(self)], self.angles()) 
                outer_fmt = '<{}>' 
            else:
                coords = self
                outer_fmt = '({})' 
            components = (format(c, fmt_spec) for c in coords)
            return outer_fmt.format(', '.join(components))

        # overloaded operators
        def __abs__(self):
            return math.sqrt(sum(x * x for x in self)) # x**2

        def __bool__(self):
            return bool(abs(self))

        def __neg__(self):
            return Vector(-x for x in self)
            #             ----------------
            #       iterable to create a new vector

        def __pos__(self):
            return Vector(self) 

        #def __add__(self, other):
        #    "operands can be any iterable with numeric items"
        #    pairs = itertools.zip_longest(self, other, fillvalue=0.0)
        #    return Vector(a + b for a, b in pairs)
        # -> for more friendly error message
        def __add__(self, other):
            """
            operands can be any iterable with numeric items
            In case of 'TypeError', it is often better to catch it
            and return 'NotImplemented'.
            """
            try:
                pairs = itertools.zip_longest(self, other, fillvalue=0.0)
                return Vector(a + b for a, b in pairs)
                #             -----------------------
                #                 generator-expr
            except TypeError:
                return NotImplemented

        def __radd__(self, other):
            "reversed version of __add__"
            return self + other

        def __mul__(self, scalar):
            if isinstance(scalar, numbers.Real):
                return Vector(n * scalar for n in self)
            else:
                return NotImplemented

        def __rmul__(self, scalar):
            return self * scalar

        @trace
        def __matmul__(self, other):
            "matrix multiplication"
            try:
                return sum(a * b for a, b in zip(self, other))
            except TypeError:
                return NotImplemented

        @trace
        def __rmatmul__(self, other):
            "reversed matrix multiplication"
            return self @ other

        #def __eq__(self, other):
        #    return tuple(self) == tuple(other)
        #def __eq__(self, other):
        #    if len(self) != len(other):
        #        return False
        #    # len(self) == len(other) now
        #    for a, b in zip(self, other):
        #        if a != b:
        #            return False
        #    return True
        # -> simpler coding follows:
        @trace
        def __eq__(self, other):
            if isinstance(other, Vector):
                return (
                    len(self) == len(other) and
                        all(a == b for a, b in zip(self, other))
                )
            else:
                "python will take care if other is not vector type"
                return NotImplemented

        pass


    if False:
        print('\n# - vector take #6: operator overloading')
        print('bool(Vector([3, 4, 5])) =', bool(Vector([3, 4, 5])))
        print('bool(Vector([0, 0, 0])) =', bool(Vector([0, 0, 0])))
        # bool(Vector([3, 4, 5])) = True
        # bool(Vector([0, 0, 0])) = False

        v1 = Vector([3, 4, 5])
        print('v1 =', v1)
        print('-v1 =', -v1)
        print('+v1 =', +v1)
        print('v1 == +v1 =', v1 == +v1)
        # v1 = (3.0, 4.0, 5.0)
        # -v1 = (-3.0, -4.0, -5.0)
        # +v1 = (3.0, 4.0, 5.0)
        # v1 == +v1 = True

        print('\n# test if vector is iterable')
        import collections.abc
        if isinstance(v1, collections.abc.Iterable):
            print('v1 is iterable!')
        else:
            print('v1 is not iterable!')
        # test if vector is iterable
        # v1 is iterable!

        print('\n# testing vector addition - __add__')
        v1 = Vector([3, 4, 5])
        v2 = Vector([6, 7, 8])
        print('v1 =', v1)
        print('v2 =', v2)
        print('v1 + v2 =', v1 + v2)
        print('v1 + v2 == Vector([3+6, 4+7, 5+8]) =', v1 + v2 == Vector([3+6, 4+7, 5+8]))

        print('\n# fill out the shortest Vector with zeros')
        v1 = Vector([3, 4, 5, 6])
        v2 = Vector([1, 2])
        print('v1 =', v1)
        print('v2 =', v2)
        print('v1 + v2 =', v1 + v2)

        print('\n# this is also possible')
        v1 = Vector([3, 4, 5])
        print('v1 =', repr(v1))
        print('v1 + (10, 20, 30) =', repr(v1 + (10, 20, 30)))
        # v1 = Vector([3.0, 4.0, 5.0])
        # v1 + (10, 20, 30) = Vector([13.0, 24.0, 35.0])


        print('\n# operations involving objects of different types - __radd__')
        v1 = Vector([3, 4, 5])
        print('v1 =', repr(v1))
        print('(10, 20, 30) + v1 =', repr((10, 20, 30) + v1))
        # tuple doesn't support 'tuple + vector'
        # -> vector.__radd__(tuple) invoked as a fall-back
        # v1 = Vector([3.0, 4.0, 5.0])
        # (10, 20, 30) + v1 = Vector([13.0, 24.0, 35.0])

        #print(v1 + 1)
        # -> Vector.__add__(v1, 1)
        # (1) TypeError: 'int' object is not iterable
        # (2) TypeError: unsupported operand type(s) for +: 'Vector' and 'int'

        #print(v1 + 'ABC')
        # -> Vector.__add__(v1, 'ABC')
        # (1) TypeError: unsupported operand type(s) for +: 'float' and 'str'
        # (2) TypeError: unsupported operand type(s) for +: 'Vector' and 'str'


        print('\n# overloading * for scalar multiplication - __add__')
        v1 = Vector([1, 2, 3])
        print('v1 =', repr(v1))
        print('v1 * 10 =', repr(v1 * 10))
        print('11 * v1 =', repr(11 * v1))
        print('v1 * True =', v1 * True)

        from fractions import Fraction
        print('v1 * Fraction(1, 3) =', v1 * Fraction(1, 3)) # 1/3 = 0.3333...
        # v1 = Vector([1.0, 2.0, 3.0])
        # v1 * 10 = Vector([10.0, 20.0, 30.0])
        # 11 * v1 = Vector([11.0, 22.0, 33.0])
        # v1 * True = (1.0, 2.0, 3.0)
        # v1 * Fraction(1, 3) = (0.3333333333333333, 0.6666666666666666, 1.0)
        
        print('\n# overloading @ for dot-product - __matmul__ & __rmatmul__')
        v1 = Vector([1, 2, 3])
        v2 = Vector([5, 6, 7])
        print('v1 =', repr(v1))
        print('v2 =', repr(v2))
        print('v1 @ v2q =', v1 @ v2)
        # v1 = Vector([1.0, 2.0, 3.0])
        # v2 = Vector([5.0, 6.0, 7.0])
        # [dgb ] __matmul__() invoked ...
        # v1 @ v2q = 38.0

        print('v1 @ [5, 6, 7] =', v1 @ [5, 6, 7])
        print('[5, 6, 7] @ v1 =', [5, 6, 7] @ v1)
        # [dgb ] __matmul__() invoked ...
        # v1 @ [5, 6, 7] = 38.0
        # [dgb ] __rmatmul__() invoked ...
        # [dgb ] __matmul__() invoked ...
        # [5, 6, 7] @ v1 = 38.0

        print('v1 @ 3 =', v1 @ 3)
        # [dgb ] __matmul__() invoked ...
        # TypeError: unsupported operand type(s) for @: 'Vector' and 'int'

    if False:
        # - rich comparison operators
        # ; __eq__ should be similar to '[1, 2] == (1, 2) -> False'
        # ; don't need implement '__ne__' because python will return
        #   'not a==b' as a fallback (default __ne__ inherited)
        print('\n# improved == operator with __eq__')
        v1 = Vector([1, 2, 3])
        v2 = Vector(range(1, 4))
        print('v1 =', repr(v1))
        print('v2 =', repr(v2))
        print('v1 == v2 =', v1 == v2)
        # v1 = Vector([1.0, 2.0, 3.0])
        # v2 = Vector([1.0, 2.0, 3.0])
        # v1 == v2 = True

        print('v1 == (1, 2, 3) =', v1 == (1, 2, 3))
        # python invokes both of the followings
        # (1) Vector.__eq__(v1, t3) -> NotImplemented
        # (2) tuple.__eq__(t3, v1) -> NotImplemented
        # (3) does 'id(v1) == id(t3)' -> False

    if False:
        # ; if a class does not implement the in-place operators listed, the
        #   augmented assignment operators are just syntactic sugar:
        #   a += b is evaluated exactly as a = a + b.
        # ; that¡¯s the expected behavior for immutable types, and if you have
        #   __add__ then += will work with no additional code.
        print('\n# augmented assignment operator +=')
        v1 = Vector([1, 2, 3])
        v1_ref = v1
        print('v1 =', repr(v1))
        print('id(v1) =', id(v1))
        print('v1_ref =', repr(v1_ref))
        print('id(v1_ref) =', id(v1_ref))

        v1 += Vector([4, 5, 6])
        print('v1 += Vector([4, 5, 6]) --->', repr(v1))
        print('id(v1) =', id(v1))
        print('v1_ref =', repr(v1_ref))
        print('id(v1_ref) =', id(v1_ref))

        v1 *= 11
        print('v1 *= 11 --->', repr(v1))
        print('id(v1) =', id(v1))
        print('v1_ref =', repr(v1_ref))
        print('id(v1_ref) =', id(v1_ref))
        # v1 = Vector([1.0, 2.0, 3.0])
        # id(v1) = 1845810869584
        # v1_ref = Vector([1.0, 2.0, 3.0])
        # id(v1_ref) = 1845810869584
        #
        # v1 += Vector([4, 5, 6]) ---> Vector([5.0, 7.0, 9.0])
        # id(v1) = 1845816157776
        # v1_ref = Vector([1.0, 2.0, 3.0])
        # id(v1_ref) = 1845810869584
        #
        # v1 *= 11 ---> Vector([55.0, 77.0, 99.0])
        # id(v1) = 1845816158352
        # v1_ref = Vector([1.0, 2.0, 3.0])
        # id(v1_ref) = 1845810869584


if False:
    # - BingoCage class for __add__ and __iadd__
    import random

    class BingoCage:
        def __init__(self, items):
            self._items = list(items) 
            random.shuffle(self._items) 

        def __repr__(self):
            return "%r" % self._items

        def pick(self):
            try:
                return self._items.pop()
            except LookupError:
                raise LookupError('pick from an empty BingoCage') 

        def __call__(self):
            "this makes self callable!"
            return self.pick()


    bingo = BingoCage(range(10))
    print("bingo=", bingo)
    # bingo= [5, 4, 3, 9, 8, 6, 0, 1, 7, 2]

    for i in range(10):
        if i % 2:
            print("pick[{}]= {}".format(i, bingo.pick()))
        else:
            print("pick[{}]= {}".format(i, bingo()))
        # bingo() does the same thing aas bingo.pick()

    print("callable(bingo)=", callable(bingo))
    # callable(bingo)= True


if False:
    # - pros and cons of operator overloading
    # ; it depends on your strategies and implementation.
    # ; don't be too confused!
    pass
