# -*- coding: utf-8 -*-
"""
Created on Tue Jul  5 01:12:45 2022

@author: asus
"""
from pytube import Playlist, YouTube
import urllib.request as url_req
import  os

def Down_YT():
    yt_input = input('請輸入影片網址:\n')
    try:
        yt = YouTube(yt_input)
        progMP4 = yt.streams.filter(progressive=True, file_extension='mp4')# 篩選 progressive 類型的 MP4 影片格式
        targetMP4 = progMP4.order_by('resolution').desc().first()# 找出解析度最好的 MP4 影片
        ask = input('是否下載 mp3 m:mp3/ v:mp4/a:all:')
        if ask == 'm':
            mp3 = yt.streams.filter().get_audio_only().download(filename= 'mp3\\'+ yt.title + '.mp3')
            print('mp3下載完成')
        elif ask == 'v':
             video_file = targetMP4.download('video')
             print('影片下載完成')
        elif ask == 'a':
              mp3 = yt.streams.filter().get_audio_only().download(filename= 'mp3\\'+ yt.title + '.mp3')
              video_file = targetMP4.download('video')
              print('影片及mp3下載完成')
        
       
    except:
        pass

def Down_List():
    list_input = input('請輸入播放清單ex:https://www.youtube.com/playlist?list=\n')
    
    
    try:
        ask = input('清單下載模式 mp3 m:mp3/ v:mp4/a:all:')
        pl = Playlist(list_input)
        for video in range(len(pl)): 
            yt = YouTube(pl[video])
            if ask == 'm':
                mp3 = yt.streams.filter(only_audio=True).first()
                mp3 = mp3.download(output_path='mp3')
                base, ext = os.path.splitext(mp3)
                new_file = base + '.mp3'
                os.rename(mp3, new_file)
                
            elif ask =='v':
                progMP4 = yt.streams.filter(progressive=True, file_extension='mp4')# 篩選 progressive 類型的 MP4 影片格式
                targetMP4 = progMP4.order_by('resolution').desc().first()# 找出解析度最好的 MP4 影片
                targetMP4.download('videos')
                
            elif ask =='a':
                mp3 = yt.streams.filter(only_audio=True).first()
                mp3 = mp3.download(output_path='mp3')
                base, ext = os.path.splitext(mp3)
                new_file = base + '.mp3'
                os.rename(mp3, new_file)
                
                progMP4 = yt.streams.filter(progressive=True, file_extension='mp4')# 篩選 progressive 類型的 MP4 影片格式
                targetMP4 = progMP4.order_by('resolution').desc().first()# 找出解析度最好的 MP4 影片
                video_file= targetMP4.download('videos')
        print('播放清單下載完成')
          
    except:
        pass
    
def Down_Image():
    yt_input = input('請輸入影片網址:\n')
    try:
         yt = YouTube(yt_input)
         yt_image_url = yt.thumbnail_url
         filename = 'image//'+ yt.title +'.jpg'
         try:
             url_req.urlretrieve(yt_image_url,filename)
             print('圖片下載完成')
         except:
             pass
         
    except:
        pass
    
    
    
if __name__ == '__main__':
    while True:
        act = input('請選擇模式:1(下載單支youtube) 2(下載清單) 3(下載縮圖)')
        if act == '1':
            Down_YT()
        elif act == '2':
            Down_List()
        elif act == '3':
            Down_Image()
        else:
            break
    
 