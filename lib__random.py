# vim: ft=python ts=4 sw=4 tw=999 expandtab
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------
# File : lib__random.py
# Author : yc0325lee
# Created : 2022-03-05 19:46:51 by lee2103
# Modified : 2022-03-05 19:46:51 by lee2103
# Description : 
# ----------------------------------------------------------------------------
import random
import numpy


if False:
    # - random.random()
    # ; return the next random floating point number in the range [0.0, 1.0)
    # - random.randint(a, b)
    # ; random integer N such that a <= N <= b
    random.seed(a=int())
    print(random.random()) # 0.0 ~ 1.0
    print(random.randint(1, 100)) # 1 ~ 100

    def random_pop(data):
        index = random.randint(0, len(data)-1)
        return data.pop(index)

    print()

    data = list(range(10))
    while data:
        print("popped=", random_pop(data))

if False:
    # random.choice(seq)
    # ; return a random element from the non-empty sequence seq.
    # ; if seq is empty, raises indexerror.
    samples = list(range(10))
    for i in range(10):
        print("choice[{}]= {}".format(i, random.choice(samples)))

    print("\n# numpy's case")
    samples = numpy.random.choice(100, 10)
    print("samples=", samples)
    print("len=", len(samples))
    # samples= [44 53 53 13 50 80 98 17  7 37]
    # len= 10

if False:
    # random.seed(a=None, version=2)
    # ; a=None -> current system time used for seed
    # ; a=int()
    random.seed(a=4321)
    pass

if False:
    # random.choice(seq)
    # ; Return a random element from the non-empty sequence seq.
    # ; If seq is empty, raises IndexError.
    pass

if False:
    # random.suffle(seq)
    # ; shuffle the sequence x in place.
    # ; seq must be mutable
    samples = list(range(10))
    print("samples=", samples)
    random.shuffle(samples)
    print("samples=", samples)
