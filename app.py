import pandas as pd
import openai
import streamlit as st

# Set OpenAI API key (Replace with your actual key)
openai.api_key = "your-api-key"

def analyze_data(df, question):
    data_str = df.to_string()
    prompt = f"Given the following dataset:\n{data_str}\n\nAnswer this question: {question}"
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "system", "content": "You are a data analyst."},
                  {"role": "user", "content": prompt}]
    )
    return response["choices"][0]["message"]["content"]

st.title("AI Data Analysis Assistant")

uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.subheader("Dataset Preview")
    st.dataframe(df.head())
    
    question = st.text_input("Ask a question about your data")
    if st.button("Get AI Insights") and question:
        insights = analyze_data(df, question)
        st.subheader("AI Insights & Recommendations")
        st.text(insights)
