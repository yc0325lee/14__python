#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from functools import wraps, partial
import logging

def logged(func=None, *, level=logging.DEBUG, name=None, message=None):
    if func is None:
        return partial(logged, level=level, name=name, message=message)
    
    logname = name if name else func.__module__
    log = logging.getLogger(logname)
    logmsg = message if message else func.__name__
    
    @wraps(func)
    def wrapper(*args, **kwargs):
        log.log(level, logmsg)
        return func(*args, **kwargs)
    return wrapper

# Example use
@logged
def add(x, y):
    return x + y

@logged(level=logging.CRITICAL, name='example')
def spam():
    print('Spam!')


# In[ ]:


@logged()
def add(x, y):
    return x+y


# In[ ]:


# Example use
@logged
def add(x, y):
    return x + y


# In[ ]:


def add(x, y):
    return x + y
add = logged(add)


# In[ ]:


@logged(level=logging.CRITICAL, name='example')
def spam():
    print('Spam!')


# In[ ]:


def spam():
    print('Spam!')
spam = logged(level=logging.CRITICAL, name='example')(spam)

