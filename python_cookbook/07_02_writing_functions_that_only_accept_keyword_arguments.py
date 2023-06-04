#!/usr/bin/env python
# coding: utf-8

# In[3]:


# Python 3
def recv(maxsize,*, block):
    'Receive a message'
    pass

recv(1024,True)


# In[4]:


recv(1024, block=True)


# In[ ]:


#Python 3

def minimum(*values, clip=None):
    m = min(values)
    if clip is not None:
        m = clip if clip > m else m
    return m

minimum(1,5,2,-5,10)
minimum(1,5,2,-5,10,clip=0)


# In[ ]:


msg = recv(1024, False)


# In[ ]:


msg = recv(1024, block = False)


# In[ ]:


help(recv)

