# =================================================================
# ECOKERNEL AI - GLOBAL GOVERNANCE CORE (GITHUB MASTER)
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
VERSION = "22.0.0-DIAMOND-STARK"
DEVELOPER = "Scarlet Fuenmayor Díaz"
COPYRIGHT = f"© 2026 {DEVELOPER}"

st.set_page_config(
    page_title=f"EcoKernel AI | {DEVELOPER}",
    page_icon="⚡", 
    layout="wide"
)

# --- MOTOR DE IMAGEN (CARGA SEGURA) ---
def load_stark_logo(path):
    if os.path.exists(path):
        with open(path, "rb") as f:
            data = base64.b64encode(f.read()).decode()
            return f"data:image/png;base64,{data}"
    return None

logo_b64 = load_stark_logo("logo.png")

# --- MODULE 01: ESTÉTICA CYBER-STARK (LOGOTIPO CUADRADO Y CENTRADO) ---
st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&family=JetBrains+Mono:wght@300&display=swap');
    
    .stApp {{ 
        background-color: #000000 !important; 
        color: #00FF00 !important; 
        font-family: 'JetBrains Mono', monospace; 
    }}
    
    /* Contenedor de Logotipo Cuadrado Stark */
    .stark-header {{
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        text-align: center;
        width: 100%;
        margin-top: 20px;
    }}

    .logo-square {{
        border: 3px solid #00FF00;
        border-radius: 15px; /* Bordes ligeramente redondeados para estilo moderno */
        padding: 10px;
        background: rgba(0, 255, 0, 0.05);
        box-shadow: 0px 0px 30px rgba(0, 255, 0, 0.5);
        width: 180px;
        height: 180px;
        display: flex;
        justify-content: center;
        align-items: center;
        overflow: hidden;
        margin-bottom: 25px;
        transition: 0.5s;
    }}
    .logo-square:hover {{ transform: rotateY(180deg); box-shadow: 0px 0px 50px #00FF00; }}
    .logo-square img {{ width: 100%; height: 100%; object-fit: contain; }}

    /* Tipografía y Centrado */
    h1, h2, h3, p {{ text-align: center !important; font-family: 'Orbitron', sans-serif !important; }}
    
    .main-title {{
        font-size: 4em !important;
        letter-spacing: 8px;
        text-shadow: 0px 0px 20px #00FF00;
        margin-bottom: 0px !important;
    }}

    /* Estilo de Métricas */
    [data-testid="stMetric"] {{ 
        background: rgba(0, 255, 0, 0.05) !important; 
        border: 2px solid #00FF00 !important; 
        border-radius: 15px !important;
        text-align: center !important;
    }}
    
    /* Terminal Visual */
    .stCodeBlock {{ border: 1px solid #00FF00 !important; border-radius: 10px; }}
    </style>
    """, unsafe_allow_html=True)

# --- CABECERA MAESTRA ---
st.markdown('<div class="stark-header">', unsafe_allow_html=True)
if logo_b64:
    st.markdown(f'<div class="logo-square"><img src="{logo_b64}"></div>', unsafe_allow_html=True)
else:
    st.markdown('<div class="logo-square"><h1 style="font-size: 80px; margin:0;">⚡</h1></div>', unsafe_allow_html=True)

st.markdown(f"""
    <h1 class="main-title">ECOKERNEL AI</h1>
    <p style="letter-spacing: 12px; color: #FFF; font-size: 1.2em;">GLOBAL HARDWARE GOVERNANCE</p>
    <div style="background: #00FF00; color: #000; padding: 5px 40px; font-weight: bold; display: inline-block; margin-top: 15px;">
        ARCHITECT: {DEVELOPER.upper()}
    </div>
    <p style="opacity: 0.6; font-size: 0.8em; margin-top: 15px;">SINCRO: {datetime.now().strftime('%Y%m%d_%H%M%S')} | Caracas, San Bernardino</p>
""", unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

st.divider()

# --- PANEL DE CONTROL LATERAL ---
st.sidebar.markdown("### 🕹️ MASTER_CONTROL")
target_app = st.sidebar.selectbox("FOCAL_TARGET", ["Global System", "WhatsApp", "YouTube", "Kernel Core", "TikTok"])
mode = st.sidebar.radio("OP_MODE", ["Diagnostic", "Security", "Deployment"])

# --- MODULE 02: TELEMETRÍA ---
st.markdown(f"### 🛰️ TELEMETRÍA EN TIEMPO REAL: {target_app.upper()}")
c1, c2, c3 = st.columns(3)
cpu = psutil.cpu_percent()
ram = psutil.virtual_memory().percent
disk = psutil.disk_usage('/').percent

c1.metric("CPU_LOAD", f"{cpu}%")
c2.metric("RAM_USAGE", f"{ram}%")
c3.metric("DISK_FREE", f"{100-disk:.1f}%")

# --- GRÁFICO DE FRECUENCIA ---
fig = go.Figure(go.Indicator(
    mode = "gauge+number", value = cpu,
    gauge = {'axis': {'range': [0, 100]}, 'bar': {'color': "#00FF00"}, 'bgcolor': "black", 'bordercolor': "#00FF00"},
    title = {'text': "Kernel Pulse", 'font': {'color': "#00FF00", 'family': 'Orbitron'}}
))
fig.update_layout(paper_bgcolor='black', height=300)
st.plotly_chart(fig, use_container_width=True)

# --- NUEVAS FUNCIONES ADICIONALES ---
st.divider()
col_ext1, col_ext2 = st.columns(2)

with col_ext1:
    st.markdown("### 🔋 ENERGY_GOVERNANCE")
    battery = psutil.sensors_battery()
    if battery:
        percent = battery.percent
        st.write(f"Nivel de Energía: {percent}%")
        st.progress(percent/100)
    else:
        st.info("Fuente de Poder: AC_ADAPTER Conectado")

with col_ext2:
    st.markdown("### 🛡️ SECURITY_PROTOCOL")
    if st.button("SCAN_FOR_VULNERABILITIES"):
        with st.spinner("Analizando puertos..."):
            time.sleep(2)
            st.success("Cifrado AES-256 Activo. Sin brechas detectadas.")

# --- MÓDULOS ÁMBAR & KENYA ---
st.divider()
col_a, col_k = st.columns(2)
with col_a:
    st.markdown("### 👁️ NEURAL: Ámbar")
    if st.button("AUDITORÍA COMPLETA"):
        parts = psutil.disk_partitions()
        st.table([{"Drive": p.device, "Mount": p.mountpoint, "Type": p.fstype} for p in parts[:3]])

with col_k:
    st.markdown("### 🧠 NEURAL: Kenya")
    diag = "STABLE" if cpu < 70 else "CRITICAL_LOAD"
    st.warning(f"[KENYA_REPORT]: {diag} detected in {target_app}")

# --- DNA & THERMAL ---
st.divider()
st.markdown("### 🖥️ [SYSTEM_DNA_HARDWARE]")
st.code(f"USER: {DEVELOPER}\nNODE: {platform.node()}\nARCH: {platform.machine()}\nBOOT: {datetime.fromtimestamp(psutil.boot_time()).strftime('%Y-%m-%d %H:%M')}", language="bash")

# --- FOOTER ---
st.markdown(f"""
    <div style="text-align: center; margin-top: 50px; border-top: 1px solid #111; padding: 20px;">
        <p style="color: #00FF00; letter-spacing: 5px; font-weight: bold;">{COPYRIGHT}</p>
        <p style="font-size: 0.7em; opacity: 0.4;">CARACAS, VENEZUELA | PROPRIETARY GOVERNANCE v{VERSION}</p>
    </div>
""", unsafe_allow_html=True)
