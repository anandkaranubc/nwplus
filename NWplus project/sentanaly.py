from textblob import TextBlob

text = input("How are you?")

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
