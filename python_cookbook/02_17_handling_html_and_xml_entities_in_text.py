#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Python 3
s = 'Elements are written as "<tag>text</tag>".'
import html
print(s)


# In[ ]:


print(html.escape(s))


# In[ ]:


print(html.escape(s, quote=False))


# In[ ]:


s = 'Spicy Jalapeño'
s.encode('ascii', errors='xmlcharrefreplace')


# In[ ]:


s = 'Spicy &quot;Jalape&#241;o&quot.'
from html.parser import HTMLParser
p = HTMLParser()
p.unescape(s)


# In[ ]:


t = 'The prompt is &gt;&gt;&gt;'
from xml.sax.saxutils import unescape
unescape(t)


# In[ ]:




