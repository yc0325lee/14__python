#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import webbrowser
webbrowser.open('http://www.python.org')


# In[ ]:


# Open the page in a new browser window
webbrowser.open_new('http://www.python.org')


# In[ ]:


# Open the page in a new browser tab
webbrowser.open_new_tab('http://www.python.org')


# In[ ]:


c = webbrowser.get('firefox')
c.open('http://www.python.org')


# In[ ]:


c.open_new_tab('http://docs.python.org')

