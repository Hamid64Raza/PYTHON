# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 11:28:47 2023

@author: Hamid Raza
"""

import numpy as np

arr=np.array([1,2,3,4,5,6,7,8,9,10])
print(np.flip(arr))


a=np.array([[1,2,3],[4,5,6],[7,8,9]]) 
for x in range (0,len(a)): 
    a[x]=np.flip(a[x]) 
print(a)


