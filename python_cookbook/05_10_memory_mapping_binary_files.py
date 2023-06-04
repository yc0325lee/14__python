#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import os
import mmap

def memory_map(filename, access=mmap.ACCESS_WRITE):
    size = os.path.getsize(filename)
    fd = os.open(filename, os.O_RDWR)
    return mmap.mmap(fd, size, access=access)


# In[ ]:


size = 1000000
with open('data', 'wb') as f:
    f.seek(size-1)
    f.write(b'\x00')


# In[ ]:


m = memory_map('data')
len(m)

m[0:10]

m[0]

# Reassign a slice
m[0:11] = b'Hello World'
m.close()
# Verify that changes were made
with open('data', 'rb') as f:
    print(f.read(11))


# In[ ]:


with memory_map('data') as m:
    print(len(m))
    print(m[0:10])


# In[ ]:


m.closed


# In[ ]:


m = memory_map(filename, mmap.ACCESS_READ)


# In[ ]:


m = memory_map(filename, mmap.ACCESS_COPY)


# In[ ]:


m = memory_map('data')
# Memoryview of unsigned integers
v = memoryview(m).cast('I')
v[0] = 7
m[0:4]

m[0:4] = b'\x07\x01\x00\x00'
v[0]

