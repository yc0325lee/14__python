# vim: ft=python ts=4 sw=4 tw=999 expandtab
# -*- coding:utf-8 -*-
# ----------------------------------------------------------------------------
# - file : data__list.py
# - author : yc0325lee
# - created : 2022-10-29 19:27:00 by lee2103
# - modified : 2022-10-29 19:27:00 by lee2103
# - description : 
# ----------------------------------------------------------------------------
#
# - list
# ; mutable
# ; list construction
#   (1) using a pair of square brackets to denote the empty list: []
#   (2) using square brackets, separating items with commas: [a], [a, b, c]
#   (3) using a list comprehension: [x for x in iterable]
#   (4) using the type constructor: list() or list(iterable)
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
#
# - operations for only mutable
#   +-----------------------+-------------------------------------------------------+
#   | operation             | description                                           |
#   +-----------------------+-------------------------------------------------------+
#   | s[i] = x              | item i of s is replaced by x                          |
#   | s[i:j] = t            | slice of s from i to j is replaced                    |
#   | s[i:j] = t            | by the contents of the iterable t                     |
#   | del s[i:j]            | same as s[i:j] = []                                   |
#   | s[i:j:k] = t          | elements of s[i:j:k] are replaced by those of t       |
#   | del s[i:j:k]          | removes the elements of s[i:j:k] from the list        |
#   | s.append(x)           | appends x to the end of the sequence                  |
#   |                       | (same as s[len(s):len(s)] = [x])                      |
#   | s.clear()             | removes all items from s (same as del s[:])           |
#   | s.copy()              | creates a shallow copy of s (same as s[:])            |
#   | s.extend(t) or s += t | extends s with the contents of t                      |
#   |                       | (for the most part the same as s[len(s):len(s)] = t)  |
#   | s *= n                | updates s with its contents repeated n times          |
#   | s.insert(i, x)        | inserts x into s at the index given by i              |
#   |                       | (same as s[i:i] = [x])                                |
#   | s.pop() or s.pop(i)   | retrieves the item at i and also removes it from s    |
#   | s.remove(x)           | remove the first item from s where s[i] is equal to x |
#   | s.reverse()           | reverses the items of s in place                      |
#   +-----------------------+-------------------------------------------------------+
#
# - list.sort(*, key=None, reverse=False)
# ; sorts the list in place, using only < comparisons between items
# ; returns None
import pprint


if False:
    for attr in dir(list()):
        print(attr)

if False:
    x = list()
    y = [ 0, 1, 2, 3, 4 ]
    strings = [ "aaa", "bbb", "ccc", "ddd", "eee" ]
    val1 = y[1]
    val2 = strings[4]
    y[4] = 5
    numElements = len(y)
    a = sorted(y)
    print(a)

    for s in strings: # looping
        print("str= %s" % s)

    location = y.index(3)
    location = strings.index("ddd")

    # containment(membership) operator
    if "bbb" in strings:
        print("bbb exists!")

if False:
    chars = list("ABCD") # type(arg)= str
    print("chars=", chars)

if False:
    fruits = ["apple", "apple", "banana", "apple", "pineapple", "grape", "watermalon", "grape", "tomato"]
    table = dict()
    for this in fruits:
        if this in table:
            table[this] = table[this] + 1 # increment
        else:
            table[this] = 1 # initial

    print(table)

# list functions
if False:
    a = [0, 1, 2, 3, 4]; del(a[1]); # [0, 2, 3, 4]
    a = [0, 1, 2, 3, 4]; del(a[2:]); # [0, 1]
    a = [0, 1, 2, 3, 4]; a.append(5); # [0, 1, 2, 3, 4, 5]
    a = [4, 3, 2, 1, 0]; a.sort(); # [0, 1, 2, 3, 4]
    a = [4, 3, 2, 1, 0]; a.reverse(); # [0, 1, 2, 3, 4]
    a = [4, 3, 2, 1, 0]; a.index(1); # 3
    a = [4, 3, 2, 1, 0]; a.index(5); # error
    a = [4, 3, 2, 1, 0]; a.insert(1, 5); # [4, 5, 3, 2, 1, 0]

    a = [4, 3, 2, 1, 0, 3];
    a.remove(3); # [4, 2, 1, 0, 3]
    a.remove(3); # [4, 2, 1, 0]

    a = [0, 1, 2, 3, 4]; print( a.pop() ); # prints '4' & remaining= [0, 1, 2, 3]
    a = [0, 1, 2, 3, 4]; print( a.pop(2) ); # prints '2' & remaining= [0, 1, 3, 4]
    a = [4, 3, 2, 1, 0, 3]; a.count(3); # 2

if False:
    # copying list
    a = [0, 1, 2, 3, 4]; print("a=", a)

    b = a; print("b=", b)
    print("id(a)= %s, id(b)= %s" % (id(a), id(b)))
    print("a is b : %s" % (a is b))

    b = a[:]; print("b=", b)
    print("a is b : %s" % (a is b))

    b = a.copy(); print("b=", b)
    print("a is b : %s" % (a is b))

    from copy import copy
    b = copy(a); print("b=", b)
    print("a is b : %s" % (a is b))

if False:
    # list concatenation and multiplication
    a = [1, 2, 3]
    b = [4, 5, 6]
    print("a + b = ", a + b) # [1, 2, 3, 4, 5, 6]
    print("a * 3 = ", a * 3) # [1, 2, 3, 1, 2, 3, 1, 2, 3]

if False:
    # deleting(removing) elements
    a = [0, 1, 2, 3, 4];
    del a[1];
    print(a); # a = [0, 2, 3, 4]
    del a[2:]; # a = [0, 1]

if False:
    # extending list
    a = [0, 1, 2];
    print('a =', a) # a = [0, 1, 2]

    a.extend([3, 4])
    print('a =', a) # a = [0, 1, 2, 3, 4]

    b = [5, 6]
    a.extend(b)
    print('a =', a) # a = [0, 1, 2, 3, 4, 5, 6]

if False:
    # augmented add/mult (in-place modification)
    a = [3, 4, 5]
    print('a =', a, 'id =', id(a))
    a += [6, 7]
    print('a =', a, 'id =', id(a))
    a *= 2
    print('a =', a, 'id =', id(a))
    # ------------------------------------------------------------
    # a = [3, 4, 5]                             id = 2377285389888
    # a += [6, 7] = [3, 4, 5, 6, 7]             id = 2377285389888
    # a *= 2 = [3, 4, 5, 6, 7, 3, 4, 5, 6, 7]   id = 2377285389888
    # -> ids not changed!
    # ------------------------------------------------------------

if False:
    # slice/slicing [start:stop:stride]
    cont = list(range(10))
    print("cont=", cont)

    print("left=", cont[:5])
    print("right=", cont[5:])
    print("even=", cont[::2])
    print("odd=", cont[1::2])
    print(cont[:-1])
    # cont= [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    # left= [0, 1, 2, 3, 4]
    # right= [5, 6, 7, 8, 9]
    # even= [0, 2, 4, 6, 8]
    # odd= [1, 3, 5, 7, 9]
    # cont[:-1]= [0, 1, 2, 3, 4, 5, 6, 7, 8]

if False:
    # list of string
    # ; 'str' is just a type hint!
    cont = list[str](); print(cont)
    cont.append(0); print(cont)
    cont.append(1); print(cont)
    cont.append(2); print(cont)
    cont.append(3); print(cont)
    cont.append(4); print(cont)
