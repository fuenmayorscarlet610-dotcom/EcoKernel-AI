# =================================================================
# ECOKERNEL AI - CORE GOVERNANCE (TERMUX CYBERPUNK EDITION)
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

# --- CONFIGURACIÓN DE ENTORNO ---
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODULES_DIR = os.path.join(BASE_DIR, "modules")
if not os.path.exists(MODULES_DIR): os.makedirs(MODULES_DIR)

# --- GLOBAL CONFIG ---
VERSION = "25.0.5-CYBER-STARK"
DEVELOPER = "Scarlet Fuenmayor Díaz"
COPYRIGHT = f"© 2026 {DEVELOPER}"

st.set_page_config(page_title=f"EcoKernel AI | {VERSION}", page_icon="🧪", layout="wide")

# --- PROCESAMIENTO DE LOGO ---
def get_base64_logo(path):
    if os.path.exists(path):
        try:
            with open(path, "rb") as f:
                return base64.b64encode(f.read()).decode()
        except: return None
    return None

logo_b64 = get_base64_logo(os.path.join(BASE_DIR, "logo.png"))

# --- ESTÉTICA CYBERPUNK AVANZADA ---
st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&family=JetBrains+Mono&family=Rajdhani:wght@500;700&display=swap');
    
    /* Fondo y Texto General */
    .stApp {{
        background-color: #050505 !important;
        background-image: linear-gradient(rgba(0, 255, 0, 0.02) 1px, transparent 1px), 
                          linear-gradient(90deg, rgba(0, 255, 0, 0.02) 1px, transparent 1px);
        background-size: 30px 30px;
        color: #00FF00 !important;
        font-family: 'JetBrains Mono', monospace;
    }}

    /* Logo con Efecto Glitch y Neón Dual */
    .stark-cyber-logo {{
        width: 180px; height: 180px;
        border: 4px double #00FF00;
        box-shadow: 0px 0px 15px #00FF00, inset 0px 0px 15px #00FF00;
        display: flex; justify-content: center; align-items: center;
        margin: 0 auto 10px auto;
        background: #000;
        clip-path: polygon(10% 0, 100% 0, 100% 90%, 90% 100%, 0 100%, 0 10%);
    }}
    
    .stark-cyber-logo img {{ max-width: 85%; filter: drop-shadow(0 0 5px #00FF00); }}

    /* Títulos Estilo Sci-Fi */
    h1, h2, h3 {{ 
        font-family: 'Orbitron', sans-serif !important; 
        color: #00FF00 !important;
        text-shadow: 2px 2px 10px rgba(0, 255, 0, 0.5);
        letter-spacing: 3px;
    }}

    /* Métricas Neón */
    [data-testid="stMetricValue"] {{
        font-family: 'Orbitron', sans-serif !important;
        color: #FF00FF !important; /* Magenta Cyberpunk */
        text-shadow: 0 0 10px #FF00FF;
    }}
    
    .stMetric {{
        background: rgba(0, 255, 0, 0.05) !important;
        border-left: 5px solid #00FF00 !important;
        border-right: 1px solid #FF00FF !important;
        padding: 10px !important;
    }}

    /* Sidebar Estilo Terminal Militar */
    [data-testid="stSidebar"] {{
        background-color: #000000 !important;
        border-right: 2px solid #00FF00;
    }}
    
    /* Botones Neón */
    .stButton>button {{
        width: 100%;
        background-color: transparent !important;
        color: #00FF00 !important;
        border: 1px solid #00FF00 !important;
        font-family: 'Orbitron', sans-serif;
        transition: 0.3s;
    }}
    .stButton>button:hover {{
        background-color: #00FF00 !important;
        color: #000 !important;
        box-shadow: 0 0 20px #00FF00;
    }}

    /* Tablas y Código */
    .stCodeBlock {{ border: 1px solid #FF00FF !important; }}
    </style>
    """, unsafe_allow_html=True)

# --- CABECERA DE OPERACIONES ---
with st.container():
    if logo_b64:
        st.markdown(f'<div class="stark-cyber-logo"><img src="data:image/png;base64,{logo_b64}"></div>', unsafe_allow_html=True)
    else:
        st.markdown('<div class="stark-cyber-logo"><h1 style="font-size: 60px;">🧪</h1></div>', unsafe_allow_html=True)
    
    st.markdown(f"<h1 style='text-align: center; font-size: 3.5em; margin-bottom:0;'>ECOKERNEL AI</h1>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align: center; color: #FF00FF; font-family: Orbitron; font-weight: bold;'>[ SYSTEM STATUS: ENCRYPTED // OPERATOR: {DEVELOPER.upper()} ]</p>", unsafe_allow_html=True)

st.write("---")

# --- SIDEBAR CONTROL ---
st.sidebar.markdown("### 🎚️ KERNEL_CONTROL")
app_monitor = st.sidebar.selectbox("TARGET APP:", ["WhatsApp", "Instagram", "Kernel Server", "Python Process"])
storage_target = st.sidebar.radio("ACCESS POINT:", ["INTERNAL_STORAGE", "EXTERNAL_SD", "VIRTUAL_CACHE"])

st.sidebar.write("---")
if st.sidebar.button("REBOOT INTERFACE"): st.rerun()

# --- MÓDULO 01: TELEMETRÍA CYBER ---
c1, c2, c3, c4 = st.columns(4)

# Bypasses de Seguridad para Termux/Android
try: cpu = psutil.cpu_percent(interval=None)
except: cpu = "LOCK"

try: ram = psutil.virtual_memory().percent
except: ram = "LOCK"

try: disk = psutil.disk_usage('/')
except: disk = None

try: net = psutil.net_io_counters()
except: net = None

c1.metric("⚡ CORE_LOAD", f"{cpu}%")
c2.metric("💾 MEM_SYNC", f"{ram}%")
c3.metric("💿 STORAGE", f"{disk.percent if disk else '0'}%")
c4.metric("📡 NET_UPLINK", f"{net.bytes_sent // (1024**2) if net else '0'} MB")

# --- MÓDULO 02: ESCÁNER DE MÓDULOS ---
st.write("---")
st.subheader("⚡ MODULE_SWAP_LINKER")
try: mods = [f for f in os.listdir(MODULES_DIR) if f.endswith('.py')]
except: mods = []

if mods:
    col_list = st.columns(4)
    for i, m in enumerate(mods):
        col_list[i % 4].info(f"CONNECTED: {m}")
else:
    st.warning("⚠️ WAITING FOR MODULE INJECTION (.py files in /modules)")

# --- MÓDULO 03: NEURAL NODES (ÁMBAR & KENYA) ---
st.write("---")
col_a, col_k = st.columns(2)

with col_a:
    st.markdown("### 👁️ NODE_AMBAR: FILES")
    st.caption(f"Path: {storage_target}")
    try:
        import modules.file_manager as fm
        fm.show_file_manager()
    except:
        if st.button("RUN DEEP SCAN"):
            data = {
                "PARTITION": ["SYS_ROOT", "USER_DATA", "KERN_CACHE"],
                "STATUS": ["MOUNTED", "READ_ONLY", "ISOLATED"],
                "VOL": [f"{disk.total // (1024**3) if disk else '0'}GB", "SECURE", "CLEAN"]
            }
            st.table(pd.DataFrame(data))

with col_k:
    st.markdown("### 🧠 NODE_KENYA: SECURITY")
    st.caption(f"Monitoring: {app_monitor}")
    try:
        import modules.security_shield as ss
        ss.show_security_monitor()
    except:
        try:
            # Gráfico con colores Cyberpunk
            loads = psutil.cpu_percent(percpu=True)
            st.area_chart(pd.DataFrame(loads, columns=['CORE_FREQ']))
        except:
            st.error("SYSTEM_DNA_ACCESS_DENIED: Android Búnker Activo")
        st.success(f"PROT_LEVEL: MAXIMUM // {app_monitor}: SECURE")

# --- MÓDULO 04: DNA REPORT ---
st.write("---")
with st.expander("📂 DECRYPT SYSTEM DNA"):
    st.code(f"""
    NODE: {platform.node()}
    DISTRO: {platform.system()} | {platform.release()}
    ARCH: {platform.machine()}
    SYNC_TIME: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
    LOCATION: Caracas, San Bernardino [Lat: 10.5 | Lon: -66.9]
    """, language="bash")

# --- FOOTER ---
st.markdown(f"""
    <div style="text-align: center; padding: 20px; border-top: 2px solid #FF00FF; margin-top: 50px; background: rgba(255,0,255,0.05);">
        <span style="color: #FF00FF; font-family: Orbitron; font-weight: bold;">{COPYRIGHT}</span><br>
        <small style="color: #00FF00; opacity: 0.8;">HARDWARE GOVERNANCE PROTOCOL v25.0.5 | ENCRYPTED BY STARK-TECH</small>
    </div>
""", unsafe_allow_html=True)
        
