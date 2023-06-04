#!/usr/bin/env python
# coding: utf-8

# In[2]:


import re 

comment = re.compile(r'/\*(.*?)\*/')
text1 = '/* this is a comment */'
text2 = '''/* this is a 
              multiline comment */
'''

comment.findall(text1)


# In[3]:


comment.findall(text2)


# In[4]:


comment = re.compile(r'/\*((?:.|\n)*?)\*/')
comment.findall(text2)


# In[6]:


comment = re.compile(r'/\*(.*?)\*/',re.DOTALL)
comment.findall(text2)


# In[ ]:




