# vim: ft=python ts=4 sw=4 tw=78 expandtab
# -*- coding:utf-8 -*-
# ----------------------------------------------------------------------------
# - file : misc__builtin_list_inheritance.py
# - author : yc0325lee
# - created : 2022-10-29 19:35:28 by lee2103
# - modified : 2022-10-30 17:14:15 by lee2103
# - description : 
# ; https://realpython.com/inherit-python-list/
# ----------------------------------------------------------------------------
from utilities import printv
import re

if True:
    # ----------------------------------------
    # - inheriting from built-in list directly
    # ; can be good, but
    # ; there can be problems because python c interface doen't use
    #   special(magic) methods
    class AttrList(list):
        """
        [note] adding more functionalities on top of basic list operations
               all values are string (assumption, 221029_200936)
        """

        def all_contains(self, pattern, regex=False):
            if regex:
                return all(re.search(pattern, val) for val in self)
            else:
                return all(pattern in val for val in self)

        def any_contains(self, pattern, regex=False):
            if regex:
                return any(re.search(pattern, val) for val in self)
            else:
                return any(pattern in val for val in self)

        def contains(self, pattern, regex=False):
            return self.all_contains(pattern, regex=regex)

        def all_inside(self, pattern, regex=False): # pattern -> module
            if regex:
                return all(
                    any(
                        re.search(pattern, module) for module in sorted(modules, reverse=True)
                    ) for modules in self
                )
            else:
                return all(
                    any(
                        pattern in module for module in sorted(modules, reverse=True)
                    ) for modules in self
                )

        def inside(self, pattern, regex=False): # pattern -> module
            return self.all_inside(pattern, regex=regex)

if False:
    # ----------------------------------------
    # - inheriting from collections.UserList
    # ; designed for creating list-like objects back when it wasn¡¯t possible
    #   to inherit from the built-in list class directly
    # ; old way for convenience and bacward compatibility
    from collections import UserList
    class AttrList(UserList):
        """
        [note] data items are access by '.data' member
               'data' is built-in list type
               all values are string (assumption, 221029_200936)
        """
        def __init__(self, iterable):
            super().__init__(item for item in iterable)

        def __setitem__(self, index, item):
            self.data[index] = item

        def insert(self, index, item):
            self.data.insert(index, item)

        def append(self, item):
            self.data.append(item)

        def extend(self, other):
            if isinstance(other, type(self)):
                self.data.extend(other)
            else:
                self.data.extend(item for item in other)

        def all_contains(self, pattern, regex=False):
            if regex:
                return all(re.search(pattern, val) for val in self)
            else:
                return all(pattern in val for val in self)

        def any_contains(self, pattern, regex=False):
            if regex:
                return any(re.search(pattern, val) for val in self)
            else:
                return any(pattern in val for val in self)

        def contains(self, pattern, regex=False):
            return self.all_contains(pattern, regex=regex)

        def all_inside(self, pattern, regex=False): # pattern -> module
            if regex:
                return all(
                    any(
                        re.search(pattern, module) for module in sorted(modules, reverse=True)
                    ) for modules in self
                )
            else:
                return all(
                    any(
                        pattern in module for module in sorted(modules, reverse=True)
                    ) for modules in self
                )

        def inside(self, pattern, regex=False): # pattern -> module
            return self.all_inside(pattern, regex=regex)




