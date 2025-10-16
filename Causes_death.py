# -*- coding: utf-8 -*-
"""
Theo Guindi
Alessandro Vellucci
The dataset chosen shows the top 10 leading causes of death in the United States
which are adjusted by age.
"""


import pandas as pd

data = pd.read_csv("NCHS_-_Leading_Causes_of_Death__United_States (3).csv")



years = data["Year"].to_numpy()

cause_name = data["113 Cause Name"].to_numpy()

cause = data["Cause Name"].to_numpy()

state = data["State"].to_numpy()

deaths = data["Deaths"].to_numpy()

death_rate = data ["Age-adjusted Death Rate"].to_numpy()


#How have age adjusted death rates for the top 10 causes of death 
#changed from the year 2000 to most recent?

        
import matplotlib.pyplot as plt

x = years
y = deaths

plt.xlabel("Years")
plt.ylabel("Number of Deaths per year")

plt.title("Deaths per year over 1999-2017")

plt.bar(x,y, color = 'r', width = 0.5)
plt.show()

#This plot looks at the total deaths per year from 1999-2017

ypoints = deaths

plt.plot(ypoints, c = '#4CAF50')
plt.show()

print(years[:3])
print(cause_name[:5])
print(cause[:3])
print(state[:10])
print(deaths[:3])
print(death_rate[:15])

