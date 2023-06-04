#!/usr/bin/env python
# coding: utf-8

# In[ ]:


s = retstr()
s

print_chars(s)


# In[ ]:


raw = b'Spicy Jalape\xc3\xb1o\xae'
raw.decode('utf-8','ignore')

raw.decode('utf-8','replace')


# In[ ]:


raw.decode('utf-8','surrogateescape')


# In[ ]:


s = raw.decode('utf-8', 'surrogateescape')
print(s)


# In[ ]:


s

s.encode('utf-8','surrogateescape')

