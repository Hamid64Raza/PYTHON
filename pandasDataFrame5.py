# -*- coding: utf-8 -*-
"""
Created on Sun Oct  8 10:58:44 2023

@author: Hamid Raza
"""

import pandas as pd
data={"cal":[12,13,14],"dur":[10,20,30]}
newData=pd.DataFrame(data,index=["day1","day2","day3"])
print(newData.loc["day3"])


"""
cal    14
dur    30

"""

import pandas as pd
data={"cal":[12,13,14],"dur":[10,20,30]}
newData=pd.DataFrame(data,index=["day1","day2","day3"])
print(newData.loc[["day1","day2"]])

"""
      cal  dur
day1   12   10
day2   13   20

"""