#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# somelib.py

import logging
log = logging.getLogger(__name__)
log.addHandler(logging.NullHandler())

# Example function (for testing)
def func():
    log.critical('A Critical Error!')
    log.debug('A debug message')


# In[ ]:


import somelib
somelib.func()


# In[ ]:


import logging
logging.basicConfig()
somelib.func()


# In[ ]:


import logging
logging.basicConfig(level=logging.ERROR)

import somelib
somelib.func()


# In[ ]:


# Change the logging level for 'somelib' only
logging.getLogger('somelib').level=logging.DEBUG
somelib.func()

