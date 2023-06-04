#!/usr/bin/env python
# coding: utf-8

# In[1]:


from fractions import Fraction
a = Fraction(5,4)
b = Fraction(7,16)
print (a+b)


# In[2]:


print (a*b)


# In[3]:


c = a*b
c.numerator


# In[4]:


c.denominator


# In[5]:


float(c)


# In[6]:


print(c.limit_denominator(8))


# In[7]:


x = 3.75
y = Fraction(*x.as_integer_ratio())
y


# In[ ]:




