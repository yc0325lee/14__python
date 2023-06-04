# vim: ft=python ts=4 sw=4 tw=999 expandtab
# -*- coding:utf-8 -*-
# ----------------------------------------------------------------------------
# - file : misc__sort.py
# - author : yc0325lee
# - created : 2022-10-15 20:23:36 by lee2103
# - modified : 2022-10-15 20:23:36 by lee2103
# - description : 
# - references
# ; 3.10.8 Documentation > Python HOWTOs > Sorting HOW TO
# ----------------------------------------------------------------------------
import sys
import random
from utilities import printv


if False:
    # --------------------------------------------------------------------
    # sorted(iterable, /, *, key=None, reverse=False)
    # ; return a new sorted list from the items in iterable
    # ; key specifies a function of one argument that is used to extract a
    #   comparison key from each element in iterable
    #   default value is none (compare the elements directly)
    #
    # list.sort(*, key=None, reverse=False)
    # ; sorts the list in place, using only < comparisons between items
    # --------------------------------------------------------------------
    simpsons = ['homer', 'marge', 'bart'] + ['ned', 'rod', 'todd']

    # sort a list in place (modifies but does not return the list)
    print("\n# list.sort()")
    simpsons.sort()
    print(simpsons)
    simpsons.sort(reverse=True) # sort in reverse
    print(simpsons)
    simpsons.sort(key=len)      # sort by a key
    print(simpsons)
    
    # return a sorted list (does not modify the original list)
    print("\n# sorted()")
    print( sorted(simpsons) )
    print( sorted(simpsons, reverse=True) )
    print( sorted(simpsons, key=len) )
    
    # insert into an already sorted list, and keep it sorted
    num = [10, 20, 40, 50]
    from bisect import insort
    insort(num, 30)


if True:
    # sorting with priorities
    class Person:
        def __init__(self, name, age, sex, blood):
            self.name = str(name)
            self.age = int(age)
            self.sex = str(sex)
            self.blood = str(blood)
        def __str__(self):
            return "('{}', {}, '{:6s}', '{:2s}')".format(
                self.name, self.age, self.sex, self.blood
            )

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

    guests = tuple(gen_person(20))

    print('\n# sort by name')
    for guest in sorted(guests, key=lambda p: p.name):
        print(guest)

    print('\n# sort by age')
    for guest in sorted(guests, key=lambda p: p.age):
        print(guest)

    print('\n# sort by sex')
    for guest in sorted(guests, key=lambda p: p.sex):
        print(guest)

    print('\n# sort by blood')
    for guest in sorted(guests, key=lambda p: p.blood):
        print(guest)

    print('\n# sort by blood & age')
    for guest in sorted(guests, key=lambda p: (p.blood, p.age)):
        print(guest)
