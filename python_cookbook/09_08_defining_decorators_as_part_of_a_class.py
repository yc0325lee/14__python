#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from functools import wraps

class A:
    # Decorator as an instance method
    def decorator1(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print('Decorator 1')
            return func(*args, **kwargs)
        return wrapper
 

    # Decorator as a class method
    @classmethod
    def decorator2(cls, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print('Decorator 2')
            return func(*args, **kwargs)
        return wrapper


# In[ ]:


# As an instance method
a = A()

@a.decorator1
def spam():
    pass

# As a class method
@A.decorator2
def grok():
    pass


# In[ ]:


class Person:
    # Create a property instance
    first_name = property()
 
    # Apply decorator methods
    @first_name.getter
    def first_name(self):
        return self._first_name
 
    @first_name.setter
    def first_name(self, value):
        if not isinstance(value, str):
            raise TypeError('Expected a string')
        self._first_name = value


# In[ ]:


class B(A):
    @A.decorator2
    def bar(self):
        pass

