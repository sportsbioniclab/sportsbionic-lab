import streamlit as st
import google.generativeai as genai # Eskisi ama en güvenli olanı
import anthropic

# Google'ı bu şekilde yapılandır
genai.configure(api_key="BURAYA_API_KEY_GELİR_AMA_KODDA_BOŞ_BIRAK")
model = genai.GenerativeModel('gemini-1.5-flash')
