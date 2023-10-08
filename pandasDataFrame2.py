# -*- coding: utf-8 -*-
"""
Created on Sun Oct  8 10:40:59 2023

@author: Hamid Raza
"""

import pandas as pd
data={"cal":[12,13,14],"dur":[10,20,30]}
newData=pd.DataFrame(data)
print(newData.loc[0])


"""
cal    12
dur    10

"""