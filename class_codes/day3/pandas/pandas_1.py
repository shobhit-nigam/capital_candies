#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


dfa = pd.read_csv("annual.csv")


# In[3]:


dfa.shape


# In[4]:


dfa


# In[5]:


dfa.columns


# In[8]:


dfa.info()


# In[9]:


dfa['Industry_aggregation_NZSIOC'].nunique()


# In[10]:


dfa['Industry_aggregation_NZSIOC'].unique()


# In[11]:


dfa['Industry_aggregation_NZSIOC'].value_counts()


# In[12]:


# dfa['Industry_aggregation_NZSIOC'] == 'Level 1'

dfa [ dfa['Industry_aggregation_NZSIOC'] == 'Level 1' ]


# In[13]:


dfa_1 = dfa [ dfa['Industry_aggregation_NZSIOC'] == 'Level 1' ]


# In[14]:


dfa_1.to_excel("level 1.xlsx", index=False)


# In[15]:


dfa[11:30]


# In[16]:


dfa['Units'].value_counts()


# In[17]:


help(dfa.value_counts)


# In[ ]:




