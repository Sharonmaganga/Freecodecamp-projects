#!/usr/bin/env python
# coding: utf-8

# In[11]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# In[12]:


# Load the dataset
df = pd.read_csv('medical_examination.csv')


# In[13]:


# Add an overweight column:
# Convert height from cm to meters
df['height'] = df['height'] / 100

# Calculate BMI and add overweight column
df['BMI'] = df['weight'] / (df['height'] ** 2)
df['overweight'] = df['BMI'].apply(lambda x: 1 if x > 25 else 0)


# In[14]:


# Normalize cholesterol and glucose data
df['cholesterol'] = df['cholesterol'].apply(lambda x: 0 if x == 1 else 1)
df['gluc'] = df['gluc'].apply(lambda x: 0 if x == 1 else 1)


# In[16]:


# Convert data into long format
df_cat = pd.melt(df, id_vars=['cardio'], value_vars=['cholesterol', 'gluc', 'alco', 'active', 'smoke'])

# Create the chart
sns.catplot(data=df_cat, kind='count', x='variable', hue='value', col='cardio')
plt.show()


# In[17]:


# Filter out incorrect data
df = df[(df['ap_lo'] <= df['ap_hi']) &
        (df['height'] >= df['height'].quantile(0.025)) &
        (df['height'] <= df['height'].quantile(0.975)) &
        (df['weight'] >= df['weight'].quantile(0.025)) &
        (df['weight'] <= df['weight'].quantile(0.975))]


# In[18]:


# Create correlation matrix
corr_matrix = df.corr()

# Plot the heatmap
sns.heatmap(corr_matrix, annot=True, fmt='.1f', cmap='coolwarm', center=0, mask=np.triu(corr_matrix))
plt.show()


# In[ ]:




