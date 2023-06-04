#!/usr/bin/env python
# coding: utf-8

# In[1]:


add = lambda x, y: x + y


# In[2]:


add(2,3)


# In[3]:


add('hello', 'world')


# In[4]:


def add(x,y):
    return x + y


# In[5]:


add(2,3)


# In[6]:


names = ['David Beazley', 'Brian Jones','Raymond Hettinger', 'Ned Batchelder']
sorted(names, key=lambda name: name.split()[-1].lower())


# In[ ]:




