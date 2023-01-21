import speech_recognition as sr

r = sr.Recognizer()


with sr.Microphone() as source:
    audio = r.listen(source)


text = r.recognize_google(audio, show_all=True)

from gtts import gTTS

# Create an instance of the gTTS class
tts = gTTS(text, lang='en', slow=False)

# Save the audio to a file
tts.save("output.mp3")
