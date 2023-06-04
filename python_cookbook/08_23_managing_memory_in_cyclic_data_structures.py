#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import weakref

class Node:
    def __init__(self, value):
        self.value = value
        self._parent = None
        self.children = []
 
    def __repr__(self):
        return 'Node({!r:})'.format(self.value)
 
    # property that manages the parent as a weak-reference
    @property
    def parent(self):
        return self._parent if self._parent is None else self._parent()
 
    @parent.setter
    def parent(self, node):
        self._parent = weakref.ref(node)
 
    def add_child(self, child):
        self.children.append(child)
        child.parent = self


# In[ ]:


root = Node('parent')
c1 = Node('child')
root.add_child(c1)
print(c1.parent)


# In[ ]:


del root
print(c1.parent)


# In[ ]:


# Class just to illustrate when deletion occurs
class Data:
    def __del__(self):
        print('Data.__del__')

# Node class involving a cycle
class Node:
    def __init__(self):
        self.data = Data()
        self.parent = None
        self.children = []
 
    def add_child(self, child):
        self.children.append(child)
        child.parent = self


# In[ ]:


a = Data()
del a 


# In[ ]:


a = Node()
del a 


# In[ ]:


a = Node()
a.add_child(Node())
del a 


# In[ ]:


import gc
gc.collect() 


# In[ ]:


# Class just to illustrate when deletion occurs
class Data:
    def __del__(self):
        print('Data.__del__')

# Node class involving a cycle
class Node:
    def __init__(self):
        self.data = Data()
        self.parent = None
        self.children = []
 # NEVER DEFINE LIKE THIS.

 # Only here to illustrate pathological behavior
    def __del__(self):
        del self.data
        del.parent
        del.children
 
    def add_child(self, child):
        self.children.append(child)
        child.parent = self


# In[ ]:


a = Node()
a.add_child(Node()
del a # No message (not collected)
import gc
gc.collect() # No message (not collected)


# In[ ]:


import weakref
a = Node()
a_ref = weakref.ref(a)
a_ref


# In[ ]:


print(a_ref())


# In[ ]:


del a


# In[ ]:


print(a_ref())

