# vim: ft=python ts=4 sw=4 tw=999 expandtab
# -*- coding:utf-8 -*-
# ----------------------------------------------------------------------------
# - file : private_protected_public.py
# - author : yc0325lee
# - created : 2022-10-10 22:25:18 by lee2103
# - modified : 2022-10-10 22:25:18 by lee2103
# - description : 
#   ; '__' private attribute names are "mangled" by prefixing the _ and the class name
#   ; python stores the name in the instance __dict__ prefixed with a leading
#     underscore and the class name
# ----------------------------------------------------------------------------
class CompanyBase:
    'CompanyBase class implementation'
    Debug = False
    Count = 0

    def __init__(self, name, age):
        self.__name = name
        self.__age = age
        __class__.Count += 1

    @property
    def name(self):
        return self.__name

    @property
    def age(self):
        return self.__age

    pass


class Apple(CompanyBase):
    'Apple class implementation'
    Debug = False
    Count = 0

    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.__name = name + '_1' # 
        self.__age = age + 1      # -> this will override base's ones!
        self.__salary = salary
        __class__.Count += 1
        pass

    @property
    def salary(self):
        return self.__salary

    pass


if __name__ == '__main__':
    engr = Apple("jason", 37, 25000)
    print("engr=", engr)
    # engr= <__main__.Apple object at 0x0000026B03EF4670>
    
    table = engr.__dict__
    for key, val in engr.__dict__.items():
        print("key=", key, "val=", val)
    # key= _CompanyBase__name val= jason
    # key= _CompanyBase__age val= 37
    # key= _Apple__name val= jason_1
    # key= _Apple__age val= 38
    # key= _Apple__salary val= 25000
    
    print("engr.name=", engr.name) # accessing base-class's one!
    print("engr.age=", engr.age)
    print("engr.salary=", engr.salary)
    # engr.name= jason
    # engr.age= 37
    # engr.salary= 25000
