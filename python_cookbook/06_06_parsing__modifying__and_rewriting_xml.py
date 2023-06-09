#!/usr/bin/env python
# coding: utf-8

# In[ ]:


<?xml version="1.0"?>
<stop>
    <id>14791</id>
    <nm>Clark &amp; Balmoral</nm>
    <sri>
        <rt>22</rt>
        <d>North Bound</d>
        <dd>North Bound</dd>
    </sri>
    <cr>22</cr>
    <pre>
        <pt>5 MIN</pt>
        <fd>Howard</fd>
        <v>1378</v>
        <rn>22</rn>
    </pre>
    <pre>
        <pt>15 MIN</pt>
        <fd>Howard</fd>
        <v>1867</v>
        <rn>22</rn>
    </pre>
</stop>


# In[ ]:


from xml.etree.ElementTree import parse, Element
doc = parse('pred.xml')
root = doc.getroot()
root


# In[ ]:


# Remove a few elements
root.remove(root.find('sri'))
root.remove(root.find('cr'))


# In[ ]:


root.getchildren().index(root.find('nm'))


# In[ ]:


e = Element('spam')
e.text = 'This is a test'
root.insert(2, e)


# In[ ]:


doc.write('newpred.xml', xml_declaration=True)


# In[ ]:


<?xml version='1.0' encoding='us-ascii'?>
<stop>
    <id>14791</id>
    <nm>Clark &amp; Balmoral</nm>
    <spam>This is a test</spam><pre>
        <pt>5 MIN</pt>
        <fd>Howard</fd>
        <v>1378</v>
        <rn>22</rn>
    </pre>
    <pre>
        <pt>15 MIN</pt>
        <fd>Howard</fd>
        <v>1867</v>
        <rn>22</rn>
    </pre>
</stop>

