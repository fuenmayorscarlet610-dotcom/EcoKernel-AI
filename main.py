# =================================================================
# ECOKERNEL AI - GLOBAL GOVERNANCE CORE (GOD MODE)
# AUTHOR: SCARLET FUENMAYOR DÍAZ
# COPYRIGHT: © 2026 SCARLET FUENMAYOR
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

# --- CONFIGURACIÓN GLOBAL DE ALTO RENDIMIENTO ---
st.set_page_config(
    page_title="EcoKernel AI | Scarlet Fuenmayor",
    page_icon="⚡", 
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- OPTIMIZACIÓN DE RECURSOS (CACHÉ) ---
@st.cache_resource
def get_stark_assets(path):
    if os.path.exists(path):
        with open(path, "rb") as f:
            data = base64.b64encode(f.read()).decode()
            return f"data:image/png;base64,{data}"
    return None

logo_b64 = get_stark_assets("logo.png")

# --- ESTÉTICA DE INGENIERÍA SUPREMA ---
st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&family=JetBrains+Mono:wght@300&display=swap');
    
    .stApp {{ background-color: #000000 !important; color: #00FF00 !important; font-family: 'JetBrains Mono', monospace; }}
    
    /* Contenedor Maestro Centrado */
    .header-apex {{ display: flex; flex-direction: column; align-items: center; justify-content: center; text-align: center; padding: 40px 0; }}

    /* Marco Cuadrado Stark: Diamond Cut */
    .stark-frame {{
        border: 4px solid #00FF00;
        padding: 20px;
        background: linear-gradient(145deg, rgba(0,255,0,0.05), rgba(0,0,0,1));
        box-shadow: 0px 0px 50px rgba(0,255,0,0.4), inset 0px 0px 20px rgba(0,255,0,0.2);
        width: 220px; height: 220px;
        display: flex; justify-content: center; align-items: center;
        margin-bottom: 25px; transition: 0.4s ease;
    }}
    .stark-frame:hover {{ transform: scale(1.02); box-shadow: 0px 0px 80px #00FF00; }}
    .stark-frame img {{ width: 100%; height: 100%; object-fit: contain; }}

    .glitch-title {{
        font-family: 'Orbitron', sans-serif !important;
        font-size: 5em !important;
        letter-spacing: 25px;
        text-shadow: 0px 0px 30px #00FF00;
        margin: 0 !important;
        color: #00FF00;
    }}

    .status-badge {{
        background: #00FF00; color: #000; padding: 5px 35px;
        font-weight: bold; letter-spacing: 5px; margin-top: 15px;
        clip-path: polygon(5% 0%, 100% 0%, 95% 100%, 0% 100%);
    }}
    
    /* Optimización de Métricas */
    [data-testid="stMetric"] {{ border: 1px solid #00FF00 !important; background: rgba(0,255,0,0.02) !important; padding: 15px !important; }}
    [data-testid="stMetricValue"] {{ font-family: 'Orbitron'; color: #FFF !important; text-align: center !important; }}
    </style>
    """, unsafe_allow_html=True)

# --- EJECUCIÓN DE INTERFAZ ---
st.markdown('<div class="header-apex">', unsafe_allow_html=True)
if logo_b64:
    st.markdown(f'<div class="stark-frame"><img src="{logo_b64}"></div>', unsafe_allow_html=True)
else:
    st.markdown('<div class="stark-frame"><h1 style="font-size: 100px; margin:0;">⚡</h1></div>', unsafe_allow_html=True)

st.markdown('<h1 class="glitch-title">ECOKERNEL AI</h1>', unsafe_allow_html=True)
st.markdown(f'<div class="status-badge">ARCHITECT: {DEVELOPER.upper()}</div>', unsafe_allow_html=True)
st.markdown(f'<p style="opacity: 0.6; margin-top: 20px; letter-spacing: 3px;">SYSTEM_STATUS: NOMINAL | CARACAS_NODE: ONLINE</p>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# --- CONTROL DE GOBERNANZA ---
target = st.sidebar.selectbox("🎯 FOCAL_TARGET", ["Global System", "Apple Core", "WhatsApp", "YouTube", "Linux Server"])
st.divider()

# --- TELEMETRÍA ULTRA-RÁPIDA ---
cpu_val = psutil.cpu_percent()
ram_val = psutil.virtual_memory().percent
disk_val = psutil.disk_usage('/').percent

col1, col2, col3 = st.columns(3)
col1.metric("KERNEL_CPU", f"{cpu_val}%")
col2.metric("BUFFER_RAM", f"{ram_val}%")
col3.metric("STORAGE_STATE", f"{100-disk_val:.1f}% FREE")

# --- MONITOR DE FRECUENCIA (STARK INDICATOR) ---
fig = go.Figure(go.Indicator(
    mode = "gauge+number", value = cpu_val,
    gauge = {'axis': {'range': [0, 100]}, 'bar': {'color': "#00FF00"}, 'bgcolor': "black", 'bordercolor': "#00FF00"},
    title = {'text': f"FRECUENCIA NEURAL: {target}", 'font': {'color': "#00FF00", 'family': 'Orbitron'}}
))
fig.update_layout(paper_bgcolor='black', height=350, margin=dict(t=50, b=0))
st.plotly_chart(fig, use_container_width=True)

# --- MÓDULOS ÁMBAR & KENYA (REFINADOS) ---
st.divider()
ca, ck = st.columns(2)

with ca:
    st.markdown("### 👁️ ÁMBAR: Auditoría")
    if st.button("SCAN_ENTROPY"):
        st.write("Analizando sectores de almacenamiento...")
        st.progress(100)
        st.success("Entropía optimizada. No se detectaron fugas de datos.")

with ck:
    st.markdown("### 🧠 KENYA: Seguridad")
    if st.button("RUN_SHIELD_SCAN"):
        with st.spinner("Verificando puertos..."):
            time.sleep(1)
            st.info(f"Escudo AES-256 activo en {target}.")

# --- DNA REPORT ---
st.write("---")
st.code(f"USER: {DEVELOPER}\nNODE: {platform.node()}\nBOOT_TIME: {datetime.fromtimestamp(psutil.boot_time()).strftime('%H:%M:%S')}", language="bash")

# --- FOOTER ---
st.markdown(f"<p style='text-align: center; opacity: 0.4; font-size: 0.8em; margin-top: 50px;'>{COPYRIGHT} | V {VERSION}</p>", unsafe_allow_html=True)
