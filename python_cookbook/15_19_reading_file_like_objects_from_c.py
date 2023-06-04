#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import io
f = io.StringIO('Hello\nWorld\n')
import sample
sample.consume_file(f)

