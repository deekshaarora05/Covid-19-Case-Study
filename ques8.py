#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
import json
import datetime
import statistics


# In[8]:


zscore_week = pd.read_csv("zscore-week.csv")


# In[9]:


zweek_nbr=zscore_week.sort_values(['weekid','neighborhoodzscore'],ascending=[True, False])
zweek_nbr.reset_index(drop=True,inplace=True)
zweek_nbr


# In[10]:


zweek_state=zscore_week.sort_values(['weekid','statezscore'],ascending=[True, False])
zweek_state.reset_index(drop=True,inplace=True)
zweek_state


# In[18]:


week_df = pd.DataFrame(columns=['weekid','method','spot','district1','district2','district3','district4','district5'])
i=0
while(i<=15674):
    hotnbr_list=[]
    coldnbr_list=[]
    hotstate_list=[]
    coldstate_list=[]
    hotnbr = zweek_nbr[i:i+627].head(5)
    coldnbr = zweek_nbr[i+622:i+627]
    hotstate = zweek_state[i:i+627].head(5)
    coldstate = zweek_state[i+622:i+627]
    week_id = str(int(hotnbr.iloc[0]['weekid']))
    hotnbr_list=list(hotnbr['districtid'])
    coldnbr_list=list(coldnbr['districtid'])
    hotstate_list=list(hotstate['districtid'])
    coldstate_list=list(coldstate['districtid'])
    week_df=week_df.append({'weekid':week_id,'method':'neighborhood','spot': 'hot','district1':hotnbr_list[0],'district2':hotnbr_list[1],'district3':hotnbr_list[2],'district4':hotnbr_list[3],'district5':hotnbr_list[4]},ignore_index=True)
    week_df=week_df.append({'weekid':week_id,'method':'neighborhood','spot': 'cold','district1':coldnbr_list[0],'district2':coldnbr_list[1],'district3':coldnbr_list[2],'district4':coldnbr_list[3],'district5':coldnbr_list[4]},ignore_index=True)  
    week_df=week_df.append({'weekid':week_id,'method':'state','spot': 'hot','district1':hotstate_list[0],'district2':hotstate_list[1],'district3':hotstate_list[2],'district4':hotstate_list[3],'district5':hotstate_list[4]},ignore_index=True)
    week_df=week_df.append({'weekid':week_id,'method':'state','spot': 'cold','district1':coldstate_list[0],'district2':coldstate_list[1],'district3':coldstate_list[2],'district4':coldstate_list[3],'district5':coldstate_list[4]},ignore_index=True)  
    i+=627


# In[19]:


week_df


# In[16]:


zscore_month = pd.read_csv("zscore-month.csv")


# In[17]:


zmonth_nbr=zscore_month.sort_values(['monthid','neighborhoodzscore'],ascending=[True, False])
zmonth_nbr.reset_index(drop=True,inplace=True)
zmonth_state=zscore_month.sort_values(['monthid','statezscore'],ascending=[True, False])
zmonth_state.reset_index(drop=True,inplace=True)


# In[21]:


month_df = pd.DataFrame(columns=['monthid','method','spot','district1','district2','district3','district4','district5'])
i=0
while(i<=4388):
    hot_nbrlist=[]
    cold_nbrlist=[]
    hot_statelist=[]
    cold_statelist=[]
    hotnbr = zmonth_nbr[i:i+627].head(5)
    coldnbr = zmonth_nbr[i+622:i+627]
    hotstate = zmonth_state[i:i+627].head(5)
    coldstate = zmonth_state[i+622:i+627]
    month = str(int(hotnbr.iloc[0]['monthid']))
    hot_nbrlist=list(hotnbr['districtid'])
    cold_nbrlist=list(coldnbr['districtid'])
    hot_statelist=list(hotstate['districtid'])
    cold_statelist=list(coldstate['districtid'])
    month_df=month_df.append({'monthid':month,'method':'neighborhood','spot': 'hot','district1':hot_nbrlist[0],'district2':hot_nbrlist[1],'district3':hot_nbrlist[2],'district4':hot_nbrlist[3],'district5':hot_nbrlist[4]},ignore_index=True)
    month_df=month_df.append({'monthid':month,'method':'neighborhood','spot': 'cold','district1':cold_nbrlist[0],'district2':cold_nbrlist[1],'district3':cold_nbrlist[2],'district4':cold_nbrlist[3],'district5':cold_nbrlist[4]},ignore_index=True)  
    month_df=month_df.append({'monthid':month,'method':'state','spot': 'hot','district1':hot_statelist[0],'district2':hot_statelist[1],'district3':hot_statelist[2],'district4':hot_statelist[3],'district5':hot_statelist[4]},ignore_index=True)
    month_df=month_df.append({'monthid':month,'method':'state','spot': 'cold','district1':cold_statelist[0],'district2':cold_statelist[1],'district3':cold_statelist[2],'district4':cold_statelist[3],'district5':cold_statelist[4]},ignore_index=True)  
    i+=627


# In[22]:


month_df


# In[25]:


zscore_overall = pd.read_csv("zscore-overall.csv")
zscore_overall


# In[26]:


zoverall_nbr=zscore_overall.sort_values(['neighborhoodzscore'],ascending=[False])
zoverall_nbr.reset_index(drop=True,inplace=True)
zoverall_state=zscore_overall.sort_values(['statezscore'],ascending=[False])
zoverall_state.reset_index(drop=True,inplace=True)


# In[27]:


overall_df = pd.DataFrame(columns=['overallid','method','spot','district1','district2','district3','district4','district5'])
hot_nbrlist=[]
cold_nbrlist=[]
hot_statelist=[]
cold_statelist=[]
hotnbr = zoverall_nbr[0:5]
coldnbr = zoverall_nbr[622:627]
hotstate = zoverall_state[0:5]
coldstate = zoverall_state[622:627]
hot_nbrlist=list(hotnbr['districtid'])
cold_nbrlist=list(coldnbr['districtid'])
hot_statelist=list(hotstate['districtid'])
cold_statelist=list(coldstate['districtid'])
overall_df=overall_df.append({'overallid':'1','method':'neighborhood','spot': 'hot','district1':hot_nbrlist[0],'district2':hot_nbrlist[1],'district3':hot_nbrlist[2],'district4':hot_nbrlist[3],'district5':hot_nbrlist[4]},ignore_index=True)
overall_df=overall_df.append({'overallid':'1','method':'neighborhood','spot': 'cold','district1':cold_nbrlist[0],'district2':cold_nbrlist[1],'district3':cold_nbrlist[2],'district4':cold_nbrlist[3],'district5':cold_nbrlist[4]},ignore_index=True)
overall_df=overall_df.append({'overallid':'1','method':'state','spot': 'hot','district1':hot_statelist[0],'district2':hot_statelist[1],'district3':hot_statelist[2],'district4':hot_statelist[3],'district5':hot_statelist[4]},ignore_index=True)
overall_df=overall_df.append({'overallid':'1','method':'state','spot': 'cold','district1':cold_statelist[0],'district2':cold_statelist[1],'district3':cold_statelist[2],'district4':cold_statelist[3],'district5':cold_statelist[4]},ignore_index=True)  


# In[28]:


overall_df


# In[29]:

week_df.to_csv("top-week.csv",index=False)
month_df.to_csv("top-month.csv",index=False)
overall_df.to_csv("top-overall.csv",index=False)


# In[ ]:




