#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


data=pd.read_csv(r"C:\Users\Deepak Kumar\Downloads\1. Weather Data.csv")


# In[3]:


data


# In[4]:


data.head()


# In[5]:


data.shape


# In[6]:


data.index


# In[8]:


data.columns


# In[9]:


data.dtypes


# In[14]:


data['Weather'].unique


# In[16]:


data.nunique()


# In[17]:


data.count


# In[18]:


data.value_counts


# In[19]:


data.head()


# Find all the unique 'Wind speed' values in the data.

# In[20]:


data.head(2)


# In[23]:


data.nunique()


# In[36]:


data['Wind Speed_km/h'].nunique()


# In[29]:


data['Wind Speed_km/h'].unique()


# Find the number of times when the "weather" is exactly 'clear'.

# In[30]:


data.head(2)


# In[39]:


data.Weather.value_counts()


# In[60]:


#Find the number of times when the "weather" is exactly 'clear'.
data[data.Weather == 'Clear']


# In[52]:



data.head()


# 
