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
           # ...try bloğunun içindeki kısım...
          import time
        
        try:
            genai.configure(api_key=gemini_key)
            model = genai.GenerativeModel("gemini-3.8-flash")
            
            prompt = f"Bütçe: {budget} TL. Maçlar: {matches}. Strateji: Çift şart yasak, 2-3 gol tuzağı yasak."
            
            # Hata verirse 5 saniye bekle ve tekrar dene (Kendi kendini düzeltme)
            max_retries = 3
            for i in range(max_retries):
                try:
                    res = model.generate_content(prompt)
                    gemini_report = res.text
                    break
                except Exception as e:
                    if i < max_retries - 1:
                        time.sleep(5)
                        continue
                    else:
                        raise e
            
            st.subheader("Analist (Gemini) Raporu:")
            st.write(gemini_report)
            
            # Claude Denetimi (Burada da aynı bekleme mantığını kurabiliriz)
            c_client = anthropic.Anthropic(api_key=claude_key)
            c_res = c_client.messages.create(
                model="claude-3-5-sonnet-20241022",
                max_tokens=2000,
                messages=[{"role": "user", "content": f"Denetle: {gemini_report}"}]
            )
            st.subheader("🛡️ Başmüfettiş (Claude) Onaylı Rapor:")
            st.write(c_res.content[0].text)
            
        except Exception as e:
            st.error(f"Sistem Hatası: {e}")
            # Claude Denetimi (Burada da aynı bekleme mantığını kurabiliriz)
            c_client = anthropic.Anthropic(api_key=claude_key)
            c_res = c_client.messages.create(
                model="claude-3-5-sonnet-20241022",
                max_tokens=2000,
                messages=[{"role": "user", "content": f"Denetle: {gemini_report}"}]
            )
            st.subheader("🛡️ Başmüfettiş (Claude) Onaylı Rapor:")
            st.write(c_res.content[0].text)
            
        except Exception as e:
            st.error(f"Sistem Hatası: {e}")
            
            # Google'ın kendi verdiği en güncel model ismi ile sabitliyoruz
            model = genai.GenerativeModel("models/gemini-3.8-flash") 
            
            prompt = f"Bütçe: {budget} TL. Maçlar: {matches}. Strateji: Çift şart yasak, 2-3 gol tuzağı yasak."
            
            res = model.generate_content(prompt)
            
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
