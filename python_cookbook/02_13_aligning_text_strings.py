#!/usr/bin/env python
# coding: utf-8

# In[1]:


text = 'Hello World'
text.ljust(20)


# In[2]:


text.rjust(20)


# In[3]:


text.center(20)


# In[4]:


text.rjust(20,'=')


# In[5]:


text.center(20,'*')


# In[6]:


format(text, '>20')


# In[7]:


format(text,'<20')


# In[8]:


format(text, '^20')


# In[9]:


format(text, '=>20s')


# In[10]:


format(text, '*^20s')


# In[11]:


'{:>10s}{:>10s}'.format('Hello','World')


# In[12]:


x = 1.2345
format(x, '>10')


# In[13]:


format(x, '^10.2f')


# In[14]:


'%-20s'%text


# In[15]:


'%20s'%text


# In[ ]:




