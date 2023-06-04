#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# sample.py

def func(n):
    return n + 10

func('Hello')


# In[ ]:


import pdb
pdb.pm()


# In[ ]:


import traceback
import sys

try:
    func(arg)
except:
    print('**** AN ERROR OCCURRED ****')
    traceback.print_exc(file=sys.stderr)


# In[ ]:


def sample(n):
    if n > 0:
        sample(n-1)
    else:
        traceback.print_stack(file=sys.stderr)

sample(5)


# In[ ]:


import pdb
def func(arg):
 
    pdb.set_trace()

