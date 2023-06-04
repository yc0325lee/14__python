#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import sys
sys.path.extend(['foo-package', 'bar-package'])
import spam.blah
import spam.grok


# In[ ]:


import spam
spam.__path__


# In[ ]:


import spam.custom
import spam.grok
import spam.blah


# In[ ]:


spam

