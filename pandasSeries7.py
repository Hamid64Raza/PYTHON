# -*- coding: utf-8 -*-
"""
Created on Sun Oct  8 10:07:42 2023

@author: Hamid Raza
"""

import pandas as pd
hamid={"day1":100,"day2":200,"day3":300,"day4":400}
hamidNew=pd.Series(hamid,index=["day1","day4"])
print(hamidNew)