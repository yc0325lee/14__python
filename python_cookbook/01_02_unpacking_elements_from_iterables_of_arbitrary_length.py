#!/usr/bin/env python
# vim: ft=python ts=4 sw=4 tw=78 expandtab
# -*- coding:utf-8 -*-
# ----------------------------------------------------------------------------
# - file : 01_02_unpacking_elements_from_iterables_of_arbitrary_length.py
# - author : yc0325lee
# - created : 2022-11-15 00:19:40 by yc032
# - modified : 2022-11-15 00:19:40 by yc032
# - description : 
# ; 'star expressions' can be used to address unpacking iterables of unknown
#   or very large length.
# ----------------------------------------------------------------------------
if False:
    record = ('Dave', 'dave@exmple.com', '773-555-1212', '847-555-1212')
    name, email, *phone_numbers = record
    print('name =', name)
    print('email =', email)
    print('phone_numbers =', phone_numbers) # list
    # name = Dave
    # email = dave@exmple.com
    # phone_numbers = ['773-555-1212', '847-555-1212']

    def drop_first_last(grades):
        first, *middle, last = grades
        print('first =', first)
        print('middle =', middle) # list
        print('last =', last)
        return sum(middle) / len(middle)

    import random
    #grades = (random.random() * 100.0 for _ in range(24)) # gen-expr
    grades = (random.randint(1, 100) * 1.0 for _ in range(24)) # gen-expr
    #for grade in grades: print(grade)
    print('average =', drop_first_last(grades))

    print('\n* can be the first one in the list')
    overall = [random.randint(1, 100) * 1.0 for _ in range(10)] # list comprehension
    *trailing, current = overall
    print('overall =', overall)
    print('trailing =', trailing)
    print('current =', current)
    # overall = [52.0, 26.0, 18.0, 67.0, 1.0, 44.0, 10.0, 66.0, 95.0, 36.0]
    # trailing = [52.0, 26.0, 18.0, 67.0, 1.0, 44.0, 10.0, 66.0, 95.0]
    # current = 36.0

if False:
    # - iterating over a sequence of tuples of varying length
    records = [
        ('foo', 1, 2),
        ('bar','hello'),     
        ('foo', 3, 4),      
    ]

    def process_foo(x,y):
        print('foo',x,y)
        
    def process_bar(s):
        print('bar',s)

    for tag, *args in records: # unpacking
        if tag == 'foo':
            process_foo(*args) # 2 arguments
        elif tag == 'bar':
            process_bar(*args) # 1 argument

if True:
    # string processing
    line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
    uname, *fields, homedir, sh = line.split(':')
    print('uname =', uname)
    print('fields =', fields) # list
    print('homedir =', homedir)
    print('sh =', sh)
    # uname = nobody
    # fields = ['*', '-2', '-2', 'Unprivileged User']
    # homedir = /var/empty
    # sh = /usr/bin/false
