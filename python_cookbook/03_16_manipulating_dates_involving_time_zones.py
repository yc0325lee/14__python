#!/usr/bin/env python
# coding: utf-8

# In[1]:


from datetime import datetime
from pytz import timezone
d= datetime(2012,12,21,9,30,0)
print(d)


# In[3]:


central = timezone('US/Central')
loc_d = central.localize(d)
print(loc_d)


# In[4]:


bang_d = loc_d.astimezone(timezone('Asia/Kolkata'))
print(bang_d)


# In[5]:


d = datetime(2013,3,10,1,45)
loc_d = central.localize(d)
print(loc_d)


# In[7]:


from datetime import datetime
from datetime import timedelta
later = loc_d + timedelta(minutes=30)
print(later)


# In[8]:


later = central.normalize(loc_d + timedelta(minutes=30))
print later


# In[9]:


print(loc_d)


# In[11]:


import pytz
utc_d = loc_d.astimezone(pytz.utc)
print utc_d


# In[12]:


later_utc = utc_d + timedelta(minutes=30)
print(later_utc.astimezone(central))


# In[13]:


pytz.country_timezones['IN']


# In[ ]:




