#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day


# In[ ]:


d = Date.__new__(Date)
d


# In[ ]:


d.year


# In[ ]:


data = {'year':2012, 'month':8, 'day':29}
for key, value in data.items():
    setattr(d, key, value)

d.year


# In[ ]:


d.month


# In[ ]:


from time import localtime

class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day
 

    @classmethod
    def today(cls):
        d = cls.__new__(cls)
        t = localtime()
        d.year = t.tm_year
        d.month = t.tm_mon
        d.day = t.tm_mday
        return d


# In[ ]:


data = { 'year': 2012, 'month': 8, 'day': 29 }

