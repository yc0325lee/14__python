#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import operator

class StructTupleMeta(type):
    def __init__(cls, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for n, name in enumerate(cls._fields):
            setattr(cls, name, property(operator.itemgetter(n)))

class StructTuple(tuple, metaclass=StructTupleMeta):
    _fields = []
    def __new__(cls, *args):
        if len(args) != len(cls._fields):
            raise ValueError('{} arguments required'.format(len(cls._fields)))
        return super().__new__(cls,args)


# In[ ]:


class Stock(StructTuple):
    _fields = ['name', 'shares', 'price']

class Point(StructTuple):
    _fields = ['x', 'y']


# In[ ]:


s = Stock('ACME', 50, 91.1)
s


# In[ ]:


s[0]


# In[ ]:


s.name


# In[ ]:


s.shares * s.price


# In[ ]:


s.shares = 23


# In[ ]:


s = Stock('ACME', 50, 91.1) # OK
s = Stock(('ACME', 50, 91.1)) # Error

