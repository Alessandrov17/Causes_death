# -*- coding: utf-8 -*-
"""
Theo Guindi
Alessandro Vellucci
The dataset chosen shows the top 10 leading causes of death in the United States
which are adjusted by age.
"""


import pandas as pd

data = pd.read_csv("NCHS_-_Leading_Causes_of_Death__United_States (3).csv")


print(data.columns)

years = data["Year"].to_numpy()

cause_name = data["113 Cause Name"].to_numpy()

cause = data["Cause Name"].to_numpy()

state = data["State"].to_numpy()

deaths = data["Deaths"].to_numpy()

death_rate = data ["Age-adjusted Death Rate"].to_numpy()



print(years[:3])
print(cause_name[:5])
print(cause[:3])
print(state[:10])
print(deaths[:3])
print(death_rate[:15])


