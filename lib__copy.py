# vim: ft=python ts=4 sw=4 tw=999 expandtab
# -*- coding:utf-8 -*-
# ----------------------------------------------------------------------------
# File : lib__copy.py
# Author : yc0325lee
# Created : 2022-10-10 00:41:31 by lee2103
# Modified : 2022-10-10 00:41:31 by lee2103
# Description : 
# ----------------------------------------------------------------------------
import copy

class Bus:
    def __init__(self, passengers=None):
        if passengers is None:
            self.passengers = []
        else:
            self.passengers = list(passengers)

    def __repr__(self):
        return "Bus({})".format(self.passengers)
        # if no custom __str__() is available,
        # python will call __repr__() instead!

    def pick(self, name):
        self.passengers.append(name)

    def drop(self, name):
        self.passengers.remove(name)

    pass

if False:
    # copy.copy() - shallow copy
    # copy.deepcopy() - deep copy
    bus1 = Bus(['alice', 'bill', 'claire', 'david'])
    bus2 = copy.copy(bus1)
    bus3 = copy.deepcopy(bus1)
    print("bus1=", bus1)
    print("bus2=", bus2)
    print("bus3=", bus3)

    bus1.drop('bill') # will affect bus2 also!
    print("bus1=", bus1)
    print("bus2=", bus2)
    print("bus3=", bus3)

