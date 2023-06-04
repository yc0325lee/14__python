#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# mymodule.py

class A:
    def spam(self):
        print('A.spam')

class B(A):
    def bar(self):
        print('B.bar')


# In[ ]:


# a.py

class A:
    def spam(self):
        print('A.spam')


# In[ ]:


# b.py

from .a import A

class B(A):
    def bar(self):
        print('B.bar')


# In[ ]:


# __init__.py

from .a import A
from .b import B


# In[ ]:


import mymodule
a = mymodule.A()
a.spam()

b = mymodule.B()
b.bar()


# In[ ]:


from mymodule.a import A
from mymodule.b import B


# In[ ]:


from mymodule import A, B


# In[ ]:


# __init__.py

def A():
    from .a import A
    return A()

def B():
    from .b import B
    return B()


# In[ ]:


import mymodule
a = mymodule.A()
a.spam()


# In[ ]:


if isinstance(x, mymodule.A): # Error
 
if isinstance(x, mymodule.a.A): # Ok

