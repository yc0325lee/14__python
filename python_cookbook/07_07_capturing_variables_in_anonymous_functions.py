#!/usr/bin/env python
# coding: utf-8

# In[1]:


x =10
a = lambda y:x+y


# In[2]:


x=20


# In[3]:


b= lambda y:x+y


# In[4]:


a(10)


# In[5]:


b(10)


# In[6]:


x = 15
a(10)


# In[7]:


x=3


# In[8]:


a(10)


# In[9]:


x=10
a = lambda y,x = x:x+y


# In[10]:


x = 20


# In[11]:


b = lambda y,x= x:x+y


# In[12]:


a(10)


# In[13]:


b(10)


# In[14]:


funcs = [lambda x: x+n for n in range(5)]
for f in funcs:
    print(f(0))


# In[15]:


funcs = [lambda x, n=n: x+n for n in range(5)]
for f in funcs:
    print(f(0))


# In[ ]:




