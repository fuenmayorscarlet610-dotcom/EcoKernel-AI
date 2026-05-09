# =================================================================
# ECOKERNEL AI - CORE GOVERNANCE (STARK-TORVALDS HYBRID)
# AUTHOR: SCARLET FUENMAYOR DÍAZ
# DEVICE: INFINIX OCTA-CORE HYBRID
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

st.set_page_config(page_title="EcoKernel AI | Stark-Linux", page_icon="🧬", layout="wide")

# --- ESTÉTICA SOFISTICADA (STARK HUD) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&family=Fira+Code:wght@300;500&display=swap');
    .stApp { background-color: #020202 !important; color: #00e5ff !important; font-family: 'Fira Code', monospace; }
    .stark-header { border-left: 5px solid #ff0055; padding: 20px; background: rgba(255, 0, 85, 0.05); margin-bottom: 25px; }
    [data-testid="stMetricValue"] { font-family: 'Orbitron', sans-serif !important; color: #ffffff !important; text-shadow: 0 0 10px #00e5ff; }
    .stMetric { border: 1px solid rgba(0, 229, 255, 0.2) !important; background: rgba(0, 0, 0, 0.6) !important; }
    </style>
    """, unsafe_allow_html=True)

# --- CABECERA ---
st.markdown(f'<div class="stark-header"><h1 style="margin:0; font-family: Orbitron;">ECOKERNEL_AI v26.1</h1><p>[ OPERATOR: {platform.node().upper()} // DEVICE: INFINIX ]</p></div>', unsafe_allow_html=True)

# --- TELEMETRÍA CON BYPASS (CORRECCIÓN DE ERROR /proc/stat) ---
st.subheader("📡 SYSTEM_TELEMETRY")
c1, c2, c3, c4 = st.columns(4)

def get_safe_metric(func, attr=None):
    try:
        data = func()
        return getattr(data, attr) if attr else data
    except (PermissionError, Exception):
        return "SECURE"

cpu = get_safe_metric(psutil.cpu_percent)
ram = get_safe_metric(psutil.virtual_memory, 'percent')
disk = get_safe_metric(lambda: psutil.disk_usage('/'), 'percent')
net = get_safe_metric(psutil.net_io_counters, 'bytes_sent')

c1.metric("CPU_CORE", f"{cpu}%" if cpu != "SECURE" else "PROTECTED")
c2.metric("RAM_LOAD", f"{ram}%" if ram != "SECURE" else "PROTECTED")
c3.metric("DISK_IO", f"{disk}%" if disk != "SECURE" else "RESTRICTED")
c4.metric("NET_UP", f"{net // (1024**2)}MB" if net != "SECURE" else "0MB")

# --- KERNEL DNA ---
st.write("---")
st.markdown("### 🛠️ KERNEL_DNA_REPORT")
st.code(f"""
OS: {platform.system()} {platform.release()}
ARCH: {platform.machine()} (Octa-Core)
TIME: {datetime.now().strftime('%H:%M:%S')}
SYNC: STARK_CLOUD_ACTIVE
""", language="bash")
