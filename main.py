# =================================================================
# ECOKERNEL AI - CORE GOVERNANCE (TERMUX MODULAR EDITION)
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
from datetime import datetime

# --- CONFIGURACIÓN DE RUTAS Y ENTORNO ---
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODULES_DIR = os.path.join(BASE_DIR, "modules")

if not os.path.exists(MODULES_DIR):
    os.makedirs(MODULES_DIR)

# --- GLOBAL CONFIG ---
VERSION = "25.0.0-STARK-TERMUX"
DEVELOPER = "Scarlet Fuenmayor Díaz"
COPYRIGHT = f"© 2026 {DEVELOPER}"

st.set_page_config(page_title=f"EcoKernel AI | {VERSION}", page_icon="⚡", layout="wide")

# --- PROCESAMIENTO DE LOGO ---
def get_base64_logo(path):
    if os.path.exists(path):
        with open(path, "rb") as f:
            return base64.b64encode(f.read()).decode()
    return None

logo_b64 = get_base64_logo(os.path.join(BASE_DIR, "logo.png"))

# --- ESTÉTICA CYBER-SQUARE (CSS AJUSTADO) ---
st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&family=JetBrains+Mono&display=swap');
    
    .stApp {{ 
        background-color: #000000 !important; 
        color: #00FF00 !important; 
        font-family: 'JetBrains Mono', monospace; 
    }}

    /* MARCO CUADRADO NEÓN PARA LOGO */
    .stark-square-logo {{
        width: 180px;
        height: 180px;
        border: 3px solid #00FF00;
        box-shadow: 0px 0px 25px rgba(0, 255, 0, 0.6);
        display: flex;
        justify-content: center;
        align-items: center;
        margin: 0 auto 20px auto;
        background: #050505;
    }}
    .stark-square-logo img {{
        max-width: 90%;
        max-height: 90%;
        object-fit: contain;
    }}

    h1, h2, h3 {{ font-family: 'Orbitron', sans-serif !important; text-transform: uppercase; }}
    
    .stMetric {{ 
        border: 1px solid #00FF00 !important; 
        background: rgba(0, 255, 0, 0.03) !important;
        padding: 15px !important;
    }}
    </style>
    """, unsafe_allow_html=True)

# --- CABECERA DE GOBERNANZA ---
with st.container():
    if logo_b64:
        st.markdown(f'<div class="stark-square-logo"><img src="data:image/png;base64,{logo_b64}"></div>', unsafe_allow_html=True)
    else:
        st.markdown('<div class="stark-square-logo"><h1 style="font-size: 60px;">⚡</h1></div>', unsafe_allow_html=True)
    
    st.markdown(f"<h1 style='text-align: center; font-size: 3em; margin-bottom:0;'>ECOKERNEL AI</h1>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align: center; letter-spacing: 5px;'>DEVELOPER: {DEVELOPER.upper()}</p>", unsafe_allow_html=True)

st.write("---")

# --- SIDEBAR: TERMUX CONTROL HUB ---
st.sidebar.title("🕹️ TERMINAL CONTROL")
app_monitor = st.sidebar.selectbox("SELECCIONAR APP MONITOR:", ["WhatsApp", "Instagram", "Kernel Server", "Python Process"])
storage_target = st.sidebar.radio("DATA SOURCE:", ["INTERNAL_STORAGE", "EXTERNAL_SD", "VIRTUAL_CACHE"])

if st.sidebar.button("FORCE REFRESH"):
    st.rerun()

# --- MÓDULO 01: TELEMETRÍA DINÁMICA ---
c1, c2, c3, c4 = st.columns(4)
cpu = psutil.cpu_percent()
ram = psutil.virtual_memory().percent
disk = psutil.disk_usage('/')
net = psutil.net_io_counters()

c1.metric("CPU_STARK", f"{cpu}%")
c2.metric("RAM_CORE", f"{ram}%")
c3.metric("DISK_ALLOC", f"{disk.percent}%")
c4.metric("NET_TRAFFIC", f"{net.bytes_sent // (1024**2)}MB")

# --- MÓDULO 02: GESTIÓN DE CARPETAS (MODULAR) ---
st.write("---")
st.subheader("📁 DIRECTORY_MODULES_SCANNER")
mods = [f for f in os.listdir(MODULES_DIR) if f.endswith('.py')]

if mods:
    col_list = st.columns(len(mods) if len(mods) < 5 else 4)
    for i, m in enumerate(mods):
        col_list[i % 4].success(f"📦 MOD: {m}")
else:
    st.info("Directorio /modules vacío. Esperando despliegue de archivos desde Termux...")

# --- MÓDULO 03: PUNTOS DE TRABAJO (ÁMBAR & KENYA) ---
st.write("---")
col_a, col_k = st.columns(2)

with col_a:
    st.markdown("### 👁️ NEURAL: Ámbar")
    st.caption(f"Target: {storage_target}")
    if st.button("EXECUTE STORAGE SCAN"):
        # Data real del almacenamiento para Benelope
        data = {
            "Partición": ["Root", "Data", "Cache"],
            "Capacidad": [f"{disk.total // (1024**3)}GB", "N/A", "N/A"],
            "Uso": [f"{disk.used // (1024**3)}GB", "Scanning...", "Cleaning..."]
        }
        st.table(pd.DataFrame(data))

with col_k:
    st.markdown("### 🧠 NEURAL: Kenya")
    st.caption(f"Vigilando: {app_monitor}")
    # Gráfico de monitoreo que cambia según la app
    chart_data = pd.DataFrame(psutil.cpu_percent(percpu=True), columns=['CPU_CORE_LOAD'])
    st.bar_chart(chart_data)
    st.info(f"Estado de {app_monitor}: NOMINAL")

# --- MÓDULO 04: KERNEL DNA ---
st.write("---")
with st.expander("🔍 VIEW SYSTEM DNA REPORT"):
    st.code(f"""
    NODE_ID: {platform.node()}
    DISTRO: {platform.system()} {platform.release()}
    ARCH: {platform.machine()}
    KERNEL_TIME: {datetime.now().strftime('%H:%M:%S')}
    LOCATION: Caracas, San Bernardino
    """, language="bash")

# --- FOOTER ---
st.markdown(f"""
    <div style="text-align: center; padding: 30px; border-top: 1px solid #00FF00; margin-top: 50px; opacity: 0.7;">
        {COPYRIGHT}<br>
        <small>HARDWARE GOVERNANCE PROTOCOL ACTIVE | TERMUX-BRIDGE STABLE</small>
    </div>
""", unsafe_allow_html=True)
