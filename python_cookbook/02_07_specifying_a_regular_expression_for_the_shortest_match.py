#!/usr/bin/env python
# coding: utf-8

# In[5]:


import re 

str_pat = re.compile(r'\"(.*)\"')
text1 = 'Computer says "no."'
str_pat.findall(text1)


# In[6]:


text2 = 'Computer says "no." Phone says "yes."'
str_pat.findall(text2)


# In[ ]:




