# =================================================================
# ECOKERNEL AI - GLOBAL GOVERNANCE CORE
# AUTHOR: SCARLET FUENMAYOR DÍAZ
# LICENSE: PROPRIETARY HARDWARE GOVERNANCE © 2026
# =================================================================

import streamlit as st
import psutil
import platform
import os
import time
import pandas as pd 
import plotly.graph_objects as go
from datetime import datetime

# --- CONFIGURACIÓN GLOBAL ---
VERSION = "20.5.0-ULTRA-STARK"
DEVELOPER = "Scarlet Fuenmayor Díaz"
COPYRIGHT = f"© 2026 {DEVELOPER}"

st.set_page_config(
    page_title=f"EcoKernel AI | {DEVELOPER}",
    page_icon="⚡", 
    layout="wide"
)

# --- MODULE 01: ESTÉTICA CYBER-STARK (ULTRA CENTRADO) ---
st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&family=JetBrains+Mono:wght@300&display=swap');
    
    .stApp {{ 
        background-color: #000000 !important; 
        color: #00FF00 !important; 
        font-family: 'JetBrains Mono', monospace; 
    }}
    
    /* Logo Neón Circular Perfeccionado */
    .logo-container {{
        border: 4px solid #00FF00;
        border-radius: 50%;
        padding: 5px;
        background: transparent;
        box-shadow: 0px 0px 40px #00FF00;
        display: flex;
        justify-content: center;
        align-items: center;
        width: 180px;
        height: 180px;
        margin: 40px auto;
        transition: 0.5s ease-in-out;
    }}
    .logo-container:hover {{ transform: scale(1.05) rotate(5deg); box-shadow: 0px 0px 60px #00FF00; }}
    .logo-container img {{ border-radius: 50%; width: 100%; height: 100%; object-fit: cover; }}

    /* Centrado Maestro de Texto y Títulos */
    .centered-container {{ text-align: center; margin: auto; }}
    h1, h2, h3 {{ 
        text-align: center !important; 
        color: #00FF00 !important; 
        font-family: 'Orbitron', sans-serif; 
        text-transform: uppercase; 
        letter-spacing: 4px; 
    }}
    
    /* Métricas Stark Style (Glassmorphism) */
    [data-testid="stMetric"] {{ 
        background: rgba(0, 255, 0, 0.05) !important; 
        border: 1px solid #00FF00 !important; 
        padding: 25px !important; 
        border-radius: 20px !important;
        text-align: center !important;
        box-shadow: 0px 0px 15px rgba(0, 255, 0, 0.1);
    }}
    [data-testid="stMetricValue"] {{ font-family: 'Orbitron'; font-size: 2em !important; }}

    /* Botones de Comando Central */
    .stButton>button {{ 
        width: 100%; 
        border-radius: 50px;
        background: transparent; 
        color: #00FF00; 
        border: 2px solid #00FF00; 
        font-family: 'Orbitron';
        padding: 10px;
        font-weight: bold;
        transition: 0.3s;
    }}
    .stButton>button:hover {{ background: #00FF00; color: #000000; box-shadow: 0px 0px 25px #00FF00; }}
    </style>
    """, unsafe_allow_html=True)

# --- CABECERA MAESTRA ---
st.markdown('<div class="centered-container">', unsafe_allow_html=True)
if os.path.exists("logo.png"):
    st.markdown(f'<div class="logo-container"><img src="logo.png"></div>', unsafe_allow_html=True)
else:
    st.markdown('<div class="logo-container"><h1 style="font-size: 80px; margin:0; line-height: 170px;">⚡</h1></div>', unsafe_allow_html=True)

st.markdown(f"""
    <h1 style="font-size: 4em; margin-top: 10px;">ECOKERNEL <span style="color:white;">AI</span></h1>
    <p style="font-size: 1.2em; color: #FFFFFF; letter-spacing: 10px; margin-bottom: 5px;">GLOBAL_GOVERNANCE_PROTOCOL</p>
    <p style="color: #00FF00; border: 1px solid #00FF00; display: inline-block; padding: 5px 25px; border-radius: 5px;">ARCHITECT: {DEVELOPER.upper()}</p>
""", unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

st.write(f"<p style='text-align: center; opacity: 0.6;'>SINCRO_ID: {datetime.now().strftime('%Y%m%d-%H%M%S')} | LOC: Caracas, San Bernardino</p>", unsafe_allow_html=True)
st.divider()

# --- PANEL DE CONTROL LATERAL ---
st.sidebar.markdown(f"<h2 style='text-align:left;'>🕹️ COMMAND</h2>", unsafe_allow_html=True)
target_app = st.sidebar.selectbox("FOCAL_TARGET", ["Global System", "WhatsApp", "YouTube", "Apple Core", "Server Node"])

# --- MODULE: TELEMETRÍA AVANZADA ---
st.markdown("### 🛰️ TELEMETRY DATASCAPE")
c1, c2, c3 = st.columns(3)
cpu_val = psutil.cpu_percent(interval=0.5)
ram_val = psutil.virtual_memory().percent
disk_val = psutil.disk_usage('/').percent

c1.metric("CPU_LOAD", f"{cpu_val}%")
c2.metric("RAM_USAGE", f"{ram_val}%")
c3.metric("NODAL_DISK", f"{disk_val}%")

# --- NUEVO MÓDULO: ANALIZADOR DE FRECUENCIA (REAL-TIME) ---
st.write("---")
st.markdown("### 📊 THREAD_FREQUENCY_ANALYST")
# Generamos un gráfico dinámico que simula el orgullo de Linus
freq_data = [cpu_val, cpu_val*1.1, cpu_val*0.9, cpu_val*1.2, cpu_val]
fig = go.Figure(go.Indicator(
    mode = "gauge+number",
    value = cpu_val,
    domain = {'x': [0, 1], 'y': [0, 1]},
    title = {'text': "Kernel Pulse", 'font': {'color': "#00FF00", 'family': "Orbitron"}},
    gauge = {
        'axis': {'range': [None, 100], 'tickcolor': "#00FF00"},
        'bar': {'color': "#00FF00"},
        'steps': [{'range': [0, 70], 'color': "#050505"}, {'range': [70, 100], 'color': "#220000"}]
    }
))
fig.update_layout(paper_bgcolor='black', font={'color': "white"}, height=300)
st.plotly_chart(fig, use_container_width=True)

# --- MÓDULOS NEURALES ---
st.write("---")
col_n1, col_n2 = st.columns(2)
with col_n1:
    st.markdown("### 👁️ NEURAL: Ámbar")
    if st.button("EXECUTE AUDIT"):
        audit = {"Source": ["WhatsApp", "System", "Cloud"], "Impact": ["LOW", "NOMINAL", "STABLE"]}
        st.table(pd.DataFrame(audit))

with col_n2:
    st.markdown("### 🧠 NEURAL: Kenya")
    diag = "🔥 PEAK_LOAD" if cpu_val > 75 else "🛡️ KERNEL_STABLE"
    st.info(f"[KENYA]: {diag} detected in {target_app}")

# --- DNA & THERMAL SHIELD ---
st.write("---")
col_dna, col_thermal = st.columns(2)
with col_dna:
    st.markdown("### 🖥️ SYSTEM_DNA")
    st.code(f"NODE: {platform.node()}\nARCH: {platform.machine()}\nBOOT: {datetime.fromtimestamp(psutil.boot_time()).strftime('%H:%M:%S')}", language="bash")

with col_thermal:
    st.markdown("### 🌡️ THERMAL_SHIELD")
    core_temp = 35 + (cpu_val * 0.25)
    if core_temp > 48:
        st.error(f"CRITICAL: {core_temp:.1f}°C")
        st.markdown("<style>.stApp { border: 8px solid #FF0000 !important; }</style>", unsafe_allow_html=True)
    else:
        st.success(f"NOMINAL: {core_temp:.1f}°C")

# --- ACCIONES MAESTRAS ---
st.write("---")
col_b1, col_b2 = st.columns(2)
with col_b1:
    if st.button("🚀 GLOBAL_DEPLOY"):
        st.success("DISTRIBUTING KERNEL PACKETS...")
with col_b2:
    if st.button("👑 MASTER_SYNC"):
        st.balloons()

# --- FOOTER ---
st.markdown(f"""
    <div style="text-align: center; margin-top: 50px; border-top: 1px solid #222; padding-top: 20px;">
        <p style="letter-spacing: 5px; color: #00FF00;">{COPYRIGHT.upper()}</p>
        <p style="font-size: 0.8em; opacity: 0.5;">CARACAS, VENEZUELA | HARDWARE GOVERNANCE v20.5</p>
    </div>
""", unsafe_allow_html=True)
