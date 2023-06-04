#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas
# Read a CSV file, skipping last line
rats = pandas.read_csv('rats.csv', skip_footer=1)
rats


# In[ ]:


# Investigate range of values for a certain field
rats['Current Activity'].unique()


# In[ ]:


# Filter the data
crew_dispatched = rats[rats['Current Activity'] == 'Dispatch Crew']
len(crew_dispatched)


# In[ ]:


# Find 10 most rat-infested ZIP codes in Chicago
crew_dispatched['ZIP Code'].value_counts()[:10]


# In[ ]:


# Group by completion date
dates = crew_dispatched.groupby('Completion Date')


# In[ ]:


len(dates)


# In[ ]:


# Determine counts on each day
date_counts = dates.size()
date_counts[0:10]


# In[ ]:


# Sort the counts
date_counts.sort()
date_counts[-10:]

