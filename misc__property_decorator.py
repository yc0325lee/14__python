#!/usr/bin/env python
# -*- coding:utf-8 -*-
# vim: ft=python ts=4 sw=4 tw=78 expandtab
# ----------------------------------------------------------------------------
# - file : misc__property_decorator.py
# - author : yc0325lee
# - created : 2022-11-21 22:21:33 by yc032
# - modified : 2022-11-21 22:21:33 by yc032
# - references
# ; https://www.daleseo.com/python-property/
# ; https://docs.python.org/3/library/functions.html#property
# ; https://hamait.tistory.com/827
# - description : 
#   (1) 변수를 변경 할 때 어떠한 제한을 두고 싶어서
#   (2) get,set 함수를 만들지 않고 더 간단하게 접근하게 하기 위해서
#   (3) 하위호환성에 도움이 됨
# ----------------------------------------------------------------------------
import sys
import random

if False:
    # members 
    class Person:
        def __init__(self, name, age, sex, blood):
            self.name = str(name)
            self.age = int(age)
            self.sex = str(sex)
            self.blood = str(blood)

        def __repr__(self):
            selfClass = type(self)
            return '{}({!r}, {!r}, {!r}, {!r})'.format(
                selfClass.__name__, self.name, self.age, self.sex, self.blood
            )

        def __str__(self):
            return "('{}', {}, '{:6s}', '{:2s}')".format(
                self.name, self.age, self.sex, self.blood
            )


    person = Person("unknown", 0, "unknown", "unknown")
    print('\nperson=', person) # __str__
    print('person.__dict__ =', person.__dict__)
    # person.name -> person.__dict__['name'] referenced

    # settings
    person.name = "james"
    person.age = 41
    person.sex = "male"
    person.blood = "b"
    print('\nperson=', person) # __str__
    print('person.__dict__ =', person.__dict__)


if False:
    class Person:
        def __init__(self, name, age, sex, blood):
            self._name = str(name)
            self._age = int(age)
            self._sex = str(sex)
            self._blood = str(blood)

        def __repr__(self):
            selfClass = type(self)
            return '{}({!r}, {!r}, {!r}, {!r})'.format(
                selfClass.__name__, self._name, self._age, self._sex, self._blood
            )

        def __str__(self):
            return "('{}', {}, '{:6s}', '{:2s}')".format(
                self._name, self._age, self._sex, self._blood
            )

        def set_name(self, name):
            self._name = name
        def get_name(self):
            return self._name

        def set_age(self, age):
            self._age = age
        def get_age(self):
            return self._age

        def set_sex(self, sex):
            self._sex = sex
        def get_sex(self):
            return self._sex

        def set_blood(self, blood):
            self._blood = blood
        def get_blood(self):
            return self._blood


    person = Person("unknown", 0, "unknown", "unknown")
    print('\nperson=', person) # __str__
    #print('person.__dict__ =', person.__dict__)
    # person.name -> person.__dict__['name'] referenced

    # settings
    person.name = "james"
    person.age = 41
    person.sex = "male"
    person.blood = "b"
    print('\nperson=', person) # -> new settings will not be reflected!!!


if False:
    # decorator for debugging
    def trace(func):
        def wrapper(*args):
            print("[dgb ] {}() invoked ...".format(func.__name__))
            decorated = func(*args)
            #print("[dgb ] {}() ends ...".format(func.__name__))
            return decorated
        return wrapper

    # Person class
    class Person:
        def __init__(self, name, age, sex, blood):
            self.name = str(name)
            self.age = int(age)
            self.sex = str(sex)
            self.blood = str(blood)

        def __repr__(self):
            selfClass = type(self)
            return '{}({!r}, {!r}, {!r}, {!r})'.format(
                selfClass.__name__, self.name, self.age, self.sex, self.blood
            )

        def __str__(self):
            return "('{}', {}, '{:6s}', '{:2s}')".format(
                self.name, self.age, self.sex, self.blood
            )

        @trace
        def get_name(self):
            return self._name
        @trace
        def set_name(self, name):
            self._name = name

        @trace
        def get_age(self):
            return self._age
        @trace
        def set_age(self, age):
            self._age = age

        @trace
        def get_sex(self):
            return self._sex
        @trace
        def set_sex(self, sex):
            self._sex = sex

        @trace
        def get_blood(self):
            return self._blood
        @trace
        def set_blood(self, blood):
            self._blood = blood

        # properties
        # ; property() 함수의 첫 번째 인자로 getter 메서드를 두 번째 인자로
        #   setter 메서드를 넘겨주면 age라는 필드명을 이용해서 다시 나이
        #   데이터에 접근할 수 있게 됩니다.
        # ; value = self.age -> self.get_age() invoked(getter)
        # ; self.age = value -> self.set_age() invoked(setter)
        # ; 외부에 티 내지 않고 내부적으로 클래스의 필드 접근 방법을 바꿀 수 있다!
        name = property(get_name, set_name)
        age = property(get_age, set_age)
        sex = property(get_sex, set_sex)
        blood = property(get_blood, set_blood)

    # test code
    person = Person("unknown", 0, "unknown", "unknown")
    # [dgb ] set_name() invoked ...
    # [dgb ] set_age() invoked ...
    # [dgb ] set_sex() invoked ...
    # [dgb ] set_blood() invoked ...
    print('\nperson=', person) # __str__
    # [dgb ] get_name() invoked ...
    # [dgb ] get_age() invoked ...
    # [dgb ] get_sex() invoked ...
    # [dgb ] get_blood() invoked ...

    # setting
    person.name = "james"
    person.age = 41
    person.sex = "male"
    person.blood = "b"
    # [dgb ] set_name() invoked ...
    # [dgb ] set_age() invoked ...
    # [dgb ] set_sex() invoked ...
    # [dgb ] set_blood() invoked ...
    print('\nperson=', person)
    # [dgb ] get_name() invoked ...
    # [dgb ] get_age() invoked ...
    # [dgb ] get_sex() invoked ...
    # [dgb ] get_blood() invoked ...

    # getting
    print('person.name=', person.name)
    print('person.age=', person.age)
    print('person.sex=', person.sex)
    print('person.blood=', person.blood)
    # [dgb ] get_name() invoked ...
    # person.name= james
    # [dgb ] get_age() invoked ...
    # person.age= 41
    # [dgb ] get_sex() invoked ...
    # person.sex= male
    # [dgb ] get_blood() invoked ...
    # person.blood= b


