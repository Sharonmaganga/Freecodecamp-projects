# How many people of each race are represented in this dataset?
import pandas as pd
# Assuming the dataset is loaded into a DataFrame named 'df'
race_counts = df['race'].value_counts()
print(race_counts)
# What is the average age of men?
average_age_men = df[df['sex'] == 'Male']['age'].mean()
print(average_age_men)
# What is the percentage of people who have a Bachelor's degree?
percentage_bachelors = (df['education'] == 'Bachelors').mean() * 100
print(percentage_bachelors)
# What percentage of people with advanced education (Bachelors, Masters, or Doctorate) make more than 50K?
advanced_education = df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
percentage_advanced_education_rich = (advanced_education['salary'] == '>50K').mean() * 100
print(percentage_advanced_education_rich)
# What percentage of people without advanced education make more than 50K?
without_advanced_education = df[~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
percentage_without_advanced_education_rich = (without_advanced_education['salary'] == '>50K').mean() * 100
print(percentage_without_advanced_education_rich)
# What is the minimum number of hours a person works per week?
min_hours_per_week = df['hours-per-week'].min()
print(min_hours_per_week)
# What percentage of the people who work the minimum number of hours per week have a salary of more than 50K?
min_hours_per_week_earning_50k = df[df['hours-per-week'] == min_hours_per_week]
percentage_min_hours_earning_50k = (min_hours_per_week_earning_50k['salary'] == '>50K').mean() * 100
print(percentage_min_hours_earning_50k)
# What country has the highest percentage of people that earn >50K and what is that percentage?
highest_earning_country = df[df['salary'] == '>50K']['native-country'].value_counts(normalize=True).idxmax()
percentage_highest_earning_country = (df[df['native-country'] == highest_earning_country]['salary'] == '>50K').mean() * 100
print(f"{highest_earning_country} with a percentage of {percentage_highest_earning_country}%")
# Identify the most popular occupation for those who earn >50K in India.
indian_earning_50k = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]
most_popular_occupation_india = indian_earning_50k['occupation'].value_counts().idxmax()
print(most_popular_occupation_india)
