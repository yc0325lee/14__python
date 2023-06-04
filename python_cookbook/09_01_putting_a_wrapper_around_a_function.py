#!/usr/bin/env python
# coding: utf-8

# In[5]:


import time
from functools import wraps

def timethis(func):
    '''
    Decorator that reports the execution time.
    '''
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__, end-start)
        return result
    return wrapper


# In[6]:


@timethis
def countdown(n):
    '''
    Counts down
    '''
    while n > 0:
        n -= 1

countdown(100000)


# In[7]:


countdown(10000000)


# In[ ]:


@timethis
def countdown(n):


# In[ ]:


def countdown(n):

countdown = timethis(countdown)


# In[ ]:


class A:
    @classmethod
    def method(cls):
        pass

class B:
    # Equivalent definition of a class method
    def method(cls):
        pass
    method = classmethod(method)

