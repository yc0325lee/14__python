# vim: ft=python ts=4 sw=4 tw=999 expandtab
# -*- coding:utf-8 -*-
# ----------------------------------------------------------------------------
# - file : lib__abc.py
# - author : yc0325lee
# - created : 2022-10-16 18:27:42 by lee2103
# - modified : 2022-10-16 18:27:42 by lee2103
# - abc - abstract base classes
# ; provides the infrastructure for defining abstract base classes (ABCs)
# ----------------------------------------------------------------------------
import abc

if False:
    # @abc.abstractmethod
    # ; a decorator indicating abstract methods.
    # ; using this decorator requires that the class's metaclass is abcmeta or
    #   is derived from it.
    # ; a class that has a metaclass derived from abcmeta cannot be
    #   instantiated unless all of its abstract methods and properties are
    #   overridden.
    # ; similar to 'pure virtual function' in c++
    pass

if False:
    class Base(abc.ABC):
        @abc.abstractmethod
        def dump(self):
            """abstract method or pure virtual function"""
            pass

    class Derived_0(Base):
        def __init__(self):
            self.data = "data"
        def dump(self):
            print("data=", self.data)

    class Derived_1(Base):
        def __init__(self):
            self.data = "data"
        #def dump(self):
        #    print("data=", self.data)
        # -> cannot not be instantiated cuz dump() not implemented

    obj = Derived_0()
    obj.dump()

    #obj = Derived_1() # error
    # TypeError: Can't instantiate abstract class Derived_1 with abstract method dump

    #obj = Base() # error
    # TypeError: Can't instantiate abstract class Base with abstract method dump
