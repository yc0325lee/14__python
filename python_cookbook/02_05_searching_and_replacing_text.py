#!/usr/bin/env python
# coding: utf-8

# In[1]:


text = 'yeah, but no, but yeah, but no, but yeah'

text.replace('yeah', 'yes')


# In[2]:


text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'

import re
re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\1-\2', text)


# In[3]:


import re
datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
datepat.sub(r'\3-\1-\2', text)


# In[4]:


from calendar import month_abbr

def change_date(m):
    mon_name = month_abbr[int(m.group(1))]
    return '{} {} {}'.format(m.group(2), mon_name, m.group(3))

datepat.sub(change_date, text)


# In[5]:


newtext, n = datepat.subn(r'\3-\1-\2', text)
newtext


# In[6]:


n


# In[ ]:




