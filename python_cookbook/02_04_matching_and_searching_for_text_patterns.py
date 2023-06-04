#!/usr/bin/env python
# coding: utf-8

# In[6]:


text = 'yeah, but no, but yeah, but no, but yeah'

text == 'yeah'


# In[7]:


text.startswith('yeah')


# In[8]:


text.endswith('no')


# In[9]:


text.find('no')


# In[11]:


text1 = '11/27/2012'
text2 = 'Nov 27, 2012'

import re

if re.match(r'\d+/\d+/\d+', text1):
    print('yes')
else:
    print('no')


# In[12]:


if re.match(r'\d+/\d+/\d+',text2):
    print('yes')
else:
    print('no')


# In[13]:


datepat = re.compile(r'\d+/\d+/\d+')

if datepat.match(text1):
    print('yes')
else:
    print('no')


# In[14]:


if datepat.match(text2):
    print('yes')
else:
    print('no')


# In[15]:


text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
datepat.findall(text)


# In[16]:


datepat = re.compile(r'(\d+)/(\d+)/(\d+)')


# In[17]:


m = datepat.match('11/27/2012')
m


# In[18]:


m.group(0)


# In[19]:


m.group(1)


# In[20]:


m.group(2)


# In[21]:


m.group(3)


# In[22]:


m.groups()


# In[23]:


text


# In[24]:


datepat.findall(text)


# In[25]:


for month,day,year in datepat.findall(text):
    print('{}-{}-{}'.format(year,month,day))


# In[26]:


for m in datepat.finditer(text):
    print(m.groups())


# In[27]:


m = datepat.match('11/27/2012abcdef')
m


# In[28]:


m.group()


# In[29]:


datepat = re.compile(r'(\d+)/(\d+)/(\d+)$')
datepat.match('11/27/2012abcdef')
datepat.match('11/27/2012')


# In[31]:


re.findall(r'(\d+)/(\d+)/(\d+)',text)


# In[ ]:




