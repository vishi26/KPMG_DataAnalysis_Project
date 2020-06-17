#!/usr/bin/env python
# coding: utf-8

# In[58]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[59]:


file_Transaction=pd.read_excel(r'C:\Users\Hp\Downloads\kpmg\vishi\Transaction.xlsx')


# In[60]:


file_Transaction.head()
df=file_Transaction


# ### Data Processing

# In[61]:


file_Transaction.dtypes


# In[62]:


df


# In[63]:


file.isnull().sum()


# In[64]:


missing_data=df.isnull()


# In[65]:


missing_data.sum()


# In[66]:


# Value counts of availabilities--Pandas Index. value_counts() function returns object containing counts of unique values. 
#The resulting object will be in descending order so that the first element is the most frequently-occurring element. 
#Excludes NA values by default.
for column in missing_data.columns.values.tolist():
    print(column)
    print(missing_data[column].value_counts())
    print("")


# In[67]:


df['online_order'].value_counts()


# In[92]:


#df['online_order'].replace(np.nan,2,inplace=True) #2 indicates unknown here
#df['online_order']=df['SOCIETY'].fillna('other')
df['online_order'].fillna(2.0,inplace=True)


# In[93]:


df['online_order'].isnull().sum()


# In[78]:


df['brand'].value_counts()


# In[90]:


df['brand'].replace(np.nan,'solex',inplace=True)


# In[91]:


df['brand'].isnull().sum()


# In[94]:


df['product_line'].value_counts()


# In[95]:


df.describe(include='all')


# In[96]:


df['product_line'].replace(np.nan,'Standard',inplace=True)


# In[98]:


df['product_line'].isnull().sum()


# In[99]:


df['product_class']=df['product_class'].fillna(method='ffill') #ffill': Ffill or forward-fill propagates the last observed non-null value forward until another non-null value is encountered


# In[100]:


df['product_class'].isnull().sum()


# In[101]:


df['product_size']=df['product_size'].fillna(method='bfill')


# In[102]:


df['product_size'].isnull().sum()


# In[103]:


df['standard_cost'].value_counts()


# In[105]:


df['standard_cost']=df['standard_cost'].fillna(method='ffill')


# In[106]:


df['standard_cost'].isnull().sum()


# In[107]:


df['product_first_sold_date'].value_counts()


# In[108]:


df['product_first_sold_date']=df['product_first_sold_date'].fillna(method='ffill')


# In[109]:


df['product_first_sold_date'].isnull().sum()


# In[110]:


#identify missing values
df.isnull().sum() #don't have any null columns


# In[113]:


duplicate_val=df.duplicated()


# In[115]:


duplicate_val.sum()


# In[ ]:




