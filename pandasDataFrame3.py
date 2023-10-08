# -*- coding: utf-8 -*-
"""
Created on Sun Oct  8 10:49:29 2023

@author: Hamid Raza
"""
import pandas as pd
data={"cal":[12,13,14],"dur":[10,20,30]}
newData=pd.DataFrame(data)
print(newData.loc[[0,1]])

"""
  cal  dur
0   12   10
1   13   20

"""