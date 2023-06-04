#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Some byte data
s = b'hello'
import base64


# Encode as Base64
a = base64.b64encode(s)
a


# In[2]:


# Decode from Base64
base64.b64decode(a)


# In[3]:


a = base64.b64encode(s).decode('ascii')
a


# In[ ]:




