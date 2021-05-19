# -*- coding: utf-8 -*-
"""
Created on Tue Apr 27 07:35:00 2021

@author: kevin
"""
import random as rand
import string

def encryption():
    n= rand.randint(1, 10)
    reps=[]
    inps=""
    while True:
        for x in range(n):
            inps = inps + rand.choice(string.ascii_letters) 
        if inps.isalpha():
            print("ok",'\n')
            break
        else:
            inps =""
    
    for index in range(len(inps)):
        tempchr = chr((ord(inps[index])*5)+11)
        reps.append(tempchr)
    
    print("已回傳密文")
    return reps

def decrypt(breakps):
    breakstr=""
    inputstr=""
    for index in range (len(breakps)):
        tempchr = chr(int(((ord(breakps[index])-11)/5)))
        breakstr = breakstr + tempchr
    for index in range(len(breakps)):
        inputstr = inputstr + breakps[index]
    
    print("密文:" +inputstr ,"\n")
    print("破譯後明文為:"+breakstr)

if __name__ == '__main__':
   pslist = encryption()
   decrypt(pslist)
    
    
