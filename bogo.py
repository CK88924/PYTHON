# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 19:51:16 2021

@author: asus
"""

import random
 
def bogosort(array):
   random.shuffle(array)
   while array != sorted(array):
       random.shuffle(array)
   return array
 
numbers=[]
    
for i in range(10):
    item = random.randint(1, 999)
    numbers.append(item)

print(str(numbers) + "\n")
print("bogo:" + str (bogosort(numbers)) + "\n")
    



