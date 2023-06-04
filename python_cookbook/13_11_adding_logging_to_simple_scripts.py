#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import logging

def main():
    # Configure the logging system
    logging.basicConfig(
            filename='app.log',
            level=logging.ERROR
        )
 
    # Variables (to make the calls that follow work)
    hostname = 'www.python.org'
    item = 'spam'
    filename = 'data.csv'
    mode = 'r'
    
    # Example logging calls (insert into your program)
    logging.critical('Host %s unknown', hostname)
    logging.error("Couldn't find %r", item)
    logging.warning('Feature is deprecated')
    logging.info('Opening file %r, mode=%r', filename, mode)
    logging.debug('Got here')

if __name__ == '__main__':
    main()


# In[ ]:


logging.basicConfig(
         filename='app.log',
         level=logging.WARNING,
         format='%(levelname)s:%(asctime)s:%(message)s')


# In[ ]:


import logging
import logging.config

def main():
    # Configure the logging system
    logging.config.fileConfig('logconfig.ini')


# In[ ]:


logging.basicConfig(level=logging.INFO)


# In[ ]:


logging.getLogger().level = logging.DEBUG

