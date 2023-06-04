#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# mypackage/A/spam.py

from . import grok


# In[ ]:


# mypackage/A/spam.py

from ..B import bar


# In[ ]:


# mypackage/A/spam.py

from mypackage.A import grok # OK
from . import grok # OK
import grok # Error (not found)


# In[ ]:


from . import grok # OK
import .grok # ERROR

