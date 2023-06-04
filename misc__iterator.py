# vim: ft=python ts=4 sw=4 tw=78 expandtab
# -*- coding:utf-8 -*-
# ----------------------------------------------------------------------------
# - file : misc__iterator.py
# - author : yc0325lee
# - created : 2022-11-06 23:38:57 by yc032
# - modified : 2022-11-06 23:49:21 by yc032
# - description : 
# ----------------------------------------------------------------------------
# - 'iterator' and 'iterator object'
# ; an object representing a stream of data
# ; repeated calls to the iterator's __next__() method (or passing it to the
#   built-in function next()) return successive items in the stream.
# ; when no more data are available a 'StopIteration' exception is raised instead.
# ; at this point, the iterator object is exhausted and any further calls to
#   its __next__() method just raise StopIteration again.
# ; iterators are required to have an __iter__() method that returns the
#   iterator object itself so every iterator is also iterable and may be used
#   in most places where other iterables are accepted.
# ; one notable exception is code which attempts multiple iteration passes.
#   a container object (such as a list) produces a fresh new iterator each time
#   you pass it to the iter() function or use it in a for loop.
#   attempting this with an iterator will just return the same exhausted
#   iterator object used in the previous iteration pass, making it appear like
#   an empty container.
# ; iterator type provides both __iter__() and __next__()
# ; iterator object - an object returned by iterator. __iter__()


if True:
    basket = range(3) # basket itself is not an iterator
    print("basket=", basket)
    print("type=", type(basket))
    for item in basket:
        print("item=", item)
    # basket= range(0, 3)
    # type= <class 'range'>
    # item= 0
    # item= 1
    # item= 2

    print()

    # (1)
    iterator = iter(basket) # invokes basket.__iter__()
    print("item=", next(iterator)) # invokes basket.__next__()
    print("item=", next(iterator))
    print("item=", next(iterator), end="\n\n")
    #print("item=", next(iterator)) # -> StopIteration exception

    print()
    
    # (2)
    iterator = iter(basket) # invokes basket.__iter__()
    try:
        while True:
            print("item=", next(iterator))
    except StopIteration as ex:
        pass

    print()
    
    # (3)
    iterator = iter(basket) # invokes basket.__iter__()
    while True:
        item = next(iterator, None) # None -> sentinel
        if item is None:
            break
        print("item=", item)

