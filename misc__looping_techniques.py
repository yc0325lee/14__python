# vim: ft=python ts=4 sw=4 tw=999 expandtab
# -*- coding:utf-8 -*-
# ----------------------------------------------------------------------------
# - file : misc__looping_techniques.py
# - author : yc0325lee
# - created : 2022-10-30 19:40:59 by lee2103
# - modified : 2022-10-30 19:41:30 by lee2103
# - description : 
# ----------------------------------------------------------------------------

if False:
    # dictionary - dict.items()
    knights = {'gallahad': 'the pure', 'robin': 'the brave'}
    for key, val in knights.items():
        print(key, val)

    for thing in knights: # -> same as knights.values()
        print(thing)

if False:
    # list with index & value -> enumerate()
    for i, item in enumerate(['tic', 'tac', 'toe']):
        print(i, item)

if False:
    # pairing 2 lists with zip()
    questions = ['name', 'quest', 'favorite color']
    answers = ['lancelot', 'the holy grail', 'blue']
    for question, answer in zip(questions, answers):
        print('What is your {0}?  It is {1}.'.format(question, answer))

if False:
    # reversing a sequence - reversed()
    for i in reversed(range(10)):
        print("i=", i)

if False:
    # sorting with sorted()
    basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
    for fruit in sorted(basket):
        print("fruit=", fruit)

if False:
    # unique list - set()
    basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
    for fruit in sorted(set(basket)):
        print("fruit=", fruit)

