from gtts import gTTS
import os

# Take input from the user
text = input("Enter the text you want to convert to speech: ")

# Create an instance of the gTTS class
tts = gTTS(text, lang='en', slow=False)

# Save the audio to a file
tts.save("output.mp3")
os.system("afplay output.mp3")