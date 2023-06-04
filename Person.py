# vim: ft=python ts=4 sw=4 tw=999 expandtab
# -*- coding:utf-8 -*-
# ----------------------------------------------------------------------------
# - file : Person.py
# - author : yc0325lee
# - created : 2022-10-28 21:42:31 by lee2103
# - modified : 2022-10-28 21:42:31 by lee2103
# - description : 
# ----------------------------------------------------------------------------
import sys
import random
from utilities import printv

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
    pass


# generator function
def gen_person(count=10):
    i = count-1
    while i >= 0:
        name = ''
        for _ in range(3):
            name += chr(random.randint(97, 122))
        age = random.randint(10, 20)
        sex = ('male', 'female', 'homo')[random.randint(0, 2)]
        blood = ('a', 'b', 'ab', 'o')[random.randint(0, 3)]
        yield Person(name, age, sex, blood)
        i -= 1


if __name__ == '__main__':

    for i, person in enumerate(gen_person(100)):
        print('person[{}] = {}'.format(i, person))
