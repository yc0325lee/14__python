#!/usr/bin/env python
# coding: utf-8

# In[1]:


x = 1234.56789

format(x, '0.2f')


# In[2]:


format(x, '>10.1f')


# In[3]:


format(x, '<10.1f')


# In[4]:


format(x, '^10.1f')


# In[5]:


format(x, '0,.1f')


# In[6]:


format(x, 'e')


# In[7]:


format(x, '0.2E')


# In[8]:


'The value is {:0,.2f}'.format(x)


# In[9]:


x


# In[10]:


format(x, '0.1f')


# In[13]:


format(-x, '0.1f')


# In[ ]:


#Pyton 3
swap_separators = { ord('.'):',', ord(','):'.' }
format(x, ',').translate(swap_separators)


# In[16]:


'%0.2f'%x


# In[17]:


'%10.1f'%x


# In[18]:


'%-10.1f'%x


# In[ ]:




