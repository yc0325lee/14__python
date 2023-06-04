#!/usr/bin/env python
# coding: utf-8

# In[1]:


a = 4.2
b = 2.1
a + b


# In[2]:


(a+b) == 6.3


# In[3]:


from decimal import Decimal 

a = Decimal('4.2')
b = Decimal('2.1')

a+b


# In[4]:


(a+b) == Decimal('6.3')


# In[5]:


from decimal import localcontext
a = Decimal('1.3')
b = Decimal('1.7')

print(a/b)


# In[6]:


with localcontext() as ctx:
    ctx.prec = 3
    print(a/b)


# In[7]:


with localcontext() as ctx:
    ctx.prec = 50
    print(a/b)


# In[8]:


nums = [1.23e+18, 1, -1.23e+18]
sum(nums)


# In[9]:


import math
math.fsum(nums)


# In[ ]:




