#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Read the entire file as a single string
with open('somefile.txt', 'rt') as f:
    data = f.read()


# Iterate over the lines of the file
with open('somefile.txt', 'rt') as f:
    for line in f:
 # process line


# In[ ]:


# Write chunks of text data
with open('somefile.txt', 'wt') as f:
    f.write(text1)
    f.write(text2)


# In[ ]:


# Redirected print statement
with open('somefile.txt', 'wt') as f:
    print(line1, file=f)
    print(line2, file=f)


# In[ ]:


with open('somefile.txt', 'rt', encoding='latin-1') as f:


# In[ ]:


f = open('somefile.txt', 'rt')
data = f.read()
f.close()


# In[ ]:


# Read with disabled newline translation
with open('somefile.txt', 'rt', newline='') as f:


# In[ ]:


# Newline translation enabled (the default)
f = open('hello.txt', 'rt')
f.read()


# In[ ]:


# Newline translation disabled
g = open('hello.txt', 'rt', newline='')
g.read()


# In[ ]:


f = open('sample.txt', 'rt', encoding='ascii')
f.read()


# In[ ]:


# Replace bad chars with Unicode U+fffd replacement char
f = open('sample.txt', 'rt', encoding='ascii', errors='replace')
f.read()


# Ignore bad chars entirely
g = open('sample.txt', 'rt', encoding='ascii', errors='ignore')
g.read()

