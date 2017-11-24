import speech_recognition as sr
import threading
import wikipedia
import webbrowser
import win32com.client as wincl
speak = wincl.Dispatch("SAPI.SpVoice")
speech= sr.Recognizer()
x=lambda: webbrowser.get(path).open_new_tab(url)
t=threading.Thread(target=x)
path= "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
# url="https://en.wikipedia.org/wiki/Lionel_Messi"
# poss=["tell me about Messi","who is Messi","about Messi"]
# with sr.Microphone() as source:
# 	print("something should be spoken")
# 	audio= speech.listen(source)
# 	text= speech.recognize_google(audio)
# 	print(text)
# 	if text is not None:
# 		for i in poss:
# 			if i in text:
# 				t.start()
# 				speak.Speak(quote)
with sr.Microphone() as source:
	print("something should be spoken")
	audio= speech.listen(source)
	text= speech.recognize_google(audio)
	print(text)
	if "who is" in text:
		text_r=text.split("who is")[1]
		person = wikipedia.page(text_r)
		url=person.url
		print(url)
		quote=wikipedia.summary(text_r, sentences=1)
		#quote=person.content
		t.start()
		speak.Speak(quote)			
# try:
# 	print("from Google:",speech.recognize_google(audio))
# except:
# 	print("error")