# -*- coding: utf-8 -*-
"""
Created on Sun Feb  6 21:33:25 2022

@author: asus
"""
import  keyboard as key
import pickle
import random as rand
import pygame
import  os

def Keys_Store():
    print('請先輸入鍵盤上所有按鍵 按 esc結束輸入')
    keys=['esc']
    pickle_file=open('keys.pkl','wb+')
    while True:
        if key.read_key() == 'esc':
            break
        else:
            touch = key.read_key()
            print (touch)
            if touch not in keys:
                keys.append(str(touch))
    
    pickle.dump(keys,pickle_file)
    pickle_file.close()
    

def Read_Keys():
    
    
    try:
        read_keys =[]
        read_file=open('keys.pkl','rb')
        read_lt=pickle.load(read_file)
        read_keys.extend(read_lt)
        read_file.close()
        return read_keys
    except:
        read_keys =[]
        Keys_Store()
        read_file=open('keys.pkl','rb')
        read_lt=pickle.load(read_file)
        read_keys.extend(read_lt)
        read_file.close()
        return read_keys
      
       
     
    


def Play_crocodile_teeth():

    print('開始鱷魚牙齒遊戲')
    read_list = Read_Keys()
    print(read_list)
    answer = rand.choice(read_list)
    #print(answer)
    pygame.init()
    
    while True:
        if key.read_key() == answer:
            pygame.mixer.music.load('ouch.mp3')
            pygame.mixer.music.play()
            print('ouch!!')
            break
        else:
            pygame.mixer.music.load('ok.mp3')
            pygame.mixer.music.play()
    os.system("pause")
    

if __name__ == '__main__':
    Play_crocodile_teeth()