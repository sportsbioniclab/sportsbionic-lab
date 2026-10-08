import streamlit as st
import google.generativeai as genai
import anthropic

st.set_page_config(page_title="SPORTSBIONIC LAB", layout="wide")

st.markdown("""
<style>
    .stApp { background-color: #05070c; color: #f1f5f9; }
    h1 { color: #00d9f5; text-align: center; }
</style>
""", unsafe_allow_html=True)

st.title("🧬 SPORTS BIONIC LAB (SBL)")

# Ayarlar
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
            # 1. Google'ın çalışan modelini otomatik bul
            genai.configure(api_key=gemini_key)
            models = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
            # Liste içinden "flash" içeren en güncel modeli seç
            model_name = next((m for m in models if 'flash' in m), models[0])
            st.write(f"Sistem hazır. Kullanılan Motor: {model_name}")
            
            model = genai.GenerativeModel(model_name)
            prompt = f"Bütçe: {budget} TL. Maçlar: {matches}. Yasaklar: Çift şart, 2-3 gol tuzağı yasak."
            
            res = model.generate_content(prompt)
            gemini_report = res.text
            st.subheader("Analist (Gemini) Raporu:")
            st.write(gemini_report)
            
            # 2. Claude Denetimi
            c_client = anthropic.Anthropic(api_key=claude_key)
            c_res = c_client.messages.create(
                model="claude-3-5-sonnet-20241022",
                max_tokens=2000,
                messages=[{"role": "user", "content": f"Bu analizi denetle: {gemini_report}"}]
            )
            st.subheader("🛡️ Başmüfettiş (Claude) Onaylı Rapor:")
            st.write(c_res.content[0].text)
            
        except Exception as e:
            st.error(f"Sistem Hatası: {e}")
