#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Pair:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __repr__(self):
        return 'Pair({0.x!r}, {0.y!r})'.format(self)
    def __str__(self):
        return '({0.x!s}, {0.y!s})'.format(self)


# In[2]:


p = Pair(3, 4)
p


# In[3]:


print p


# In[4]:


p = Pair(3,4)
print('p is {0!r}'.format(p))


# In[5]:


print('p is {0}'.format(p))


# In[ ]:


f = open('file.dat')
f


# In[ ]:


def __repr__(self):
    return 'Pair({0.x!r}, {0.y!r})'.format(self)


# In[ ]:


def __repr__(self):
    return 'Pair(%r, %r)' % (self.x, self.y)

