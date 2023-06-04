#!/usr/bin/env python
# coding: utf-8

# In[1]:


stocks = [
 ('GOOG', 100, 490.1),
 ('AAPL', 50, 545.75),
 ('FB', 150, 7.45),
 ('HPQ', 75, 33.2),
]


# In[2]:


import sqlite3
db = sqlite3.connect('database.db')


# In[3]:


c = db.cursor()
c.execute('create table portfolio (symbol text, shares integer, price real)')

db.commit()


# In[4]:


c.executemany('insert into portfolio values (?,?,?)', stocks)

db.commit()


# In[5]:


for row in db.execute('select * from portfolio'):
    print(row)


# In[6]:


min_price = 100
for row in db.execute('select * from portfolio where price >= ?',
                       (min_price,)):
    print(row)


# In[ ]:




