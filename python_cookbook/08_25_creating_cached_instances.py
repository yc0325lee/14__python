#!/usr/bin/env python
# coding: utf-8

# In[1]:


import logging
a = logging.getLogger('foo')
b = logging.getLogger('bar')
a is b


# In[2]:


c = logging.getLogger('foo')


# In[3]:


a is c


# In[4]:


# The class in question
class Spam:
    def __init__(self, name):
        self.name = name

# Caching support
import weakref
_spam_cache = weakref.WeakValueDictionary()

def get_spam(name):
    if name not in _spam_cache:
        s = Spam(name)
        _spam_cache[name] = s
    else:
        s = _spam_cache[name]
    return s


# In[5]:


a= get_spam('foo')


# In[6]:


b = get_spam('bar')


# In[7]:


a is b


# In[9]:


c = get_spam('foo')


# In[10]:


a is c


# In[11]:


# Note: This code doesn't quite work
import weakref

class Spam:
    _spam_cache = weakref.WeakValueDictionary()
    def __new__(cls, name):
        if name in cls._spam_cache:
            return cls._spam_cache[name]
        else:
            self = super().__new__(cls)
            cls._spam_cache[name] = self
        return self
 
    def __init__(self, name):
        print('Initializing Spam')
        self.name = name


# In[12]:


s = Spam('Dave')


# In[13]:


t = Spam('Dave')


# In[ ]:


s is t 


# In[15]:


a = get_spam('foo')
b = get_spam('bar')
c = get_spam('foo')
list(_spam_cache)


# In[16]:


del a
del c
list(_spam_cache)


# In[17]:


del b
list(_spam_cache)


# In[18]:


import weakref

class CachedSpamManager:
    def __init__(self):
        self._cache = weakref.WeakValueDictionary()
    def get_spam(self, name):
        if name not in self._cache:
            s = Spam(name)
            self._cache[name] = s
        else:
            s = self._cache[name]
        return s
 
    def clear(self):
        self._cache.clear()

        
class Spam:
    manager = CachedSpamManager()
    def __init__(self, name):
        self.name = name

def get_spam(name):
    return Spam.manager.get_spam(name)


# In[19]:


a = Spam('foo')
b = Spam('foo')
a is b


# In[20]:


class Spam:
    def __init__(self, *args, **kwargs):
        raise RuntimeError("Can't instantiate directly")
 
    # Alternate constructor
    @classmethod
    def _new(cls, name):
        self = cls.__new__(cls)
        self.name = name


# In[ ]:


import weakref

class CachedSpamManager:
    def __init__(self):
        self._cache = weakref.WeakValueDictionary()
    def get_spam(self, name):
        if name not in self._cache:
            s = Spam._new(name) # Modified creation
            self._cache[name] = s
        else:
            s = self._cache[name]
        return s

