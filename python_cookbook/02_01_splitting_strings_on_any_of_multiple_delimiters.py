#!/usr/bin/env python
# coding: utf-8

# In[1]:


line = 'asdf fjdk; afed, fjek,asdf,       foo'
import re
re.split(r'[;,\s]\s*',line)


# In[2]:


fields = re.split(r'(;|,|\s)\s*',line)
fields


# In[4]:


values = fields[::2]
delimiters = fields[1::2] + ['']
values


# In[5]:


delimiters


# In[6]:


''.join(v+d for v,d in zip(values,delimiters))


# In[7]:


re.split(r'(?:,|;|\s)\s*',line)


# In[ ]:




