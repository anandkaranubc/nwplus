import speech_recognition as sr
import os
from gtts import gTTS
from textblob import TextBlob

from pydub import AudioSegment

# Prompt the user to enter the file path
file_path = input("Enter the file path of the mp3 file: ")

# Load mp3 file
audio = AudioSegment.from_mp3(file_path)

# Export the audio to wav file
output_file = file_path.split(".")[0] + ".wav"
audio.export(output_file, format="wav")


# Open the audio file using the AudioFile class
with sr.AudioFile(output_file) as source:
    audio = r.record(source)


text = r.recognize_google(audio)

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
