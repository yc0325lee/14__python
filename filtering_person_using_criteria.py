# vim: ft=python ts=4 sw=4 tw=999 expandtab
# -*- coding:utf-8 -*-
# ----------------------------------------------------------------------------
# - file : filtering_person_using_criteria.py
# - author : yc0325lee
# - created : 2022-10-28 22:25:34 by lee2103
# - modified : 2022-10-30 19:29:26 by lee2103
# - description : 
# ----------------------------------------------------------------------------
import sys
import random
import operator
import functools
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
        return "('{}', {:>2d}, '{:6s}', '{:2s}')".format(
            self.name, self.age, self.sex, self.blood
        )

    def __hash__(self):
        hashes = [hash(self.name), hash(self.age), hash(self.sex), hash(self.blood)]
        return functools.reduce(operator.xor, hashes, 0)

    pass


# generator function
def gen_person(count=10):
    i = count-1
    while i >= 0:
        name = ''
        for _ in range(3):
            name += chr(random.randint(97, 122))
        age = random.randint(1, 99)
        sex = ('male', 'female', 'homo')[random.randint(0, 2)]
        blood = ('a', 'b', 'ab', 'o')[random.randint(0, 3)]
        yield Person(name, age, sex, blood)
        i -= 1

if __name__ == '__main__':

    # label : criterion
    criteria = dict(
        type_0 = lambda p: 1 <= p.age < 4, # baby_all
        type_1 = lambda p: 4 <= p.age <= 7, # infant_all
        type_2 = lambda p: 13 <= p.age <= 19 and p.sex == 'female', # teenager_female
        type_3 = lambda p: 70 <= p.age and p.sex == 'male', # senior_male
    )


    if False:
        # -----------------------------
        # (1) no way for capture others
        persons = tuple(gen_person(100))
        #for i, person in enumerate(persons):
        #    print('person[{:>2d}] = {}'.format(i, person))

        bucket = {}
        for label, criteria in sorted(criteria.items(), key=lambda c: c[0]):
            bucket[label] = list(filter(criteria, persons))
            print('\n# bucket[{}] = {}'.format(label, len(bucket[label])))
            for j, person in enumerate(sorted(bucket[label], key=lambda p: p.age)):
                print('person[{:>2d}] = {}'.format(j, person))

    if True:
        # -----------------------------
        # (1) no way for capture others
        persons = set(gen_person(100))
        print('len(persons) =', len(persons))

        bucket = {} # dict
        for label, criteria in sorted(criteria.items(), key=lambda c: c[0]):
            filtered = list(filter(criteria, persons))
            for person in filtered:
                persons.remove(person)
                bucket.setdefault(label, set()).add(person)

        # remaining persons
        label = 'other'
        for person in persons:
            bucket.setdefault(label, set()).add(person)
        # set size must not be changed during iteration!
        for person in bucket[label]:
            persons.remove(person)

        if False:
            for label, basket in sorted(bucket.items(), key=lambda c: c[0]):
                print('\n# bucket[{}] = {}'.format(label, len(basket)))
                for i, person in enumerate(sorted(basket, key=lambda p: p.age)):
                    print('person[{:>2d}] = {}'.format(i, person))

        import csv
        basename = 'filtering_person_using_criteria'
        for label, basket in sorted(bucket.items(), key=lambda c: c[0]):
            filename = basename + '.' + label + '.csv'
            print("[info] writing {} ...".format(filename))
            with open(filename, "w", newline="") as csvfile:
                csvWriter = csv.writer(csvfile)
                csvWriter.writerow('index name age sex blood'.split())
                for i, person in enumerate(sorted(basket, key=lambda p: p.age)):
                    csvWriter.writerow([i, person.name, person.age, person.sex, person.blood])
