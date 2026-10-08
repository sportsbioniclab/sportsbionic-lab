import streamlit as st
from google import genai
import anthropic

# Bağlantıyı şu şekilde kuracağız (yeni nesil Google yöntemi)
def get_gemini_response(prompt, api_key):
    client = genai.Client(api_key=api_key)
    response = client.models.generate_content(
        model="gemini-2.0-flash-exp", # Güncel ve ücretsiz çalışan model
        contents=prompt,
    )
    return response.text
