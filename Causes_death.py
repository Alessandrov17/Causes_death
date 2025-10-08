# -*- coding: utf-8 -*-
"""
Theo Guindi
Alessandro Vellucci
The dataset chosen shows the top 10 leading causes of death in the United States
which are adjusted by age.
"""

import numpy as np 
Year,Cause_Name,Cause_Name,State,Deaths,Age_adjusted_Death_Rate = np.loadtxt("NCHS_-_Leading_Causes_of_Death__United_States (3).csv",skiprows=1,unpack=True,delimiter=',',usecols=range(0,6))
  