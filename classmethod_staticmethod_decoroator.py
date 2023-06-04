# vim: ft=python ts=4 sw=4 tw=999 expandtab
# -*- coding:utf-8 -*-
# ----------------------------------------------------------------------------
# File : classmethod_staticmethod_decoroator.py
# Author : yc0325lee
# Created : 2022-10-08 13:32:05 by lee2103
# Modified : 2022-10-08 13:32:05 by lee2103
# Description : 
# ----------------------------------------------------------------------------

class Base:
    default = "base"
    data_base = "base_data"
    
    def __init__(self, name=None):
        if name is None:
            self.name = __class__.default
        else:
            self.name = name
        pass

    def get_name(self):
        return self.name

    @classmethod
    def get_default_class(cls):
        return cls.default

    @classmethod
    def get_data_derived(cls):
        return cls.data_derived

    @staticmethod
    def get_default_static():
        return __class__.default

    pass


class Derived_A(Base):
    default = "aaa"
    data_derived = "data_derived_a"

    def __init__(self, name=None):
        super().__init__(__class__.default)
        pass

    pass


class Derived_B(Base):
    default = "bbb"
    data_derived = "data_derived_a"
    def __init__(self, name=None):
        super().__init__(__class__.default)
        pass
    pass


if __name__ == "__main__":

    obj0 = Base()
    obj1 = Derived_A()
    obj2 = Derived_B()

    print(obj0.get_name()) # name=base
    print(obj1.get_name()) # name=aaa
    print(obj2.get_name()) # name=bbb
    print()

    # @classmethod
    print(Base.get_default_class()) # default=base
    print(Derived_A.get_default_class()) # default=aaa
    print(Derived_B.get_default_class()) # default=bbb
    print()

    # @staticmethod
    print(Base.get_default_static()) # default=base
    print(Derived_A.get_default_static()) # default=base
    print(Derived_B.get_default_static()) # default=base
    print()

    print(Base.data_base) # base_data
    print(Derived_A.data_base) # base_data
    print(Derived_B.data_base) # base_data
    print()
