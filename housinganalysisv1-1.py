#!/usr/bin/env python
# coding: utf-8

# In[28]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#import datasets
sales_data = pd.read_csv(r"C:\Users\kwasi\OneDrive\Desktop\Books\Statistics\wisconsin_housing_sales.csv")
price_data = pd.read_csv(r"C:\Users\kwasi\OneDrive\Desktop\Books\Statistics\wisconsin_housing_median_prices.csv")

#print(sales_data.head())
#print(price_data.head())


#print(sales_data.describe())
#print(price_data.describe())

x = sales_data['Year']
y = sales_data['Avg']
plt.subplot(1,2,1)
plt.plot(x,y)

x = price_data['Year']
y = price_data['Avg']
plt.subplot(1,2,2)
plt.plot(x,y)

#plt.plot(sales_data['Year'],sales_data['Avg'] )
#plt.plot(price_data['Year'], price_data['Avg'])

plt.show()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




