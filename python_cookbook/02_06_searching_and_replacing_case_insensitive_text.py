#!/usr/bin/env python
# coding: utf-8

# In[2]:


import re
text = 'UPPER PYTHON, lower python, Mixed Python'

re.findall('python', text, flags=re.IGNORECASE)


# In[9]:


re.sub('python', 'snake', text, flags=re.IGNORECASE)


# In[10]:


def matchcase(word):
    def replace(m):
        text = m.group()
        if text.isupper():
            return word.upper()
        elif text.islower():
            return word.lower()
        elif text[0].isupper():
            return word.capitalize()
        else:
            return word
    return replace


# In[12]:


re.sub('python', matchcase('snake'), text, flags=re.IGNORECASE)


# In[ ]:




