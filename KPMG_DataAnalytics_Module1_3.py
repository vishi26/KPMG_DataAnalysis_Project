#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[3]:


file_cd=pd.read_excel(r'C:\Users\Hp\Downloads\kpmg\vishi\CustomerDemography.xlsx')


# In[4]:


file_cd.dtypes


# In[5]:


file_cd.isnull().sum()


# In[6]:


file_cd['last_name']=file_cd['last_name'].fillna(method='ffill')


# In[7]:


file_cd['DOB']=file_cd['DOB'].fillna(method='ffill')


# In[8]:


file_cd['job_title'].value_counts()


# In[9]:


file_cd['job_title']=file_cd['job_title'].fillna(method='bfill')


# In[10]:


file_cd['job_industry_category'].value_counts()


# In[11]:


file_cd['job_industry_category']=file_cd['job_industry_category'].fillna(method='ffill')


# In[12]:


file_cd['default'].value_counts()


# In[13]:


del file_cd['default']


# In[14]:


file_cd['tenure'].value_counts()


# In[15]:


avg_tenure=file_cd['tenure'].mean()


# In[16]:


avg_tenure


# In[18]:


file_cd.describe()


# In[22]:


file_cd['tenure'].replace(np.nan,avg_tenure,inplace=True)


# In[24]:


file_cd.isnull().sum()


# In[25]:


file_cd = file_cd.dropna(how='any',axis=0)


# In[26]:


file_cd.isnull().sum()


# In[28]:


file_cd['gender'].value_counts()


# In[29]:


file_cd['gender']=file_cd['gender'].replace('F','Female').replace('M','Male').replace('Femal','Female').replace('U','Unspecified')


# In[30]:


file_cd['gender'].value_counts()


# In[31]:


sns.countplot(file_cd['gender'])


# In[ ]:




