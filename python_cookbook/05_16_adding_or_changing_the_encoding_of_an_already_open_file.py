#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import urllib.request
import io

u = urllib.request.urlopen('http://www.python.org')
f = io.TextIOWrapper(u,encoding='utf-8')
text = f.read()


# In[ ]:


import sys
sys.stdout.encoding

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='latin-1')
sys.stdout.encoding


# In[ ]:


f = open('sample.txt','w')
f

f.buffer

f.buffer.raw


# In[ ]:


f

f = io.TextIOWrapper(f.buffer, encoding='latin-1')
f

f.write('Hello')


# In[ ]:


f = open('sample.txt', 'w')
f

b = f.detach()
b

f.write('hello')


# In[ ]:


f = io.TextIOWrapper(b, encoding='latin-1')
f


# In[ ]:


sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='ascii',
                errors='xmlcharrefreplace')
print('Jalape\u00f1o')

