from pydub import AudioSegment
from pydub.playback import play
import subprocess
import threading

def play_sound():
	sound = AudioSegment.from_mp3('mask.mp3')
	play(sound)

a=1
while True: 
	if(a<10):
		playing_sound_thread = threading.Thread(target=play_sound, args=())
		playing_sound_thread.start()
		print(a)
		a=1+a
		playing_sound_thread.join()
	else:
		a=1
