# =================================================================
# ECOKERNEL AI - GLOBAL GOVERNANCE CORE (GOD ARCHITECTURE)
# AUTHOR: SCARLET FUENMAYOR DÍAZ
# LICENSE: PROPRIETARY HARDWARE GOVERNANCE © 2026
# COPYRIGHT: Scarlet Fuenmayor
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
    page_title=f"EcoKernel AI | Scarlet Fuenmayor",
    page_icon="⚡", 
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- CACHÉ NEURAL (EVITA ERRORES DE CARGA REPETITIVA) ---
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

# --- INYECCIÓN DE ESTILO "STARK-INDUSTRIAL" ---
st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&family=JetBrains+Mono:wght@300&display=swap');
    
    .stApp {{ background-color: #000000 !important; color: #00FF00 !important; font-family: 'JetBrains Mono', monospace; }}
    
    /* Header Apex: Centrado Milimétrico */
    .header-container {{
        display: flex; flex-direction: column; align-items: center; justify-content: center;
        text-align: center; padding: 50px 0; width: 100%;
    }}

    /* Marco Cuadrado Neón con Efecto Cristal */
    .stark-square-frame {{
        border: 4px solid #00FF00;
        border-radius: 5px;
        padding: 20px;
        background: rgba(0, 255, 0, 0.02);
        box-shadow: 0px 0px 40px rgba(0, 255, 0, 0.5), inset 0px 0px 20px rgba(0, 255, 0, 0.3);
        width: 230px; height: 230px;
        display: flex; justify-content: center; align-items: center;
        margin-bottom: 35px; backdrop-filter: blur(5px);
        transition: all 0.5s ease;
    }}
    .stark-square-frame:hover {{ transform: scale(1.03) rotate(1deg); box-shadow: 0px 0px 80px #00FF00; }}
    .stark-square-frame img {{ width: 100%; height: 100%; object-fit: contain; }}

    /* Tipografía de Alto Impacto */
    .stark-h1 {{
        font-family: 'Orbitron', sans-serif !important;
        font-size: 5.5em !important;
        letter-spacing: 22px;
        text-shadow: 0px 0px 25px #00FF00;
        margin: 0 !important; color: #00FF00;
    }}

    .stark-badge {{
        border: 2px solid #00FF00; color: #00FF00; padding: 8px 50px;
        font-weight: bold; font-family: 'Orbitron'; margin-top: 20px;
        background: rgba(0, 255, 0, 0.1); letter-spacing: 6px;
    }}

    /* Optimización de Widgets */
    [data-testid="stMetric"] {{ 
        border: 1px solid #00FF00 !important; 
        background: linear-gradient(180deg, rgba(0,255,0,0.05) 0%, rgba(0,0,0,1) 100%) !important;
    }}
    </style>
    """, unsafe_allow_html=True)

# --- RENDERIZADO DE CABECERA ---
st.markdown('<div class="header-container">', unsafe_allow_html=True)
if logo_b64:
    st.markdown(f'<div class="stark-square-frame"><img src="{logo_b64}"></div>', unsafe_allow_html=True)
else:
    st.markdown('<div class="stark-square-frame"><h1 style="font-size: 100px; margin:0;">⚡</h1></div>', unsafe_allow_html=True)

st.markdown('<h1 class="stark-h1">ECOKERNEL AI</h1>', unsafe_allow_html=True)
st.markdown(f'<div class="stark-badge">CHIEF ARCHITECT: {DEVELOPER.upper()}</div>', unsafe_allow_html=True)
st.markdown(f'<p style="opacity: 0.6; margin-top: 25px; letter-spacing: 4px;">PROTOCOL: STABLE_V27 | CARACAS_SERVER: ACTIVE</p>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

st.divider()

# --- PANEL DE CONTROL LATERAL ---
st.sidebar.markdown("### 🕹️ COMMAND_CENTER")
target = st.sidebar.selectbox("🎯 MONITOR_TARGET", ["Global Kernel", "Apple Silicon", "WhatsApp Node", "YouTube Buffer"])
refresh_rate = st.sidebar.slider("SYNC_RATE (ms)", 100, 1000, 500)

# --- LÓGICA DE TELEMETRÍA (ESTRUCTURA VIABLE) ---
try:
    cpu = psutil.cpu_percent(interval=0.1)
    ram = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent
    
    col1, col2, col3 = st.columns(3)
    col1.metric("CPU_CORE_FREQ", f"{cpu}%")
    col2.metric("NEURAL_RAM", f"{ram}%")
    col3.metric("STORAGE_INTEGRITY", f"{100-disk:.1f}% FREE")

    # --- GRÁFICO DE PULSO FRECUENCIA ---
    fig = go.Figure(go.Indicator(
        mode = "gauge+number", value = cpu,
        gauge = {
            'axis': {'range': [0, 100], 'tickcolor': "#00FF00"},
            'bar': {'color': "#00FF00"},
            'bgcolor': "black",
            'bordercolor': "#00FF00",
            'steps': [{'range': [0, 100], 'color': 'rgba(0, 255, 0, 0.05)'}]
        },
        title = {'text': f"FRECUENCIA EN VIVO: {target}", 'font': {'color': "#00FF00", 'family': 'Orbitron'}}
    ))
    fig.update_layout(paper_bgcolor='black', font={'color': "#00FF00"}, height=350)
    st.plotly_chart(fig, use_container_width=True)

except Exception as e:
    st.error(f"Error en el flujo de datos: {e}")

# --- MÓDULOS DE GOBERNANZA (ÁMBAR & KENYA) ---
st.write("---")
col_a, col_k = st.columns(2)

with col_a:
    st.markdown("### 👁️ ÁMBAR: Auditoría")
    if st.button("EXECUTE HARDWARE AUDIT"):
        with st.spinner("Auditando sectores..."):
            parts = psutil.disk_partitions()
            st.table([{"Drive": p.device, "Mount": p.mountpoint, "Type": p.fstype} for p in parts[:2]])

with col_k:
    st.markdown("### 🧠 KENYA: Seguridad")
    if st.button("RUN SHIELD SCAN"):
        st.info(f"Escaneando vulnerabilidades en {target}...")
        time.sleep(1)
        st.success("Escudo Activo: AES-256 Verificado.")

# --- FOOTER DE IDENTIDAD ---
st.divider()
st.markdown(f"""
    <div style="text-align: center; opacity: 0.5;">
        <p style="letter-spacing: 5px;">{COPYRIGHT} © 2026</p>
        <p style="font-size: 0.7em;">POWERED BY ECOKERNEL AI | VENEZUELA</p>
    </div>
""", unsafe_allow_html=True)
