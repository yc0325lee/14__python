#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from configparser import ConfigParser
cfg = ConfigParser()
cfg.read('config.ini')


# In[ ]:


cfg.sections()


# In[ ]:


cfg.get('installation','library')


# In[ ]:


cfg.getboolean('debug','log_errors')


# In[ ]:


cfg.getint('server','port')


# In[ ]:


cfg.getint('server','nworkers')


# In[ ]:


print(cfg.get('server','signature'))


# In[ ]:


cfg.set('server','port','9000')
cfg.set('debug','log_errors','False')
import sys
cfg.write(sys.stdout)


# In[ ]:


cfg.get('installation','PREFIX')


# In[ ]:


cfg.get('installation','prefix')


# In[ ]:


# Previously read configuration
cfg.get('installation', 'prefix')


# In[ ]:


# Merge in user-specific configuration
import os
cfg.read(os.path.expanduser('~/.config.ini'))


# In[ ]:


cfg.get('installation', 'prefix')


# In[ ]:


cfg.get('installation', 'library')


# In[ ]:


cfg.getboolean('debug', 'log_errors')


# In[ ]:


cfg.get('installation','library')


# In[ ]:


cfg.set('installation','prefix','/tmp/dir')
cfg.get('installation','library')

