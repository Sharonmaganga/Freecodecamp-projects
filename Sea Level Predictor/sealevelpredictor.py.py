#!/usr/bin/env python
# coding: utf-8

# # Step 1: Importing the Data using Pandas

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

# Read the data from the CSV file
data = pd.read_csv('epa-sea-level.csv')

# Display a few rows of the data to ensure it was imported correctly
print(data.head())


# # Step 2: Creating a Scatter Plot
# we'll create a scatter plot using the Year column as the x-axis and the CSIRO Adjusted Sea Level column as the y-axis.

# In[2]:


# Scatter plot
plt.scatter(data['Year'], data['CSIRO Adjusted Sea Level'])

# Set the labels and title
plt.xlabel('Year')
plt.ylabel('Sea Level (inches)')
plt.title('Rise in Sea Level')

# Display the plot
plt.show()


# # Step 3: Calculating the Line of Best Fit (Full Dataset)
# Now, we'll calculate the line of best fit using the linregress function from scipy.stats and plot it over the scatter plot. We'll make the line go through the year 2050 to predict the sea level rise in 2050.

# In[3]:


# Calculate the line of best fit using linregress
slope, intercept, r_value, p_value, std_err = linregress(data['Year'], data['CSIRO Adjusted Sea Level'])

# Plot the line of best fit
plt.plot(data['Year'], slope * data['Year'] + intercept, color='red', label='Best Fit Line')

# Set the labels and title
plt.xlabel('Year')
plt.ylabel('Sea Level (inches)')
plt.title('Rise in Sea Level')

# Display the plot
plt.show()

# Predict sea level rise in 2050
year_2050 = 2050
predicted_sea_level_2050 = slope * year_2050 + intercept
print("Predicted Sea Level Rise in 2050:", predicted_sea_level_2050, "inches")


# # Step 4: Calculating the Line of Best Fit (Since Year 2000)
# Lastly, we'll calculate a new line of best fit using the data from year 2000 through the most recent year in the dataset. We'll then plot this line along with the previous line, both going through the year 2050 to predict the sea level rise in 2050 if the rate of rise continues as it has since the year 2000.
# 
# 

# In[5]:



# Filter the data for years from 2000 to the most recent year
recent_data = data[data['Year'] >= 2000]

# Calculate the line of best fit using linregress for the recent data
slope_recent, intercept_recent, _, _, _ = linregress(recent_data['Year'], recent_data['CSIRO Adjusted Sea Level'])

# Plot the line of best fit for the recent data
plt.plot(recent_data['Year'], slope_recent * recent_data['Year'] + intercept_recent, color='green', label='Best Fit Line (Since 2000)')

# Set the labels and title
plt.xlabel('Year')
plt.ylabel('Sea Level (inches)')
plt.title('Rise in Sea Level')

# Display the plot
plt.show()

# Predict sea level rise in 2050 based on recent data
predicted_sea_level_2050_recent = slope_recent * year_2050 + intercept_recent
print("Predicted Sea Level Rise in 2050 (Since 2000):", predicted_sea_level_2050)


# In[ ]:




