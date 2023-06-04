#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def apply_async(func, args, *, callback):
    # Compute the result
    result = func(*args)

    # Invoke the callback with the result
    callback(result)


# In[ ]:


def print_result(result):
    print('Got:', result)


# In[ ]:


def add(x,y):
    return x+y


# In[ ]:


apply_async(add, (2, 3), callback=print_result)


# In[ ]:


apply_async(add, ('hello', 'world'), callback=print_result)


# In[ ]:


class ResultHandler:
    def __init__(self):
        self.sequence = 0
    def handler(self, result):
        self.sequence += 1
        print('[{}] Got: {}'.format(self.sequence, result))


# In[ ]:


r = ResultHandler()
apply_async(add, (2, 3), callback=r.handler)

apply_async(add, ('hello', 'world'), callback=r.handler)


# In[ ]:


def make_handler():
    sequence = 0
    def handler(result):
        nonlocal sequence
        sequence += 1
        print('[{}] Got: {}'.format(sequence, result))
    return handler


# In[ ]:


handler = make_handler()
apply_async(add, (2, 3), callback=handler)

apply_async(add, ('hello', 'world'), callback=handler)


# In[ ]:


def make_handler():
    sequence = 0
    while True:
        result = yield
        sequence += 1
        print('[{}] Got: {}'.format(sequence, result))


# In[ ]:


handler = make_handler()
next(handler)
apply_async(add, (2, 3), callback=handler.send)

apply_async(add, ('hello', 'world'), callback=handler.send)


# In[ ]:


class SequenceNo:
    def __init__(self):
    self.sequence = 0

def handler(result, seq):
    seq.sequence += 1
    print('[{}] Got: {}'.format(seq.sequence, result))

seq = SequenceNo()
from functools import partial
apply_async(add, (2, 3), callback=partial(handler, seq=seq))

apply_async(add, ('hello', 'world'), callback=partial(handler, seq=seq))


# In[ ]:


apply_async(add, (2, 3), callback=lambda r: handler(r, seq))

