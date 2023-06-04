# vim: ft=python ts=4 sw=4 tw=999 expandtab
# -*- coding:utf-8 -*-
# ----------------------------------------------------------------------------
# - file : running_average_using_closure.py
# - author : yc0325lee
# - created : 2022-10-17 23:01:51 by lee2103
# - modified : 2022-10-17 23:01:51 by lee2103
# - description : 
# ; a closure is a function that retains the bindings of the free
#   variables that exist when the function is defined
# ----------------------------------------------------------------------------
import collections

if False:
    # a class to calculate a running average
    # ; instantiation -> callable object with __call__()
    class Average:
        def __init__(self):
            self.window = window = collections.deque([0.0] * 5, maxlen=5)

        def __call__(self, value):
            self.window.append(value)
            if True:
                print("[debug] window=", self.window)
            return sum(self.window)/len(self.window)
            #      ---------------------------------
            #                  average

    # callable object
    average = Average()

    for val in (float(i) for i in range(10)):
        print("        average({})= {:.6f}".format(val, average(val)))
    print()


if False:
    # a class to calculate a running average - (2) parametered
    # ; instantiation -> callable object with __call__()
    class Average:
        def __init__(self, maxlen=5):
            self.window = window = collections.deque([0.0] * maxlen, maxlen=maxlen)

        def __call__(self, value):
            self.window.append(value)
            if True:
                print("[debug] window=", self.window)
            return sum(self.window)/len(self.window)
            #      ---------------------------------
            #                  average

    # callable object
    average = Average(maxlen=3)

    for val in (float(i) for i in range(10)):
        print("        average({})= {:.6f}".format(val, average(val)))
    print()


if False:
    # a function that returns a callable object(closure)
    def make_closure():
        window = collections.deque([0.0] * 5, maxlen=5)
        def calculate(current): # closure
            window.append(current)
            if True:
                print("[debug] window=", window)
            return sum(window)/len(window) # not efficient!
        return calculate

    # parametered closures
    average = make_closure() # returns callable object
    del make_closure # not required from now on!

    for val in (float(i) for i in range(10)):
        print("        average({})= {:.6f}".format(val, average(val)))
    print()
    # ----------------------------------------------------------
    # [debug] window= deque([0.0, 0.0, 0.0, 0.0, 0.0], maxlen=5)
    #         average(0.0)= 0.000000
    # [debug] window= deque([0.0, 0.0, 0.0, 0.0, 1.0], maxlen=5)
    #         average(1.0)= 0.200000
    # [debug] window= deque([0.0, 0.0, 0.0, 1.0, 2.0], maxlen=5)
    #         average(2.0)= 0.600000
    # [debug] window= deque([0.0, 0.0, 1.0, 2.0, 3.0], maxlen=5)
    #         average(3.0)= 1.200000
    # [debug] window= deque([0.0, 1.0, 2.0, 3.0, 4.0], maxlen=5)
    #         average(4.0)= 2.000000
    # [debug] window= deque([1.0, 2.0, 3.0, 4.0, 5.0], maxlen=5)
    #         average(5.0)= 3.000000
    # [debug] window= deque([2.0, 3.0, 4.0, 5.0, 6.0], maxlen=5)
    #         average(6.0)= 4.000000
    # [debug] window= deque([3.0, 4.0, 5.0, 6.0, 7.0], maxlen=5)
    #         average(7.0)= 5.000000
    # [debug] window= deque([4.0, 5.0, 6.0, 7.0, 8.0], maxlen=5)
    #         average(8.0)= 6.000000
    # [debug] window= deque([5.0, 6.0, 7.0, 8.0, 9.0], maxlen=5)
    #         average(9.0)= 7.000000
    # ----------------------------------------------------------

    # free variables of closure
    print("average.__code__.co_varnames=", average.__code__.co_varnames)
    print("average.__code__.co_freevars=", average.__code__.co_freevars)
    print("average.__closure__=", average.__closure__)
    print("average.__closure__[0].cell_contents=", average.__closure__[0].cell_contents)
    # average.__code__.co_varnames= ('current',)
    # average.__code__.co_freevars= ('window',)
    # average.__closure__= (<cell at 0x0000026E3BA79FD0: collections.deque object at 0x0000026E3B7C8340>,)
    # average.__closure__[0].cell_contents= deque([5.0, 6.0, 7.0, 8.0, 9.0], maxlen=5)

if False:
    # paramerters
    def make_closure(maxlen=5):
        window = collections.deque([0.0] * maxlen, maxlen=maxlen)
        def calculate(current): # closure
            window.append(current)
            if True:
                print("[debug] window=", window)
            return sum(window)/len(window) # not efficient!
        return calculate

    # parametered closures
    average_2 = make_closure(2) # returns callable object
    average_3 = make_closure(3)
    average_4 = make_closure(4)
    average_5 = make_closure(5)

    del make_closure # not required from now on!

    #closures = [average_2, average_3, average_4, average_5]
    closures = [average_5]
    for val in (float(i) for i in range(10)):
        for i, closure in enumerate(closures, 5):
            print("        average_{}({})= {:.6f}".format(i, val, closure(val)))
        print()

    # ----------------------------------------------------------
    # [debug] window= deque([0.0, 0.0, 0.0, 0.0, 0.0], maxlen=5)
    #         average_5(0.0)= 0.000000
    # [debug] window= deque([0.0, 0.0, 0.0, 0.0, 1.0], maxlen=5)
    #         average_5(1.0)= 0.200000
    # [debug] window= deque([0.0, 0.0, 0.0, 1.0, 2.0], maxlen=5)
    #         average_5(2.0)= 0.600000
    # [debug] window= deque([0.0, 0.0, 1.0, 2.0, 3.0], maxlen=5)
    #         average_5(3.0)= 1.200000
    # [debug] window= deque([0.0, 1.0, 2.0, 3.0, 4.0], maxlen=5)
    #         average_5(4.0)= 2.000000
    # [debug] window= deque([1.0, 2.0, 3.0, 4.0, 5.0], maxlen=5)
    #         average_5(5.0)= 3.000000
    # [debug] window= deque([2.0, 3.0, 4.0, 5.0, 6.0], maxlen=5)
    #         average_5(6.0)= 4.000000
    # [debug] window= deque([3.0, 4.0, 5.0, 6.0, 7.0], maxlen=5)
    #         average_5(7.0)= 5.000000
    # [debug] window= deque([4.0, 5.0, 6.0, 7.0, 8.0], maxlen=5)
    #         average_5(8.0)= 6.000000
    # [debug] window= deque([5.0, 6.0, 7.0, 8.0, 9.0], maxlen=5)
    #         average_5(9.0)= 7.000000
    # ----------------------------------------------------------
