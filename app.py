import streamlit as st
import google.generativeai as genai

st.title("Model Kontrol Paneli")
key = st.text_input("API Key Gir:", type="password")
if st.button("Model Listesini Göster"):
    genai.configure(api_key=key)
    for m in genai.list_models():
        if 'generateContent' in m.supported_generation_methods:
            st.write(f"Model Adı: {m.name}")
