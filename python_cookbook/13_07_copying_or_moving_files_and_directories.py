#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import shutil

# Copy src to dst. (cp src dst)
shutil.copy(src, dst)

# Copy files, but preserve metadata (cp -p src dst)
shutil.copy2(src, dst)

# Copy directory tree (cp -R src dst)
shutil.copytree(src, dst)

# Move src to dst (mv src dst)
shutil.move(src, dst)


# In[ ]:


shutil.copy2(src, dst, follow_symlinks=False)


# In[ ]:


shutil.copytree(src, dst, symlinks=True)


# In[ ]:


def ignore_pyc_files(dirname, filenames):
    return [name in filenames if name.endswith('.pyc')]

shutil.copytree(src, dst, ignore=ignore_pyc_files)


# In[ ]:


shutil.copytree(src, dst, ignore=shutil.ignore_patterns('*~','*.pyc'))


# In[ ]:


filename = '/Users/guido/programs/spam.py'
import os.path
os.path.basename(filename)


# In[ ]:


os.path.dirname(filename)


# In[ ]:


os.path.split(filename)


# In[ ]:


os.path.join('/new/dir', os.path.basename(filename))


# In[ ]:


os.path.expanduser('~/guido/programs/spam.py')


# In[ ]:


try:
    shutil.copytree(src, dst)
except shutil.Error as e:
    for src, dst, msg in e.args[0]:
        # src is source name
        # dst is destination name
        # msg is error message from exception
        print(dst, src, msg)

