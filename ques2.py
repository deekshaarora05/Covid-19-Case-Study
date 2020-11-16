#!/usr/bin/env python
# coding: utf-8

# In[1]:


import datetime
import numpy as np
import pandas as pd
import json


# In[6]:


file = open('neighbor-districts-modified.json') # Contains the neighbors of each district
neighbors = json.load(file)
neighbors


# In[7]:


f = open('data-all.json') # Contains the neighbors of each district
data_all = json.load(f)
data_all


# In[8]:


date_list=['2020-01-30','2020-02-02','2020-02-03','2020-02-14','2020-03-02','2020-03-03','2020-03-04','2020-03-05','2020-03-06','2020-03-07',
          '2020-03-08','2020-03-09','2020-03-10','2020-03-11','2020-03-12','2020-03-13','2020-03-14','2020-09-06','2020-09-07',
          '2020-09-08','2020-09-09','2020-09-10','2020-09-11','2020-09-12','2020-09-13','2020-09-14','2020-09-15','2020-09-16',
          '2020-09-17','2020-09-18','2020-09-19','2020-09-20','2020-09-21']


# In[9]:


dataall_list=[]
for (k1,v1) in data_all.items():
    if k1 not in date_list:
        for (k2,v2) in v1.items():
            if "districts" in v2.keys():
                for (k3,v3) in v2["districts"].items():
                    if 'delta' in v3.keys():
                        for (k4,v4) in v3['delta'].items():
                            if k4=='confirmed':
                                if(k2=='TG'):
                                    dataall_list.append((k1, k2,'telangana districts',v4))
                                elif(k2=='SK'):
                                    dataall_list.append((k1,k2,'sikkim districts',v4))
                                elif(k2=='MN'):
                                    dataall_list.append((k1,k2,'manipur districts',v4))
                                elif(k2=='GA'):
                                    dataall_list.append((k1,k2,'goa districts',v4))
                                elif(k2=='AS'):
                                    dataall_list.append((k1,k2,'assam districts',v4))
                                else:
                                    a=k3.lower()
                                    dataall_list.append((k1,k2,a,v4))
dataall_list


# In[10]:


df=pd.DataFrame(dataall_list,columns=['date','statecode','district','cases'])


# In[11]:


df


# In[12]:


mapping=pd.DataFrame(columns=['district','statecode','Q_id','district_id'])
for key in neighbors.keys():
    arr= key.split('_')
    mapping=mapping.append({'district':arr[0],'statecode':arr[1],'Q_id':arr[2],'district_id':arr[3]},ignore_index=True)


# In[13]:


mapping


# In[14]:


datewise_cases=pd.merge(df,mapping,how='left',on=['statecode','district'])
datewise_cases


# In[15]:


datewise_cases=datewise_cases.drop('Q_id',axis=1)


# In[16]:


datewise_cases=datewise_cases.dropna()


# In[17]:


datewise_cases['cases'].sum()


# In[18]:


datewise_cases


# In[19]:


date=list(datewise_cases['date'].unique())


# In[18]:


#datewise_cases.to_csv('datewise_cases.csv')


# In[20]:


i=1
date_series={}
for val in date:
    date_series[val]=i
    i+=1
date_series


# In[21]:


cases_timeseries={}
for i in range(101,728):
    cases_timeseries[i]={}
for i in range(101,728):
    for j in range(1,176):
        cases_timeseries[i][j]=0
cases_timeseries


# In[22]:


for index,row in datewise_cases.iterrows():
    cases_timeseries[int(row['district_id'])][date_series[row['date']]]=row['cases']


# In[23]:


cases_timeseries


# In[24]:


mapping.to_csv('mapping.csv',index=False)


# In[25]:


with open("date_mapping.json", "w") as outfile: 
    json.dump(date_series, outfile) 


# In[26]:


with open("cases_timeseries.json", "w") as outfile: 
    json.dump(cases_timeseries, outfile) 


# In[27]:


cases_week_list=[]
for (k1,v1) in cases_timeseries.items():
    week=1
    totalcases=0
    for i in range(1,176):
        totalcases+=v1[i]
        if(i%7==0):
            cases_week_list.append((k1,week,totalcases))
            week+=1
            totalcases=0
cases_week_list


# In[39]:


cases_week=pd.DataFrame(cases_week_list,columns=['districtid','weekid','cases'])
cases_week


# In[40]:


cases_week.to_csv('cases-week.csv',index=False)


# In[30]:


cases_month_list=[]
for (k1,v1) in cases_timeseries.items():
    total_cases=0
    month=1
    for j in range(1,176):
        total_cases+=v1[j]
        if (j==17 or j==47 or j==79 or j==108 or j==139 or j==170 or j==175):
            cases_month_list.append((k1,month,total_cases))
            month+=1
            total_cases=0
cases_month_list


# In[31]:


cases_month=pd.DataFrame(cases_month_list,columns=['districtid','monthid','cases'])
cases_month


# In[32]:


cases_month['cases'].sum()


# In[33]:


cases_month.to_csv('cases-month.csv',index=False)


# In[34]:


cases_overall_list=[]
j=-1
for k in range(101,728):
    totalcase_overall=0
    for i in range(1,8):
        j+=1
        totalcase_overall+=cases_month_list[j][2]
    cases_overall_list.append((k,1,totalcase_overall))


# In[35]:


cases_overall=pd.DataFrame(cases_overall_list,columns=['districtid','overallid','cases'])


# In[36]:


cases_overall


# In[37]:


cases_overall['cases'].sum()


# In[38]:


cases_overall.to_csv('cases-overall.csv',index=False)


# In[ ]:




