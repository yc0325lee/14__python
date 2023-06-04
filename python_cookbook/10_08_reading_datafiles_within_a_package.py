#!/usr/bin/env python
# coding: utf-8

# In[ ]:


mypackage/
    __init__.py
    somedata.dat
    spam.py


# In[ ]:


# spam.py

import pkgutil
data = pkgutil.get_data(__package__, 'somedata.dat')

