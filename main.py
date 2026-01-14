# =================================================================
# ECOKERNEL AI - GLOBAL GOVERNANCE CORE (GITHUB MASTER)
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
VERSION = "20.7.0-STARK-PREMIUM"
DEVELOPER = "Scarlet Fuenmayor Díaz"
COPYRIGHT = f"© 2026 {DEVELOPER}"

st.set_page_config(
    page_title=f"EcoKernel AI | {DEVELOPER}",
    page_icon="⚡", 
    layout="wide"
)

# --- MODULE 01: ESTÉTICA CYBER-STARK (ULTRA-CENTRADO DINÁMICO) ---
st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&family=JetBrains+Mono:wght@300&display=swap');
    
    .stApp {{ 
        background-color: #000000 !important; 
        color: #00FF00 !important; 
        font-family: 'JetBrains Mono', monospace; 
    }}
    
    /* Marco Neón Circular Proyectado */
    .logo-container {{
        border: 5px solid #00FF00;
        border-radius: 50%;
        padding: 8px;
        background: radial-gradient(circle, rgba(0,255,0,0.1) 0%, rgba(0,0,0,1) 70%);
        box-shadow: 0px 0px 50px #00FF00, inset 0px 0px 20px #00FF00;
        display: flex;
        justify-content: center;
        align-items: center;
        width: 190px;
        height: 190px;
        margin: 40px auto;
        transition: 0.4s all ease;
    }}
    .logo-container:hover {{ transform: scale(1.08); box-shadow: 0px 0px 70px #00FF00; }}
    .logo-container img {{ border-radius: 50%; width: 100%; height: 100%; object-fit: cover; }}

    /* Centrado Maestro Stark */
    .centered-content {{ text-align: center !important; width: 100%; }}
    h1, h2, h3, p, .stMarkdown {{ text-align: center !important; }}
    
    h1 {{ 
        color: #00FF00 !important; 
        font-family: 'Orbitron', sans-serif; 
        text-transform: uppercase; 
        letter-spacing: 6px;
        text-shadow: 0px 0px 10px #00FF00;
    }}
    
    /* Metrics Glass-Effect */
    [data-testid="stMetric"] {{ 
        background: rgba(0, 255, 0, 0.03) !important; 
        border: 2px solid #00FF00 !important; 
        padding: 25px !important; 
        border-radius: 25px !important;
        box-shadow: 0px 10px 20px rgba(0, 0, 0, 0.5);
    }}
    
    [data-testid="stMetricLabel"] {{ color: #FFFFFF !important; font-size: 1.1em !important; }}
    [data-testid="stMetricValue"] {{ font-family: 'Orbitron'; color: #00FF00 !important; font-weight: bold; }}

    /* Botones Propietarios */
    .stButton>button {{ 
        width: 100%; 
        border-radius: 10px;
        background: linear-gradient(45deg, #000, #050505); 
        color: #00FF00; 
        border: 2px solid #00FF00; 
        font-family: 'Orbitron';
        padding: 15px;
        letter-spacing: 2px;
        transition: 0.3s;
    }}
    .stButton>button:hover {{ background: #00FF00; color: #000; font-weight: bold; box-shadow: 0px 0px 40px #00FF00; }}
    </style>
    """, unsafe_allow_html=True)

# --- CABECERA MAESTRA (LOGO & IDENTITY) ---
st.markdown('<div class="centered-content">', unsafe_allow_html=True)
if os.path.exists("logo.png"):
    st.markdown(f'<div class="logo-container"><img src="logo.png"></div>', unsafe_allow_html=True)
else:
    st.markdown('<div class="logo-container"><h1 style="font-size: 90px; margin:0; line-height: 190px;">⚡</h1></div>', unsafe_allow_html=True)

st.markdown(f"""
    <h1 style="font-size: 3.8em; margin-top: 10px;">ECOKERNEL <span style="color:#FFF;">AI</span></h1>
    <p style="font-size: 1.3em; color: #AAA; letter-spacing: 15px; margin-bottom: 5px;">HARDWARE_GOVERNANCE_v20</p>
    <div style="background: #00FF00; color: black; display: inline-block; padding: 2px 30px; font-weight: bold; font-family: 'Orbitron'; margin-bottom: 20px;">
        {DEVELOPER.upper()}
    </div>
    <p style="opacity: 0.5;">SINCRO_DATA: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} | Caracas, San Bernardino</p>
""", unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

st.divider()

# --- PANEL DE COMANDO ---
st.sidebar.markdown("### 🕹️ MASTER_CONTROL")
target_app = st.sidebar.selectbox("FOCAL_MONITOR", ["Global System", "WhatsApp", "YouTube", "TikTok", "Chrome", "Spotify"])
refresh = st.sidebar.select_slider("SCAN_SPEED", options=["LOW", "MED", "STARK"], value="MED")

# --- MODULE 02: TELEMETRÍA DE ALTO IMPACTO ---
st.markdown("### 🛰️ [TELEMETRY_DATASCAPE]")
c1, c2, c3 = st.columns(3)
cpu_val = psutil.cpu_percent(interval=0.5)
ram_val = psutil.virtual_memory().percent
disk_val = psutil.disk_usage('/').percent

c1.metric(f"CPU: {target_app}", f"{cpu_val}%")
c2.metric("MEMORY_LOAD", f"{ram_val}%")
c3.metric("STORAGE_STATUS", f"{disk_val}%")

# --- ANALIZADOR DE PULSO NEURAL ---
st.write("---")
st.markdown("### 📊 [NEURAL_PULSE_FREQUENCY]")
fig = go.Figure(go.Indicator(
    mode = "gauge+number+delta",
    value = cpu_val,
    delta = {'reference': 50, 'relative': True, 'increasing': {'color': "red"}},
    gauge = {
        'axis': {'range': [None, 100], 'tickwidth': 1, 'tickcolor': "#00FF00"},
        'bar': {'color': "#00FF00"},
        'bgcolor': "rgba(0,0,0,0)",
        'borderwidth': 2,
        'bordercolor': "#00FF00",
        'steps': [{'range': [0, 100], 'color': 'rgba(0,0,0,0)'}],
        'threshold': {'line': {'color': "red", 'width': 4}, 'thickness': 0.75, 'value': 90}
    }
))
fig.update_layout(paper_bgcolor='black', font={'color': "#00FF00", 'family': "Orbitron"}, height=300, margin=dict(t=0, b=0))
st.plotly_chart(fig, use_container_width=True)

# --- MÓDULOS DE GOBERNANZA (ÁMBAR & KENYA) ---
st.write("---")
col_n1, col_n2 = st.columns(2)
with col_n1:
    st.markdown("### 👁️ NEURAL: Ámbar")
    st.caption("ANÁLISIS DE PARTICIONES Y CACHÉ")
    if st.button("RUN_STORAGE_AUDIT"):
        parts = psutil.disk_partitions()
        audit_data = []
        for p in parts[:4]:
            try:
                usage = psutil.disk_usage(p.mountpoint)
                audit_data.append({"Mount": p.mountpoint, "Total": f"{usage.total // (1024**3)}GB", "Usage": f"{usage.percent}%"})
            except: continue
        st.dataframe(pd.DataFrame(audit_data), use_container_width=True)

with col_n2:
    st.markdown("### 🧠 NEURAL: Kenya")
    st.caption("DIAGNÓSTICO DE HILOS Y PRIORIDAD")
    diag = "🔥 PEAK_REACHED" if cpu_val > 80 else "🛡️ KERNEL_STABLE"
    st.info(f"[KENYA_REPORT]: {diag} - Sincronización activa en {target_app}")

# --- DNA & THERMAL MONITOR ---
st.write("---")
cdna, ctherm = st.columns(2)
with cdna:
    st.markdown("### 🖥️ [SYSTEM_DNA]")
    st.code(f"ID: {platform.node()}\nARCH: {platform.machine()}\nKERNEL: {platform.system()}", language="bash")

with ctherm:
    st.markdown("### 🌡️ [THERMAL_SHIELD]")
    temp_sim = 35 + (cpu_val * 0.3)
    if temp_sim > 50:
        st.error(f"WARNING: {temp_sim:.1f}°C - OVERHEATING")
        st.markdown("<style>.stApp { border: 10px solid #FF0000 !important; }</style>", unsafe_allow_html=True)
    else:
        st.success(f"STABLE: {temp_sim:.1f}°C")

# --- ACCIONES DE ÉLITE ---
st.write("---")
if st.button("🚀 DEPLOY GLOBAL ARCHITECTURE"):
    with st.spinner("Sincronizando con el Núcleo Stark..."):
        time.sleep(2)
        st.balloons()
        st.success("SISTEMA ECOKERNEL AI DESPLEGADO CON ÉXITO")

# --- FOOTER ---
st.write("---")
st.markdown(f"""
    <div class="centered-content">
        <p style="color: #00FF00; letter-spacing: 5px; font-weight: bold; font-family: 'Orbitron';">{COPYRIGHT}</p>
        <p style="font-size: 0.8em; opacity: 0.6;">CARACAS, VENEZUELA | PROTOTYPE v{VERSION}</p>
        <p style="font-size: 0.7em; opacity: 0.4;">Authorized access only. Hardware Governance Active.</p>
    </div>
""", unsafe_allow_html=True)
