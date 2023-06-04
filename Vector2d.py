# vim: ft=python ts=4 sw=4 tw=999 expandtab
# -*- coding:utf-8 -*-
# ----------------------------------------------------------------------------
# File : Vector2d.py
# Author : yc0325lee
# Created : 2022-10-10 21:11:08 by lee2103
# Modified : 2022-10-10 21:11:08 by lee2103
# Description : 
# - object representations
# ; built-in : repr(), str()
# ; magic method to support representations
#   repr()   -> __repr__() invoked
#   str()    -> __str__() invoked
#   format() -> __format__() invoked
#   bytes()  -> __bytes__() invoked
# ----------------------------------------------------------------------------
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
        #                                          -----
        #                                          unpacking invokes
        #                                          __iter__()

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



if __name__ == '__main__':

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
