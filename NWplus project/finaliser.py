import speech_recognition as sr
import os
from gtts import gTTS
from textblob import TextBlob


r = sr.Recognizer()


with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source)
    audio = r.listen(source)



text = r.recognize_google(audio)


#tts = gTTS(most_likely_text, lang='en', slow=False)
#tts.save("output.mp3")
#os.system("afplay output.mp3")

blob = TextBlob(text)

polarity = blob.sentiment.polarity

if polarity > 0:
    print("Positive")
elif polarity == 0:
    print("Neutral")
else:
    print("Negative")

print(f'Polarity: {polarity}')
print(f'Subjectivity: {blob.sentiment.subjectivity}')
