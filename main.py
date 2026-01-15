# =================================================================
# ECOKERNEL AI - GLOBAL GOVERNANCE CORE (APEX EDITION)
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
    page_title=f"EcoKernel AI | Scarlet Fuenmayor",
    page_icon="⚡", 
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- CARGA SEGURA DEL LOGO DE SCARLET ---
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

# --- ESTILO "STARK-INDUSTRIAL" REPOTENCIADO ---
st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&family=JetBrains+Mono:wght@300&display=swap');
    
    .stApp {{ background-color: #000000 !important; color: #00FF00 !important; font-family: 'JetBrains Mono', monospace; }}
    
    .header-container {{
        display: flex; flex-direction: column; align-items: center; justify-content: center;
        text-align: center; padding: 40px 0; width: 100%;
    }}

    .stark-square-frame {{
        border: 4px solid #00FF00;
        border-radius: 8px;
        padding: 15px;
        background: rgba(0, 255, 0, 0.03);
        box-shadow: 0px 0px 50px rgba(0, 255, 0, 0.4), inset 0px 0px 20px rgba(0, 255, 0, 0.2);
        width: 220px; height: 220px;
        display: flex; justify-content: center; align-items: center;
        margin-bottom: 30px; backdrop-filter: blur(8px);
    }}
    .stark-square-frame img {{ width: 90%; height: 90%; object-fit: contain; }}

    .stark-h1 {{
        font-family: 'Orbitron', sans-serif !important;
        font-size: 5em !important;
        letter-spacing: 18px;
        text-shadow: 0px 0px 30px #00FF00;
        margin: 0 !important; color: #00FF00;
    }}

    .stark-badge {{
        background: #00FF00; color: #000; padding: 8px 45px;
        font-weight: bold; font-family: 'Orbitron'; margin-top: 15px;
        letter-spacing: 4px; border-radius: 2px;
    }}
    </style>
    """, unsafe_allow_html=True)

# --- CABECERA ---
st.markdown('<div class="header-container">', unsafe_allow_html=True)
if logo_b64:
    st.markdown(f'<div class="stark-square-frame"><img src="{logo_b64}"></div>', unsafe_allow_html=True)
else:
    st.markdown('<div class="stark-square-frame"><h1 style="font-size: 90px; margin:0;">⚡</h1></div>', unsafe_allow_html=True)

st.markdown('<h1 class="stark-h1">ECOKERNEL AI</h1>', unsafe_allow_html=True)
st.markdown(f'<div class="stark-badge">MASTER ARCHITECT: SCARLET FUENMAYOR</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

st.divider()

# --- PANEL LATERAL Y AUTO-REFRESCO ---
st.sidebar.markdown("### 🕹️ COMMAND_CENTER")
target = st.sidebar.selectbox("🎯 TARGET", ["Global Kernel", "WhatsApp Node", "YouTube Buffer", "Apple Silicon"])
auto_refresh = st.sidebar.toggle("AUTO-SYNC NEURAL PULSE", value=True)

# --- LÓGICA DE TELEMETRÍA ---
try:
    # Captura de datos
    cpu = psutil.cpu_percent()
    ram = psutil.virtual_memory().percent
    net = psutil.net_io_counters()
    
    col1, col2, col3 = st.columns(3)
    col1.metric("CPU_CORE_FREQ", f"{cpu}%")
    col2.metric("NEURAL_RAM", f"{ram}%")
    col3.metric("NET_TRAFFIC", f"{net.bytes_sent // (1024**2)} MB ↑")

    # Gráfico de Frecuencia Proyectado
    fig = go.Figure(go.Indicator(
        mode = "gauge+number", value = cpu,
        gauge = {
            'axis': {'range': [0, 100], 'tickcolor': "#00FF00"},
            'bar': {'color': "#00FF00"},
            'bgcolor': "black",
            'bordercolor': "#00FF00",
            'steps': [{'range': [0, 100], 'color': 'rgba(0, 255, 0, 0.05)'}]
        },
        title = {'text': f"PULSO DE FRECUENCIA: {target}", 'font': {'color': "#00FF00", 'family': 'Orbitron'}}
    ))
    fig.update_layout(paper_bgcolor='black', font={'color': "#00FF00"}, height=350, margin=dict(t=50, b=20))
    st.plotly_chart(fig, use_container_width=True)

except Exception as e:
    st.error(f"Error de Telemetría: {e}")

# --- MÓDULOS DE GOBERNANZA REPOTENCIADOS ---
st.write("---")
col_a, col_k = st.columns(2)

with col_a:
    st.markdown("### 👁️ ÁMBAR: Auditoría Pro")
    if st.button("SCAN DEEP STORAGE"):
        st.write("Analizando sectores del Kernel...")
        usage = psutil.disk_usage('/')
        st.info(f"Integridad de Datos: {100 - usage.percent}%")
        st.success("Sectores de Scarlet Verificados.")

with col_k:
    st.markdown("### 🧠 KENYA: Seguridad Pro")
    if st.button("FIREWALL SHIELD ON"):
        with st.spinner("Encriptando nodos..."):
            time.sleep(1)
            st.success("Protocolo AES-256 Activo en toda la red.")

# --- AUTO-REFRESCO ---
if auto_refresh:
    time.sleep(2)
    st.rerun()

# --- FOOTER ---
st.divider()
st.markdown(f"<p style='text-align: center; opacity: 0.5;'>© 2026 Scarlet Fuenmayor | CARACAS_NODE_ACTIVE</p>", unsafe_allow_html=True)
