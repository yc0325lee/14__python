#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from functools import partial
RECORD_SIZE = 32

with open('somefile.data', 'rb') as f:
    records = iter(partial(f.read, RECORD_SIZE), b'')
    for r in records:


# In[ ]:




