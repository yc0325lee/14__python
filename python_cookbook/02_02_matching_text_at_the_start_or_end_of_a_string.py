#!/usr/bin/env python
# coding: utf-8

# In[1]:


filename = 'spam.txt'
filename.endswith('.txt')


# In[2]:


filename.startswith('file:')


# In[3]:


url = 'http://www.python.org'
url.startswith('http:')


# In[8]:


import os
filename = os.listdir('.')
filename

[name for name in filename if name.endswith('ipynb')]
any(name.endswith('ipynb') for name in filename)


# In[ ]:


from urllib.request import urlopen

def read_data(name):
    if name.startswith(('http:', 'https:','ftp:')):
        return urlopen(name).read()
    else:
        with open(name) as f:
            return f.read()


# In[10]:


choices = ['http:','ftp:']
url = 'http://www.python.org'
url.startswith(choices)


# In[11]:


url.startswith(tuple(choices))


# In[12]:


filename = 'spam.txt'
filename[-4:] == '.txt'


# In[13]:


url = 'http://www.python.org'
url[:5] == 'http:' or url[:6] == 'https:' or url[:4]=='ftp:'


# In[17]:


import re
url = 'http://www.python.org'
print bool(re.match('http:|https:|ftp:', url))


# In[ ]:




