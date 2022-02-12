# -*- coding: utf-8 -*-
"""
Created on Fri Jan  7 00:55:05 2022

@author: asus
"""
import pytube as pyt
import  random as rand
import os
import keyboard
import  numpy as np
#from moviepy.editor import *
from pydub import  AudioSegment
import pygame


class Yt_Inf():
    video_title = ''
    video_filename_mp4 = ''
    audio_filename_mp3 = ''

class Q():
    mp3 =''
    title =''


      

    
   
def download_yt_musiclist():
    Playlist = []
    cin_playlist = input('輸入YT播放清單:')
    try:    
        playlist = pyt.Playlist(cin_playlist)
        print('Number of videos in playlist: %s' % len(playlist.video_urls))
    except:
        playlist = pyt.Playlist('https://www.youtube.com/playlist?list=PLyZLDwpoDzzrCty7lTvbxS1ytbWpe59pQ')
        print('Number of videos in playlist: %s' % len(playlist.video_urls))
        
    
    for video in range(len(playlist)):
       
        try:
            temp_yt = Yt_Inf()
            yt = pyt.YouTube(playlist[video])
            
            mp4 = yt.streams.filter(file_extension='mp4', res='360p').first().download('music')
        
            mp4_path ='./music/' + yt.title + '.mp4'
            #mp4 = VideoFileClip(mp4_path)
        
            mp3_path ='./music/' + yt.title +'.mp3'
            #mp4.audio.write_audiofile(mp3_path)
            mp3_export = AudioSegment.from_file(mp4_path)
            mp3_export.export(mp3_path,format ='mp3' )
            
            temp_yt.video_title = yt.title
            temp_yt.video_filename_mp4 = mp4_path
            temp_yt.audio_filename_mp3 = mp3_path 
            
            Playlist.append(temp_yt)
        except:
                pass
        continue
    print('download_ok')
    return Playlist
 

def Music_Guess(playlist):
    pygame.mixer.init()
    player = input('輸入遊玩人數:(1~9):')
    player_score = np.zeros(int (player) )
    answer_list =[] 
    
   
    
    try:
        q = rand.randint(5,20)
        for i in range(1,(q+1)):
            temp_answer_list =[]
            temp_list = rand.sample(range( 0, len(playlist) ), 4 )
            for j in range(len(temp_list)):
                q2 = Q()
                q2.title = playlist[temp_list[j]].video_title
                q2.mp3 = playlist[temp_list[j]].audio_filename_mp3
                temp_answer_list.append(q2)
            answer_list.append(temp_answer_list)
            
            
            
            
            
        
    except :
        print('歌曲隨機錯誤')
        pass
    
    roundd = 0
    check = False

    while  roundd < len(answer_list):
        if check == False:
            check = True
            print('第', str(roundd + 1),'題:' )
            for i in answer_list[roundd]:
                print(i.title)
       
            
        
        decide_ans = rand.randint(0,len(answer_list[roundd] )-1 )
        decide_title  = answer_list[roundd][decide_ans].title
        decide_mp3 = answer_list[roundd][decide_ans].mp3
       
        
            
       
        
        
        
        if os.path.isfile(decide_mp3):
           
            pygame.mixer.music.load(decide_mp3)
            pygame.mixer.music.play(-1)
           
            
            if keyboard.read_key() <= str(len(player_score)) and keyboard.is_pressed("0") == False :
                responder = int(keyboard.read_key())
                pygame.mixer.music.stop()
                a_str = input("答案:")
                if decide_title == answer_list[roundd][int(a_str)-1].title:
                    print('正解')
                    player_score[responder - 1] += 1
                    roundd = roundd + 1
                    check = False
                else:
                    print("正確答案:",decide_title)
                    roundd  += 1
                    check = False
        else:
            print('音檔不存在')
            
    print("全員分數統計:(左至右依序為玩家 1,2,3...)",player_score)
    os.system("pause")
       
           

    
               
            
    

        
   
        

  
        
    
    
    
    


    
if __name__ == '__main__':
    get_playlist = download_yt_musiclist()
    Music_Guess(get_playlist) 
   