if __name__ == '__main__':

    if False:
        print('\n# test for basic functionalities')
        a = AttrList(range(10))
        print(type(a))
        print(a)
        a.append(10)
        print(a)
        a += [11, 12]
        print(a)
        a.extend([13, 14, 15])
        print(a)
        a[0] = 17
        print(a)
        # <class '__main__.AttrList'>
        # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
        # [17, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

    if False:
        print('\n# testing contains() functions')
        Signal0 = AttrList('__abc__ __abc__ __abc__ __abc__ __abc__'.split()) # homogenous
        Module0 = AttrList([
            AttrList(['000', '000', '000', '000', 'aaa']),
            AttrList(['000', '000', '000', 'aaa', '000']),
            AttrList(['000', '000', 'aaa', '000', '000']),
            AttrList(['000', 'aaa', '000', '000', '000']),
            AttrList(['aaa', '000', '000', '000', '000']),
        ])
        print('\nSignal0 =', Signal0)
        print('Module0 =')
        for modules in Module0:
            print(modules)


        Signal1 = AttrList('__abc__ __abc__ __abx__ __abc__ __abc__'.split()) # heterogenous
        Module1 = AttrList([
            AttrList(['000', '000', '000', '000', 'aaa']),
            AttrList(['000', '000', '000', 'aaa', '000']),
            AttrList(['000', '000', 'xxx', '000', '000']),
            AttrList(['000', 'aaa', '000', '000', '000']),
            AttrList(['aa0', '000', '000', '000', '000']),
        ])
        print('\nSignal1 =', Signal1)
        print('Module1 =')
        for modules in Module0:
            print(modules)

        print('\n# re=False')
        print("Signal0.all_contains('abc') =", Signal0.all_contains('abc'))
        print("Signal1.all_contains('abc') =", Signal1.all_contains('abc'))
        print("Signal0.any_contains('abx') =", Signal0.any_contains('abx'))
        print("Signal1.any_contains('abx') =", Signal1.any_contains('abx'))
        print("Signal0.contains('abc') =", Signal0.contains('abc'))
        print("Signal1.contains('abx') =", Signal1.contains('abx'))
        print("Module0.all_inside('aaa') =", Module0.all_inside('aaa'))
        print("Module1.all_inside('aaa') =", Module1.all_inside('aaa'))

        print('\n# re=True')
        print("Signal0.all_contains('[abc]{{3}}', regex=True) =", Signal0.all_contains('[abc]{3}', regex=True))
        print("Signal1.all_contains('[abc]{{3}}', regex=True) =", Signal1.all_contains('[abc]{3}', regex=True))
        print("Signal0.any_contains('[abx]{{3}}', regex=True) =", Signal0.any_contains('[abx]{3}', regex=True))
        print("Signal1.any_contains('[abx]{{3}}', regex=True) =", Signal1.any_contains('[abx]{3}', regex=True))
        print("Signal0.contains('[abc]{{3}}', regex=True) =", Signal0.contains('[abc]{3}', regex=True))
        print("Signal1.contains('[abc]{{3}}', regex=True) =", Signal1.contains('[abc]{3}', regex=True))
        print("Module0.all_inside('a{{3}}', regex=True) =", Module0.all_inside('a{3}', regex=True))
        print("Module1.all_inside('a{{3}}', regex=True) =", Module1.all_inside('a{3}', regex=True))

        # re=False
        # Signal0.all_contains('abc') = True
        # Signal1.all_contains('abc') = False
        # Signal0.any_contains('abx') = False
        # Signal1.any_contains('abx') = True
        # Signal0.contains('abc') = True
        # Signal1.contains('abx') = False
        # Module0.all_inside('aaa') = True
        # Module1.all_inside('aaa') = False
        # 
        # re=True
        # Signal0.all_contains('[abc]{{3}}', regex=True) = True
        # Signal1.all_contains('[abc]{{3}}', regex=True) = False
        # Signal0.any_contains('[abx]{{3}}', regex=True) = False
        # Signal1.any_contains('[abx]{{3}}', regex=True) = True
        # Signal0.contains('[abc]{{3}}', regex=True) = True
        # Signal1.contains('[abc]{{3}}', regex=True) = False
        # Module0.all_inside('a{{3}}', regex=True) = True
        # Module1.all_inside('a{{3}}', regex=True) = False

    if True:
        # NumericList
        class NumberList(list):
            def __init__(self, iterable):
                super().__init__(self._validate_number(item) for item in iterable)

            def __setitem__(self, index, item):
                super().__setitem__(index, self._validate_number(item))

            def insert(self, index, item):
                super().insert(index, self._validate_number(item))

            def append(self, item):
                super().append(self._validate_number(item))

            def extend(self, other):
                if isinstance(other, type(self)):
                    super().extend(other)
                else:
                    super().extend(self._validate_number(item) for item in other)

            def _validate_number(self, value):
                if isinstance(value, (int, float, complex)):
                    return value
                else:
                    raise TypeError(
                        f"numeric value expected, but has got {type(value).__name__} type!"
                    )

        a = NumberList([1, 2, 3, 4])
        print(type(a), a)
        b = NumberList([1, 2, 3, 'four'])
        print(type(b), b)
        # <class '__main__.NumberList'> [1, 2, 3, 4]
        # TypeError: numeric value expected, but has got str type!
