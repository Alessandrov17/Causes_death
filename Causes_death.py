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
import seaborn as sns

# Part 2: loading data (using pandas)

data = pd.read_csv("NCHS_-_Leading_Causes_of_Death__United_States (3).csv")

# Making all columns into numpy arrays
years = data["Year"].to_numpy()
cause_name = data["113 Cause Name"].to_numpy()
cause = data["Cause Name"].to_numpy()
state = data["State"].to_numpy()
deaths = data["Deaths"].to_numpy()
death_rate = data["Age-adjusted Death Rate"].to_numpy()


# Part 3: Apllying filter using Loops and Conditionals

# Sets these variables as arrays, to prepare them for the for loop
filtered_years = []
filtered_cause_name = []
filtered_cause = []
filtered_state = []
filtered_deaths = []
filtered_death_rate = []

# Loop through all rows and apply condition
for i in range(len(state)):
    if state[i] == "Colorado":  # Colorado data
        filtered_years.append(years[i])
        filtered_cause_name.append(cause_name[i])
        filtered_cause.append(cause[i])
        filtered_state.append(state[i])
        filtered_deaths.append(deaths[i])
        filtered_death_rate.append(death_rate[i])

# Replace the old arrays with the filtered ones
years = filtered_years
cause_name = filtered_cause_name
cause = filtered_cause
state = filtered_state
deaths = filtered_deaths
death_rate = filtered_death_rate

print("Filtered dataset only includes entries for the state of Colorado.")
print("Remaining records:", len(years))

# Part 4
# c) Heatmap: Age-adjusted Death Rates by State and Top 10 Causes (2017)

import numpy as np

# Filter US only data
us_data = data[data["State"] == "United States"]

# Filter US states. Filters for data in 2017
states_data = data[(data["State"] != "United States") & (data["Year"] == 2017)]

# Identify top 10 causes nationally. Groups each "113 Cause Name" category and adds
# The sum of all the "death" values. Then it sorts the values in ascending order, 
# choosing only the top 10.
top10_causes = (us_data.groupby("113 Cause Name")["Deaths"]
                .sum().sort_values(ascending=False).head(10).index)
    
# Filters top 10 causes of death
heatmap_data = states_data[states_data["113 Cause Name"].isin(top10_causes)]

# Specifices to filter only for 2017 data
heatmap_data = states_data[states_data["113 Cause Name"].isin(top10_causes)]

# Creates pivot table: rows = states, columns = causes, values = death rate
heatmap_pivot = heatmap_data.pivot_table(index="State",columns="113 Cause Name",values="Age-adjusted Death Rate",aggfunc="mean")
# Convert to numbers for plotting
values = heatmap_pivot.values
states = heatmap_pivot.index
causes = heatmap_pivot.columns

# Matplotlib Plotting
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
    
# Filter only those causes
top10_data = us_data[us_data["113 Cause Name"].isin(top10_causes)]

# Loop runs once for each "cause" and it will plot one at a time.
plt.figure(figsize=(12, 6))
for cause in top10_causes:
    subset = top10_data[top10_data["113 Cause Name"] == cause]
    plt.plot(subset["Year"], subset["Age-adjusted Death Rate"], marker='o', label=cause)
#Matplotlib Plotting
plt.title("Age-adjusted Death Rate Trends for Top 10 Causes (2000–2017)")
plt.xlabel("Year")
plt.ylabel("Age-adjusted Death Rate (per 100,000 population)")
plt.legend(fontsize=7, loc="upper right")
plt.grid(True)
plt.tight_layout()
plt.show()


# e) Two Subplots: Top 5 Causes – Deaths vs. Death Rates in 2017
import textwrap

# Filter 2017 data
data_2017 = data[data["Year"] == 2017]

# Groups data from 2017, adds deaths for each 113 cause name category, and selects
# only top 5.
top5_causes_2017 = (data_2017.groupby("113 Cause Name")["Deaths"].sum().sort_values(ascending=False).head(5))

# Groups data for 2017, takes mean of age adjusted death rate, 
# .loc selects rows from the top5_causes_2017, index gives the names of top 5 causes.
death_rates_2017 = (data_2017.groupby("113 Cause Name")["Age-adjusted Death Rate"].mean().loc[top5_causes_2017.index])

# Wrap long labels for better readability
labels_wrapped = [textwrap.fill(label, 15) for label in top5_causes_2017.index]

