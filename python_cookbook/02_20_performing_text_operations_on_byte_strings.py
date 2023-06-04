#!/usr/bin/env python
# coding: utf-8

# In[1]:


data = b'Hello World'
data[0:5]


# In[2]:


data.startswith(b'Hello')


# In[3]:


data.split()


# In[4]:


data.replace(b'Hello', b'Hello Cruel')


# In[ ]:


data = bytearray(b'Hello World')


# In[5]:


data[0:5]


# In[6]:


data.startswith(b'Hello')


# In[ ]:


data.split()


# In[ ]:


data.replace(b'Hello', b'Hello Cruel')


# In[7]:


data = b'FOO:BAR,SPAM'

import re
re.split('[:,]',data)


# In[8]:


a = 'Hello World' # Text string
print a[0]
print a[1]


# In[ ]:


b = b'Hello World' 

print b[0]
print b[1]


# In[ ]:


s = b'Hello World'
print(s)
print(s.decode('ascii'))

