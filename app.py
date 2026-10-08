import streamlit as st
import google.generativeai as genai
import anthropic

st.set_page_config(page_title="SPORTSBIONIC LAB", layout="wide")

# Tasarım
st.markdown("""
<style>
    .main { background-color: #05070c; color: white; }
    h1 { color: #00d9f5; text-align: center; }
</style>
""", unsafe_allow_html=True)

st.title("🧬 SPORTS BIONIC LAB (SBL)")
st.write("Çift Yapay Zekâlı (Gemini + Claude) Analitik Motoru")

# Kenar Çubuğu
with st.sidebar:
    gemini_key = st.text_input("Gemini API Key:", type="password")
    claude_key = st.text_input("Claude Opus Key:", type="password")
    st.info("Bütçe ve API yönetimi aktif.")

# Ana Arayüz
budget = st.number_input("Toplam Bütçe (TL):", min_value=50, value=500, step=50)
matches = st.text_area("Analiz Edilecek Maçlar:", placeholder="Örn: Galatasaray - Kasımpaşa", height=100)

if st.button("🚀 ÇİFT AJANLI ANALİZİ BAŞLAT"):
    if not gemini_key or not claude_key:
        st.error("API anahtarlarını girmedin!")
    else:
        # Gemini Analizi
        genai.configure(api_key=gemini_key)
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        prompt = f"Bütçe: {budget} TL. Maçlar: {matches}. Strateji: Çift şart yasak, tavan gol tuzağı (2-3 gol) yasak."
        
        try:
            res = model.generate_content(prompt)
            gemini_report = res.text
            st.subheader("Analist (Gemini) Raporu:")
            st.write(gemini_report)
            
            # Claude Denetimi
            c_client = anthropic.Anthropic(api_key=claude_key)
            c_res = c_client.messages.create(
                model="claude-3-5-sonnet-20241022",
                max_tokens=1000,
                messages=[{"role": "user", "content": f"Bu analizi denetle: {gemini_report}"}]
            )
            st.subheader("🛡️ Başmüfettiş (Claude) Onaylı Rapor:")
            st.write(c_res.content[0].text)
            
        except Exception as e:
            st.error(f"Hata: {e}")
