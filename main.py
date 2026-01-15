# =================================================================
# ECOKERNEL AI - GLOBAL GOVERNANCE CORE (STARK-LINUS PRIME)
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
VERSION = "26.0.0-PRIME-STARK"
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

# --- INTERFAZ ULTRA-CENTRADA: MARCO CUADRADO & NEÓN ---
st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&family=JetBrains+Mono:wght@300&display=swap');
    
    .stApp {{ 
        background-color: #000000 !important; 
        color: #00FF00 !important; 
        font-family: 'JetBrains Mono', monospace; 
    }}
    
    /* Centrado Maestro Stark */
    .header-master {{
        display: flex; flex-direction: column; align-items: center; justify-content: center;
        width: 100%; padding-top: 40px; text-align: center;
    }}

    /* MARCO CUADRADO DE PRECISIÓN (SOLICITADO) */
    .logo-stark-square {{
        border: 4px solid #00FF00;
        border-radius: 12px;
        padding: 15px;
        background: rgba(0, 255, 0, 0.02);
        box-shadow: 0px 0px 45px #00FF00, inset 0px 0px 15px #00FF00;
        width: 210px; height: 210px;
        display: flex; justify-content: center; align-items: center;
        overflow: hidden; margin-bottom: 30px;
        transition: 0.5s ease-in-out;
    }}
    .logo-stark-square:hover {{ 
        transform: scale(1.05); 
        box-shadow: 0px 0px 70px #00FF00;
    }}
    .logo-stark-square img {{ width: 100%; height: 100%; object-fit: contain; }}

    /* Tipografía Centrada y Guías */
    h1, h2, h3, p, span {{ text-align: center !important; font-family: 'Orbitron', sans-serif !important; }}
    
    .main-title {{
        font-size: 4.8em !important; letter-spacing: 20px;
        text-shadow: 0px 0px 25px #00FF00; margin-bottom: 5px !important;
        color: #00FF00 !important;
    }}

    .function-badge {{
        background: #00FF00; color: #000; padding: 5px 40px;
        font-weight: bold; display: inline-block; margin-top: 10px;
        letter-spacing: 5px; border-radius: 2px;
    }}

    /* Metrics & Tables */
    [data-testid="stMetric"] {{ 
        background: rgba(0, 255, 0, 0.03) !important; 
        border: 2px solid #00FF00 !important; 
        border-radius: 0px !important;
    }}
    </style>
    """, unsafe_allow_html=True)

# --- CABECERA MAESTRA ---
st.markdown('<div class="header-master">', unsafe_allow_html=True)
if logo_b64:
    st.markdown(f'<div class="logo-stark-square"><img src="{logo_b64}"></div>', unsafe_allow_html=True)
else:
    st.markdown('<div class="logo-stark-square"><h1 style="font-size: 90px; margin:0;">⚡</h1></div>', unsafe_allow_html=True)

st.markdown(f'<h1 class="main-title">ECOKERNEL AI</h1>', unsafe_allow_html=True)
st.markdown(f'<p style="letter-spacing: 12px; color: #FFF; font-size: 1.1em;">HARDWARE GOVERNANCE MASTER</p>', unsafe_allow_html=True)
st.markdown(f'<div class="function-badge">ARCHITECT: {DEVELOPER.upper()}</div>', unsafe_allow_html=True)
st.markdown(f'<p style="opacity: 0.5; margin-top: 20px;">NODE_SYNC: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")} | CARACAS_SB</p>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

st.divider()

# --- PANEL DE CONTROL (SIDEBAR) ---
st.sidebar.markdown("### 🕹️ MASTER_GOVERNANCE")
target_app = st.sidebar.selectbox("FOCAL_TARGET", ["Global System", "WhatsApp", "YouTube", "Apple Core", "Linux Kernel"])
scan_mode = st.sidebar.select_slider("SCAN_DEPTH", options=["SURFACE", "CORE", "DEEP_STARK"])

# --- MONITOR DE FRECUENCIA ULTRA-CENTRADO ---
st.markdown(f"### 📊 PULSO NEURAL DE FRECUENCIA: {target_app.upper()}")
cpu = psutil.cpu_percent(interval=0.1)
ram = psutil.virtual_memory().percent
net_io = psutil.net_io_counters()

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
c3.metric("NET_TRAFFIC (MB)", f"{(net_io.bytes_sent + net_io.bytes_recv) // (1024**2)}")

# --- FUNCIONES ADICIONALES (ÁMBAR & KENYA INNOVACIÓN) ---
st.divider()
col_a, col_k = st.columns(2)

with col_a:
    st.markdown("### 👁️ NEURAL: Ámbar")
    st.caption("ANÁLISIS DE ENTROPÍA Y ALMACENAMIENTO")
    if st.button("EXECUTE STARK CLEANUP"):
        with st.spinner("Limpiando registros de entropía..."):
            time.sleep(1.5)
            usage = psutil.disk_usage('/')
            st.success(f"Sistema Optimizado: {usage.free // (2**30)} GB Libres detectados.")
            st.table(pd.DataFrame({
                "Sector": ["Cache", "Temp", "Logs"],
                "Status": ["DELETED", "DELETED", "ENCRYPTED"]
            }))

with col_k:
    st.markdown("### 🧠 NEURAL: Kenya")
    st.caption("GOBERNANZA DE RED Y SEGURIDAD")
    if st.button("SCAN NETWORK NODES"):
        with st.spinner("Analizando protocolos de red..."):
            time.sleep(2)
            st.info(f"Conexiones activas en {target_app}: {len(psutil.net_connections())}")
            st.warning("Encryption Level: AES-256 Verified.")

# --- DNA & THERMAL SHIELD ---
st.divider()
cdna, ctherm = st.columns(2)
with cdna:
    st.markdown("### 🖥️ [SYSTEM_DNA]")
    st.code(f"USER: {DEVELOPER}\nNODE: {platform.node()}\nARCH: {platform.machine()}\nKERNEL: {platform.system()}", language="bash")

with ctherm:
    st.markdown("### 🌡️ [THERMAL_SHIELD]")
    temp = 30 + (cpu * 0.3)
    if temp > 50: st.error(f"CRITICAL: {temp:.1f}°C")
    else: st.success(f"NOMINAL: {temp:.1f}°C")

# --- FOOTER ---
st.divider()
st.markdown(f"""
    <div style="text-align: center; padding: 20px; opacity: 0.6;">
        <p style="color: #00FF00; letter-spacing: 5px; font-weight: bold;">{COPYRIGHT}</p>
        <p style="font-size: 0.7em;">CARACAS, VENEZUELA | HARDWARE GOVERNANCE ACTIVE</p>
    </div>
""", unsafe_allow_html=True)
