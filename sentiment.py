from scraper import get_all_headlines
import pandas as pd
from textblob import TextBlob
import re
import matplotlib.pyplot as plt
from datetime import datetime

headlines = get_all_headlines()

def clean_headline(text):
    text = text.strip()
    text = re.sub(r'\s+', ' ', text)
    text = re.sub(r'[^\w\s]', '', text)
    return text.lower()

headlines_cleaned = [clean_headline(h) for h in headlines]

def get_sentiment(text):
    polarity = TextBlob(text).sentiment.polarity
    if polarity > 0.05:
        return "Positive"
    elif polarity < -0.05:
        return "Negative"
    else:
        return "Neutral"

sentiments = [get_sentiment(h) for h in headlines_cleaned]

current_time = datetime.now()

df = pd.DataFrame({
    "headline": headlines_cleaned,
    "sentiment": sentiments,
    "time": current_time
})

print(df.head(10))

df.to_csv("finaldata.csv", mode="a", header=False, index=False)

plt.figure(figsize=(6,4))
df['sentiment'].value_counts().plot(kind='bar', color=['green','grey','red'])
plt.title("Market Sentiment from News Headlines")
plt.xlabel("Sentiment")
plt.ylabel("Number of Headlines")
plt.tight_layout()
plt.show()