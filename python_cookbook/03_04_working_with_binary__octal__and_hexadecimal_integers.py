#!/usr/bin/env python
# coding: utf-8

# In[1]:


x = 1234
bin(x)


# In[2]:


oct(x)


# In[3]:


hex(x)


# In[4]:


format(x, 'b')


# In[5]:


format(x,'o')


# In[6]:


format(x,'x')


# In[7]:


x = -1234
format(x, 'b')


# In[8]:


format(x,'x')


# In[9]:


x = -1234
format(2**32 + x, 'b')


# In[10]:


format(2**32 + x, 'x')


# In[11]:


int('4d2', 16)


# In[12]:


int('10011010010', 2)


# In[ ]:


import os
os.chmod('script.py', 0755)


# In[ ]:


os.chmod('script.py', 0o755)

