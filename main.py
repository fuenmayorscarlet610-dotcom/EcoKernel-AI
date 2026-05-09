# =================================================================
# ECOKERNEL AI - CORE GOVERNANCE (HYBRID STARK-TORVALDS EDITION)
# AUTHOR: SCARLET FUENMAYOR DÍAZ
# LICENSE: PROPRIETARY HARDWARE GOVERNANCE © 2026
# =================================================================

import streamlit as st
import psutil
import platform
import os
import base64
import pandas as pd
from datetime import datetime

# --- CONFIGURACIÓN DE ENTORNO ---
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODULES_DIR = os.path.join(BASE_DIR, "modules")
if not os.path.exists(MODULES_DIR): os.makedirs(MODULES_DIR)

# --- GLOBAL CONFIG ---
VERSION = "26.1.0-STARK-LINUX"
DEVELOPER = "Scarlet Fuenmayor Díaz"
COPYRIGHT = f"© 2026 {DEVELOPER}"

st.set_page_config(page_title=f"EcoKernel AI | {VERSION}", page_icon="🧬", layout="wide")

# --- PROCESAMIENTO DE LOGO ---
def get_base64_logo(path):
    if os.path.exists(path):
        try:
            with open(path, "rb") as f:
                return base64.b64encode(f.read()).decode()
        except: return None
    return None

logo_b64 = get_base64_logo(os.path.join(BASE_DIR, "logo.png"))

# --- ESTÉTICA SOFISTICADA: STARK INDUSTRIES MEETS LINUX KERNEL ---
st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&family=Fira+Code:wght@300;500&family=Rajdhani:wght@500;700&display=swap');
    
    .stApp {{
        background-color: #020202 !important;
        background-image: radial-gradient(circle at 50% 50%, #001a1a 0%, #020202 100%);
        color: #00e5ff !important;
        font-family: 'Fira Code', monospace;
    }}

    /* Panel de Identidad Stark */
    .stark-header {{
        border-left: 5px solid #ff0055;
        padding: 20px;
        margin-bottom: 30px;
        background: linear-gradient(90deg, rgba(255, 0, 85, 0.1) 0%, transparent 100%);
        box-shadow: -10px 0px 20px rgba(255, 0, 85, 0.2);
    }}

    /* HUD Metrics */
    [data-testid="stMetricValue"] {{
        font-family: 'Orbitron', sans-serif !important;
        color: #ffffff !important;
        text-shadow: 0 0 15px #00e5ff, 0 0 30px #00e5ff;
    }}
    
    .stMetric {{
        border: 1px solid rgba(0, 229, 255, 0.2) !important;
        background: rgba(0, 0, 0, 0.6) !important;
        border-radius: 0px !important;
        backdrop-filter: blur(10px);
        transition: 0.5s;
    }}
    .stMetric:hover {{ border-color: #ff0055 !important; transform: scale(1.02); }}

    /* Sidebar Estilo Consola */
    [data-testid="stSidebar"] {{
        background-color: #000000 !important;
        border-right: 1px solid #ff0055;
    }}

    /* Botones de Comando */
    .stButton>button {{
        border-radius: 0px !important;
        border: 1px solid #00e5ff !important;
        background: transparent !important;
        color: #00e5ff !important;
        font-family: 'Orbitron', sans-serif;
        letter-spacing: 2px;
    }}
    .stButton>button:hover {{
        background: #00e5ff !important;
        color: #000 !important;
        box-shadow: 0 0 25px #00e5ff;
    }}
    </style>
    """, unsafe_allow_html=True)

# --- CABECERA ---
with st.container():
    st.markdown(f"""
    <div class="stark-header">
        <h1 style='margin:0; font-family: Orbitron; font-size: 3.5em; color: #ffffff;'>ECOKERNEL_AI <span style='color:#ff0055;'>v{VERSION}</span></h1>
        <p style='letter-spacing: 5px; color: #00e5ff; font-family: Rajdhani;'>[ AUTH_OPERATOR: {DEVELOPER.upper()} // STATUS: ACTIVE ]</p>
    </div>
    """, unsafe_allow_html=True)

# --- MÓDULO 01: TELEMETRÍA DE ALTA PRECISIÓN ---
st.markdown("### 📡 LIVE_CORE_FEED")
c1, c2, c3, c4 = st.columns(4)

def fetch_data(func, attr=None):
    try:
        val = func()
        return getattr(val, attr) if attr else val
    except: return "LOCKED"

cpu = fetch_data(psutil.cpu_percent)
ram = fetch_data(psutil.virtual_memory, 'percent')
disk = fetch_data(lambda: psutil.disk_usage('/'), 'percent')
net = fetch_data(psutil.net_io_counters, 'bytes_sent')

c1.metric("CPU_ANALYSIS", f"{cpu}%" if cpu != "LOCKED" else "[PROTECTED]")
c2.metric("MEM_SYNC", f"{ram}%" if ram != "LOCKED" else "[PROTECTED]")
c3.metric("STORAGE_LINK", f"{disk}%" if disk != "LOCKED" else "[RESTRIC]")
c4.metric("UPLINK_TRAFFIC", f"{net // (1024**2)}MB" if net != "LOCKED" else "0MB")

st.write("---")

# --- MÓDULO 02: KERNEL DNA & NEURAL NODES ---
col_dna, col_neural = st.columns([1, 1])

with col_dna:
    st.markdown("### 🛠️ KERNEL_DNA_REPORT")
    st.code(f"""
    OS_DIST: {platform.system()} {platform.release()}
    ARCH_TYPE: {platform.machine()}
    KERNEL_TIME: {datetime.now().strftime('%H:%M:%S')}
    HOST_NODE: {platform.node()}
    LOCATION: Caracas, San Bernardino
    """, language="bash")

with col_neural:
    st.markdown("### 🧠 NEURAL_NODES: KENYA & ÁMBAR")
    try:
        # Gráfico con estética de Stark Industries
        loads = psutil.cpu_percent(percpu=True) if cpu != "LOCKED" else [20, 45, 30, 60]
        st.area_chart(pd.DataFrame(loads, columns=['NODE_LOAD']))
    except:
        st.info("Neural link stable. Visualizing encrypted packets...")

# --- FOOTER ---
st.markdown(f"""
    <div style="text-align: center; padding: 40px; opacity: 0.5; font-family: Rajdhani;">
        {COPYRIGHT} // HARDWARE GOVERNANCE PROTOCOL // INFINIX BRIDGE STABLE
    </div>
""", unsafe_allow_html=True)

