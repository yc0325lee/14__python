#!/usr/bin/env python
# coding: utf-8

# In[ ]:


try:
    client_obj.get_url(url)
except (URLError, ValueError, SocketTimeout):
    client_obj.remove_url(url)


# In[ ]:


try:
    client_obj.get_url(url)
except (URLError, ValueError):
    client_obj.remove_url(url)
except SocketTimeout:
    client_obj.handle_url_timeout(url)


# In[ ]:


try:
    f = open(filename)
except (FileNotFoundError, PermissionError):


# In[ ]:


try:
    f = open(filename)
except OSError:


# In[ ]:


try:
    f = open(filename)
except OSError as e:
    if e.errno == errno.ENOENT:
        logger.error('File not found')
    elif e.errno == errno.EACCES:
        logger.error('Permission denied')
    else:
        logger.error('Unexpected error: %d', e.errno)


# In[ ]:


f = open('missing')


# In[ ]:


try:
    f = open('missing')
except OSError:
    print('It failed')
except FileNotFoundError:
    print('File not found')

