# -*- coding: utf-8 -*-
"""
Theo Guindi
Alessandro Vellucci
The dataset chosen shows the top 10 leading causes of death in the United States
which are adjusted by age.
LIA Deliverable 2
a) All plots should contain a title and a description for both axis x and y. - Done
b) You should comment your code with a quick explanation about each plot. - Done

To enhance readability, each graph corresponds to a certain letter, 
which corresponds to the following instructions:

c) 1 plot of any type containing data from more than 1 array using different - 
colors and line styles.
d) 1 plot of any type using grid.
e) 1 plot of any type containing 2 subplots side by side (counts as 1).
f) 1 scatter plot.
g) 1 bar plot.
h) 1 histogram.
i) 1 pie chart.

"""

import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("NCHS_-_Leading_Causes_of_Death__United_States (3).csv")

years = data["Year"].to_numpy()
cause_name = data["113 Cause Name"].to_numpy()
cause = data["Cause Name"].to_numpy()
state = data["State"].to_numpy()
deaths = data["Deaths"].to_numpy()
death_rate = data["Age-adjusted Death Rate"].to_numpy()

# c) Heatmap: Age-adjusted Death Rates by State and Top 10 Causes (2017)

import numpy as np

# Filter U.S.-only data
us_data = data[data["State"] == "United States"]

# Filter U.S. states only (exclude national totals)
states_data = data[(data["State"] != "United States") & (data["Year"] == 2017)]

# Identify top 10 causes nationally
top10_causes = (us_data.groupby("113 Cause Name")["Deaths"].sum().sort_values(ascending=False).head(10).index)
    
# Filter for top 10 causes
heatmap_data = states_data[states_data["113 Cause Name"].isin(top10_causes)]

# Filter only those causes for 2017
heatmap_data = states_data[states_data["113 Cause Name"].isin(top10_causes)]

# Create pivot table: rows = states, columns = causes, values = death rate
heatmap_pivot = heatmap_data.pivot_table(index="State",columns="113 Cause Name",values="Age-adjusted Death Rate",aggfunc="mean")
# Convert to numeric array for plotting
values = heatmap_pivot.values
states = heatmap_pivot.index
causes = heatmap_pivot.columns

# Plot using Matplotlib
plt.figure(figsize=(12, 8))
plt.imshow(values, aspect='auto', cmap='coolwarm')
plt.colorbar(label="Age-adjusted Death Rate (per 100,000)")
plt.xticks(np.arange(len(causes)), causes, rotation=45, ha='right', fontsize=8)
plt.yticks(np.arange(len(states)), states, fontsize=8)
plt.title("Age-adjusted Death Rates by State for Top 10 Causes (2017)")
plt.xlabel("Cause of Death")
plt.ylabel("State")
plt.tight_layout()
plt.show()


# d) Line Plot: Trends in Age-Adjusted Death Rates for Top 10 Causes (2000–2017)

# Get top 10 causes overall
top10_causes = (us_data.groupby("113 Cause Name")["Deaths"].sum().sort_values(ascending=False).head(10).index)
    
# Filter only those causes
top10_data = us_data[us_data["113 Cause Name"].isin(top10_causes)]

# Plot each cause as a line
plt.figure(figsize=(12, 6))
for cause in top10_causes:
    subset = top10_data[top10_data["113 Cause Name"] == cause]
    plt.plot(subset["Year"], subset["Age-adjusted Death Rate"], marker='o', label=cause)

plt.title("Age-adjusted Death Rate Trends for Top 10 Causes (2000–2017)")
plt.xlabel("Year")
plt.ylabel("Age-adjusted Death Rate (per 100,000 population)")
plt.legend(fontsize=7, loc="upper right")
plt.grid(True)
plt.tight_layout()
plt.show()


# e) Two Subplots: Top 5 Causes – Deaths vs. Death Rates in 2017
import textwrap

# Filter for 2017
data_2017 = data[data["Year"] == 2017]

# Get top 5 causes by total deaths
top5_causes_2017 = (data_2017.groupby("113 Cause Name")["Deaths"].sum().sort_values(ascending=False).head(5))

# Compute corresponding death rates for same causes
death_rates_2017 = (data_2017.groupby("113 Cause Name")["Age-adjusted Death Rate"].mean().loc[top5_causes_2017.index])
    
# Wrap long labels for better readability
labels_wrapped = [textwrap.fill(label, 15) for label in top5_causes_2017.index]

# Create subplots
fig, axes = plt.subplots(1, 2, figsize=(14, 6))

#Left subplot: Death counts
x = range(len(top5_causes_2017))
axes[0].bar(x, top5_causes_2017.values, color='skyblue')
axes[0].set_title("Deaths by Top 5 Causes in 2017")
axes[0].set_xlabel("Cause of Death")
axes[0].set_ylabel("Number of Deaths")
axes[0].set_xticks(x)
axes[0].set_xticklabels(labels_wrapped, rotation=30, ha='right', fontsize=9)

#Right subplot: Age-adjusted Death Rates
x2 = range(len(death_rates_2017))
axes[1].bar(x2, death_rates_2017.values, color='salmon')
axes[1].set_title("Age-adjusted Death Rates for Top 5 Causes in 2017")
axes[1].set_xlabel("Cause of Death")
axes[1].set_ylabel("Age-adjusted Death Rate (per 100,000)")
axes[1].set_xticks(x2)
axes[1].set_xticklabels(labels_wrapped, rotation=30, ha='right', fontsize=9)

# Adjust layout to fit labels properly
plt.subplots_adjust(bottom=0.25, wspace=0.4)
plt.show()


# f) scatter plot filtered for one cause 

heart=data[data["Cause Name"]=="Heart disease"] 

plt.figure(figsize=(8,6)) 
plt.scatter(heart["Deaths"], heart["Age-adjusted Death Rate"],color="red",alpha=0.7)
plt.title("Heart disease: Death vs age adjusted death rate") 
plt.xlabel("Deaths")
plt.ylabel("Age-adjusted Death Rate")
plt.show()



# g) This is a bar graph showcasing the deaths per year from the year 1999-2017

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



# h) Histogram with age-adjusted death rates for 1999-2017
plt.figure(figsize=(8,5))
plt.hist(us_data["Age-adjusted Death Rate"], bins=30, color='purple')
plt.title("Distribution of Age-adjusted Death Rates (1999 - 2017)")
plt.xlabel("Age-adjusted Death Rate (per 100,000 population)")
plt.ylabel("Frequency")
plt.show()


# i) Pie chart Deaths by state for a specific cause

heart= data[data["Cause Name"]=="Heart disease"]

#Removing all cases labelled united states
heart = heart[heart["State"]!="United States"]


state_deaths=heart.groupby("State")["Deaths"].sum()

plt.figure(figsize=(8,8))
plt.pie(state_deaths, labels=state_deaths.index,autopct='%1.1f%%', startangle=90)
plt.title("Heart disease death by states")
plt.show()

