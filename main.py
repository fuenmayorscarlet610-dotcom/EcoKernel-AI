# =================================================================
# ECOKERNEL AI - GLOBAL GOVERNANCE CORE
# AUTHOR: SCARLET FUENMAYOR DÍAZ
# LICENSE: PROPRIETARY HARDWARE GOVERNANCE © 2026
# =================================================================

import streamlit as st
import psutil
import platform
import os
import base64
from datetime import datetime
import pandas as pd
import plotly.graph_objects as go

# --- CONFIGURACIÓN GLOBAL ---
VERSION = "21.0.0-PRO-FINAL"
DEVELOPER = "Scarlet Fuenmayor Díaz"
COPYRIGHT = f"© 2026 {DEVELOPER}"

st.set_page_config(page_title="EcoKernel AI", page_icon="⚡", layout="wide")

# --- MOTOR DE IMAGEN (SOLUCIÓN DE LOGO) ---
def load_logo_stark(path):
    if os.path.exists(path):
        with open(path, "rb") as f:
            data = base64.b64encode(f.read()).decode()
            return f"data:image/png;base64,{data}"
    return None

logo_url = load_logo_stark("logo.png")

# --- INTERFAZ NEURAL (CSS BLINDADO) ---
st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&display=swap');
    
    .stApp {{ background-color: #000000 !important; color: #00FF00 !important; }}
    
    /* Contenedor Maestro de Centrado */
    .stark-header {{
        display: flex; flex-direction: column; align-items: center;
        justify-content: center; text-align: center; width: 100%;
    }}

    /* El Círculo Neón Perfecto */
    .circle-frame {{
        width: 200px; height: 200px;
        border: 4px solid #00FF00;
        border-radius: 50% !important;
        box-shadow: 0px 0px 45px #00FF00;
        display: flex; justify-content: center; align-items: center;
        overflow: hidden; background: #000; margin: 20px auto;
    }}
    .circle-frame img {{ width: 100%; height: 100%; object-fit: cover; }}

    h1, h2, h3, p {{ font-family: 'Orbitron', sans-serif !important; text-align: center !important; }}
    
    .stMetric {{ 
        border: 2px solid #00FF00 !important; border-radius: 20px !important;
        background: rgba(0, 255, 0, 0.05) !important; padding: 20px !important;
    }}
    
    /* Botones de Mando */
    .stButton>button {{
        border: 2px solid #00FF00 !important; background: transparent !important;
        color: #00FF00 !important; border-radius: 50px !important;
        font-family: 'Orbitron' !important; width: 100% !important;
    }}
    .stButton>button:hover {{ box-shadow: 0px 0px 30px #00FF00 !important; background: #00FF00 !important; color: #000 !important; }}
    </style>
""", unsafe_allow_html=True)

# --- HEADER (LOGOTIPO Y AUTORÍA) ---
st.markdown('<div class="stark-header">', unsafe_allow_html=True)
if logo_url:
    st.markdown(f'<div class="circle-frame"><img src="{logo_url}"></div>', unsafe_allow_html=True)
else:
    st.markdown('<div class="circle-frame"><h1 style="font-size: 80px; margin-top: 40px;">⚡</h1></div>', unsafe_allow_html=True)

st.markdown(f"""
    <h1 style="font-size: 4em; letter-spacing: 5px; margin-bottom: 0;">ECOKERNEL AI</h1>
    <p style="color: #FFF; letter-spacing: 10px; opacity: 0.8;">GLOBAL HARDWARE GOVERNANCE</p>
    <div style="background: #00FF00; color: #000; padding: 5px 30px; font-weight: bold; margin-top: 10px;">
        ARCHITECT: {DEVELOPER.upper()}
    </div>
    <p style="font-size: 0.8em; margin-top: 20px; opacity: 0.5;">ID_SINCRO: {datetime.now().strftime('%Y%m%d_%H%M')} | Caracas, SB</p>
""", unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

st.divider()

# --- SIDEBAR CONTROL ---
st.sidebar.markdown("### 🕹️ CONTROL PANEL")
target = st.sidebar.selectbox("FOCAL_TARGET", ["Global System", "WhatsApp", "YouTube", "Kernel Core"])

# --- TELEMETRÍA DINÁMICA ---
cpu = psutil.cpu_percent()
ram = psutil.virtual_memory().percent
disk = psutil.disk_usage('/').percent

st.markdown(f"### 🛰️ TELEMETRÍA: {target.upper()}")
c1, c2, c3 = st.columns(3)
c1.metric("CPU_CORE", f"{cpu}%")
c2.metric("RAM_BUFFER", f"{ram}%")
c3.metric("STORAGE", f"{disk}%")

# --- GRÁFICO DE PULSO KERNEL ---
fig = go.Figure(go.Indicator(
    mode = "gauge+number", value = cpu,
    gauge = {'axis': {'range': [0, 100]}, 'bar': {'color': "#00FF00"}, 'bgcolor': "black", 'bordercolor': "#00FF00"},
    title = {'text': "Frecuencia de Hilos", 'font': {'color': "#00FF00", 'family': "Orbitron"}}
))
fig.update_layout(paper_bgcolor='black', font={'color': "white"}, height=300)
st.plotly_chart(fig, use_container_width=True)

# --- MÓDULOS ÁMBAR & KENYA ---
st.divider()
col_a, col_k = st.columns(2)

with col_a:
    st.markdown("### 👁️ NEURAL: Ámbar")
    if st.button("AUDITORÍA DE PARTICIONES"):
        usage_data = {"Punto": ["Raíz", "Cache", "Apps"], "Carga": [f"{disk}%", "12%", "45%"]}
        st.table(pd.DataFrame(usage_data))

with col_k:
    st.markdown("### 🧠 NEURAL: Kenya")
    diag_status = "STABLE" if cpu < 70 else "WARNING: PEAK"
    st.info(f"**[KENYA_DIAG]:** Estado del nodo {target} es {diag_status}.")

# --- DNA DEL SISTEMA ---
st.divider()
st.markdown("### 🖥️ [SYSTEM_DNA_HARDWARE]")
st.code(f"USER: {DEVELOPER}\nNODE: {platform.node()}\nARCH: {platform.machine()}\nBOOT: {datetime.fromtimestamp(psutil.boot_time()).strftime('%Y-%m-%d %H:%M')}", language="bash")

# --- FOOTER ---
st.markdown(f"""
    <div style="text-align: center; margin-top: 50px; padding: 20px; border-top: 1px solid #111;">
        <p style="color: #00FF00; letter-spacing: 5px;">{COPYRIGHT}</p>
        <p style="font-size: 0.7em; opacity: 0.4;">Hardware Governance Protocol Active - All Rights Reserved.</p>
    </div>
""", unsafe_allow_html=True)
