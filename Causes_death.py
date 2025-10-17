# -*- coding: utf-8 -*-
"""
Theo Guindi
Alessandro Vellucci
The dataset chosen shows the top 10 leading causes of death in the United States
which are adjusted by age.
"""

import pandas as pd
import matplotlib.pyplot as plt
import textwrap

data = pd.read_csv("NCHS_-_Leading_Causes_of_Death__United_States (3).csv")

years = data["Year"].to_numpy()
cause_name = data["113 Cause Name"].to_numpy()
cause = data["Cause Name"].to_numpy()
state = data["State"].to_numpy()
deaths = data["Deaths"].to_numpy()
death_rate = data["Age-adjusted Death Rate"].to_numpy()

# 1) This is a bar graph showcasing the deaths per year from the year 1999-2017

#How have age adjusted death rates for the top 10 causes of death 
#changed from the year 2000 to most recent?

# Take away the variety in the different states, unites values for the whole united states
us_data = data[data["State"] == "United States"]

total_deaths_per_year = us_data.groupby("Year")["Deaths"].sum()

plt.bar(total_deaths_per_year.index, total_deaths_per_year.values, color='red', width=0.6)

plt.title("Total Deaths per Year in the United States (1999 - 2017)")
plt.xlabel("Year")
plt.ylabel("Total Number of Deaths")
plt.show()



# 2) Histogram with age-adjusted death rates for 1999-2017
plt.figure(figsize=(8,5))
plt.hist(us_data["Age-adjusted Death Rate"], bins=30, color='purple')
plt.title("Distribution of Age-adjusted Death Rates (1999 - 2017)")
plt.xlabel("Age-adjusted Death Rate (per 100,000 population)")
plt.ylabel("Frequency")
plt.show()




# Filter data for 2017
# 7) Two Subplots: Top 5 Causes – Deaths vs. Death Rates in 2017


# Data in 2017 only
data_2017 = us_data[us_data["Year"] == 2017]

# Top five deaths only in year 2017
top5_causes_2017 = (
    data_2017.groupby("113 Cause Name")["Deaths"].sum().sort_values(ascending=False).head(5))

# Compute corresponding death rates for same causes
death_rates_2017 = (data_2017.groupby("113 Cause Name")["Age-adjusted Death Rate"].mean().loc[top5_causes_2017.index])

# Makes labels shorter
labels_wrapped = [textwrap.fill(label, 15) for label in top5_causes_2017.index]

# Making subplots
fig, axes = plt.subplots(1, 2, figsize=(14, 6))

# ==>Left subplot: Death counts
x = range(len(top5_causes_2017))
axes[0].bar(x, top5_causes_2017.values, color='skyblue')
axes[0].set_title("Deaths by Top 5 Causes in 2017")
axes[0].set_xlabel("Cause of Death")
axes[0].set_ylabel("Number of Deaths")
axes[0].set_xticks(x)
axes[0].set_xticklabels(labels_wrapped, rotation=30, ha='right', fontsize=9)

# ==>Right subplot: Age-adjusted Death Rates
x2 = range(len(death_rates_2017))
axes[1].bar(x2, death_rates_2017.values, color='salmon')
axes[1].set_title("Age-adjusted Death Rates for Top 5 Causes in 2017")
axes[1].set_xlabel("Cause of Death")
axes[1].set_ylabel("Age-adjusted Death Rate (per 100,000)")
axes[1].set_xticks(x2)
axes[1].set_xticklabels(labels_wrapped, rotation=30, ha='right', fontsize=9)

# Make plots adjusted for better fit
plt.subplots_adjust(bottom=0.25, wspace=0.4)
plt.show()






