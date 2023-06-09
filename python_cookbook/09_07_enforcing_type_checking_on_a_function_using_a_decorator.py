#!/usr/bin/env python
# coding: utf-8

# In[2]:


#@typeassert(int, int)
def add(x, y):
    return x + y


add(2, 3)


# In[3]:


add(2, 'hello')


# In[ ]:


from inspect import signature
from functools import wraps

def typeassert(*ty_args, **ty_kwargs):
    def decorate(func):
        # If in optimized mode, disable type checking
        if not __debug__:
            return func

        # Map function argument names to supplied types
        sig = signature(func)
        bound_types = sig.bind_partial(*ty_args, **ty_kwargs).arguments
 
    @wraps(func)
    def wrapper(*args, **kwargs):
        bound_values = sig.bind(*args, **kwargs)
        # Enforce type assertions across supplied arguments
        for name, value in bound_values.arguments.items():
            if name in bound_types:
                if not isinstance(value, bound_types[name]):
                    raise TypeError(
                        'Argument {} must be {}'.format(name, bound_types[name])
                        )
            return func(*args, **kwargs)
        return wrapper
    return decorate


# In[ ]:


@typeassert(int, z=int)
def spam(x, y, z=42):
    print(x, y, z)

spam(1, 2, 3)


# In[ ]:


spam(1, 'hello', 3)

spam(1, 'hello', 'world')


# In[ ]:


def decorate(func):
    # If in optimized mode, disable type checking
    if not __debug__:
        return func


# In[ ]:


from inspect import signature
def spam(x, y, z=42):
    pass

sig = signature(spam)
print(sig)


# In[ ]:


sig.parameters


# In[ ]:


sig.parameters['z'].name


# In[ ]:


sig.parameters['z'].default


# In[ ]:


sig.parameters['z'].kind


# In[ ]:


bound_types = sig.bind_partial(int,z=int)
bound_types


# In[ ]:


bound_types.arguments


# In[ ]:


bound_values = sig.bind(1, 2, 3)
bound_values.arguments


# In[ ]:


for name, value in bound_values.arguments.items():
    if name in bound_types.arguments:
        if not isinstance(value, bound_types.arguments[name]):
            raise TypeError()


# In[ ]:


@typeassert(int, list)
def bar(x, items=None):
    if items is None:
        items = []
    items.append(x)
    return items
bar(2)


# In[ ]:


bar(2,3)

