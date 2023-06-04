#!/usr/bin/env python
# -*- coding:utf-8 -*-
# vim: ft=python ts=4 sw=4 tw=78 expandtab
# ----------------------------------------------------------------------------
# - file : 01_05_implementing_a_priority_queue.py
# - author : yc0325lee
# - created : 2022-11-19 19:10:02 by yc032
# - modified : 2022-11-19 19:10:02 by yc032
# - description : 
# ----------------------------------------------------------------------------

if True:
    # - implement a queue that sorts items by a given priority and always
    #   returns the item with the highest priority on each pop operation.
    import heapq

    class PriorityQueue:
        def __init__(self):
            self._queue = []
            self._index = 0

        def push(self, item, priority):
            heapq.heappush(self._queue, (-priority, self._index, item))
            self._index += 1

        def pop(self):
            return heapq.heappop(self._queue)[-1]
            #                                ----
            #                                retrieves item

        def __len__(self):
            return len(self._queue)

        def __bool__(self):
            return len(self) > 0

        def __repr__(self):
            return repr(self._queue)
        
    class Item:
        def __init__(self, name):
            self.name = name

        def __repr__(self):
            return 'Item({!r})'.format(self.name)

    queue = PriorityQueue()
    print(queue)
    queue.push(Item('foo'), 1)
    queue.push(Item('bar'), 5)
    queue.push(Item('spam'), 4)
    queue.push(Item('grok'), 1)
    print(queue)
    print(len(queue))

    # uses '__bool__' and '__len__'
    while queue:
        print(queue.pop())

    # now queue is empty
