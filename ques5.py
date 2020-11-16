#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import json
import math
import numpy as np
import statistics


# In[2]:


mappings=pd.read_csv('mapping.csv')
mappings


# In[3]:


state_dic={}
for index,row in mappings.iterrows():
    if state_dic.get(row['statecode'])!= None:
        state_dic[row['statecode']] += [row['district_id']]
    else:
        state_dic[row['statecode']] = [row['district_id']]
state_dic


# In[4]:


f1 = open('week_dic.json') # neighbors of each district
week_dic = json.load(f1)


# In[5]:


state_week=[]
for curr_dist in range(101,728):
    flag=0
    for (k1,v1) in state_dic.items():
        for dist in v1:
            if (dist == curr_dist):
                otherdistricts = v1[:]
                otherdistricts.remove(dist)
                for i in range(1,26):
                    mean=0
                    stdev=0
                    otherdist_cases=[]
                    for otherdist in otherdistricts:
                        otherdist_cases.append(int(week_dic[str((int(otherdist)-101)*25+i-1)]))
                    if (len(otherdist_cases)<1):
                        mean=0
                        std=0
                    elif (len(otherdist_cases)<2):
                        mean = round(otherdist_cases[0],2)
                        std=0
                    else:
                        mean = round(np.mean(otherdist_cases),2)
                        std= round(statistics.stdev(otherdist_cases,mean),2)
                    state_week.append((str(curr_dist),str(i),mean,std))
                flag=1
                break
        if (flag==1):
            break
    


# In[6]:


stateweek_df = pd.DataFrame(state_week,columns=['districtid','weekid','statemean','statestdev'])
stateweek_df


# In[7]:


stateweek_df.to_csv("state-week.csv",index=False)


# In[8]:


f2 = open('month_dic.json') #neighbors of each district
month_dic = json.load(f2)


# In[9]:


state_month=[]
for curr_dist in range(101,728):
    flag=0
    for (k1,v1) in state_dic.items():
        for dist in v1:
            if (dist ==curr_dist):
                otherdistrict_list = v1[:]
                otherdistrict_list.remove(dist)
                for i in range(1,8):
                    mean=0
                    stdev=0
                    otherdist_cases=[]
                    for otherdist in otherdistrict_list:
                        otherdist_cases.append(int(month_dic[str((int(otherdist)-101)*7+i-1)]))
                    if len(otherdist_cases)<1:
                        mean=0
                        std=0
                    elif len(otherdist_cases)<2:
                        mean = round(otherdist_cases[0],2)
                        std=0
                    else:
                        mean = round(np.mean(otherdist_cases),2)
                        std= round(statistics.stdev(otherdist_cases,mean),2)
                    state_month.append((str(curr_dist),str(i),mean,std))
                flag=1
                break
        if flag==1:
            break


# In[10]:


statemonth_df = pd.DataFrame(state_month,columns=['districtid','monthid','statemean','statestdev'])
statemonth_df


# In[11]:


statemonth_df['statemean'].sum()


# In[12]:


statemonth_df['statestdev'].sum()


# In[13]:


statemonth_df.to_csv("state-month.csv",index=False)


# In[14]:


f3 = open('overall_dic.json') #neighbors of each district
overall_dic = json.load(f3)


# In[15]:


state_overall=[]
for curr_dist in range(101,728):
    for (k1,v1) in state_dic.items():
        for dist in v1:
            if (dist ==  curr_dist):
                otherdist_list = v1[:]
                otherdist_list.remove(dist)
                mean=0
                stdev=0
                otherdist_cases=[]
                for otherdist in otherdist_list:
                    otherdist_cases.append(int(overall_dic[str(int(otherdist)-101)]))
                if (len(otherdist_cases)<1):
                    mean=0
                    std=0
                elif (len(otherdist_cases)<2):
                    mean = round(otherdist_cases[0],2)
                    std=0
                else:
                    mean = round(np.mean(otherdist_cases),2)
                    std = round((statistics.stdev(otherdist_cases,mean)),2)
                state_overall.append((str(curr_dist),str(1),mean,std))


# In[16]:


stateoverall_df = pd.DataFrame(state_overall,columns=['districtid','overallid','statemean','statestdev'])
stateoverall_df


# In[17]:


stateoverall_df['statestdev'].sum()


# In[18]:


stateoverall_df.to_csv("state-overall.csv",index=False)


# In[ ]:




