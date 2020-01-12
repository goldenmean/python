import wave
import os

if os.path.isfile('Sample1.wav') == True:
    print("file is present")
else:
    print("file missing")
	
if True == os.path.exists('Sample31.wav'):
    print("file exists True")
else:
    print("file exists false")

#https://stackoverflow.com/questions/17657103/how-to-play-wav-file-in-python  
#rate, wavData = scipy.io.wavfile.read('test.wav')

f=wave.open('Sample1.wav', 'rb' )

print("Number of channels = ", f.getnchannels())
print("Sampling rate = ", f.getframerate())
print("Sample width in bytes = ", f.getsampwidth())
print("Number of audio frames = ", f.getnframes())
print("Compression name = ", f.getcompname())
chunk = 1024
data = f.readframes(chunk) 

""""
while data:
    print(data)
    data = f.readframes(chunk) 	
"""
#Playback the python wave file using PyAudio

import pyaudio 
#instantiate PyAudio  
p = pyaudio.PyAudio()  
#open stream  
stream = p.open(format = p.get_format_from_width(f.getsampwidth()),  
                channels = f.getnchannels(),  
                rate = f.getframerate(),  
                output = True)  
#read data  
data = f.readframes(chunk)  

#play stream  
while data:  
    stream.write(data)  
    data = f.readframes(chunk)  

#stop stream  
stream.stop_stream()  
stream.close()  

#close PyAudio  
p.terminate()  

f.close()