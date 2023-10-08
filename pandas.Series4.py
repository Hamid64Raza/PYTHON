# -*- coding: utf-8 -*-
"""
Created on Sun Oct  8 10:00:25 2023

@author: Hamid Raza
"""


import pandas as pd
hamid=[1,2,3]
hamidNew=pd.Series(hamid,index=["x","y","z"])
print(hamidNew["x"])