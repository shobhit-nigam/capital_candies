#!/usr/bin/env python
# coding: utf-8

# ### Learning json today
#  will also do:
#  - csv
#  - pandas 

# In[1]:


import json


# In[2]:


with open("example_1.json") as fj:
    data = json.load(fj)


# In[3]:


type(data)


# In[4]:


data


# In[5]:


data['size']


# In[6]:


with open("example_2.json") as fb:
    data = json.load(fb)


# In[7]:


data


# In[8]:


data['quiz']['maths']['q1']['options'][2]


# In[9]:


dictx = {10:"ww", 20:"ee", 30:"rr"}


# In[11]:


with open("example_3.json", "w") as fb:
    json.dump(dictx, fb)


# In[ ]:




