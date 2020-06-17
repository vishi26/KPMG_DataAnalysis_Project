#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[3]:


df_newCustList=pd.read_excel(r'C:\Users\Hp\Downloads\kpmg\vishi\NewCustomerList.xlsx')


# In[4]:


df_newCustList.head(10)


# In[5]:


#data.columns = map(str.upper, data.columns)
df_newCustList.columns=map(str.upper,df_newCustList.columns) #converting to uppercase


# In[6]:


df_newCustList.head()


# In[7]:


df_newCustList.isnull().sum()


# In[8]:


df_newCustList['LAST_NAME'].value_counts()


# In[19]:


df_newCustList['LAST_NAME']=df_newCustList['LAST_NAME'].fillna(method='ffill')#,inplace=True)


# In[20]:


df_newCustList['LAST_NAME'].isnull().sum()


# In[12]:


df_newCustList['DOB'].value_counts()


# In[13]:


df_newCustList['DOB']=df_newCustList['DOB'].fillna(method='ffill')


# In[14]:


df_newCustList['DOB'].isnull().sum()


# In[15]:


df_newCustList['JOB_TITLE']=df_newCustList['JOB_TITLE'].fillna(method='ffill')
df_newCustList['JOB_INDUSTRY_CATEGORY']=df_newCustList['JOB_INDUSTRY_CATEGORY'].fillna(method='ffill')


# In[16]:


#identify missing values
df_newCustList.isnull().sum() #don't have any null columns


# In[23]:


df_newCustList.describe()


# In[26]:


# Drop Unnamed Column
columns = ['UNNAMED: 16','UNNAMED: 17','UNNAMED: 18','UNNAMED: 19','UNNAMED: 20']
df_newCustList = df_newCustList.drop(columns, axis=1)


# In[27]:


df_newCustList.head()


# In[28]:


df_newCustList.isnull().sum()


# In[32]:


df_newCustList['LAST_NAME'].replace(np.nan,'unknown',inplace=True)


# In[33]:


df_newCustList.isnull().sum()


# In[ ]:




