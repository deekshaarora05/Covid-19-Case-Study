#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import json
import datetime
import statistics


# In[2]:


neighbor_week = pd.read_csv("neighbor-week.csv")
neighbor_month = pd.read_csv("neighbor-month.csv")
neighbor_overall = pd.read_csv("neighbor-overall.csv")
state_week = pd.read_csv("state-week.csv")
state_month = pd.read_csv("state-month.csv")
state_overall = pd.read_csv("state-overall.csv")


# In[3]:


neighbor_week


# In[4]:


neighbor_month


# In[5]:


state_week


# In[7]:


f1 = open('week_dic.json') # Contains the neighbors of each district
week_dic = json.load(f1)
f2 = open('month_dic.json') # Contains the neighbors of each district
month_dic = json.load(f2)
f3 = open('overall_dic.json') # Contains the neighbors of each district
overall_dic = json.load(f3)


# In[8]:


week_dic


# In[9]:


month_dic


# In[10]:


overall_dic


# In[12]:


nmeanweek_dic={}
for i in range(15675):
    nmeanweek_dic[i]=neighbor_week.iloc[i]['neighbormean']
nmeanmonth_dic={}
for i in range(4389):
    nmeanmonth_dic[i]=neighbor_month.iloc[i]['neighbormean']
nmeanoverall_dic={}
for i in range(627):
    nmeanoverall_dic[i]=neighbor_overall.iloc[i]['neighbormean']


# In[13]:


nstdweek_dic={}
for i in range(15675):
    nstdweek_dic[i]=neighbor_week.iloc[i]['neighborstdev']
nstdmonth_dic={}
for i in range(4389):
    nstdmonth_dic[i]=neighbor_month.iloc[i]['neighborstdev']
nstdoverall_dic={}
for i in range(627):
    nstdoverall_dic[i]=neighbor_overall.iloc[i]['neighborstdev']


# In[42]:


nweek_list=[]
for week_id in range(1,26):
    spot=""
    curr_index = week_id-1
    while(curr_index<=15674):
        cases = int(week_dic[str(curr_index)])
        mean = nmeanweek_dic[curr_index]
        std = nstdweek_dic[curr_index]
        disid = (curr_index-week_id+1)//25 + 101
        if (cases>(mean+std)):
            spot = "hot"
        else:
            spot = "cold"
        nweek_list.append((str(week_id),"neighborhood",spot,str(disid)))
        curr_index +=25


# In[43]:


nweek_df = pd.DataFrame(nweek_list,columns=['weekid','method','spot','districtid'])
nweek_df


# In[44]:


nweek_df.to_csv('neighborhood-spot-week.csv',index=False)


# In[33]:


nmonth_list=[]
for month_id in range(1,8):
    spot=""
    curr_index = month_id-1
    while(curr_index<=4388):
        cases = int(month_dic[str(curr_index)])
        mean = nmeanmonth_dic[curr_index]
        std = nstdmonth_dic[curr_index]
        disid = (curr_index-month_id+1)//7 + 101
        if cases>(mean+std):
            spot = "hot"
        else:
            spot = "cold"
        nmonth_list.append((str(month_id),"neighborhood",spot,str(disid)))
        curr_index+=7


# In[34]:


nmonth_df = pd.DataFrame(nmonth_list,columns=['monthid','method','spot','districtid'])
nmonth_df


# In[35]:


nmonth_df.to_csv('neighborhood-spot-month.csv',index=False)


# In[39]:


noverall_list=[]
for dis_id in range(101,728):
    cases = int(overall_dic[str(dis_id-101)])
    mean = nmeanoverall_dic[dis_id-101]
    std = nstdoverall_dic[dis_id-101]
    if (cases>(mean+std)):
        spot = "hot"
    else:
        spot = "cold"
    noverall_list.append(('1',"neighborhood",spot,str(dis_id)))


# In[40]:


noverall_df = pd.DataFrame(noverall_list,columns=['overallid','method','spot','districtid'])
noverall_df


# In[45]:


noverall_df.to_csv('neighborhood-spot-overall.csv',index=False)


# In[46]:


smeanweek_dic={}
for i in range(15675):
    smeanweek_dic[i]=state_week.iloc[i]['statemean']
smeanmonth_dic={}
for i in range(4389):
    smeanmonth_dic[i]=state_month.iloc[i]['statemean']
smeanoverall_dic={}
for i in range(627):
    smeanoverall_dic[i]=state_overall.iloc[i]['statemean']


# In[47]:


sstdweek_dic={}
for i in range(15675):
    sstdweek_dic[i]=state_week.iloc[i]['statestdev']
sstdmonth_dic={}
for i in range(4389):
    sstdmonth_dic[i]=state_month.iloc[i]['statestdev']
sstdoverall_dic={}
for i in range(627):
    sstdoverall_dic[i]=state_overall.iloc[i]['statestdev']


# In[48]:


sweek_list=[]
for week_id in range(1,26):
    spot=""
    curr_index = week_id-1
    while(curr_index<=15674):
        cases = int(week_dic[str(curr_index)])
        mean = smeanweek_dic[curr_index]
        std = sstdweek_dic[curr_index]
        disid = (curr_index-week_id+1)//25 + 101
        if cases>(mean+std):
            spot = "hot"
        else:
            spot = "cold"
        sweek_list.append((str(week_id),"state",spot,str(disid)))
        curr_index +=25


# In[49]:


sweek_df = pd.DataFrame(sweek_list,columns=['weekid','method','spot','districtid'])
sweek_df


# In[50]:


sweek_df.to_csv('state-spot-week.csv',index=False)


# In[51]:


smonth_list=[]
for month_id in range(1,8):
    spot=""
    curr_index = month_id-1
    while(curr_index<=4388):
        cases = int(month_dic[str(curr_index)])
        mean = smeanmonth_dic[curr_index]
        std = sstdmonth_dic[curr_index]
        disid = (curr_index-month_id+1)//7 + 101
        if (cases>(mean+std)):
            spot = "hot"
        else:
            spot = "cold"
        smonth_list.append((str(month_id),"state",spot,str(disid)))
        curr_index +=7


# In[52]:


smonth_df = pd.DataFrame(smonth_list,columns=['monthid','method','spot','districtid'])
smonth_df


# In[53]:


smonth_df.to_csv('state-spot-month.csv',index=False)


# In[54]:


soverall_list=[]
for disid in range(101,728):
    cases = int(overall_dic[str(disid-101)])
    mean = smeanoverall_dic[disid-101]
    std = sstdoverall_dic[disid-101]
    if (cases>(mean+std)):
        spot = "hot"
    else:
        spot = "cold"
    soverall_list.append(('1',"state",spot,str(disid)))


# In[55]:


soverall_df = pd.DataFrame(soverall_list,columns=['overallid','method','spot','districtid'])
soverall_df


# In[84]:


soverall_df.to_csv('state-spot-overall.csv',index=False)


# In[ ]:




