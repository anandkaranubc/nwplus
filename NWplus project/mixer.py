import speech_recognition as sr
import os
from gtts import gTTS
def start_mixer():  
    r = sr.Recognizer()


    with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)



    text = r.recognize_google(audio, show_all=True)
    most_likely_text = text["alternative"][0]["transcript"]

    tts = gTTS(most_likely_text, lang='en', slow=False)
    tts.save("output.mp3")
    os.system("output.mp3")
start_mixer()
