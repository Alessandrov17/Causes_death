# -*- coding: utf-8 -*-
"""
Theo Guindi
Alessandro Vellucci
The dataset chosen shows the top 10 leading causes of death in the United States
which are adjusted by age.
"""


import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("NCHS_-_Leading_Causes_of_Death__United_States (3).csv")

years = data["Year"].to_numpy()
cause_name = data["113 Cause Name"].to_numpy()

cause = data["Cause Name"].to_numpy()

state = data["State"].to_numpy()

deaths = data["Deaths"].to_numpy()

death_rate = data ["Age-adjusted Death Rate"].to_numpy()


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




