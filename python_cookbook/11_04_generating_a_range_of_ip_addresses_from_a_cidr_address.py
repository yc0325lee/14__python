#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import ipaddress
net = ipaddress.ip_network('123.45.67.64')
net


# In[ ]:


for a in net:
    print(a)


# In[ ]:


net6 = ipaddress.ip_network('12:3456:78:90ab:cd:ef01:23:30/125')
net6


# In[ ]:


for a in net6:
    print(a)


# In[ ]:


net.num_addresses
net[0]


# In[ ]:


net[1]


# In[ ]:


net[-1]


# In[ ]:


net[-2]


# In[ ]:


a = ipaddress.ip_address('123.45.67.69')
a in net


# In[ ]:


b = ipaddress.ip_address('123.45.67.123')
b in net


# In[ ]:


inet = ipaddress.ip_interface('123.45.67.73/27')
inet.network


# In[ ]:


inet.ip


# In[ ]:


a = ipaddress.ip_address('127.0.0.1')
from socket import socket, AF_INET, SOCK_STREAM
s = socket(AF_INET, SOCK_STREAM)
s.connect((a, 8080))


# In[ ]:


s.connect((str(a), 8080))

