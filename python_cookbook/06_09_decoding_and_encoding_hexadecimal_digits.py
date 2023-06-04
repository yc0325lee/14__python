#!/usr/bin/env python
# coding: utf-8

# In[3]:


# Initial byte string
s = b'hello'


# Encode as hex
import binascii
h = binascii.b2a_hex(s)
h


# In[2]:


# Decode back to bytes
binascii.a2b_hex(h)


# In[5]:


import base64
h = base64.b16encode(s)
h


# In[6]:


base64.b16decode(h)


# In[7]:


h = base64.b16encode(s)
print(h)

print(h.decode('ascii'))


# In[ ]:




