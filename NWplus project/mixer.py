import speech_recognition as sr
import os
from gtts import gTTS

# defines start_mixer
def start_mixer():  
    # sets variable r as recognizer which uses microphone to listen through listen function
    # Also r is adjusted for mild and slow noises to improve recognition
    r = sr.Recognizer()


    with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)

    # recognizes the input and generates its text

    text = r.recognize_google(audio, show_all=True)
    most_likely_text = text["alternative"][0]["transcript"]
    # takes the generated text and produces an audio of it in english 
    tts = gTTS(most_likely_text, lang='en', slow=False)
    #save the audio file
    tts.save("output.mp3")
    # runs the file
    os.system("output.mp3")
#initializes the function
start_mixer()
