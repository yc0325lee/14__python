# vim: ft=python ts=4 sw=4 tw=999 expandtab
# -*- coding:utf-8 -*-
# ----------------------------------------------------------------------------
# - file : data__tuple.py
# - author : yc0325lee
# - created : 2022-10-29 19:27:12 by lee2103
# - modified : 2022-10-29 19:27:12 by lee2103
# - description : 
# ----------------------------------------------------------------------------
# - tuple
# ; immutable
# ; assigment to tuple not possible(immutable)
# ; but tuple can contain mutable objects like list or set
# ; faster than list
# ; 2 aspects
#    immutable list
#    records with no field names
# ; hash() supported(__hash__ implemented)
# 
# - tuple construction
# (1) using a pair of parentheses to denote the empty tuple: ()
# (2) using a trailing comma for a singleton tuple: a, or (a,)
# (3) separating items with commas: a, b, c or (a, b, c) - optional parenthesis
# (4) using the tuple() built-in: tuple() or tuple(iterable)
#
# - operations for both mutable and immutable
#   +-----------------------+-------------------------------------------------------+
#   | operation             | description                                           |
#   +-----------------------+-------------------------------------------------------+
#   | x in s                | True if an item of s is equal to x, else False        |
#   | x not in s            | False if an item of s is equal to x, else True        |
#   | s + t                 | the concatenation of s and t                          |
#   | s * n or n * s        | equivalent to adding s to itself n times              |
#   | s[i]                  | ith item of s, origin 0                               |
#   | s[i:j]                | slice of s from i to j                                |
#   | s[i:j:k]              | slice of s from i to j with step k                    |
#   | len(s)                | length of s                                           |
#   | min(s)                | smallest item of s                                    |
#   | max(s)                | largest item of s                                     |
#   | s.index(x[, i[, j]])  | index of the first occurrence of x in s               |
#   | s.count(x)            | total number of occurrences of x in s                 |
#   +-----------------------+-------------------------------------------------------+
# - for clearer data access -> collections.namedtuple

if False:
    # class tuple([iterable])
    x = tuple() # emtpy, but useless
    y = () # emtpy, but useless
    y = ( 0, 1, 2, 3, 4 )
    strings = ("aaa", "bbb", "ccc", "ddd", "eee")
    z = (1,) # comma required for 1-element tuple

if False:
    # assignment using tuple style
    # ; tuple unpacking
    a, b   =   'AAA', 'BBB'
    a, b   = ( 'AAA', 'BBB' ); # tuple을 사용한 value assignment!
    ( a, b ) = ( 'AAA', 'BBB' )
    name, age, sex, hobby   =   "yclee", 46, "male", "coding"
    ( name, age, sex, hobby ) = ( "yclee", 46, "male", "coding" ) # same!

if True:
    # operations
    a = (3, 4, 5) # (3, 4, 5)
    print('a =', a, 'id =', id(a))
    a += (6, 7) # (3, 4, 5, 6, 7)
    print('a =', a, 'id =', id(a))
    a *= 2 # (3, 4, 5, 6, 7, 3, 4, 5, 6, 7)
    print('a =', a, 'id =', id(a))
    # ------------------------------------------------------
    # a = (3, 4, 5)                       id = 2323048944000
    # a = (3, 4, 5, 6, 7)                 id = 2323050680704
    # a = (3, 4, 5, 6, 7, 3, 4, 5, 6, 7)  id = 2323048272448
    # -> ids changed!
    # ------------------------------------------------------

if False:
    # concatenation
    a = (1, 2)
    b = (3, 4)
    y = a + b # (1, 2, 3, 4) -> concatenation
    z = a * 3 # (1, 2, 1, 2, 1, 2) -> repeat
