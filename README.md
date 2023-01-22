# Welcome to LATER  (Listen And Transcribe Easily and Rapidly): A Potential Revolutionary Audio Transcription Project

Welcome to LATER, a revolutionary audio transcription project that utilizes the power of the Google Natural Language API to transcribe audio with unprecedented accuracy and speed. Our goal is to revolutionize the transcription process and make it more efficient, accurate and faster.


## Project Description

This project is built on the powerful Python programming language and leverages the capabilities of the Google Natural 
Language API, SpeechRecognition library, and AudioSegment library to transcribe audio to text and perform audio
manipulation tasks.

Our project is unique in that it not only transcribes audio to text but also extracts entities and sentiments from the
transcription, providing a deeper understanding of the audio content. The sentiment analysis feature of our project is
particularly powerful and can be used to analyze the emotional state of the speaker, making it an ideal tool for
various applications such as market research, customer service, and more.

The instructions to use the program are very simple - one just has to run the finaliser.py file in order to be able to
input audio through a connected microphone and thus, the magic should be revealed. Moreover, one can browse and play with
the other files in the project to understand how we came up with the final version of the finaliser.py file.
## Project Structure

The project is divided into several modules:

- **audio_transcription.py**: This module contains the main transcription logic. It uses the SpeechRecognition library to transcribe audio to text and the Google Natural Language API to analyze the transcription and extract entities and sentiment.
- **audio_manipulation.py**: This module contains functions to manipulate audio files. It utilizes the AudioSegment library to perform tasks such as splitting audio files into smaller segments, converting audio files to different formats, and increasing/decreasing the volume of audio files.
- **utilities.py**: This module contains utility functions such as functions to save and load the results of the transcription process.
- **test_transcription.py**: This module contains test cases for the transcription process. It can be used to check if the transcription process is working as expected.