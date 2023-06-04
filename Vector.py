# vim: ft=python ts=4 sw=4 tw=999 expandtab
# -*- coding:utf-8 -*-
# ----------------------------------------------------------------------------
# - file : Vector.py
# - author : yc0325lee
# - created : 2022-10-30 22:40:44 by lee2103
# - modified : 2022-10-30 22:40:44 by lee2103
# - description : 
# ----------------------------------------------------------------------------
# - vector take #1: vector2d compatible
# ; a user-defined sequence type
#
# - vector take #2: a sliceable sequence
# ; a user-defined sequence type
# ; for pythonic objects like FrenchDeck
#   __getitem__() -> index-ed accessing v[3], iteration, ...
#   __len__() -> len(deck)
#
# - vector take #2: a sliceable sequence
# ; slice-aware __getitem__
#
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
#
# - vector take #4: hashing and a faster ==
# ; implementing __hash__ to make objects hashable
# ; __eq__ improved for efficiency
# ; Vector([1.0, 2.0]) == (1, 2) -> True
#
# - vector take #5: formatting
# ; __format__ method implemented for format()
# ; https://en.wikipedia.org/wiki/N-sphere
# ----------------------------------------------------------------------------
from array import array
import reprlib # to produce limited-length representations,
import math
import numbers
import operator # xor
import functools # reduce
import itertools
from utilities import printv


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

    #@trace
    def __matmul__(self, other):
        "matrix multiplication"
        try:
            return sum(a * b for a, b in zip(self, other))
        except TypeError:
            return NotImplemented

    #@trace
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
    #def __eq__(self, other):
    #    return len(self) == len(other) and all(a == b for a, b in zip(self, other))
    #@trace
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



if __name__ == '__main__':

    if False:
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
    

    if False:
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
    

    if False:
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
    

    if False:
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


    if False:
        print('\n# - vector take #6: operator overloading - (1)')
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
        print('\n# - vector take #6: operator overloading - (2)')
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
        print('\n# - vector take #6: operator overloading - (3)')
        # ; if a class does not implement the in-place operators listed, the
        #   augmented assignment operators are just syntactic sugar:
        #   a += b is evaluated exactly as a = a + b.
        # ; that’s the expected behavior for immutable types, and if you have
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
