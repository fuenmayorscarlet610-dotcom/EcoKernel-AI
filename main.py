# =================================================================
# ECOKERNEL AI - GLOBAL GOVERNANCE CORE (STARK-LINUS EDITION)
# AUTHOR: SCARLET FUENMAYOR DÍAZ
# LICENSE: PROPRIETARY HARDWARE GOVERNANCE © 2026
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

# --- CONFIGURACIÓN GLOBAL ---
VERSION = "25.0.0-CORE-DIAMOND"
DEVELOPER = "Scarlet Fuenmayor Díaz"
COPYRIGHT = f"© 2026 {DEVELOPER}"

st.set_page_config(
    page_title=f"EcoKernel AI | {DEVELOPER}",
    page_icon="⚡", 
    layout="wide"
)

# --- MOTOR DE IMAGEN (CARGA SEGURA BASE64) ---
def load_stark_logo(path):
    if os.path.exists(path):
        with open(path, "rb") as f:
            data = base64.b64encode(f.read()).decode()
            return f"data:image/png;base64,{data}"
    return None

logo_b64 = load_stark_logo("logo.png")

# --- INTERFAZ DE INGENIERÍA APEX (MARCO CUADRADO & CENTRADO) ---
st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&family=JetBrains+Mono:wght@300&display=swap');
    
    .stApp {{ 
        background-color: #000000 !important; 
        color: #00FF00 !important; 
        font-family: 'JetBrains Mono', monospace; 
    }}
    
    /* Header Unificado y Centrado */
    .header-master {{
        display: flex; flex-direction: column; align-items: center; justify-content: center;
        width: 100%; padding-top: 40px; text-align: center;
    }}

    /* Marco del Logo: CUADRADO DE PRECISIÓN NEÓN */
    .logo-stark-frame {{
        border: 3px solid #00FF00;
        border-radius: 10px; /* Corte diamante suave */
        padding: 15px;
        background: rgba(0, 255, 0, 0.03);
        box-shadow: 0px 0px 40px #00FF00, inset 0px 0px 15px #00FF00;
        width: 220px; height: 220px;
        display: flex; justify-content: center; align-items: center;
        overflow: hidden; margin-bottom: 30px;
        transition: 0.5s ease-in-out;
    }}
    .logo-stark-frame:hover {{ 
        transform: scale(1.05); 
        box-shadow: 0px 0px 60px #00FF00;
        background: rgba(0, 255, 0, 0.08);
    }}
    .logo-stark-frame img {{ width: 100%; height: 100%; object-fit: contain; }}

    /* Centrado Maestro de Tipografía */
    h1, h2, h3, p, span {{ text-align: center !important; font-family: 'Orbitron', sans-serif !important; }}
    
    .main-title {{
        font-size: 4.8em !important; letter-spacing: 18px;
        text-shadow: 0px 0px 20px #00FF00; margin-bottom: 5px !important;
        color: #00FF00 !important;
    }}

    .sub-guide {{
        border-top: 1px solid #00FF00; border-bottom: 1px solid #00FF00;
        padding: 8px 40px; display: inline-block; letter-spacing: 5px;
        color: #FFFFFF; font-weight: bold; margin-top: 15px;
    }}

    /* Metrics Grid Centered */
    [data-testid="stMetric"] {{ 
        background: rgba(0, 255, 0, 0.04) !important; 
        border: 2px solid #00FF00 !important; 
        border-radius: 0px !important; /* Estilo industrial */
        padding: 20px !important;
    }}
    
    [data-testid="stMetricValue"] {{ justify-content: center !important; font-size: 2.5em !important; }}
    </style>
    """, unsafe_allow_html=True)

# --- CABECERA DE IDENTIDAD ---
st.markdown('<div class="header-master">', unsafe_allow_html=True)
if logo_b64:
    st.markdown(f'<div class="logo-stark-frame"><img src="{logo_b64}"></div>', unsafe_allow_html=True)
else:
    st.markdown('<div class="logo-stark-frame"><h1 style="font-size: 100px; margin:0;">⚡</h1></div>', unsafe_allow_html=True)

st.markdown(f'<h1 class="main-title">ECOKERNEL AI</h1>', unsafe_allow_html=True)
st.markdown(f'<p style="letter-spacing: 10px; opacity: 0.8;">HARDWARE GOVERNANCE MASTER</p>', unsafe_allow_html=True)
st.markdown(f'<div class="sub-guide">DEVELOPER: {DEVELOPER.upper()}</div>', unsafe_allow_html=True)
st.markdown(f'<p style="font-size: 0.8em; margin-top: 15px; opacity: 0.5;">{datetime.now().strftime("%Y-%m-%d | %H:%M:%S")} | CARACAS_SB</p>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

st.divider()

# --- PANEL DE COMANDO LATERAL ---
st.sidebar.markdown("### 🕹️ MASTER_GOVERNANCE")
target_app = st.sidebar.selectbox("FOCAL_TARGET", ["Global System", "WhatsApp", "YouTube", "Apple Core", "Linux Kernel", "TikTok"])
mode = st.sidebar.select_slider("INTENSITY", options=["QUIET", "BALANCED", "OVERCLOCK"])

# --- MONITOR DE FRECUENCIA (STARK STYLE) ---
st.markdown(f"### 📊 PULSO NEURAL DEL NODO: {target_app.upper()}")
cpu = psutil.cpu_percent(interval=0.1)
ram = psutil.virtual_memory().percent
disk = psutil.disk_usage('/').percent

# Gráfico de Frecuencia Proyectado
fig = go.Figure(go.Indicator(
    mode = "gauge+number", value = cpu,
    gauge = {
        'axis': {'range': [0, 100], 'tickcolor': "#00FF00"},
        'bar': {'color': "#00FF00"},
        'bgcolor': "black",
        'bordercolor': "#00FF00",
        'steps': [{'range': [0, 100], 'color': 'rgba(0, 255, 0, 0.05)'}]
    }
))
fig.update_layout(paper_bgcolor='black', font={'color': "#00FF00", 'family': "Orbitron"}, height=300, margin=dict(t=0, b=0))
st.plotly_chart(fig, use_container_width=True)

# --- TELEMETRÍA DE ALTO IMPACTO ---
st.write("---")
c1, c2, c3 = st.columns(3)
c1.metric("NODAL_CPU", f"{cpu}%")
c2.metric("MEMORY_BUFFER", f"{ram}%")
c3.metric("STORAGE_FREE", f"{100-disk:.1f}%")

# --- BLOQUE DE MÓDULOS (INSERTE AQUÍ MÓDULOS ADICIONALES) ---
# [PRÓXIMAMENTE: MÓDULO ÁMBAR / KENYA MEJORADOS]

st.divider()
st.markdown(f"""
    <div style="text-align: center; opacity: 0.4; font-size: 0.7em;">
        {COPYRIGHT} | Sincronización de Servidores Activa
    </div>
""", unsafe_allow_html=True)
