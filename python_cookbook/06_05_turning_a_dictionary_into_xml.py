#!/usr/bin/env python
# coding: utf-8

# In[1]:


from xml.etree.ElementTree import Element
def dict_to_xml(tag, d):
    '''
    Turn a simple dict of key/value pairs into XML
    '''
    elem = Element(tag)
    for key, val in d.items():
        child = Element(key)
        child.text = str(val)
        elem.append(child)
    return elem


# In[2]:


s = { 'name': 'GOOG', 'shares': 100, 'price':490.1 }
e = dict_to_xml('stock', s)
e


# In[3]:


from xml.etree.ElementTree import tostring
tostring(e)


# In[4]:


e.set('_id','1234')
tostring(e)


# In[5]:


def dict_to_xml_str(tag, d):
    '''
    Turn a simple dict of key/value pairs into XML
    '''
    parts = ['<{}>'.format(tag)]
    for key, val in d.items():
        parts.append('<{0}>{1}</{0}>'.format(key,val))
    parts.append('</{}>'.format(tag))
    return ''.join(parts)


# In[6]:


d = { 'name' : '<spam>' }


# In[7]:


# String creation
dict_to_xml_str('item',d)


# In[8]:


# Proper XML creation
e = dict_to_xml('item',d)
tostring(e)


# In[9]:


from xml.sax.saxutils import escape, unescape
escape('<spam>')

unescape(_)


# In[ ]:




