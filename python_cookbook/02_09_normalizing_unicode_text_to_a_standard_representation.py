#!/usr/bin/env python
# coding: utf-8

# In[50]:


#Python 2
s1 = u'Spicy Jalape\u00f1o'
s2 = u'Spicy Jalapen\u0303o'
print s1


# In[42]:


print s2


# In[43]:


s1 == s2


# In[44]:


len(s1)


# In[45]:


len(s2)


# In[23]:


import unicodedata

t1 = unicodedata.normalize('NFC',s1)
t2 = unicodedata.normalize('NFD',s2)

t1 == t2


# In[ ]:


#python 3
print(ascii(t1))


# In[27]:


#Python 2
print t1


# In[25]:


t3 = unicodedata.normalize('NFD',s1)
t4 = unicodedata.normalize('NFD',s2)

t3 == t4


# In[ ]:


#Python 3
print (ascii(t3))


# In[28]:


#Python 2
print t3


# In[36]:


#Python 3
s = u'\ufb01'
print s


# In[32]:


#Python 2
s = u'\ufb01'
t = unicodedata.normalize('NFD',s)


# In[34]:


print t


# In[46]:


print unicodedata.normalize('NFKD', s)


# In[47]:


print unicodedata.normalize('NFKC',s)


# In[49]:


t1 = unicodedata.normalize('NFD',s1)

''.join(c for c in t1 if not unicodedata.combining(c))


# In[ ]:




