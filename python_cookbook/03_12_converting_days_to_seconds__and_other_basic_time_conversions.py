#!/usr/bin/env python
# coding: utf-8

# In[1]:


from datetime import timedelta
a = timedelta(days=2, hours=6)
b = timedelta(hours=4.5)
c = a + b
c.days


# In[2]:


c.seconds


# In[3]:


c.seconds/3600


# In[4]:


c.total_seconds()/3600


# In[5]:


from datetime import datetime
a = datetime(2012,9,23)
print(a + timedelta(days=10))


# In[7]:


b = datetime(2012,12,21)
d = b -a
d.days


# In[8]:


now = datetime.today()
print(now)


# In[9]:


print(now + timedelta(minutes=10))


# In[10]:


a = datetime(2012, 3, 1)
b = datetime(2012, 2, 28)
a - b


# In[11]:


(a-b).days


# In[12]:


c = datetime(2013, 3, 1)
d = datetime(2013, 2, 28)
(c-d).days


# In[13]:


a = datetime(2012, 9, 23)
a + timedelta(months=1)


# In[14]:


from dateutil.relativedelta import relativedelta
a + relativedelta(months=+1)


# In[15]:


a + relativedelta(months=+4)


# In[16]:


b = datetime(2012, 12, 21)
d = b - a
d


# In[17]:


d = relativedelta(b,a)
d


# In[18]:


d.months


# In[19]:


d.days


# In[ ]:




