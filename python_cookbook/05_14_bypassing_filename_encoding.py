#!/usr/bin/env python
# coding: utf-8

# In[2]:


import sys
sys.getfilesystemencoding()


# In[ ]:


with open('jalape\xf1o.txt', 'w') as f:
    f.write('Spicy!')


# In[ ]:


# Directory listing (decoded)
import os
os.listdir('.')


# In[ ]:


# Directory listing (raw)
os.listdir(b'.') # Note: byte string


# In[ ]:


# Open file with raw filename
with open(b'jalapen\xcc\x83o.txt') as f:
    print(f.read())

