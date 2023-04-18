import streamlit as st
import pandas as pd
import numpy as np
from prediction import predict

st.title('Tweet Sentiment Analysis')
st.markdown('Model to classify a Tweet into: positive, neutral, negative')

tweet = st.text_input('Tweet (in less than 140 words): ', 'How are you feeling?')

if st.button('Analyze Tweet Sentiment'):
    result = predict(tweet)
    st.text(result)