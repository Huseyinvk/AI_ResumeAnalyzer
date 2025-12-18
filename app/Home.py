import streamlit as st
import json
import os
import sys
from pathlib import Path

# Proje kök dizinini sisteme tanıt
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from core.parsing.extract_text import extract_text
from core.privacy.pii_redaction import redact_pii
from core.scoring.fit_score import calculate_fit_score
from core.generation.roadmap import generate_roadmap
from core.generation.rewrites import suggest_rewrites

# --- SAYFA AYARLARI VE ÖZEL CSS ---
st.set_page_config(page_title="Career Copilot AI", layout="wide", page_icon="🎯")

# Sayfaya "Canlılık" katacak CSS dokunuşları
st.markdown("""
    <style>
    /* Ana başlık stili */
    .main-title {
        font-size: 3rem !important;
        font-weight: 800;
        background: -webkit-linear-gradient(#00f2fe, #4facfe);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0rem;
    }
    /* Kart yapısı */
    .stMetric {
        background-color: #1e2130;
        padding: 20px;
        border-radius: 15px;
        border: 1px solid #3e4259;
    }
    /* Arka planı biraz yumuşatalım */
    .stApp {
        background-color: #0e1117;
    }
    </style>
    """, unsafe_allow_html=True)

# --- HEADER SECTION ---
st.markdown('<h1 class="main-title">Career Copilot AI</h1>', unsafe_allow_html=True)
st.write("✨ **Kariyer yolculuğunuzu yapay zeka ile profesyonelce tasarlayın.**")
st.markdown("---")

# Rol Kataloğunu Yükle
CATALOG_PATH = "core/taxonomy/roles_catalog.json"
with open(CATALOG_PATH, "r") as f:
    roles_data = json.load(f)

# --- ANA ARAYÜZ ---
col1, col2 = st.columns([1, 1.5], gap="large")

with col1:
    st.markdown("### 📥 CV ve Hedef Analizi")
    with st.container():
        target_role = st.selectbox("Hedeflediğiniz Rolü Seçin:", sorted(list(roles_data.keys())))
        uploaded_file = st.file_uploader("", type=["pdf", "docx"], help="PDF veya Word formatında CV'nizi bırakın.")

if uploaded_file:
    file_extension = Path(uploaded_file.name).suffix
    temp_filename = f"temp_cv{file_extension}"
    
    with open(temp_filename, "wb") as f:
        f.write(uploaded_file.getbuffer())
    
    try:
        raw_text = extract_text(temp_filename)
        safe_text = redact_pii(raw_text)
        
        all_target_skills = roles_data[target_role]["must_have"] + roles_data[target_role]["nice_to_have"]
        found_skills = [s for s in all_target_skills if s.lower() in safe_text.lower()]
        
        cv_profile = {"skills": found_skills}
        analysis = calculate_fit_score(cv_profile, roles_data[target_role])
        
        with col2:
            st.markdown(f"### 🎯 Analiz Raporu: {target_role}")
            
            # Skor Gösterimi
            score = analysis['fit_score']
            st.metric(label="Genel Uyumluluk Skoru", value=f"%{score}")
            
            # Alt Skorlar
            st.write("#### 📊 Metrikler")
            m1, m2, m3 = st.columns(3)
            m1.caption(f"Yetenek: %{analysis['subscores']['skills']}")
            m2.caption(f"Deneyim: %{analysis['subscores']['experience']}")
            m3.caption(f"ATS Puanı: %{analysis['subscores']['ats']}")

            # Skill Gap
            st.info("💡 **Gelişim Alanları:** " + ", ".join(analysis.get("missing_must", [])))
            
            # Tab Menü (Ruhsuzluktan kurtaran dinamik yapı)
            tab1, tab2 = st.tabs(["🗺️ Yol Haritası", "✍️ CV İyileştirme"])
            
            with tab1:
                with st.spinner("AI planını çiziyor..."):
                    roadmap = generate_roadmap(analysis["missing_must"], target_role, safe_text)
                    st.markdown(roadmap)
            
            with tab2:
                if st.button("🚀 Cümlelerimi Profesyonelleştir"):
                    with st.spinner("AI cümleleri parlatıyor..."):
                        tips = suggest_rewrites(safe_text)
                        st.success(tips)

    except Exception as e:
        st.error(f"Hata: {e}")
    finally:
        if os.path.exists(temp_filename):
            os.remove(temp_filename)
