import streamlit as st
from google import genai
st.title("Model Adresi Bulucu")
key = st.text_input("API Key:", type="password")
if st.button("Adresleri Listele"):
    client = genai.Client(api_key=key)
    for m in client.models.list():
        st.write(f"Model Adresi: {m.name}")
