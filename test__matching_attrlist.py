# vim: ft=python ts=4 sw=4 tw=78 expandtab
# -*- coding:utf-8 -*-
# ----------------------------------------------------------------------------
# - file : test__matching_attrlist.py
# - author : yc0325lee
# - created : 2022-10-31 23:30:26 by lee2103
# - modified : 2022-10-31 23:30:26 by lee2103
# - description : 
# ----------------------------------------------------------------------------
import re

# ----------------------------------------
# - inheriting from built-in list directly
# ; preferred approach
class AttrList(list):
    """
    [note] adding more functionalities on top of basic list operations
           all values are string (assumption, 221029_200936)
    """

    def all_contains(self, pattern):
        return all(re.search(pattern, val) for val in self)

    def any_contains(self, pattern):
        return any(re.search(pattern, val) for val in self)

    def all_within(self, *patterns): # all contains one of the patterns
        #                ---------     
        pattern = '(:?' + '|'.join(patterns) + ')'
        return all(re.search(pattern, item) for item in self) 


if __name__ == '__main__':

    signals = [
        AttrList('__abc__ __bcd__ __cde__ __def__ __efg__'.split()), # homogenous
        AttrList('__abc__ __abc__ __abx__ __abc__ __abc__'.split()), # heterogenous
    ]
    print('signals[0] =', signals[0])
    print('signals[1] =', signals[1], "\n")


    # True case
    print("signals[0].all_within('abc', 'bcd', 'cde', 'def', 'efg') =",
        signals[0].all_within('abc', 'bcd', 'cde', 'def', 'efg'))

    patterns = 'abc bcd cde def efg'.split()
    print(
        "signals[0].all_within(*patterns) =",
        signals[0].all_within(*patterns)
    )

    # False case
    print("signals[0].all_within('abc', 'bcd', 'cde', 'def') =",
        signals[0].all_within('abc', 'bcd', 'cde', 'def'))

    patterns = 'abc bcd cde def'.split()
    print(
        "signals[0].all_within(*patterns) =",
        signals[0].all_within(*patterns)
    )

    # signals[0] = ['__abc__', '__bcd__', '__cde__', '__def__', '__efg__']
    # signals[1] = ['__abc__', '__abc__', '__abx__', '__abc__', '__abc__']
    # 
    # signals[0].all_within('abc', 'bcd', 'cde', 'def', 'efg') = True
    # signals[0].all_within(*patterns) = True
    # signals[0].all_within('abc', 'bcd', 'cde', 'def') = False
    # signals[0].all_within(*patterns) = False
