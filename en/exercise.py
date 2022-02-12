# -*- coding: utf-8 -*-
"""
Created on Sun Jan 16 22:14:47 2022

@author: asus
"""
import os
import  random as rand
import  gtts
from translate import Translator

class Player():
    score = 0
    life = 3

def question():
    q_store = []
    with open('q.txt') as f:
        for line in f.readlines():
            line = line.strip()
            q_store.append(line)
            
    return rand.sample(q_store, len(q_store) )

def shuffle_str(s):
    # 將字串轉換成列表
    str_list = list(s)
    # 呼叫random模組的shuffle函式打亂列表
    rand.shuffle(str_list)
    # 將列表轉字串
    return ''.join(str_list)
    

if __name__ == '__main__':
    
    player = Player()
    q_list = question()
    translator= Translator(from_lang="english",to_lang="chinese")
    
    
    for word in q_list:
        if player.life == 0:
            break
        else:
            print(shuffle_str(word),'\t', translator.translate(word))
            ans = input('請輸入拼字答案:')
            
            if ans == word:
                player.score = player.score + 10
                print('正解得10分')
                
            else:
                print('正確答案:', word , translator.translate(word))
                word_file = './output/' + word +'.mp3'
                word_speak = gtts.gTTS(text= word , lang='en', slow=False) 
                word_speak.save(word_file)
                os.system('start'+ ' ' + word_file)
                player.life = player.life - 1
                print('玩家剩餘', player.life,'次機會')
                
    print('玩家得分', player.score)
    os.system("pause")        
    
    
   
        
    
        