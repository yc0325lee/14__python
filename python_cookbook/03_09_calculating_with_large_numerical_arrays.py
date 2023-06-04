#!/usr/bin/env python
# coding: utf-8

# In[1]:


x = [1,2,3,4]
y = [5,6,7,8]
x * 2


# In[2]:


x + 10


# In[3]:


x + y 


# In[4]:


import numpy as np
ax = np.array([1,2,3,4])
ay = np.array([5,6,7,8])

ax*2


# In[5]:


ax + 10


# In[6]:


ax + ay


# In[7]:


ax * ay


# In[8]:


def f(x):
    return 3*x**2 - 2*x + 7


# In[9]:


f(ax)


# In[10]:


np.sqrt(ax)


# In[11]:


np.cos(ax)


# In[13]:


grid = np.zeros((10000,10000), dtype=float)


# In[14]:


grid


# In[15]:


grid += 10


# In[16]:


grid


# In[17]:


np.sin(grid)


# In[19]:


a = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
a


# In[20]:


a[1]


# In[21]:


a[:,1]


# In[22]:


a[1:3, 1:3]


# In[23]:


a[1:3, 1:3] += 10


# In[24]:


a


# In[25]:


a + [100, 101, 102, 103]


# In[26]:


a


# In[28]:


np.where(a < 10, a, 10)


# In[ ]:


a

