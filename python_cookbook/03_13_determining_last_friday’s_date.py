#!/usr/bin/env python
# coding: utf-8

# In[2]:


from datetime import datetime, timedelta

weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday','Friday', 'Saturday', 'Sunday']

def get_previous_byday(dayname, start_date=None):
    if start_date is None:
        start_date = datetime.today()
    day_num = start_date.weekday()
    day_num_target = weekdays.index(dayname)
    days_ago = (7 + day_num - day_num_target) % 7
    if days_ago == 0:
        days_ago = 7
    target_date = start_date - timedelta(days=days_ago)
    return target_date


# In[3]:


datetime.today()


# In[4]:


get_previous_byday('Monday')


# In[5]:


get_previous_byday('Tuesday')


# In[6]:


get_previous_byday('Friday')


# In[7]:


get_previous_byday('Sunday', datetime(2012,12,21))


# In[8]:


from datetime import datetime
from dateutil.relativedelta import relativedelta
from dateutil.rrule import *

d = datetime.now()
print(d)


# In[9]:


print(d + relativedelta(weekday=FR))


# In[11]:


print(d + relativedelta(weekday=FR(-1)))


# In[ ]:




