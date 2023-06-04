#!/usr/bin/env python
# coding: utf-8

# In[1]:


import time
from functools import wraps

# A simple decorator
def timethis(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        r = func(*args, **kwargs)
        end = time.time()
        print(end-start)
        return r
    return wrapper


# Class illustrating application of the decorator to different kinds of methods
class Spam:
    @timethis
    def instance_method(self, n):
        print(self, n)
        while n > 0:
            n -= 1
    
    @classmethod
    @timethis
    def class_method(cls, n):
        print(cls, n)
        while n > 0:
            n -= 1
 
    @staticmethod
    @timethis
    def static_method(n):
        print(n)
        while n > 0:
            n -= 1


# In[2]:


s = Spam()
s.instance_method(1000000)


# In[3]:


Spam.class_method(1000000)


# In[4]:


Spam.static_method(1000000)


# In[ ]:


class Spam:
    @timethis
    @staticmethod
    def static_method(n):
        print(n)
        while n > 0:
            n -= 1


# In[ ]:


from abc import ABCMeta, abstractmethod
class A(metaclass=ABCMeta):
    @classmethod
    @abstractmethod
    def method(cls):
        pass

