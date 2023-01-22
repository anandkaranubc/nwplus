import speech_recognition as sr
import os
from gtts import gTTS

r = sr.Recognizer()


with sr.Microphone() as source:
    audio = r.listen(source)


text = r.recognize_google(audio, show_all=True)
most_likely_text = text["alternative"][0]["transcript"]

tts = gTTS(most_likely_text, lang='en', slow=False)
tts.save("output.mp3")
os.system("afplay output.mp3")
