#!/usr/bin/env python
# coding: utf-8

# In[1]:


s = '   hello world  \n'
s.strip()


# In[2]:


s.lstrip()


# In[3]:


s.rstrip()


# In[4]:


t = '-----hello====='
t.strip('-')


# In[6]:


t.lstrip('-')


# In[8]:


t.strip('-=')


# In[9]:


s = '   hello          world     \n'
s = s.strip()
s


# In[10]:


s.replace(' ','')


# In[11]:


import re
re.sub('\s+', ' ', s)


# In[ ]:


with open(filename) as f:
    lines = (line.strip() for line in f)
    for line in lines:

