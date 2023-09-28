# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 11:27:21 2023

@author: Hamid Raza
"""
import numpy as np
temp=np.array([1,2,2,3,4,5,5,5,6,7,8])
p=float(input("Enter the number: "))
q=float(input("Enter the number to replaced with: "))
temp[temp==p]=q
#temp[temp>p]=q
#temp[temp<p]=q
print(temp)