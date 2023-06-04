#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class NetworkError(Exception):
    pass

class HostnameError(NetworkError):
    pass

class TimeoutError(NetworkError):
    pass

class ProtocolError(NetworkError):
    pass


# In[ ]:


try:
    msg = s.recv()

except TimeoutError as e:
     
except ProtocolError as e:


# In[ ]:


try:
    s.send(msg)
except ProtocolError:


# In[ ]:


try:
    s.send(msg)
except NetworkError:


# In[ ]:


class CustomError(Exception):
    def __init__(self, message, status):
        super().__init__(message, status)
        self.message = message
        self.status = status


# In[ ]:


try:
    raise RuntimeError('It failed')
except RuntimeError as e:
    print(e.args)


# In[ ]:


try:
    raise RuntimeError('It failed', 42, 'spam')
except RuntimeError as e:
    print(e.args)

