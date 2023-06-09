#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def example():
    try:
        int('N/A')
    except ValueError as e:
        raise RuntimeError('A parsing error occurred') from e...

example()


# In[ ]:


try:
    example()
except RuntimeError as e:
    print("It didn't work:", e)
    if e.__cause__:
        print('Cause:', e.__cause__)


# In[ ]:


def example2():
    try:
        int('N/A')
    except ValueError as e:
        print("Couldn't parse:", err)


example2()


# In[ ]:


def example3():
    try:
        int('N/A')
    except ValueError:
        raise RuntimeError('A parsing error occurred') from None...

example3()


# In[ ]:


try:
    
except SomeException as e:
    raise DifferentException() from e


# In[ ]:


try:

except SomeException:
    raise DifferentException()

