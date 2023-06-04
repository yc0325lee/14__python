#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def log_getattribute(cls):
    # Get the original implementation
    orig_getattribute = cls.__getattribute__
    
    # Make a new definition
    def new_getattribute(self, name):
        print('getting:', name)
        return orig_getattribute(self, name)
 
    # Attach to the class and return
    cls.__getattribute__ = new_getattribute
    return cls

# Example use
@log_getattribute
class A:
    def __init__(self,x):
        self.x = x
    def spam(self):
        pass


# In[ ]:


a = A(42)
a.x


a.spam()


# In[ ]:


class LoggedGetattribute:
    def __getattribute__(self, name):
        print('getting:', name)
        return super().__getattribute__(name)

# Example:
class A(LoggedGetattribute):
    def __init__(self,x):
        self.x = x
    def spam(self):
        pass

