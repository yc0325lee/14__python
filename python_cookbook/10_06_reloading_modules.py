#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import spam
import imp
imp.reload(spam)


# In[ ]:


# spam.py
def bar():
    print('bar')

def grok():
    print('grok')


# In[ ]:


import spam
from spam import grok
spam.bar()


# In[ ]:


grok()


# In[ ]:


def grok():
    print('New grok')


# In[ ]:


import imp
imp.reload(spam)


# In[ ]:


spam.bar()


# In[ ]:


grok()


# In[ ]:


spam.grok()

