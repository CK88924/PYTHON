# -*- coding: utf-8 -*-
"""
Created on Mon May 17 09:53:23 2021

@author: asus
"""

def TwoSum(num,traget):
    for i in range(len(num)):
        for j in range(i+1, len(num)-1):
            if num[i] + num[j] == traget:
                return i,j

one,two = TwoSum([9,1,6],10)
print(one,two)