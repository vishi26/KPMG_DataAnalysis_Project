#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#importing modules

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


# In[ ]:


file = pd.read_excel(r'C:\Users\Hp\Downloads\kpmg\KPMG_VI_New_raw_data_update_final1.xlsx',
                     sheat = ['Transactions','NewCustomerList','CustomerDemographic',
                              'CustomerAddress'])


# In[ ]:


Transactions = pd.read_excel(r'C:\Users\Hp\Downloads\kpmg\KPMG_VI_New_raw_data_update_final1.xlsx',sheet_name =
                     'Transactions')
NewCustomerList = pd.read_excel(r'C:\Users\Hp\Downloads\kpmg\KPMG_VI_New_raw_data_update_final1.xlsx',sheet_name =
                     'NewCustomerList')
CustomerDemographic = pd.read_excel(r'C:\Users\Hp\Downloads\kpmg\KPMG_VI_New_raw_data_update_final1.xlsx',sheet_name =
                     'CustomerDemographic')
CustomerAddress = pd.read_excel(r'C:\Users\Hp\Downloads\kpmg\KPMG_VI_New_raw_data_update_final1.xlsx',sheet_name =
                     'CustomerAddress')


# In[ ]:


#Transactions
Transactions.head()


# In[ ]:


Transactions.info()


# In[ ]:


Transactions.columns


# In[ ]:


Transactions.describe()


# ### Data Processing

# In[9]:


#identify missing values
Transactions.isnull().sum()


# In[10]:


missing_data=Transactions.isnull()


# In[11]:


for column in missing_data.columns.values.tolist():
    print(column)
    print(missing_data[column].value_counts())
    print("")


# In[12]:


Transactions['online_order'].value_counts()


# In[13]:


Transactions['online_order'].replace(np.nan,2,inplace=True) #2 indicates unknown here


# In[14]:


Transactions['brand'].value_counts()


# In[15]:


Transactions['brand'].replace(np.nan,'Solex',inplace=True)


# In[16]:


Transactions['product_line'].value_counts()


# In[17]:


Transactions['product_line'].replace(np.nan,'Standard',inplace=True)


# In[18]:


Transactions['product_class'].value_counts()


# In[19]:


Transactions['product_class'].replace(np.nan,'medium',inplace=True)


# In[20]:


Transactions['product_size'].value_counts()


# In[21]:


Transactions['product_size'].replace(np.nan,'medium',inplace=True)


# In[22]:


Transactions['standard_cost'].value_counts()


# In[23]:


avg_standard_cost=Transactions['standard_cost'].mean(axis=0)
avg_standard_cost


# In[24]:


Transactions['standard_cost'].replace(np.nan,avg_standard_cost,inplace=True)


# In[25]:


Transactions = Transactions.dropna(how='any',axis=0)


# In[26]:


#identify missing values
Transactions.isnull().sum()            #now we have no null values


# In[27]:


duplicates = Transactions.duplicated()
Transactions[duplicates].sum()


# In[ ]:





# In[28]:


NewCustomerList.head()


# In[29]:


NewCustomerList.info()


# In[30]:


NewCustomerList.describe()


# In[31]:


# Drop Unnamed Column
columns = ['Unnamed: 16','Unnamed: 17','Unnamed: 18','Unnamed: 19','Unnamed: 20']
NewCustomerList = NewCustomerList.drop(columns, axis=1)


# In[32]:


NewCustomerList.head()


# In[33]:


#identify missing values
NewCustomerList.isnull().sum()


# In[34]:


for column in missing_data.columns.values.tolist():
    print(column)
    print(missing_data[column].value_counts())
    print("")


# In[35]:


NewCustomerList['last_name'].value_counts()


# In[36]:


NewCustomerList['last_name'].replace(np.nan,'unknown',inplace=True)


# In[37]:


NewCustomerList['job_title'].value_counts()


# In[38]:


NewCustomerList['job_title'].replace(np.nan,'unknown',inplace=True)


# In[39]:


NewCustomerList['job_industry_category'].value_counts()


# In[40]:


NewCustomerList['job_industry_category'].replace(np.nan,'Financial Services',inplace=True)


# In[41]:


NewCustomerList = NewCustomerList.dropna(how='any',axis=0)


# In[42]:


duplicates = NewCustomerList.duplicated()     #no duplicates
NewCustomerList[duplicates].sum()


# In[43]:


#identify missing values       #no null values
NewCustomerList.isnull().sum()


# In[ ]:





# In[44]:


CustomerDemographic.head()


# In[45]:


CustomerDemographic.info()


# In[46]:


CustomerDemographic.describe()


# In[47]:


CustomerDemographic.isnull().sum()


# In[48]:


CustomerDemographic['last_name'].value_counts()


# In[49]:


CustomerDemographic['last_name'].replace(np.nan,'unknown',inplace=True)


# In[50]:


CustomerDemographic['job_title'].value_counts()


# In[51]:


CustomerDemographic['job_title'].replace(np.nan,'unknown',inplace=True)


# In[52]:


CustomerDemographic['job_industry_category'].value_counts()


# In[53]:


CustomerDemographic['job_industry_category'].replace(np.nan,'Manufacturing',inplace=True)


# In[54]:


CustomerDemographic['default'].value_counts()


# In[55]:


