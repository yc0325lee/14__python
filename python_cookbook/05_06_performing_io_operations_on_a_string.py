#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Python 2

import io
s = io.StringIO()
int(s.write(u'Hello World\n'))


# In[ ]:


print('This is a test', file=s)


# In[ ]:


# Python 3
s = io.StringIO()
s.write('Hello World\n')


# In[ ]:


s.getvalue()


# In[15]:


# Wrap a file interface around an existing string
s = io.StringIO(u'Hello\nWorld\n')
s.read(4)


# In[16]:


s.read()


# In[17]:


s = io.BytesIO()
s.write(b'binary data')
s.getvalue()


# In[ ]:




