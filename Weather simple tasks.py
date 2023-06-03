#!/usr/bin/env python
# coding: utf-8

# In[43]:


import pandas as pd


# In[44]:


data=pd.read_csv(r'C:\Users\Saimum Adil Khan\OneDrive\Desktop\Python Course\Weather Data.csv')


# In[45]:


data.isnull().sum()


# In[46]:


data.head(3)


# In[47]:


data['Date/Time']=pd.to_datetime(data['Date/Time'])


# In[48]:


data['Date/Time']=data['Date/Time'].astype(str)


# In[49]:


data.head()


# In[50]:


data_january=data[data['Date/Time'].str.startswith('2012-01')]


# In[51]:


avg_celcius=data_january['Temp_C'].mean()


# In[52]:


avg_frnht=(avg_celcius*9/5)+32

print(f"The temperature in January is {avg_celcius:.2f} in celcius Scale and {avg_frnht:.2f} in Ferhenhit scale")


# In[53]:


data['Date/Time']=pd.to_datetime(data['Date/Time'])


# In[54]:


data=data.set_index('Date/Time')


# In[55]:


data_rain_snow=data[data['Weather'].str.contains('Rain')| data['Weather'].str.contains('Snow')]


# In[56]:


data_rain_snow


# In[57]:


day_counts=pd.Series(data_rain_snow.index.date).nunique()


# In[58]:


print(f"Only {day_counts} days in this year contained Rain or Snow")


# In[59]:


data_max_wind=data['Wind Speed_km/h'].max()


# In[60]:


data_max_wind_row=data[data['Wind Speed_km/h']==data_max_wind]


# In[61]:


data_max_wind_row


# In[62]:


date=data_max_wind_row.index.date[0]


# In[63]:


time=data_max_wind_row.index.time[0]


# In[64]:


print(f"The Maximum wind speed was {data_max_wind} km/h at the date {date} at {time}")


# In[65]:


data_fog=data[data['Weather'].str.contains('Fog')]


# In[66]:


average_vis_speed=data_fog.groupby(data_fog.index.date)['Visibility_km'].mean()


# In[67]:


average_vis_speed.columns=['Date','Average Visible Wind Speed']


# In[68]:


average_vis_speed.to_csv('Average_wind_speed_visible.csv')


# In[69]:


import matplotlib.pyplot as plt


# In[70]:


plt.figure(figsize=(16,8))
plt.hist(data['Temp_C'],bins=20,label='Temperature Distribution',color='red')
plt.title('Temperature Distribution')
plt.xlabel('Increase of Temperature')
plt.ylabel('Frequency')
plt.show()


# In[82]:


plt.figure(figsize=(20,10))
plt.plot(data.index,data['Press_kPa'],label='The pressure trend over time.',color='g')
plt.title('The pressure trend over time')
plt.xlabel('Change of Time')
plt.ylabel('Amount of Pressure')
plt.show()

