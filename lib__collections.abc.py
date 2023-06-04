# vim: ft=python ts=4 sw=4 tw=78 expandtab
# -*- coding:utf-8 -*-
# ----------------------------------------------------------------------------
# - file : lib__collections.abc.py
# - author : yc0325lee
# - created : 2022-10-19 23:55:54 by lee2103
# - modified : 2022-10-19 23:55:54 by lee2103
# - description : 
# ; this module provides abstract base classes that can be used to test
#   whether a class provides a particular interface; for example, whether it is
#   hashable or whether it is a mapping.
# ----------------------------------------------------------------------------
import collections
import collections.abc

if False:
    # (1) inheriting from collections.abc.Sequence
    class SomeClass(collections.abc.Sequence):
        def __getitem__(self):
            "TypeError if not provided"
            pass

        def __len__(self):
            "TypeError if not provided"
            pass

    someobj = SomeClass()

    print('\n(1) inheriting from collections.abc.Sequence')
    print('issubclass(SomeClass, collections.abc.Sequence) =',
        issubclass(SomeClass, collections.abc.Sequence))
    print('isinstance(some, collections.abc.Sequence) =',
        isinstance(someobj, collections.abc.Sequence))
    # issubclass(SomeClass, collections.abc.Sequence) = True
    # isinstance(some, collections.abc.Sequence) = True


if False:
    # (2) testing if SomeClass satisfies a protocol
    class SomeClass:
            pass

    someobj = SomeClass()

    print('\n(2) testing if SomeClass satisfies a protocol')
    print('issubclass(SomeClass, collections.abc.Sequence) =',
        issubclass(SomeClass, collections.abc.Sequence))
    print('isinstance(some, collections.abc.Sequence) =',
        isinstance(someobj, collections.abc.Sequence))
    # issubclass(SomeClass, collections.abc.Sequence) = False
    # isinstance(some, collections.abc.Sequence) = False


if False:
    # (3) testing if SomeClass satisfies a protocol
    class SomeClass:
        def __getitem__(self):
            pass
        def __len__(self):
            pass
        pass

    # we need this! why? 221110_120526
    # ; an interface is more than just the presence of method names.
    collections.abc.Sequence.register(SomeClass)

    someobj = SomeClass()

    print('\n(3) testing if SomeClass satisfies a protocol')
    print('issubclass(SomeClass, collections.abc.Sequence) =',
        issubclass(SomeClass, collections.abc.Sequence))
    print('isinstance(some, collections.abc.Sequence) =',
        isinstance(someobj, collections.abc.Sequence))
    # issubclass(SomeClass, collections.abc.Sequence) = True
    # isinstance(some, collections.abc.Sequence) = True


if False:
    class CustomDict(collections.UserDict):
        pass

    lookup = CustomDict()
    lookup['a'] = 0
    lookup['b'] = 1
    lookup['c'] = 2
    lookup['d'] = 3
    lookup['e'] = 4

    print("\nlookup=", lookup, type(lookup))
    # lookup= {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4} <class '__main__.CustomDict'>

    print("\nlookup.data=", lookup.data, type(lookup.data))
    # lookup.data= {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4} <class 'dict'>

    if 'f' in lookup:
        print("f found!")
    else:
        print("f not found!")
