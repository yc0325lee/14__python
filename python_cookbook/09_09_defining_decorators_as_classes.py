#!/usr/bin/env python
# coding: utf-8

# In[1]:


import types
from functools import wraps

class Profiled:
    def __init__(self, func):
        wraps(func)(self)
        self.ncalls = 0
 
    def __call__(self, *args, **kwargs):
        self.ncalls += 1
        return self.__wrapped__(*args, **kwargs)
 
    def __get__(self, instance, cls):
        if instance is None:
            return self
        else:
            return types.MethodType(self, instance)


# In[2]:


@Profiled
def add(x, y):
    return x + y

class Spam:
    @Profiled
    def bar(self, x):
        print(self, x)


# In[ ]:


add(2,3)


# In[ ]:


add(4,5)


# In[ ]:


add.ncalls


# In[ ]:


s = Spam()


# In[ ]:


s.bar(1)


# In[ ]:


s.bar(2)


# In[ ]:


s.bar(3)


# In[ ]:


s = Spam()
s.bar(3)


# In[ ]:


s = Spam()
def grok(self, x):
    pass

grok.__get__(s,Spam)


# In[5]:


import types
from functools import wraps

def profiled(func):
    ncalls = 0
    @wraps(func)
    def wrapper(*args, **kwargs):
        nonlocal ncalls
        ncalls += 1
        return func(*args, **kwargs)
    wrapper.ncalls = lambda: ncalls
    return wrapper

# Example
@profiled
def add(x, y):
    return x + y


# In[ ]:


add(2,3)


# In[ ]:


add(4,5)


# In[ ]:


add.ncal

