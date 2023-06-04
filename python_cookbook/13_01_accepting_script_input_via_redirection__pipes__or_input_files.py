#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#!/usr/bin/env python3
import fileinput

with fileinput.input() as f_input:
    for line in f_input:
        print(line, end='')


# In[ ]:


import fileinput
with fileinput.input('/etc/passwd') as f:
    for line in f:
        print(f.filename(), f.lineno(), line, end='')

