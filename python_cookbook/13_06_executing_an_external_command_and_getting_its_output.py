#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import subprocess
out_bytes = subprocess.check_output(['netstat','-a'])


# In[ ]:


out_text = out_bytes.decode('utf-8')


# In[ ]:


try:
    out_bytes = subprocess.check_output(['cmd','arg1','arg2'])
except subprocess.CalledProcessError as e:
    out_bytes = e.output # Output generated before error
    code = e.returncode # Return code


# In[ ]:


out_bytes = subprocess.check_output(['cmd','arg1','arg2'],
            stderr=subprocess.STDOUT)


# In[ ]:


try:
    out_bytes = subprocess.check_output(['cmd','arg1','arg2'], timeout=5)
except subprocess.TimeoutExpired as e:


# In[ ]:


out_bytes = subprocess.check_output('grep python | wc > out', shell=True)


# In[ ]:


import subprocess

# Some text to send
text = b'''
hello world
this is a test
goodbye
'''

# Launch a command with pipes
p = subprocess.Popen(['wc'],
        stdout = subprocess.PIPE,
        stdin = subprocess.PIPE)

# Send the data and get the output
stdout, stderr = p.communicate(text)

# To interpret as text, decode
out = stdout.decode('utf-8')
err = stderr.decode('utf-8')

