#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# stock.py
# Example of making a class manually from parts
# Methods
def __init__(self, name, shares, price):
    self.name = name
    self.shares = shares
    self.price = price

def cost(self):
    return self.shares * self.price

cls_dict = {
 '__init__' : __init__,
 'cost' : cost,
}

# Make a class


import types

Stock = types.new_class('Stock', (), {}, lambda ns: ns.update(cls_dict))
Stock.__module__ = __name__


# In[ ]:


s = Stock('ACME', 50, 91.1)
s


# In[ ]:


s.cost()


# In[ ]:


import abc
Stock = types.new_class('Stock', (), {'metaclass': abc.ABCMeta},
                         lambda ns: ns.update(cls_dict))

Stock.__module__ = __name__
Stock


# In[ ]:


class Spam(Base, debug=True, typecheck=False):


# In[ ]:


Spam = types.new_class('Spam', (Base,),
                       {'debug': True, 'typecheck': False},
                        lambda ns: ns.update(cls_dict))


# In[ ]:


Stock = collections.namedtuple('Stock', ['name', 'shares', 'price'])
Stock


# In[ ]:


import operator
import types
import sys

def named_tuple(classname, fieldnames):
    # Populate a dictionary of field property accessors
    cls_dict = { name: property(operator.itemgetter(n))
                 for n, name in enumerate(fieldnames) }
 
    # Make a __new__ function and add to the class dict
    def __new__(cls, *args):
        if len(args) != len(fieldnames):
            raise TypeError('Expected {} arguments'.format(len(fieldnames)))
        return tuple.__new__(cls, args)

    cls_dict['__new__'] = __new__
 
    # Make the class
    cls = types.new_class(classname, (tuple,), {},
                          lambda ns: ns.update(cls_dict))
 
    # Set the module to that of the caller
    cls.__module__ = sys._getframe(1).f_globals['__name__']
    return cls


# In[ ]:


Point = named_tuple('Point', ['x', 'y'])
Point


# In[ ]:


p = Point(4, 5)
len(p)


# In[ ]:


p.x


# In[ ]:


p.y


# In[ ]:


p.x = 2


# In[ ]:


Stock = type('Stock', (), cls_dict)


# In[ ]:


import types

metaclass, kwargs, ns = types.prepare_class('Stock', (), {'metaclass': type})

