#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from __future__ import print_function
with open('/etc/passwd') as f:
    try:
        while True:
            line = next(f)
            print(line, end='')
    except StopIteration:
        pass


# In[ ]:


with open('/etc/passwd') as f:
    while True:
        line = next(f, None)
        if line is None:
            break
        print(line, end='')


# In[4]:


items = [1,2,3]
it = iter(items)


# In[5]:


next(it)


# In[6]:


next(it)


# In[7]:


next(it)


# In[8]:


next(it)


# In[ ]:




