#!/usr/bin/env python
# coding: utf-8

# In[ ]:


raise SystemExit('It failed!')


# In[ ]:


import sys
sys.stderr.write('It failed!\n')
raise SystemExit(1)