CustomerDemographic['tenure'].value_counts()


# In[56]:


avg_tenure=CustomerDemographic['tenure'].mean()
avg_tenure


# In[57]:


CustomerDemographic['tenure'].replace(np.nan,avg_tenure,inplace=True)


# In[58]:


CustomerDemographic = CustomerDemographic.dropna(how='any',axis=0)


# In[59]:


CustomerDemographic.isnull().sum() #null values


# In[60]:


CustomerDemographic['gender'].value_counts()


# In[61]:


CustomerDemographic['gender'] = CustomerDemographic['gender'].replace('F','Female').replace('M','Male').replace('Femal','Female').replace('U','Unspecified')


# In[62]:


CustomerDemographic['gender'].value_counts()


# In[63]:


sns.countplot(CustomerDemographic['gender'])


# In[64]:


CustomerDemographic.head()


# In[65]:


CustomerDemographic.info()


# In[66]:


NewCustomerList.head()


# In[67]:


NewCustomerList.info()


# In[68]:


CustomerDemographic['customer_id'].iloc[-1]


# In[69]:


NewCustomerList.insert(0, 'customer_id', range(4001, 4001 + len(NewCustomerList)))


# In[70]:


len(NewCustomerList)


# In[ ]:


#since there is no cutomer id column in NewCustomerList..we are adding a new.
NewCustomerList.insert(0,'customer_id', range(4001,4001+len(NewCustomerList)))


# In[72]:


NewCustomerList.head()


# In[73]:


CustomerDemographic.sort_values(by=['customer_id'], inplace=True)


# In[74]:


CustomerDemographic.head()


# In[75]:


new_df = pd.concat([CustomerDemographic, NewCustomerList], ignore_index=True, sort=False)


# In[77]:


new_df.isnull().sum()


# In[78]:


CustomerDemographic = new_df


# In[79]:


CustomerDemographic


# In[83]:


current_year=2020   #calculating the age by extracting dob year  minus current year and adding a new column 'age' .
for i in CustomerDemographic['DOB']:
    CustomerDemographic['age']=current_year-pd.DatetimeIndex(CustomerDemographic['DOB']).year


# In[84]:


CustomerDemographic['age']


# In[85]:


print(min(CustomerDemographic['age']))


# In[88]:


x1 = CustomerDemographic[(CustomerDemographic['age'] <= 30)]
x1 = len(x1)

x2 = CustomerDemographic[(CustomerDemographic['age']>30)&(CustomerDemographic['age']<60)]
x2 = len(x2)

x3 = CustomerDemographic[(CustomerDemographic['age'] >= 60)]
x3 =len(x3)


# In[91]:


x2


# In[92]:


m1 = CustomerDemographic[(CustomerDemographic['age'] <= 30) & 
          (CustomerDemographic['gender']=='Male')] 
m1 = len(m1)

m2 = CustomerDemographic[(CustomerDemographic['age']>30) &(CustomerDemographic['age']<60) & 
          (CustomerDemographic['gender']=='Male')] 
m2 = len(m2)

m3 = CustomerDemographic[(CustomerDemographic['age'] >= 60) & 
          (CustomerDemographic['gender']=='Male')] 
m3 = len(m3)


# In[94]:


CustomerDemographic


# In[95]:


f1 = CustomerDemographic[(CustomerDemographic['age'] <= 30) & 
          (CustomerDemographic['gender']=='Female')] 
f1 = len(f1)

f2 = CustomerDemographic[(CustomerDemographic['age']>30) &(CustomerDemographic['age']<60) & 
          (CustomerDemographic['gender']=='Female')] 
f2 = len(f2)

f3 = CustomerDemographic[(CustomerDemographic['age'] >= 60) & 
          (CustomerDemographic['gender']=='Female')] 
f3 =len(f3)


# In[98]:


X=['Under 30','Between 30 and 60','Above 60']
x=[x1,x2,x3]


# In[100]:


sns.barplot(X,x)
plt.text(2.1,3000, "Total", fontsize = 12, color='Black', fontstyle='italic')


# In[101]:


M = ['Under 30', 'Between 30 and 60', 'Over 60']
m = [m1, m2, m3]

F = ['Under 30', 'Between 30 and 60', 'Over 60']
f = [f1, f2, f3]


# In[102]:


sns.barplot(M,m)
plt.text(2.1,1400, "Male", fontsize = 12, color='Black', fontstyle='italic')


# In[106]:


sns.barplot(x = F,y = f)
plt.text(1.98,1600, "Female", fontsize = 12, color='Black', fontstyle='italic')


# In[104]:


fig = plt.figure(figsize=(10,5))
chart=sns.countplot(x='wealth_segment',data=CustomerDemographic)
chart.set_xticklabels(chart.get_xticklabels(), rotation=80)
plt.show()


# In[107]:


fig = plt.figure(figsize=(10,5))
chart=sns.countplot(x='job_industry_category',data=CustomerDemographic)
chart.set_xticklabels(chart.get_xticklabels(), rotation=80)
plt.show()


# In[108]:


fig = plt.figure(figsize=(4,3))
chart=sns.countplot(x='owns_car',data=CustomerDemographic)
chart.set_xticklabels(chart.get_xticklabels(), rotation=80)
plt.show()


# In[ ]:




