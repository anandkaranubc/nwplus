import speech_recognition as sr

# defines start recording
def start_recording():
# sets variable r as the recognizer which uses microphone to listen through listen function
    r = sr.Recognizer()

    with sr.Microphone() as source:
        audio = r.listen(source)
# recognizes the input and generates its test
    text = r.recognize_google(audio, show_all=True)
# prints the generated text
    print(text["alternative"][0]["transcript"])
#initializes the function
start_recording()
   



