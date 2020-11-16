#!/usr/bin/env python
# coding: utf-8

# In[13]:


import pandas as pd
import numpy as np
import json
import datetime


# In[14]:


f1 = open('neighbor-districts-modified.json') # Contains the neighbors of each district
neighbor = json.load(f1)
neighbor


# In[15]:


mapping=pd.read_csv('mapping.csv')
mapping


# In[23]:


neighbor_dic={}
neighbor_list=[]
for i in range(101,728):
    neighbor_dic[i]={}
neighbor_dic
id=101
for (k,v) in neighbor.items():
    l=0
    for v2 in v:
        nid=mapping[(mapping['district']==v2.split('/')[0]) & (mapping['Q_id']==v2.split('/')[1])]['district_id'].unique()[0]
        neighbor_dic[id][l]=str(nid)
        neighbor_list.append((id,nid))
        l+=1
    id+=1


# In[24]:


neighbor_dic


# In[25]:


neighbor_list


# In[26]:


edge_graph=pd.DataFrame(neighbor_list,columns=['districtid','neighbor'])
edge_graph


# In[27]:


edge_graph.to_csv("edge-graph.csv",index=False)


# In[29]:


with open("neighborlist.json", "w") as fp: 
    json.dump(neighbor_dic, fp) 


# In[ ]:




