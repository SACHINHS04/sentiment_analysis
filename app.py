import streamlit as st
from textblob import TextBlob

st.title("Sentiment Analysis")

text = st.text_area("Enter your text here:")

if text:
    analysis = TextBlob(text)
    sentiment = analysis.sentiment.polarity
    if sentiment > 0:
        result = "Positive"
        emoji = "😊"
    elif sentiment == 0:
        result = "Neutral"
        emoji = "😐"
    else:
        result = "Negative"
        emoji = "😔"
    st.write("Sentiment:", result, emoji)
