#!/usr/bin/env python
# coding: utf-8

# In[1]:


def spam(a, b=42):
    print(a,b)

spam(1)


# In[2]:


spam(1,2)


# In[3]:


def spam(a, b=None):
    if b is None:
        b = []


# In[4]:


_no_value = object()


# In[5]:


def spam(a, b=_no_value):
    if b is _no_value:
        print('No b value supplied')


# In[6]:


spam(1)


# In[7]:


spam(1,2)


# In[8]:


spam(1, None)


# In[9]:


x = 42
def spam(a, b=x):
    print(a,b)


# In[10]:


spam(1)


# In[11]:


x = 23


# In[12]:


spam(1)


# In[ ]:


def spam(a, b=[]):


# In[14]:


def spam(a, b=[]):
    print(b)
    return(b)


# In[15]:


x = spam(1)


# In[16]:


x.append(99)


# In[17]:


x.append('Yow!')


# In[18]:


x


# In[19]:


spam(1)


# In[20]:


def spam(a, b=None):
    if not b:
        b = []


# In[21]:


spam(1)


# In[22]:


x=[]


# In[23]:


spam(1,x)


# In[24]:


spam(1,0)


# In[25]:


spam(1,'')


# In[ ]:




