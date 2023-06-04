# vim: ft=python ts=4 sw=4 tw=78 expandtab
# -*- coding:utf-8 -*-
# ----------------------------------------------------------------------------
# - file : lib__pprint.py
# - author : yc0325lee
# - created : 2022-11-10 21:18:03 by yc032
# - modified : 2022-11-10 21:18:03 by yc032
# - description : 
# ; the pprint module provides a capability to “pretty-print” arbitrary python
#   data structures in a form which can be used as input to the interpreter.
# ----------------------------------------------------------------------------
import pprint
from Person import *
from Vector import *

if False:
    # -------------------------------------
    # - pprint.pprint(
    #       object, stream=None, indent=1, width=80, depth=None, *,
    #       compact=False, sort_dicts=True, underscore_numbers=False
    #   )
    # ; prints the formatted representation of object on stream, followed by a
    #   newline.
    persons = list(gen_person(10))
    print('persons =')
    pprint.pprint(persons, indent=4)
    # persons =
    # [   Person('zfi', 16, 'homo', 'a'),
    #     Person('mqk', 18, 'male', 'ab'),
    #     Person('yzz', 10, 'homo', 'ab'),
    #     Person('zxa', 13, 'male', 'o'),
    #     Person('mdt', 12, 'male', 'a'),
    #     Person('cus', 16, 'homo', 'b'),
    #     Person('lpl', 17, 'homo', 'ab'),
    #     Person('lgx', 19, 'male', 'ab'),
    #     Person('dij', 12, 'female', 'a'),
    #     Person('pip', 16, 'female', 'a')]
    
    for person in persons:
        pprint.pprint(person, indent=4)
    # Person('zfi', 16, 'homo', 'a')
    # Person('mqk', 18, 'male', 'ab')
    # Person('yzz', 10, 'homo', 'ab')
    # Person('zxa', 13, 'male', 'o')
    # Person('mdt', 12, 'male', 'a')
    # Person('cus', 16, 'homo', 'b')
    # Person('lpl', 17, 'homo', 'ab')
    # Person('lgx', 19, 'male', 'ab')
    # Person('dij', 12, 'female', 'a')
    # Person('pip', 16, 'female', 'a')
    
    vector = Vector([1, 2, 3])
    pprint.pprint(vector, indent=4)
    # Vector([1.0, 2.0, 3.0])
    
