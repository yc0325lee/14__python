#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from abc import ABCMeta, abstractmethod

class IStream(metaclass=ABCMeta):
    @abstractmethod
    def read(self, maxsize=None):
        pass

    @abstractmethod
    def write(self, data):
        pass


# In[ ]:


class Spam(metaclass=MyMeta, debug=True, synchronize=True):


# In[ ]:


class MyMeta(type):
    # Optional
    @classmethod
    def __prepare__(cls, name, bases, *, debug=False, synchronize=False):
        # Custom processing
 
        return super().__prepare__(name, bases)
 
    # Required
    def __new__(cls, name, bases, ns, *, debug=False, synchronize=False):
        # Custom processing
 
        return super().__new__(cls, name, bases, ns)
 
    # Required
    def __init__(self, name, bases, ns, *, debug=False, synchronize=False):
        # Custom processing
 
        super().__init__(name, bases, ns)


# In[ ]:


class Spam(metaclass=MyMeta):
    debug = True
    synchronize = True