if False:
    # decorator for debugging
    def trace(func):
        def wrapper(*args):
            print("[dgb ] {}() invoked ...".format(func.__name__))
            decorated = func(*args)
            #print("[dgb ] {}() ends ...".format(func.__name__))
            return decorated
        return wrapper

    # Person class
    class Person:
        def __init__(self, name, age, sex, blood):
            self.name = str(name)
            self.age = int(age)
            self.sex = str(sex)
            self.blood = str(blood)

        def __repr__(self):
            selfClass = type(self)
            return '{}({!r}, {!r}, {!r}, {!r})'.format(
                selfClass.__name__, self.name, self.age, self.sex, self.blood
            )

        def __str__(self):
            return "('{}', {}, '{:6s}', '{:2s}')".format(
                self.name, self.age, self.sex, self.blood
            )

        @property # get()
        @trace
        def name(self):
            return self._name
        @name.setter # set()
        @trace
        def name(self, name):
            self._name = name

        @property # get()
        @trace
        def age(self):
            return self._age
        @age.setter # set()
        @trace
        def age(self, age):
            self._age = age

        @property # get()
        @trace
        def sex(self):
            return self._sex
        @sex.setter # set()
        @trace
        def sex(self, sex):
            self._sex = sex

        @property # get()
        @trace
        def blood(self):
            return self._blood
        @blood.setter # set()
        @trace
        def blood(self, blood):
            self._blood = blood

    # test code
    person = Person("unknown", 0, "unknown", "unknown")
    # [dgb ] name() invoked ...
    # [dgb ] age() invoked ...
    # [dgb ] sex() invoked ...
    # [dgb ] blood() invoked ...

    print('\nperson=', person) # __str__
    # [dgb ] name() invoked ...
    # [dgb ] age() invoked ...
    # [dgb ] sex() invoked ...
    # [dgb ] blood() invoked ...

    # setting
    person.name = "james"
    person.age = 41
    person.sex = "male"
    person.blood = "b"
    # [dgb ] name() invoked ...
    # [dgb ] age() invoked ...
    # [dgb ] sex() invoked ...
    # [dgb ] blood() invoked ...

    print('\nperson=', person)
    # [dgb ] name() invoked ...
    # [dgb ] age() invoked ...
    # [dgb ] sex() invoked ...
    # [dgb ] blood() invoked ...

    # getting
    print('person.name=', person.name)
    print('person.age=', person.age)
    print('person.sex=', person.sex)
    print('person.blood=', person.blood)
    # [dgb ] name() invoked ...
    # person.name= james
    # [dgb ] age() invoked ...
    # person.age= 41
    # [dgb ] sex() invoked ...
    # person.sex= male
    # [dgb ] blood() invoked ...
    # person.blood= b


if False:
    # - let's limit on setting temperature below -273!
    # without @property
    class Celsius:
        def __init__(self, value=0.0):
            self.set_temperature(value)

        def to_fahrenheit(self):
            return self.get_temperature() * 1.8 + 32

        def get_temperature(self):
            return self._temperature

        def set_temperature(self, value):
            if value < -273:
                raise ValueError("temperature below -273 is not allowed!")
            self._temperature = value

        def __str__(self):
            return '{:.6f}'.format(self._temperature)

    #current = Celsius(-300) # error!
    current = Celsius()
    current._temperature = -300.0 # [note] this is possible!
    print(current)


if False:
    # - let's limit on setting temperature below -273
    # using @property and @attrname.setter decorators
    class Celsius:
        def __init__(self, value=0.0):
            self.temperature = value

        def to_fahrenheit(self):
            return self.temperature * 1.8 + 32

        @property
        def temperature(self):
            print('[dbg ] getting temperature ...')
            return self._temperature

        @temperature.setter
        def temperature(self, value):
            if value < -273:
                raise ValueError("temperature below -273 is not allowed!")
            print('[dbg ] setting temperature ...')
            self._temperature = value

        def __str__(self):
            return '{:.6f}'.format(self.temperature)

    #current = Celsius(-300) # error!
    current = Celsius()
    current.temperature = -300.0 # [note] this is not possible.
                                 # because setter current.temperature(-300.0)
                                 # is invoked!
    print(current)
    # ---------------------------------------------------------------
    # [dbg ] setting temperature ...
    # Traceback (most recent call last):
    #   File "misc__property_decorator.py", line 378, in <module>
    #     current.temperature = -300.0 # [note] this is not possible.
    #     ^^^^^^^^^^^^^^^^^^^
    #   File "misc__property_decorator.py", line 369, in temperature
    #     raise ValueError("temperature below -273 is not allowed!")
    # ValueError: temperature below -273 is not allowed!
    # ---------------------------------------------------------------
