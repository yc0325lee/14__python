#!/usr/bin/env python
# coding: utf-8

# In[1]:


def frange(start, stop, increment):
    x = start
    while x < stop:
        yield x
        x += increment


# In[2]:


for n in frange(0,4,0.5):
    print n


# In[3]:


list(frange(0,1,0.125))


# In[6]:


def countdown(n):
    print('Starting to count from', n)
    while n > 0:
        yield n
        n -= 1
    print('Done!')


# In[7]:


c = countdown(3)


# In[8]:


c


# In[9]:


next(c)


# In[10]:


next(c)


# In[11]:


next(c)


# In[12]:


next(c)


# In[ ]:




