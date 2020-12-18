from gtts import gTTS
import os
import time
import playsound
import speech_recognition as sr

def speak(text):
    output = gTTS(text=text, lang='en', slow=False)
    file = "output.mp3"
    output.save(file)
    os.system("start output.mp3")
    playsound.playsound(file)

def get_audio():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        audio= r.listen(source)
        said = ""
        try:
            said = r.recognize_google(audio)
            print(said)
        except Exception as e:
            print("Exception: " + str(e))
        return said

mytext = get_audio()
speak (mytext)
