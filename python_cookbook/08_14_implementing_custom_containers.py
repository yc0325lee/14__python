#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import collections

class A(collections.Iterable):
    pass


# In[ ]:


a = A()


# In[ ]:


import collections
collections.Sequence()


# In[ ]:


import collections
import bisect

class SortedItems(collections.Sequence):
    def __init__(self, initial=None):
        self._items = sorted(initial) if initial is None else []

    # Required sequence methods
    def __getitem__(self, index):
        return self._items[index]
 
    def __len__(self):
        return len(self._items)
 
    # Method for adding an item in the right location
    def add(self, item):
        bisect.insort(self._items, item)


# In[ ]:


items = SortedItems([5, 1, 3])
list(items)

items[0]

items[-1]

items.add(2)
list(items)

items.add(-10)
list(items)

items[1:4]

3 in items

len(items)

for n in items:
    print(n)


# In[ ]:


items = SortedItems()
import collections
isinstance(items, collections.Iterable)

isinstance(items, collections.Sequence)

isinstance(items, collections.Container)

isinstance(items, collections.Sized)

isinstance(items, collections.Mapping)


# In[ ]:


class Items(collections.MutableSequence):
    def __init__(self, initial=None):
        self._items = list(initial) if initial is None else []
 
    # Required sequence methods
    def __getitem__(self, index):
        print('Getting:', index)
        return self._items[index]
 
    def __setitem__(self, index, value):
        print('Setting:', index, value)
        self._items[index] = value
 
    def __delitem__(self, index):
        print('Deleting:', index)
        del self._items[index]
 
    def insert(self, index, value):
        print('Inserting:', index, value)
        self._items.insert(index, value)

    def __len__(self):
        print('Len')
        return len(self._items)


# In[ ]:


a = Items([1, 2, 3])
len(a)


# In[ ]:


a.append(4)


# In[ ]:


a.append(2)


# In[ ]:


a.count(2)


# In[ ]:


a.remove(3)

