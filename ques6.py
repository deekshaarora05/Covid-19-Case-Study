#!/usr/bin/env python
# coding: utf-8

# In[13]:


import pandas as pd
import numpy as np
import json
import datetime
import statistics


# In[14]:


state_week = pd.read_csv('state-week.csv')
state_week


# In[15]:


cases_week = pd.read_csv('cases-week.csv')
cases_week


# In[16]:


neighbor_week=pd.read_csv('neighbor-week.csv')
neighbor_week


# In[17]:


state_week.loc[1]


# In[18]:


zscore_list=[]
for i in range(0,15675):
    neighbor = neighbor_week.iloc[i]
    state = state_week.iloc[i]
    district = cases_week.iloc[i]
    if(neighbor['neighborstdev']==0):
        neighbor_zscore = round(0,2)
    else:
        neighbor_zscore = round((district['cases']-neighbor['neighbormean'])/neighbor['neighborstdev'],2)
    if(state['statestdev']==0):
        state_zscore=round(0,2)
    else:
        state_zscore = round((district['cases']-state['statemean'])/state['statestdev'],2)
    zscore_list.append((district['districtid'],district['weekid'],neighbor_zscore,state_zscore))
zscore_df = pd.DataFrame(zscore_list, columns =['districtid','weekid','neighborhoodzscore','statezscore']) 
zscore_df


# In[12]:


zscore_df.to_csv("zscore-week.csv",index=False)


# In[19]:


state_month = pd.read_csv('state-month.csv')
state_month


# In[20]:


cases_month = pd.read_csv('cases-month.csv')
cases_month


# In[21]:


neighbor_month=pd.read_csv('neighbor-month.csv')
neighbor_month


# In[25]:


zscore_month=[]
for i in range(0,4389):
    state = state_month.iloc[i]
    district= cases_month.iloc[i]
    neighbor = neighbor_month.iloc[i]
    if(neighbor['neighborstdev']==0):
        neighbor_zscore = round(0,2)
    else:
        neighbor_zscore = round((district['cases']-neighbor['neighbormean'])/neighbor['neighborstdev'],2)
    if(state['statestdev']==0):
        state_zscore=round(0,2)
    else:
        state_zscore = round((district['cases']-state['statemean'])/state['statestdev'],2)
    zscore_month.append((district['districtid'],district['monthid'],neighbor_zscore,state_zscore))


# In[26]:


zscoremonth_df = pd.DataFrame(zscore_month, columns =['districtid','monthid','neighborhoodzscore','statezscore']) 
zscoremonth_df


# In[27]:


zscoremonth_df.to_csv("zscore-month.csv",index=False)


# In[28]:


state_overall = pd.read_csv('state-overall.csv')
state_overall


# In[29]:


cases_overall = pd.read_csv('cases-overall.csv')
cases_overall


# In[30]:


neighbor_overall=pd.read_csv('neighbor-overall.csv')
neighbor_overall


# In[31]:


zscore_overall=[]
for i in range(0,627):
    state = state_overall.iloc[i]
    district = cases_overall.iloc[i]
    neighbor = neighbor_overall.iloc[i]
    if(neighbor['neighborstdev']==0):
        neighbor_zscore = round(0,2)
    else:
        neighbor_zscore = round((district['cases']-neighbor['neighbormean'])/neighbor['neighborstdev'],2)
    if(state['statestdev']==0):
        state_zscore=round(0,2)
    else:
        state_zscore = round((district['cases']-state['statemean'])/state['statestdev'],2)
    zscore_overall.append((district['districtid'],district['overallid'],neighbor_zscore,state_zscore))


# In[32]:


zscoreoverall_df=pd.DataFrame(zscore_overall, columns =['districtid','overallid','neighborhoodzscore','statezscore']) 


# In[33]:


zscoreoverall_df


# In[34]:


zscoreoverall_df.to_csv("zscore-overall.csv",index=False)


# In[ ]:




