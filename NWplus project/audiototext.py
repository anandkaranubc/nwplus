import speech_recognition as sr


def start_recording():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        audio = r.listen(source)

    text = r.recognize_google(audio, show_all=True)

    print(text["alternative"][0]["transcript"])
start_recording()
   



