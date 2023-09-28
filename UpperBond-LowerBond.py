# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 11:03:45 2023

@author: Hamid Raza
"""

import numpy as np

arr=np.array([12,34,10,11,34,67,89])

upperBond=67
lowerBond=12
print(arr[(arr<=upperBond) & (arr>=lowerBond)])