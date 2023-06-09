#!/usr/bin/env python
# coding: utf-8

# In[11]:


import time

class Date:
    # Primary constructor
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day
 
    # Alternate constructor
    @classmethod
    def today(cls):
        t = time.localtime()
        return cls(t.tm_year, t.tm_mon, t.tm_mday)


# In[12]:


a = Date(2012, 12, 21) # Primary
b = Date.today() 


# In[13]:


class NewDate(Date):
    pass
c = Date.today() # Creates an instance of Date (cls=Date)
d = NewDate.today() # Creates an instance of NewDate (cls=NewDate)


# In[14]:


class Date:
    def __init__(self, *args):
        if len(args) == 0:
            t = time.localtime()
            args = (t.tm_year, t.tm_mon, t.tm_mday)
        self.year, self.month, self.day = args


# In[15]:


a = Date(2012, 12, 21) # Clear. A specific date.
b = Date() # ??? What does this do?


# In[ ]:


# Class method version
c = Date.today() # Clear. Today's date.

