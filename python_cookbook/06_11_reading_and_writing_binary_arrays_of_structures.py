#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from struct import Struct


def write_records(records, format, f):
    '''
    Write a sequence of tuples to a binary file of structures.
    '''
    record_struct = Struct(format)
    for r in records:
        f.write(record_struct.pack(*r))

# Example
if __name__ == '__main__':
    records = [ (1, 2.3, 4.5),
    (6, 7.8, 9.0),
    (12, 13.4, 56.7) ]
    with open('data.b', 'wb') as f:
        write_records(records, '<idd', f)


# In[ ]:


from struct import Struct


def read_records(format, f):
    record_struct = Struct(format)
    chunks = iter(lambda: f.read(record_struct.size), b'')
    return (record_struct.unpack(chunk) for chunk in chunks)


# Example
if __name__ == '__main__':
    with open('data.b','rb') as f:
        for rec in read_records('<idd', f):
            # Process rec


# In[ ]:


from struct import Struct


def unpack_records(format, data):
    record_struct = Struct(format)
    return (record_struct.unpack_from(data, offset)
        for offset in range(0, len(data), record_struct.size))


# Example
if __name__ == '__main__':
    with open('data.b', 'rb') as f:
        data = f.read()
    for rec in unpack_records('<idd', data):
        # Process rec


# In[ ]:


# Little endian 32-bit integer, two double precision floats
record_struct = Struct('<idd')


# In[1]:


from struct import Struct
record_struct = Struct('<idd')
record_struct.size


# In[2]:


record_struct.pack(1, 2.0, 3.0)


# In[3]:


record_struct.unpack(_)


# In[4]:


import struct
struct.pack('<idd', 1, 2.0, 3.0)


# In[5]:


struct.unpack('<idd', _)


# In[ ]:


f = open('data.b', 'rb')
chunks = iter(lambda: f.read(20), b'')
chunks


# In[ ]:


for chk in chunks:
    print(chk)


# In[ ]:


def read_records(format, f):
    record_struct = Struct(format)
    while True:
        chk = f.read(record_struct.size)
        if chk == b'':
            break
        yield record_struct.unpack(chk)
    return records


# In[ ]:


def unpack_records(format, data):
    record_struct = Struct(format)
    return (record_struct.unpack(data[offset:offset + record_struct.size])
            for offset in range(0, len(data), record_struct.size))


# In[ ]:


from collections import namedtuple


Record = namedtuple('Record', ['kind','x','y'])


with open('data.p', 'rb') as f:
    records = (Record(*r) for r in read_records('<idd', f))

    
for r in records:
    print(r.kind, r.x, r.y)


# In[ ]:


import numpy as np
f = open('data.b', 'rb')
records = np.fromfile(f, dtype='<i,<d,<d')
records


# In[ ]:


records[0]


# In[ ]:


records[1]

