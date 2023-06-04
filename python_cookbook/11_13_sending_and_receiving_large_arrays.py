#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# zerocopy.py

def send_from(arr, dest):
    view = memoryview(arr).cast('B')
    while len(view):
        nsent = dest.send(view)
        view = view[nsent:]

def recv_into(arr, source):
    view = memoryview(arr).cast('B')
    while len(view):
        nrecv = source.recv_into(view)
        view = view[nrecv:]


# In[ ]:


from socket import *
s = socket(AF_INET, SOCK_STREAM)
s.bind(('', 25000))
s.listen(1)
c,a = s.accept()


# In[ ]:


from socket import *
c = socket(AF_INET, SOCK_STREAM)
c.connect(('localhost', 25000))


# In[ ]:


# Server
import numpy
a = numpy.arange(0.0, 50000000.0)
send_from(a, c)


# In[ ]:


# Client
import numpy
a = numpy.zeros(shape=50000000, dtype=float)
a[0:10]


# In[ ]:


recv_into(a, c)
a[0:10


# In[ ]:


view = memoryview(arr).cast('B')

