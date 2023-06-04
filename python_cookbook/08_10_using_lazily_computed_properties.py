#!/usr/bin/env python
# coding: utf-8

# In[1]:


class lazyproperty:
    def __init__(self, func):
        self.func = func
 

    def __get__(self, instance, cls):
        if instance is None:
            return self
        else:
            value = self.func(instance)
            setattr(instance, self.func.__name__, value)
            return value


# In[2]:


import math

class Circle:
    def __init__(self, radius):
        self.radius = radius
 
    @lazyproperty
    def area(self):
        print('Computing area')
        return math.pi * self.radius ** 2
 
    @lazyproperty
    def perimeter(self):
        print('Computing perimeter')
        return 2 * math.pi * self.radius


# In[3]:


c = Circle(4.0)
c.radius


# In[5]:


print(c.area)


# In[ ]:


c.area


# In[6]:


c.perimeter


# In[7]:


c.perimeter


# In[8]:


c = Circle(4.0)


# In[9]:


vars(c)


# In[10]:


c.area


# In[11]:


c.area


# In[ ]:


del c.area
vars(c)


# In[ ]:


c.area


# In[ ]:


c.area


# In[13]:


c.area = 25
c.area


# In[14]:


def lazyproperty(func):
    name = '_lazy_' + func.__name__
    @property
    def lazy(self):
        if hasattr(self, name):
            return getattr(self, name)
        else:
            value = func(self)
            setattr(self, name, value)
            return value
    return lazy


# In[15]:


c = Circle(4.0)
c.area


# In[16]:


c.area


# In[17]:


c.area


# In[ ]:




