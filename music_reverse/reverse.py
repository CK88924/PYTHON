import os
from pydub import AudioSegment as audio
from pydub.playback import play


song = audio.from_mp3('winter.mp3')
backwards = song.reverse()
play(backwards)



