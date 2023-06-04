#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def bad_filename(filename):
    return repr(filename)[1:-1]

try:
    print(filename)
except UnicodeEncodeError:
    print(bad_filename(filename))


# In[ ]:


import os
files = os.listdir('.')
files


# In[ ]:


for name in files:
    print(name)


# In[ ]:


for name in files:
    try:
        print(name)
    except UnicodeEncodeError:
        print(bad_filename(name))


# In[ ]:


def bad_filename(filename):
    temp = filename.encode(sys.getfilesystemencoding(), errors='surrogateescape')
    return temp.decode('latin-1')


# In[ ]:


for name in files:
    try:
        print(name)
    except UnicodeEncodeError:
        print(bad_filename(name))


# In[ ]:




