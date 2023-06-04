#!/usr/bin/env python
# -*- coding:utf-8 -*-
# vim: ft=python ts=4 sw=4 tw=78 expandtab
# ----------------------------------------------------------------------------
# - file : 08_08_extending_a_property_in_a_subclass.py
# - author : yc0325lee
# - created : 2022-11-23 00:08:36 by yc032
# - modified : 2022-11-23 00:08:36 by yc032
# - description : 
# ----------------------------------------------------------------------------


class Person:
    def __init__(self, name):
        self.name = name

    # getter function
    @property
    def name(self):
        return self._name
 
    # setter function
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError('Expected a string')
        self._name = value
 
    # deleter function
    @name.deleter
    def name(self):
        raise AttributeError("Can't delete attribute")


class SubPerson(Person):
    @property
    def name(self):
        print('Getting name')
        return super().name
 
    @name.setter
    def name(self, value):
        print('Setting name to', value)
        super(SubPerson, SubPerson).name.__set__(self, value)
 
    @name.deleter
    def name(self):
        print('Deleting name')
        super(SubPerson, SubPerson).name.__delete__(self)


# In[3]:


s = SubPerson('Guido')


# In[4]:


s.name


# In[5]:


s.name = 'Larry'
s.name = 42


# In[7]:


class SubPerson(Person):
    @Person.name.getter
    def name(self):
        print('Getting name')
        return super().name


# In[8]:


class SubPerson(Person):
    @Person.name.setter
    def name(self, value):
        print('Setting name to', value)
        super(SubPerson, SubPerson).name.__set__(self, value)


# In[9]:


class SubPerson(Person):
    @property # Doesn't work
    def name(self):
        print('Getting name')
        return super().name


# In[10]:


s = SubPerson('Guido')


# In[ ]:


class SubPerson(Person):
    @Person.getter
    def name(self):
        print('Getting name')
        return super().name


# In[12]:


s = SubPerson('Guido')
s.name


# In[13]:


s.name = 'Larry'
s.name


# In[ ]:


s.name = 42


# In[ ]:


# A descriptor
class String:
    def __init__(self, name):
        self.name = name
 
    def __get__(self, instance, cls):
        if instance is None:
            return self
        return instance.__dict__[self.name]
 
    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise TypeError('Expected a string')
        instance.__dict__[self.name] = value

        
# A class with a descriptor
class Person:
    name = String('name')
    def __init__(self, name):
        self.name = name

# Extending a descriptor with a property
class SubPerson(Person):
    @property
    def name(self):
        print('Getting name')
        return super().name
 
    @name.setter
    def name(self, value):
        print('Setting name to', value)
        super(SubPerson, SubPerson).name.__set__(self, value)

    @name.deleter
    def name(self):
        print('Deleting name')
        super(SubPerson, SubPerson).name.__delete__(self)

