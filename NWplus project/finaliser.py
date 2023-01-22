import speech_recognition as sr
import os
from gtts import gTTS
from textblob import TextBlob

#
r = sr.Recognizer()


with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source)
    audio = r.listen(source)


#transcribe audio input to selected language (default : English)
text = r.recognize_google(audio)

#sentiment analysis
blob = TextBlob(text)

#determines polarity of transcribed statements
polarity = blob.sentiment.polarity

#assigns descriptive value depending on polarity sign
if polarity > 0:
    print("Positive")
elif polarity == 0:
    print("Neutral")
else:
    print("Negative")

print(f'Polarity: {polarity}')
print(f'Subjectivity: {blob.sentiment.subjectivity}')
