# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 23:00:51 2021

@author: kevin
"""
class store:
    itr=""
    num=0
    
strs=""
stores=store()

fp = open('input.txt', "r")

for line in iter(fp):
 strs=strs+line   
fp.close()


for i in range(128):
  stores.itr=chr(i)
  stores.num =strs.count(chr(i),0, len(strs))
  print(stores.itr,"\t" , stores.num,"\n")

