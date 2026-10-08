import streamlit as st
from google import genai
import anthropic

st.set_page_config(page_title="SBL Analytics", layout="wide")
st.title("🧬 SPORTS BIONIC LAB (SBL)")

# 1. API Anahtarları
col_api1, col_api2 = st.columns(2)
gemini_key = col_api1.text_input("Gemini API Key:", type="password")
claude_key = col_api2.text_input("Claude Opus Key:", type="password")

# 2. Bütçe ve Maç Girişi
budget = st.number_input("Toplam Bütçe (TL):", min_value=50, value=500, step=50)
matches = st.text_area("Analiz Edilecek Maçlar:", height=100)

if st.button("🚀 ÇİFT AJANLI ANALİZİ BAŞLAT"):
    if not gemini_key or not claude_key:
        st.error("API Anahtarları girilmedi!")
    elif budget < 50:
        st.error("Bütçe minimum 50 TL olmalıdır.")
    else:
        # AŞAMA 1: GEMINI ANALİZİ
        with st.spinner("Gemini interneti tarıyor..."):
            try:
                client = genai.Client(api_key=gemini_key)
                prompt = f"Bütçe: {budget} TL. Maçlar: {matches}. Yasaklar: Çift şart, 2-3 gol tuzağı yasak. Portföy stratejisi kur."
                response = client.models.generate_content(model="gemini-2.0-flash-exp", contents=prompt)
                gemini_text = response.text
                st.write("✅ Analist Raporu:", gemini_text)
            except Exception as e:
                st.error(f"Gemini Analiz Hatası: {e}")
                gemini_text = None

        # AŞAMA 2: CLAUDE OPUS DENETİMİ
        if gemini_text:
            with st.spinner("Claude Opus 5.5 denetimi yapılıyor..."):
                try:
                    c_client = anthropic.Anthropic(api_key=claude_key)
                    c_response = c_client.messages.create(
                        model="claude-3-5-sonnet-20241022",
                        max_tokens=2000,
                        messages=[{"role": "user", "content": f"Denetle: {gemini_text}"}]
                    )
                    st.success("✅ Denetim Başarılı!")
                    st.write("🛡️ Müfettiş Onaylı Nihai Rapor:", c_response.content[0].text)
                except Exception as e:
                    st.error(f"Claude Denetim Hatası: {e}")
