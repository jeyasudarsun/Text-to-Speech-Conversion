import pyttsx3
import os
from pydub import Audiosegment
engine = pyttsx3.init()
engine.setProperty('rate', 160)  
engine.setProperty('volume', 1.0) 
text = "Hi,iam jack .i love playing football"
engine.save_to_file(text,"output.wav")
engine.runAndWait()
audio=AudioSegment.from_wav("output.wav")
audio.export("output.mp3", format="mp3")
os.remove("output.wav")
print("speech saved as output.mp3")