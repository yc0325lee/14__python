#!/usr/bin/env python
# coding: utf-8

# In[ ]:


try:
    
except Exception as e:
    log('Reason:', e) # Important!


# In[ ]:


def parse_int(s):
    try:
        n = int(v)
    except Exception:
        print("Couldn't parse")


# In[ ]:


parse_int('n/a')


# In[ ]:


parse_int('42')


# In[ ]:


def parse_int(s):
    try:
        n = int(v)
    except Exception as e:
        print("Couldn't parse")
        print('Reason:', e)


# In[ ]:


parse_int('42')

