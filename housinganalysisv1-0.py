#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#import dataset
sales_data = pd.read_csv(r"C:\Users\kwasi\OneDrive\Desktop\Books\Statistics\wisconsin_housing_sales.csv")
#price_data = pd.read_csv(r"C:\Users\kwasi\OneDrive\Desktop\Books\Statistics\wisconsin_housing_median_prices.csv")

#print(sales_data.head())
#print(price_data.head())

#print(sales_data.describe())
#print(price_data.describe())

plt.plot(sales_data['Year'],sales_data['Avg'] )
#plt.plot(price_data['Year'],price_data['Jun'])
#plt.plot(sales_data['Year'],sales_data['Mar'] )
#plt.plot(sales_data['Year'],sales_data['May'] )
#plt.plot(sales_data['Year'],sales_data['Jul'] )
#plt.plot(sales_data['Year'],sales_data['Sep'] )
#plt.plot(sales_data['Year'],sales_data['Nov'] )


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




