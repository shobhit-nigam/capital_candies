#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


obje = pd.ExcelFile("last.xlsx")


# In[3]:


obje.sheet_names


# In[4]:


dfa = pd.read_excel("last.xlsx", sheet_name='thursday')


# In[6]:


dfa.shape


# In[7]:


dfa


# In[8]:


dfa.isna()


# In[10]:


dfa.isna().sum()


# In[11]:


dfa.describe()


# In[12]:


dfa.info()


# In[13]:


ia = dfa['values_a'].min()


# In[14]:


print(ia)


# In[17]:


dfa['values_c'] = dfa['values_a'] * 1.0825


# In[18]:


dfa


# In[20]:


dfb = dfa [ (dfa['values_a'] > 50) & (dfa['values_b'] > 30) ]


# In[21]:


dfb


# In[23]:


dfb.dropna()


# In[24]:


dfb


# In[25]:


dfb.dropna(inplace=True)


# In[26]:


dfb


# In[27]:


dfa


# In[28]:


lista = [12, 45, 67]
ia = 33


# In[29]:


lista.sort()


# In[30]:


del lista[1]


# In[31]:


lista


# In[32]:


del lista


# In[33]:


lista[1]


# In[34]:


del ia


# In[35]:


del dfb['Unnamed: 2']


# In[36]:


dfb


# In[38]:


dfa


# In[40]:


dfa.sort_values(['values_a'])


# In[41]:


dfa


# In[42]:


pd.read_excel("last.xlsx", index_col=1)


# In[ ]:




