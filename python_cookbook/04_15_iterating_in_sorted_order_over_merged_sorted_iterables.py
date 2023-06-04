#!/usr/bin/env python
# coding: utf-8

# In[1]:


import heapq
a = [1, 4, 7, 10]
b = [2, 5, 6, 11]

for c in heapq.merge(a, b):
    print(c)


# In[ ]:


import heapq
with open('sorted_file_1', 'rt') as file1, \
    open('sorted_file_2') 'rt' as file2, \
    open('merged_file', 'wt') as outf:

    for line in heapq.merge(file1, file2):
        outf.write(line)

