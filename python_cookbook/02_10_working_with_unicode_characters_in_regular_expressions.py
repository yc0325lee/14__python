#!/usr/bin/env python
# coding: utf-8

# In[1]:


import re

num = re.compile('\d+')
num.match('123')


# In[7]:


print num.match('u\u0661\u0662\u0663')


# In[4]:


arabic = re.compile('[\u0600-\u06ff\u0750-\u077f\u08a0-\u08ff]+')


# In[6]:


print arabic


# In[19]:


pat = re.compile(u'stra\u00dfe', re.IGNORECASE)
s = 'straße'
pat.match(s)


# In[20]:


pat.match(s.upper())


# In[21]:


s.upper()


# In[ ]:





# In[ ]:




