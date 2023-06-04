# vim: ft=python ts=4 sw=4 tw=78 expandtab
# -*- coding:utf-8 -*-
# ----------------------------------------------------------------------------
# - file : data__range.py
# - author : yc0325lee
# - created : 2022-10-30 17:27:44 by lee2103
# - modified : 2022-10-30 17:27:44 by lee2103
# - description : 
# ; the range type represents an immutable sequence of numbers and is commonly
#   used for looping a specific number of times in for loops.
# ; the advantage of the range type over a regular list or tuple is that a
#   range object will always take the same (small) amount of memory, no matter
#   the size of the range it represents
# ; collections.abc.Sequence
#   containment tests, element index lookup, slicing and
#   support for negative indices 
# ----------------------------------------------------------------------------

if False:
    # class range(stop)
    # class range(start, stop[, step])
    pass

if False:
    r = range(0, 20, 2)
    print('type(r) =', type(r))
    print('r =', r)
    print('11 in r =', 11 in r)
    print('10 in r =', 10 in r)
    print('r.index(10) =', r.index(10))
    print('r[:5] =', r[:5])
    print('r[-1] =', r[-1])

    for val in r[:5]:
        print(val, sep=' ')
