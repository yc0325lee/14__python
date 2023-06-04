#!/usr/bin/env python
# coding: utf-8

# In[ ]:


a = 13
exec('b = a + 1')
print(b)


# In[ ]:


def test():
    a = 13
    exec('b = a + 1')
    print(b)

test()


# In[ ]:


def test():
    a = 13
    loc = locals()
    exec('b = a + 1')
    b = loc['b']
    print(b)

test()


# In[ ]:


def test1():
    x = 0
    exec('x += 1')
    print(x)

test1()


# In[ ]:


def test2():
    x = 0
    loc = locals()
    print('before:', loc)
    exec('x += 1')
    print('after:', loc)
    print('x =', x)

test2()


# In[ ]:


def test3():
    x = 0
    loc = locals()
    print(loc)
    exec('x += 1')
    print(loc)
    locals()
    print(loc)

test3()


# In[ ]:


def test4():
    a = 13
    loc = { 'a' : a }
    glb = { }
    exec('b = a + 1', glb, loc)
    b = loc['b']
    print(b)

test4()

