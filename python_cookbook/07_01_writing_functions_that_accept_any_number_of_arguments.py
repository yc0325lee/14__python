#!/usr/bin/env python
# coding: utf-8

# In[3]:


def avg(first, *rest):
    return float(first + sum(rest))/float(1+len(rest))

avg(1,2)


# In[4]:


avg(1,2,3,4)


# In[ ]:


import html

def make_element(name, value, **attrs):
    keyvals = [' %s="%s"' % item for item in attrs.items()]
    attr_str = ''.join(keyvals)
    element = '<{name}{attrs}>{value}</{name}>'.format(
                name=name,
                attrs=attr_str,
                value=html.escape(value))
    return element

# Example
# Creates '<item size="large" quantity="6">Albatross</item>'
make_element('item', 'Albatross', size='large', quantity=6)


# Creates '<p>&lt;spam&gt;</p>'
make_element('p', '<spam>')


# In[ ]:


def anyargs(*args, **kwargs):
    print(args)
    print(kwargs)


# In[ ]:


def a(x, *args, y):
    pass


def b(x, *args, y, **kwargs):
    pass