# subplots (basic format for subplot) Essentially creates a type of canvas for the graphs
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

# Helps with layout of two subplots
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

# 2. Preliminary steps
# a) Initial data inspection:
print(data.head(10))
print(data.shape)
print(data.info())
print(data.describe())

# b) Handle duplicate entries:
# dupdata becomes new dataset with removed row duplicates
dupdata = data.duplicated(keep='first')
# Test to see if there have been any rows removed,
print(dupdata.info())

# Drop data for all column "Year", output shows first data for each year
dropdata = data.drop_duplicates(keep='first')
print(data.info())
# No change were made, because all rows are unique

# c) Identify and manage missing values:
print(data.isnull())
# Boolean is false, all columns have values within them

# d) Correct data types and formats:
# All of these are boolean which verify if one of these columns contains empty columns
# They all return False, thus, all columns are full, no empty values
print("Col. Year:", pd.isnull('Year'))
print("Col. 113 Cause Name:", pd.isnull('113 Cause Name'))
print("Col. Cause Name:", pd.isnull('Cause Name'))
print("Col. State:", pd.isnull('State'))
print("Col. Deaths:", pd.isnull('Deaths'))
print("Age-adjusted Death Rate:", pd.isnull('Age-adjusted Death Rate'))

# d) Correct data types and formats: (unecessary))

# 3. Univariate non-graphical EDA

# Numerical variable EDA
# Mean, median, standard deviation, and quartiles.
print(data.describe())
# Kurtosis of each numerical column:
print("Kurtosis of each numerical column:")
print(data.kurt(axis = 0, numeric_only=True))
# Mode of each numerical column:
print("The mode of each numerical column is:")
print(data.mode(numeric_only = True))
# Variance of each numerical column:
print("The variance of each numerical column is:")
print(data.var(numeric_only = True))
# Skewness of each numerical column:
print("The skew of each numerical column is:")
print(data.skew(numeric_only = True))

# Categorical variables EDA

# frequency counts

print(data.value_counts("113 Cause Name"))
print(data['Cause Name'].value_counts())
print(data['State'].value_counts())

# proportion
print(data.value_counts("113 Cause Name", normalize = True))
print(data['Cause Name'].value_counts(normalize = True))
print(data['State'].value_counts(normalize = True))

# mode, [0] returns the first element in the mode series
print(data["113 Cause Name"].mode()[0])
print(data['Cause Name'].mode()[0])
print(data['State'].mode()[0])
# These give answers for the most frequent value in each categorical variables,
# however, they are not actually the most frequent, since they all have the same
# frequency. 

#4.  Univariate graphical EDA
#a) custom number of bins 
sns.displot(data,x="Age-adjusted Death Rate",bins=25)
#b) Conditioning on other variables
sns.displot(data,x="Age-adjusted Death Rate",hue="Year",element="step",bins=25)

#c)stacked histogram

sns.displot(data,x="Age-adjusted Death Rate",hue="Year",multiple="stack",bins=25)

#d) dodge bars

sns.displot(data,x="Age-adjusted Death Rate",hue="Year",multiple="dodge",bins=25)

#e)normalized histogram statistics

sns.displot(data,x="Age-adjusted Death Rate",hue="Year",stat="density",common_norm="False",bins=25)

#f) Kernal density estimation (KDE)

sns.displot(data,x="Age-adjusted Death Rate",kind="kde",bw_adjust=1.25,hue="Year",fill="True" )

#g) Empirical cumulative distributions

sns.displot(data,x="Age-adjusted Death Rate",hue="Year",kind="ecdf")

# 5. Multivariate non-graphical EDA        

# Two categorical variables using the crosstab()
table1 = pd.crosstab(data['Cause Name'], data['Age-adjusted Death Rate'])
table2 = pd.crosstab(data['Cause Name'], data['Deaths'])
table3 = pd.crosstab(data['113 Cause Name'], data['Deaths'])

# Percentage using the crosstab()
proportion1 = pd.crosstab(data['Cause Name'], data['Age-adjusted Death Rate'], normalize=True)
proportion2 = pd.crosstab(data['Cause Name'], data['Deaths'], normalize=True)
proportion3 = pd.crosstab(data['113 Cause Name'], data['Deaths'], normalize=True)

# Three categorical variables using the crosstab()
table4 = pd.crosstab([data['Cause Name'], data['Age-adjusted Death Rate']], data['State'])





