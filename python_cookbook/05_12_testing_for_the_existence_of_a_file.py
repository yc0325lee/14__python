#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import os
os.path.exists('/etc/passwd')

os.path.exists('/tmp/spam')


# In[ ]:


os.path.isfile('/etc/passwd')


# In[ ]:


os.path.isdir('/etc/passwd')


# In[ ]:


os.path.islink('/usr/local/bin/python3')


# In[ ]:


os.path.realpath('/usr/local/bin/python3')


# In[ ]:


os.path.getsize('/etc/passwd')


# In[ ]:


os.path.getmtime('/etc/passwd')


# In[ ]:


import time
time.ctime(os.path.getmtime('/etc/passwd'))


# In[ ]:


os.path.getsize('/Users/guido/Desktop/foo.txt')

