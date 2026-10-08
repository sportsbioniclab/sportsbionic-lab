import streamlit as st
import google.generativeai as genai
import anthropic
import time

st.set_page_config(page_title="SPORTSBIONIC LAB", layout="wide")
st.title("🧬 SPORTS BIONIC LAB (SBL)")

with st.sidebar:
    gemini_key = st.text_input("Gemini API Key:", type="password")
    claude_key = st.text_input("Claude Opus Key:", type="password")

budget = st.number_input("Toplam Bütçe (TL):", min_value=50, value=500, step=50)
matches = st.text_area("Analiz Edilecek Maçlar:", height=100)

if st.button("🚀 ÇİFT AJANLI ANALİZİ BAŞLAT"):
    if not gemini_key or not claude_key:
        st.error("API Anahtarlarını girin!")
    else:
        try:
            genai.configure(api_key=gemini_key)
            # Modeli gemini-1.5-flash olarak zorluyoruz
            model = genai.GenerativeModel("gemini-1.5-flash")
            prompt = f"Bütçe: {budget} TL. Maçlar: {matches}. Analiz et."
            
            # Hata detayını yakalamak için try-except'i güncelliyoruz
            try:
                res = model.generate_content(prompt)
                gemini_report = res.text
                st.subheader("Analist (Gemini) Raporu:")
                st.write(gemini_report)
                
                # Claude Denetimi
                c_client = anthropic.Anthropic(api_key=claude_key)
                c_res = c_client.messages.create(
                    model="claude-3-5-sonnet-20241022",
                    max_tokens=2000,
                    messages=[{"role": "user", "content": f"Denetle: {gemini_report}"}]
                )
                st.subheader("🛡️ Başmüfettiş (Claude) Onaylı Rapor:")
                st.write(c_res.content[0].text)
                
            except Exception as e:
                st.error(f"GEMINI DETAYLI HATA: {e}")
        
        except Exception as e:
            st.error(f"Sistem Hatası: {e}")
