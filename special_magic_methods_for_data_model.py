# vim: ft=python ts=4 sw=4 tw=78 expandtab
# -*- coding:utf-8 -*-
# ----------------------------------------------------------------------------
# - file : special_magic_methods_for_data_model.py
# - author : yc0325lee
# - created : 2022-11-10 23:11:04 by yc032
# - modified : 2022-11-10 23:11:04 by yc032
# - description : 
# ----------------------------------------------------------------------------

# See The "Data Model" chapter of The Python Language Reference 

# special method names (operators excluded)
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

# special method names for operators
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

if False:
    # - object.__init__(self[, ...])
    # ; called after the instance has been created (by __new__()), but before
    #   it is returned to the caller.
    # ; if a base class has an __init__() method, the derived class¡¯s
    #   __init__() method, if any, must explicitly call it to ensure proper
    #   initialization of the base class part of the instance
    # ; super().__init__([args, ...])
    pass

if False:
    # object.__call__(self[, args...])
    # ; called when the instance is ¡°called¡± as a function; if this method
    # is defined, x(arg1, arg2, ...) roughly translates to type(x).__call__(x, arg1, arg2, ...)
    pass

if False:
    # object.__iter__(self)
    # ; this method is called when an iterator is required for a container.
    #   this method should return a new iterator object that can iterate over
    #   all the objects in the container.
    # ; iter() invokes __iter__() method
    pass

if False:
    # - 'with' statement context managers
    # ; a context manager is an object that defines the runtime context to be
    #   established when executing a with statement.
    # ; usages
    #   saving and restoring various kinds of global state
    #   locking and unlocking resources
    #   closing opened files
    # - object.__enter__(self)
    # ; enter the runtime context related to this object
    # - object.__exit__(self, exc_type, exc_value, traceback)
    # ; exit the runtime context related to this object

    # ; __enter__ and __exit__ methods are invoked implicitly
    # ; (1) __enter__ is invoked on the context manager object
    # ; (2) __exit__ on the context manager object is invoked implicitly
    #       at the end of the with block
    with open("input.txt", "r", encoding="utf8") as inFile:
        for lineno, line in enumerate(inFile, 1):
            print(lineno + ": " + line, end="")
        # no need to close the opened file here! -> convenient!

if False:
    # - __repr__(self)
    # ; special method for repr() and print()
    # ; if no custom __str__() is available, python will call __repr__()
    #   instead as a fallback
    # ; %r or !r : standard representation of object using repr() built-in function
    # ; if not implemented -> <Vector object at 0x10e100070>
    # ; __repr__ is invoked by repr()
    # ; __str__ is invoked by str() <- print() will use str() by default
    class Vector:
        def __init__(self, x=0, y=0):
            self.x = x
            self.y = y

        def __repr__(self):
            #return 'Vector({!r}, {!r})' % (self.x, self.y)
            return 'Vector(%r, %r)' % (self.x, self.y)
            # Vector(1.0, 2.0)

        def __str__(self):
            return str((self.x, self.y))
            # (1.0, 2.0)

    def print_vector(obj):
        print('{!r}'.format(obj)) # not {:r}
    
    v1 = Vector(2, 4)
    print(v1) # (2, 4)
    print(repr(v1)) # Vector(2, 4)

if False:
    # ---------------------------------
    # - object.__getitem__(self, key)
    # ; called to implement evaluation of self[key]
    # - object.__setitem__(self, key, value)
    # ; called to implement assignment to self[key].
    pass
