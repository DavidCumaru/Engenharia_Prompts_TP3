import streamlit as st
import pandas as pd
import plotly.express as px

st.title("CSV Data Visualizer")

uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)
    st.dataframe(data)

    sentiment_counts = data['sentiment'].value_counts()
    fig_pie = px.pie(names=sentiment_counts.index, values=sentiment_counts.values, title='Sentiment Distribution')
    st.plotly_chart(fig_pie)

    fig_line = px.line(data, x='line', y='sentiment', title='Sentiment over Lines')
    st.plotly_chart(fig_line)

