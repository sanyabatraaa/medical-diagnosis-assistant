import streamlit as st
import requests

API_URL = "http://localhost:8080/diagnosis"

st.title("🩺 AI Medical Assistant")
st.write("Enter a description of your symptoms below to receive a diagnosis, relevant research, and a summary.")

# User input
description = st.text_area("Describe your symptoms", height=150)

if st.button("Analyze Symptoms"):
    if not description.strip():
        st.warning("Please enter a symptom description.")
    else:
        with st.spinner("Processing..."):
            try:
                response = requests.post(API_URL, json={"description": description})
                if response.status_code == 200:
                    data = response.json()

                    st.subheader("🧬 Extracted Symptoms")
                    st.write(", ".join(data["symptoms"]))

                    st.subheader("🩻 Possible Diagnosis")
                    st.success(data["diagnosis"])

                    st.subheader("📚 PubMed Research Summary")
                    st.write(data["pubmed_summary"])
                else:
                    st.error(f"Error: {response.status_code} - {response.text}")
            except Exception as e:
                st.error(f"Connection failed: {e}")
