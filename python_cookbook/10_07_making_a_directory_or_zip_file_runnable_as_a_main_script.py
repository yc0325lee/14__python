#!/usr/bin/env python
# coding: utf-8

# In[ ]:


myapplication/
    spam.py
    bar.py
    grok.py
    __main__.py


# In[ ]:


bash % ls
spam.py bar.py grok.py __main__.py
bash % zip -r myapp.zip *.py
bash % python3 myapp.zip


# In[ ]:


#!/usr/bin/env python3 /usr/local/bin/myapp.zip

