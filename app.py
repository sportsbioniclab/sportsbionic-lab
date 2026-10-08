import streamlit as st
from google import genai
import anthropic

st.title("SPORTSBIONIC LAB (SBL)")
st.write("Sistem çalışıyor, arayüz başarıyla yüklendi!")

# Bütçe giriş kutusunu ekleyelim ki ekrana bir şeyler gelsin
bütçe = st.number_input("Bütçe Giriniz:", min_value=50, value=500)
if st.button("Analizi Başlat"):
    st.write(f"{bütçe} TL ile analiz motoru hazır!")
