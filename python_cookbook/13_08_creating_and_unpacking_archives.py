#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import shutil
shutil.unpack_archive('Python-3.3.0.tgz')
shutil.make_archive('py33','zip','Python-3.3.0')


# In[ ]:


shutil.get_archive_formats()

