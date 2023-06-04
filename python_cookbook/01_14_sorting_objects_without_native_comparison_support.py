#!/usr/bin/env python
# -*- coding:utf-8 -*-
# vim: ft=python ts=4 sw=4 tw=78 expandtab
# ----------------------------------------------------------------------------
# - file : 01_14_sorting_objects_without_native_comparison_support.py
# - author : yc0325lee
# - created : 2022-11-19 22:09:03 by yc032
# - modified : 2022-11-19 22:09:03 by yc032
# - description : 
# ----------------------------------------------------------------------------
import random
import operator

if True:
    random.seed(a=int()) # seeding

    class User:
        def __init__(self, user_id):
            self.user_id = user_id
        
        def __repr__(self):
            return 'User({})'.format(self.user_id)

    #users = [User(23), User(3), User(99)]
    users = []
    for _ in range(10):
        user_id = random.randint(0, 9)
        users.append(User(user_id))

    print('\nusers =', users)
    print('\nsorted =', list(sorted(users, key=lambda u: u.user_id)))
    print('\nsorted =', list(sorted(users, key=operator.attrgetter('user_id'))))

    # -----------------------------------------------------
    # [note]
    # it's a bit faster to use operator.attrgetter()
    # simpler when using more than 2 attributes for sorting
    # -----------------------------------------------------

    print('minimum =', min(users, key=operator.attrgetter('user_id')))
    print('maximum =', max(users, key=operator.attrgetter('user_id')))


## In[6]:
#
#
#from operator import attrgetter
#sorted(users, key=attrgetter('user_id'))
#
#
## In[8]:
#
#
#by_name = sorted(users, key=attrgetter('user_id'))
#by_name
#
#
## In[10]:
#
#
#print min(users, key=attrgetter('user_id'))
#print max(users, key=attrgetter('user_id'))
#
#
## In[ ]:
#
#
#
#
