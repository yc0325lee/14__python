#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
m = np.matrix([[1,-2,3],[0,4,5],[7,8,-9]])
m


# In[2]:


m.T


# In[3]:


m.I


# In[4]:


v = np.matrix([[2],[3],[4]])
v


# In[5]:


m*v


# In[6]:


import numpy.linalg
numpy.linalg.eigvals(m)


# In[7]:


x = numpy.linalg.solve(m,v)
x


# In[8]:


m*x


# In[9]:


v


# In[ ]:




