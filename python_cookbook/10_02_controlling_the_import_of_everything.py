#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# somemodule.py

def spam():
    pass

def grok():
    pass

blah = 42

# Only export 'spam' and 'grok'
__all__ = ['spam', 'grok']

