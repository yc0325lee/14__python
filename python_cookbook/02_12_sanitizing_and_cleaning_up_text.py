#!/usr/bin/env python
# coding: utf-8

# In[ ]:


s = 'pýtĥöñ\fis\tawesome\r\n'
s


# In[ ]:


# Python 3
remap = {
    ord('\t'): ' ',
    ord('\f'): ' ',
}

a = s.translate(remap)
a


# In[ ]:


import unicodedata
import sys

cmb_chrs = dict.fromkeys(c for c in range(sys.maxunicode) if unicodedata.combining(chr(c)))

b = unicodedata.normalize('NFD', a)
b


# In[ ]:


b.translate(cmb_chrs)


# In[ ]:


# Python 3
digitmap = { c: ord('0') + unicodedata.digit(chr(c))
             for c in range(sys.maxunicode)
             if unicodedata.category(chr(c)) == 'Nd'}
len(digitmap)


# In[ ]:


x = '\u0661\u0662\u0663'
x.translate(digitmap)


# In[ ]:


a


# In[ ]:


b = unicodedata.normalize('NFD', a)
b.encode('ascii', 'ignore').decode('ascii')


# In[ ]:


def clean_spaces(s):
    s = s.replace('\r', '')
    s = s.replace('\t', ' ')
    s = s.replace('\f', ' ')
    return s

