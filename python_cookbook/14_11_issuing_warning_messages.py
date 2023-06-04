#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import warnings

def func(x, y, logfile=None, debug=False):
    if logfile is not None:
        warnings.warn('logfile argument deprecated', DeprecationWarning)


# In[ ]:


import warnings
warnings.simplefilter('always')
f = open('/etc/passwd')
del f

