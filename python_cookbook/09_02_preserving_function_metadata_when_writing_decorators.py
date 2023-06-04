#!/usr/bin/env python
# coding: utf-8

# In[4]:


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


# In[5]:


@timethis
def countdown(n):
    '''
    Counts down
    '''
    while n > 0:
        n -= 1

countdown(100000)


# In[6]:


countdown.__name__


# In[7]:


countdown.__doc__


# In[ ]:


countdown.__annotations__


# In[ ]:


countdown.__name__

countdown.__doc__
countdown.__annotations__


# In[ ]:


countdown.__wrapped__(100000)


# In[ ]:


from inspect import signature
print(signature(countdown))


# In[ ]:




