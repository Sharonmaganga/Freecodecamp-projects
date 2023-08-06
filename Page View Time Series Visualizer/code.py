#!/usr/bin/env python
# coding: utf-8

# # Import necessary libraries and load the dataset
# 

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset and set the index to the date column
df = pd.read_csv('fcc-forum-pageviews.csv', parse_dates=['date'], index_col='date')


# # Clean the data by filtering out days with extreme page views:

# In[7]:


# Calculate the top and bottom 2.5% of page views
lower_bound = df['value'].quantile(0.025)
upper_bound = df['value'].quantile(0.975)

# Filter out the extreme values
df_cleaned = df[(df['value'] >= lower_bound) & (df['value'] <= upper_bound)]


# # Create the draw_line_plot function to draw the line chart:

# In[3]:


def draw_line_plot():
    # Create the line chart
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.plot(df_cleaned.index, df_cleaned['value'], color='r', linewidth=1)
    ax.set_xlabel('Date')
    ax.set_ylabel('Page Views')
    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    plt.show()


# # Create the draw_bar_plot function to draw the bar chart:

# In[4]:


def draw_bar_plot():
    # Extract year and month from the date
    df_cleaned['year'] = df_cleaned.index.year
    df_cleaned['month'] = df_cleaned.index.month_name()

    # Create the bar chart
    df_pivot = df_cleaned.pivot_table(values='value', index='year', columns='month', aggfunc='mean')
    df_pivot = df_pivot.reindex(columns=['January', 'February', 'March', 'April', 'May', 'June',
                                         'July', 'August', 'September', 'October', 'November', 'December'])
    ax = df_pivot.plot(kind='bar', figsize=(14, 6))
    ax.set_xlabel('Years')
    ax.set_ylabel('Average Page Views')
    ax.legend(title='Months')
    plt.show()


# # Create the draw_box_plot function to draw the box plots:

# In[5]:


def draw_box_plot():
    # Extract year and month from the date
    df_cleaned['year'] = df_cleaned.index.year
    df_cleaned['month'] = df_cleaned.index.strftime('%b')

    # Create the box plots
    fig, axes = plt.subplots(1, 2, figsize=(15, 6))
    sns.boxplot(data=df_cleaned, x='year', y='value', ax=axes[0])
    sns.boxplot(data=df_cleaned, x='month', y='value', ax=axes[1],
                order=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
    axes[0].set_title('Year-wise Box Plot (Trend)')
    axes[0].set_xlabel('Year')
    axes[0].set_ylabel('Page Views')
    axes[1].set_title('Month-wise Box Plot (Seasonality)')
    axes[1].set_xlabel('Month')
    axes[1].set_ylabel('Page Views')
    plt.show()


# # Now, you can call these functions to create the required visualizations:

# In[8]:


draw_line_plot()
draw_bar_plot()
draw_box_plot()


# In[ ]:




