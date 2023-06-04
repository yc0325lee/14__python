#!/usr/bin/env python
# coding: utf-8

# In[1]:


print('ACME', 50, 91.5)


# In[ ]:


# Python 3
print('ACME', 50, 91.5, sep=',')


# In[2]:


# Python 2
from __future__ import print_function
print('ACME', 50, 91.5, sep=',')


# In[ ]:


#Python 3
 print('ACME', 50, 91.5, sep=',', end='!!\n')


# In[ ]:


# Python 2
from __future__ import print_function
print('ACME', 50, 91.5, sep=',', end='!!\n')


# In[4]:


for i in range(5):
    print(i)


# In[6]:


for i in range(5):
    print(i, end=' ')


# In[ ]:


#Python 3
print('.'.join('ACME','50','91.5'))


# In[9]:


#Python 2
print('.'.join(['ACME','50','91.5']))


# In[10]:


row = ('ACME', 50, 91.5)
print(','.join(row))


# In[11]:


print('.'.join(str(x) for x in row))


# In[12]:


print(*row, sep='.')


# In[ ]:




