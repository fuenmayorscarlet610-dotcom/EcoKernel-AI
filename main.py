# =================================================================
# ECOKERNEL AI - CORE GOVERNANCE (DARK OPS & STARK HYBRID)
# AUTHOR: SCARLET FUENMAYOR DÍAZ
# DEVICE: INFINIX OPTIMIZED // KERNEL 5.x
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
VERSION = "26.8.0-DARK-OPS"
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

# --- ESTÉTICA DARK SOFISTICADA (STARK HUD V3) ---
st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&family=Fira+Code:wght@300;500&family=Rajdhani:wght@500;700&display=swap');
    
    /* Fondo Negro Puro para Infinix AMOLED */
    .stApp {{
        background-color: #000000 !important;
        color: #00e5ff !important;
        font-family: 'Rajdhani', sans-serif;
    }}

    /* EL TOQUE INESPERADO: Resplandor del Logo */
    .logo-container {{
        text-align: center;
        padding: 40px 0;
        background: radial-gradient(circle, rgba(0, 229, 255, 0.1) 0%, rgba(0,0,0,0) 70%);
    }}

    .stark-cyber-logo {{
        width: 160px; height: 160px;
        margin: 0 auto;
        border: 1px solid rgba(0, 229, 255, 0.3);
        border-radius: 50%; /* Cambio a circular para suavizar */
        display: flex; justify-content: center; align-items: center;
        background: rgba(0,0,0,0.8);
        box-shadow: 0 0 40px rgba(0, 229, 255, 0.2), inset 0 0 20px rgba(0, 229, 255, 0.1);
        animation: pulse 4s infinite ease-in-out;
    }}
    
    @keyframes pulse {{
        0% {{ box-shadow: 0 0 30px rgba(0, 229, 255, 0.2); }}
        50% {{ box-shadow: 0 0 60px rgba(255, 0, 85, 0.3); }}
        100% {{ box-shadow: 0 0 30px rgba(0, 229, 255, 0.2); }}
    }}

    .stark-cyber-logo img {{ max-width: 75%; filter: drop-shadow(0 0 10px #00e5ff); }}

    /* Títulos Elegantes */
    h1, h2, h3 {{ 
        font-family: 'Orbitron', sans-serif !important; 
        letter-spacing: 5px !important;
        text-transform: uppercase;
        color: #ffffff !important;
        text-shadow: 0 0 10px rgba(0, 229, 255, 0.5);
    }}

    /* Métricas: Estilo Stark HUD */
    [data-testid="stMetricValue"] {{
        font-family: 'Fira Code', monospace !important;
        color: #ffffff !important;
        text-shadow: 0 0 8px #00e5ff;
        font-size: 1.8rem !important;
    }}
    
    .stMetric {{
        background: rgba(10, 10, 10, 0.8) !important;
        border: 1px solid rgba(255, 255, 255, 0.05) !important;
        border-left: 3px solid #ff0055 !important; /* Acento Magenta */
        border-radius: 4px !important;
        backdrop-filter: blur(5px);
    }}

    /* Sidebar Invisible */
    [data-testid="stSidebar"] {{
        background-color: #050505 !important;
        border-right: 1px solid rgba(255, 255, 255, 0.1);
    }}

    /* Estilo de los módulos */
    .module-card {{
        border: 1px solid rgba(0, 229, 255, 0.2);
        padding: 15px;
        background: rgba(0, 229, 255, 0.02);
        border-radius: 5px;
    }}
    </style>
    """, unsafe_allow_html=True)

# --- CABECERA DE OPERACIONES ---
with st.container():
    st.markdown('<div class="logo-container">', unsafe_allow_html=True)
    if logo_b64:
        st.markdown(f'<div class="stark-cyber-logo"><img src="data:image/png;base64,{logo_b64}"></div>', unsafe_allow_html=True)
    else:
        st.markdown('<div class="stark-cyber-logo"><h1 style="font-size: 50px; margin:0;">🧬</h1></div>', unsafe_allow_html=True)
    
    st.markdown(f"""
        <h1 style='text-align: center; font-size: 2.8em; margin-top: 20px;'>ECOKERNEL <span style='color: #ff0055;'>AI</span></h1>
        <p style='text-align: center; color: rgba(255,255,255,0.4); font-family: Fira Code; font-size: 0.8em;'>
            [ SYSTEM_DNA: ENCRYPTED // OPERATOR: {DEVELOPER.upper()} ]
        </p>
    </div>
    """, unsafe_allow_html=True)

# --- SIDEBAR CONTROL ---
st.sidebar.markdown("### 🛠️ HARDWARE_CON")
app_monitor = st.sidebar.selectbox("WATCH_STREAM:", ["WhatsApp", "Instagram", "Kernel Server", "Python Process"])
storage_target = st.sidebar.radio("I/O_ACCESS:", ["INT_MEM", "SD_CARD", "VIRTUAL"])
if st.sidebar.button("SYNC_KERNEL"): st.rerun()

# --- MÓDULO 01: TELEMETRÍA (CON BYPASS PROFESIONAL) ---
c1, c2, c3, c4 = st.columns(4)

def get_hw_stat(func, attr=None):
    try:
        data = func()
        return getattr(data, attr) if attr else data
    except: return None

cpu = get_hw_stat(psutil.cpu_percent)
ram = get_hw_stat(psutil.virtual_memory, 'percent')
disk = get_hw_stat(lambda: psutil.disk_usage('/'), 'percent')
net = get_hw_stat(psutil.net_io_counters, 'bytes_sent')

c1.metric("CORE_HZ", f"{cpu}%" if cpu is not None else "[RESTRIC]")
c2.metric("MEM_USE", f"{ram}%" if ram is not None else "[RESTRIC]")
c3.metric("I/O_VOL", f"{disk}%" if disk is not None else "[LOCKED]")
c4.metric("UP_LINK", f"{net // (1024**2)}MB" if net is not None else "0MB")

st.write("---")

# --- MÓDULO 02: TOOLS & NODES ---
col_left, col_right = st.columns(2)

with col_left:
    st.markdown("### 👁️ NODE_AMBAR: FILES")
    st.markdown('<div class="module-card">', unsafe_allow_html=True)
    if st.button("RUN_DEEP_FILES_SCAN"):
        st.write("Scanning partitions...")
    st.markdown('</div>', unsafe_allow_html=True)

with col_right:
    st.markdown("### 🧠 NODE_KENYA: SECURITY")
    st.markdown('<div class="module-card">', unsafe_allow_html=True)
    st.success(f"STATUS: {app_monitor} IS NOMINAL")
    st.markdown('</div>', unsafe_allow_html=True)

# --- MÓDULO 04: DNA REPORT ---
with st.expander("📂 DECRYPT_SYSTEM_DNA"):
    st.code(f"""
    NODE_ID: {platform.node()}
    OS_TYPE: {platform.system()} {platform.release()}
    ARCH: {platform.machine()}
    TIMESTAMP: {datetime.now().strftime('%H:%M:%S')}
    LOC: Caracas, San Bernardino (Infinix Device)
    """, language="bash")

# --- FOOTER ---
st.markdown(f"""
    <div style="text-align: center; padding: 40px; border-top: 1px solid rgba(255,255,255,0.05); margin-top: 40px; color: rgba(255,255,255,0.2);">
        {COPYRIGHT} // PROTOCOLO DE GOBERNANZA ACTIVO<br>
        <small>STARK TECH // LINUX KERNEL OPTIMIZED</small>
    </div>
""", unsafe_allow_html=True)
        
