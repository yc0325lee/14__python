#!/usr/bin/env python
# coding: utf-8

# In[ ]:


text = 'foo = 23 + 42 * 10'


# In[3]:


tokens  = [('NAME', 'foo'), ('EQ','='), ('NUM', '23'), ('PLUS','+'),
           ('NUM', '42'), ('TIMES', '*'), ('NUM', '10')]

import re
NAME = r'(?P<NAME>[a-zA-Z_][a-zA-Z_0-9]*)'
NUM = r'(?P<NUM>\d+)'
PLUS = r'(?P<PLUS>\+)'
TIMES = r'(?P<TIMES>\*)'
EQ = r'(?P<EQ>=)'
WS = r'(?P<WS>\s+)'

master_pat = re.compile('|'.join([NAME, NUM, PLUS, TIMES, EQ, WS]))


# In[4]:


master_pat


# In[5]:


scanner = master_pat.scanner('foo = 42')
scanner.match()


# In[6]:


_.lastgroup, _.group()


# In[7]:


scanner.match()


# In[9]:


_.lastgroup, _.group()


# In[10]:


scanner.match()


# In[11]:


_.lastgroup, _.group()


# In[12]:


scanner.match()


# In[13]:


_.lastgroup, _.group()


# In[14]:


scanner.match()


# In[16]:


_.lastgroup, _.group()


# In[17]:


scanner.match()


# In[18]:


from collections import namedtuple

Token = namedtuple('Token', ['type','value'])

def generate_tokens(pat, text):
    scanner = pat.scanner(text)
    for m in iter(scanner.match, None):
        yield Token(m.lastgroup, m.group())


# In[19]:


for tok in generate_tokens(master_pat, 'foo = 42'):
    print(tok)


# In[22]:


text = 'foo = 42'
tokens = (tok for tok in generate_tokens(master_pat, text) if tok.type != 'WS')

for tok in tokens:
    print tok


# In[23]:


LT = r'(?P<LT><)'
LE = r'(?P<LE><=)'
EQ = r'(?P<EQ>=)'

master_pat = re.compile('|'.join([LE, LT, EQ])) 


# In[25]:


PRINT = r'(P<PRINT>print)'
NAME = r'(P<NAME>[a-zA-Z_][a-zA-Z_0-9]*)'
master_pat = re.compile('|'.join([PRINT, NAME]))

for tok in generate_tokens(master_pat, 'printer'):
    print(tok)


# In[ ]:




