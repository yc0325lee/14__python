#!/usr/bin/env python
# coding: utf-8

# In[ ]:


s = 'Spicy Jalape\u00f1o'
print_chars(s)

print_wchars(s)


# In[ ]:


import sys
s = 'Spicy Jalape\u00f1o'
sys.getsizeof(s)

print_chars(s)

sys.getsizeof(s)

print_wchars(s)

sys.getsizeof(s)

