#!/usr/bin/env python
# coding: utf-8

# In[1]:


data = b'\x00\x124V\x00x\x90\xab\x00\xcd\xef\x01\x00#\x004'


# In[2]:


len(data)


# In[ ]:


int.from_bytes(data, 'little')


# In[ ]:


int.from_bytes(data, 'big')


# In[ ]:


x = 94522842520747284487117727783387188
x.to_bytes(16, 'big')


# In[ ]:


x.to_bytes(16, 'little')


# In[6]:


data


# In[ ]:


hi, lo = struct.unpack('>QQ', data)
(hi << 64) + lo


# In[ ]:


x = 0x01020304
x.to_bytes(4, 'big')
x.to_bytes(4, 'little')


# In[9]:


x = 523 ** 23


# In[10]:


x


# In[ ]:


x.to_bytes(16,'little')


# In[12]:


x.bit_length()


# In[13]:


nbytes, rem = divmod(x.bit_length(),8)
if rem:
    nbytes += 1


# In[ ]:


x.to_bytes(nbytes, 'little')


# In[ ]:




