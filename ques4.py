#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import json
import datetime
import statistics


# In[2]:


n = open('neighborlist.json') # Contains the neighbors of each district
neighbor_list = json.load(n)
neighbor_list


# In[7]:


cases_week=pd.read_csv('cases-week.csv')
cases_week


# In[25]:


week_dic={}
for i in range(0,15675):
    week_dic[i]=str(cases_week.iloc[i]['cases'])
week_dic


# In[28]:


week_list=[]
j=-1
for (k1,v1) in neighbor_list.items():
    j+=1
    x=len(v1)
    for i in range(1,26):
        l=[]
        for (k2,v2) in v1.items():
            l.append(int(week_dic[(int(v2)-101)*25+i-1]))
       
        if(x<2):
            mean=l[0]
            std=round(0,2)
        else:
            mean= round(np.mean(l),2)
            std=round(statistics.stdev(l,mean),2)
        week_list.append((str(k1),str(i),mean,std))    
week_list


# In[29]:


mean_std=pd.DataFrame(week_list,columns=['districtid', 'weekid', 'neighbormean', 'neighborstdev'])
mean_std


# In[30]:


mean_std.to_csv('neighbor-week.csv',index=False)


# In[31]:


with open("week_dic.json","w") as outfile:
    json.dump(week_dic,outfile)


# In[32]:


cases_month=pd.read_csv('cases-month.csv')


# In[33]:


month_dic={}
for i in range(0,4389):
    month_dic[i]=str(cases_month.loc[i]['cases'])


# In[34]:


month_list=[]
for(k1,v1) in neighbor_list.items():
    x=len(v1)
    for i in range(1,8):
        neighbor_month=[]
        for (k2,v2) in v1.items():
            neighbor_month.append(int(month_dic[(int(v2)-101)*7+i-1]))
        if(x<2):
            mean=neighbor_month[0]
            std=round(0,0)
        else:
            mean=round(np.mean(neighbor_month),2)
            std=round(statistics.stdev(neighbor_month,mean),2)
        month_list.append((str(k1),str(i),mean,std))    
month_list


# In[35]:


mean_month=pd.DataFrame(month_list,columns=['districtid', 'monthid', 'neighbormean', 'neighborstdev'])
mean_month


# In[36]:


mean_month.to_csv('neighbor-month.csv',index=False)


# In[37]:


with open("month_dic.json","w") as outfile:
    json.dump(month_dic,outfile)


# In[45]:


cases_overall=pd.read_csv('cases-overall.csv')
cases_overall


# In[51]:


overall_dic={}
for i in range(0,627):
    overall_dic[i]=str(cases_overall.loc[i]['cases'])


# In[52]:


overall_list=[]
for(k1,v1) in neighbor_list.items():
    x=len(v1)
    neighbor_overall=[]
    for (k2,v2) in v1.items():
        neighbor_overall.append(int(overall_dic[int(v2)-101]))
    if(x<2):
        mean=neighbor_month[0]
        std=round(0,0)
    else:
        mean=round(np.mean(neighbor_overall),2)
        std=round(statistics.stdev(neighbor_overall,mean),2)
    overall_list.append((str(k1),str(1),mean,std))

overall_list


# In[53]:


mean_overall=pd.DataFrame(overall_list,columns=['districtid', 'overallid', 'neighbormean', 'neighborstdev'])
mean_overall


# In[54]:


mean_overall.to_csv('neighbor-overall.csv',index=False)


# In[55]:


with open("overall_dic.json","w") as outfile:
    json.dump(overall_dic,outfile)


# In[ ]:




