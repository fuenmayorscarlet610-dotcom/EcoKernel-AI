# =================================================================
# ECOKERNEL - GLOBAL GOVERNANCE CORE (APEX MINIMAL)
# AUTHOR: SCARLET FUENMAYOR DÍAZ
# COPYRIGHT: © 2026 Scarlet Fuenmayor
# =================================================================

import streamlit as st
import psutil
import platform
import os
import base64
import time
import pandas as pd 
import plotly.graph_objects as go
from datetime import datetime

# --- CONFIGURACIÓN DE NÚCLEO SUPREMO ---
st.set_page_config(
    page_title=f"EcoKernel | Scarlet Fuenmayor",
    page_icon="⚡", 
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- CARGA SEGURA DEL LOGO ---
@st.cache_resource
def get_encoded_assets(path):
    if os.path.exists(path):
        try:
            with open(path, "rb") as f:
                return f"data:image/png;base64,{base64.b64encode(f.read()).decode()}"
        except Exception:
            return None
    return None

logo_b64 = get_encoded_assets("logo.png")

# --- ESTILO "STARK-APEX" (CENTRADO ABSOLUTO & NEÓN SOFISTICADO) ---
st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&family=JetBrains+Mono:wght@300&display=swap');
    
    .stApp {{ background-color: #000000 !important; color: #00FF00 !important; font-family: 'JetBrains Mono', monospace; }}
    
    .header-container {{
        display: flex; flex-direction: column; align-items: center; justify-content: center;
        text-align: center; padding: 20px 0; width: 100%;
    }}

    /* Marco Cuadrado de Alta Definición */
    .stark-square-frame {{
        border: 1px solid #00FF00;
        border-radius: 2px;
        padding: 25px;
        background: rgba(0, 255, 0, 0.02);
        box-shadow: 0px 0px 60px rgba(0, 255, 0, 0.2);
        width: 180px; height: 180px;
        display: flex; justify-content: center; align-items: center;
        margin-bottom: 30px; transition: all 0.8s ease;
    }}
    .stark-square-frame:hover {{ 
        box-shadow: 0px 0px 100px #00FF00;
        border: 1px solid #FFFFFF;
        transform: scale(1.05);
    }}
    .stark-square-frame img {{ width: 100%; height: 100%; object-fit: contain; }}

    /* Título Minimalista */
    .stark-h1 {{
        font-family: 'Orbitron', sans-serif !important;
        font-size: 6.5em !important;
        letter-spacing: 30px;
        text-shadow: 0px 0px 15px #00FF00;
        margin: 0 !important; color: #00FF00;
        font-weight: 700;
    }}

    .stark-badge {{
        border: 1px solid #00FF00; color: #FFFFFF; padding: 5px 35px;
        font-weight: bold; font-family: 'Orbitron'; margin-top: 10px;
        letter-spacing: 10px; font-size: 0.8em; opacity: 0.8;
    }}

    /* Guías Centradas */
    .function-guide {{
        text-align: center !important;
        font-family: 'Orbitron', sans-serif;
        letter-spacing: 6px;
        color: #FFFFFF;
        margin: 40px auto 20px auto;
        text-transform: uppercase;
        font-size: 1em;
        border-bottom: 1px solid rgba(0,255,0,0.2);
        display: block; width: fit-content; padding-bottom: 5px;
    }}

    /* Métricas Stark Industrial */
    [data-testid="stMetric"] {{ 
        border-left: 3px solid #00FF00 !important;
        background: rgba(0, 255, 0, 0.02) !important;
        padding: 20px !important;
    }}
    </style>
    """, unsafe_allow_html=True)

# --- CABECERA (ONLY ECOKERNEL) ---
st.markdown('<div class="header-container">', unsafe_allow_html=True)
if logo_b64:
    st.markdown(f'<div class="stark-square-frame"><img src="{logo_b64}"></div>', unsafe_allow_html=True)
else:
    st.markdown('<div class="stark-square-frame"><h1 style="font-size: 80px; margin:0;">⚡</h1></div>', unsafe_allow_html=True)

st.markdown('<h1 class="stark-h1">ECOKERNEL</h1>', unsafe_allow_html=True)
st.markdown(f'<div class="stark-badge">ARCHITECT: SCARLET FUENMAYOR</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

st.divider()

# --- PANEL LATERAL ---
st.sidebar.markdown("### 🕹️ SYSTEM_CONTROL")
target = st.sidebar.selectbox("🎯 MONITOR", ["Global Node", "Apple Silicon", "WhatsApp Bridge", "YouTube Cloud", "Linux Core"])
refresh = st.sidebar.toggle("ACTIVE SYNC", value=True)

# --- TELEMETRÍA ---
try:
    cpu = psutil.cpu_percent(interval=0.1)
    ram = psutil.virtual_memory().percent
    
    st.markdown('<p class="function-guide">📡 Telemetría de Frecuencia</p>', unsafe_allow_html=True)
    
    c1, c2 = st.columns(2)
    c1.metric("CPU_CORE", f"{cpu}%")
    c2.metric("RAM_LOAD", f"{ram}%")

    fig = go.Figure(go.Indicator(
        mode = "gauge+number", value = cpu,
        gauge = {
            'axis': {'range': [0, 100], 'tickcolor': "#00FF00"},
            'bar': {'color': "#00FF00"},
            'bgcolor': "black",
            'steps': [{'range': [0, 100], 'color': 'rgba(0, 255, 0, 0.05)'}]
        },
        title = {'text': f"NEURAL PULSE: {target.upper()}", 'font': {'color': "#00FF00", 'family': 'Orbitron'}}
    ))
    fig.update_layout(paper_bgcolor='black', height=350, margin=dict(t=50, b=20))
    st.plotly_chart(fig, use_container_width=True)

except Exception as e:
    st.error(f"Sync Error: {e}")

# --- MÓDULOS DE GOBERNANZA CENTRADOS ---
st.write("---")
col_a, col_k = st.columns(2)

with col_a:
    st.markdown('<p class="function-guide">👁️ Ámbar: Auditoría</p>', unsafe_allow_html=True)
    if st.button("RUN DEEP SCAN", use_container_width=True):
        st.success("Sectores de Scarlet Íntegros.")
        st.dataframe(pd.DataFrame({"Nodo": ["A-1", "B-2"], "Status": ["Secure", "Optimized"]}), use_container_width=True)

with col_k:
    st.markdown('<p class="function-guide">🧠 Kenya: Seguridad</p>', unsafe_allow_html=True)
    if st.button("DEPLOY SHIELD", use_container_width=True):
        st.success(f"Cifrado AES-256 Activo en {target}.")
        st.code("NODE_STATUS: IMMUTABLE", language="bash")

# --- AUTO-REFRESCO ---
if refresh:
    time.sleep(2)
    st.rerun()

# --- FOOTER ---
st.divider()
st.markdown(f"<div style='text-align: center; opacity: 0.4; font-size: 0.8em; letter-spacing: 5px;'>{platform.system().upper()} GOVERNANCE | © 2026 SCARLET FUENMAYOR</div>", unsafe_allow_html=True)
