#!/usr/bin/env python
# -*- coding:utf-8 -*-
# vim: ft=python ts=4 sw=4 tw=78 expandtab
# ----------------------------------------------------------------------------
# - file : 08_06_creating_managed_attributes.py
# - author : yc0325lee
# - created : 2022-11-21 23:59:11 by yc032
# - modified : 2022-11-21 23:59:11 by yc032
# - description : 
# ----------------------------------------------------------------------------

if False:
    # - extra processing (e.g., type checking or validation) to the getting or
    #   setting of an instance attribute.
    class Person:
        def __init__(self, first_name):
            self.first_name = first_name # invokes setter() -> type checking!
        
        @property # getter function
        def first_name(self):
            return self._first_name
     
        @first_name.setter # setter function
        def first_name(self, value):
            if not isinstance(value, str):
                raise TypeError('expected a string for first_name')
            self._first_name = value
     
        # deleter function (optional)
        @first_name.deleter
        def first_name(self):
            raise AttributeError("can't delete attribute")

        def __str__(self):
            return self.first_name

    person = Person('Guido')
    print('person=', person)
    print('person.first_name=', person.first_name) # calls getter
    if False:
        person.first_name = 42 # calls setter -> TypeError!
    if False:
        del person.first_name # calls deleter -> AttributeError!



if False:
    # - the followings are also possible
    class Person:
        def __init__(self, first_name):
            self.set_first_name(first_name)
     
        # getter function
        def get_first_name(self):
            return self._first_name
     
        # setter function
        def set_first_name(self, value):
            if not isinstance(value, str):
                raise TypeError('Expected a string')
            self._first_name = value

        # deleter function (optional)
        def del_first_name(self):
            raise AttributeError("Can't delete attribute")
     
        # make a property from existing get/set methods
        first_name = property(get_first_name, set_first_name, del_first_name)
        #               --------------  --------------  --------------
        #                   getter          setter         deleter


    print('Person.first_name.fget=', Person.first_name.fget)
    print('Person.first_name.fset=', Person.first_name.fset)
    print('Person.first_name.fdel=', Person.first_name.fdel)
    # Person.first_name.fget= <function Person.get_first_name at 0x0000014EFB0427A0>
    # Person.first_name.fset= <function Person.set_first_name at 0x0000014EFB042980>
    # Person.first_name.fdel= <function Person.del_first_name at 0x0000014EFB0428E0>
    # -> [note] these functions are invoked implicitly!


if False:
    # on-the-fly attributes
    import math
    class Circle:
        def __init__(self, radius):
            self.radius = radius

        @property
        def area(self):
            return math.pi * self.radius ** 2

        @property
        def perimeter(self):
            return 2 * math.pi * self.radius

        def __str__(self):
            return 'radius= {:.6f}, area= {:.6f}, perimeter= {:.6f}'.format(
                self.radius, self.area, self.perimeter
            )

        # --------------------------------------------------------
        # [note] area and perimeter are read-only properties here!
        # --------------------------------------------------------

    circle = Circle(4.0)
    print(circle)
    print('circle.area=', circle.area) # area() invoked
    print('circle.perimeter=', circle.perimeter) # perimeter() invoked
    # radius= 4.000000, area= 50.265482, perimeter= 25.132741
    # circle.area= 50.26548245743669
    # circle.perimeter= 25.132741228718345


if False:
    # - repetitive property definitions
    # ; leads to bloated, error prone, and ugly code
    # ; using descriptors or closures will be better!
    class Person:
        def __init__(self, first_name, last_name):
            self.first_name = first_name
            self.last_name = last_name

        @property
        def first_name(self):
            return self._first_name
     
        @first_name.setter
        def first_name(self, value):
            if not isinstance(value, str):
                raise TypeError('Expected a string')
            self._first_name = value
     
        # repeated property code, but for a different name (bad!)
        @property
        def last_name(self):
            return self._last_name
        
        @last_name.setter
        def last_name(self, value):
            if not isinstance(value, str):
                raise TypeError('Expected a string')
            self._last_name = value
