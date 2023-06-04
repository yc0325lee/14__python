#!/usr/bin/env python
# coding: utf-8

# In[ ]:


with open('somefile', 'wt') as f:
    f.write('Hello\n')

with open('somefile', 'xt') as f:
    f.write('Hello\n')


# In[ ]:


import os
if not os.path.exists('somefile'):
    with open('somefile', 'wt') as f:
        f.write('Hello\n')

else:
    print('File already exists!')

