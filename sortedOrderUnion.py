# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 11:49:29 2023

@author: Hamid Raza
"""

import numpy as np

array1=np.array([0,10,20,40,60,80])
print("Array1: ", array1)
array2=([10,30,40,50,70])
print("Array2: ",array2)
print("Union of above array")
print(np.union1d(array1, array2))
#print(dir(np))