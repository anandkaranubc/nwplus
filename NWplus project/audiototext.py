import speech_recognition as sr

r = sr.Recognizer()


with sr.Microphone() as source:
    audio = r.listen(source)


text = r.recognize_google(audio, show_all=True)

print(text["alternative"][0]["transcript"])


