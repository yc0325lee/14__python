#!/usr/bin/env python
# coding: utf-8

# In[1]:


import importlib
math = importlib.import_module('math')
math.sin(2)


# In[ ]:


mod = importlib.import_module('urllib.request')
u = mod.urlopen('http://www.python.org')


# In[ ]:


import importlib

# Same as 'from . import b'
b = importlib.import_module('.b', __package__)

