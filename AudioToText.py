import speech_recognition as sr
import pyaudio 

flag = 0
while(flag == 0):
	r = sr.Recognizer()
	with sr.Microphone() as source:
		print("Speak: ")
		audio = r.listen(source)
	
		try:
			text = r.recognize_google(audio)
			print("You said:",text)
			flag =1
		except:
			print("Sorry couldn't hear, record again")
