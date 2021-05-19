# -*- coding: utf-8 -*-
"""
Created on Mon May 17 20:01:49 2021

@author: asus
"""
from gtts import gTTS

def say(ttsstr):
    tts = gTTS(ttsstr)
    tts.save( ttsstr +".mp3")


def read(path):
    f = open(path, 'r')
    strs = f.read()
    f.close()
    return strs


x=read('two.txt')
say(x)