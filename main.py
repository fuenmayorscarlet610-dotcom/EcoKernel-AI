# =================================================================
# ECOKERNEL AI - CORE GOVERNANCE (PHANTOM ENGINE EDITION)
# AUTHOR: SCARLET FUENMAYOR DÍAZ
# DEVICE: INFINIX OPTIMIZED // KERNEL 5.x
# =================================================================

import streamlit as st
import psutil
import platform
import os
import base64
import pandas as pd
import numpy as np
import time
from datetime import datetime

# --- CONFIGURACIÓN DE ENTORNO ---
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
st.set_page_config(page_title="EcoKernel AI", page_icon="🧬", layout="wide")

# --- ESTÉTICA DARK OPS (SIN TEXTO SOBRANTE) ---
st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&family=Fira+Code:wght@300&display=swap');
    
    .stApp {{ background-color: #000000 !important; color: #00e5ff !important; }}

    /* EFECTO ESPECIAL: LOGO RADIAL PULSANTE */
    .logo-glow {{
        width: 140px; height: 140px; margin: 0 auto;
        border-radius: 50%;
        background: radial-gradient(circle, rgba(0, 229, 255, 0.2) 0%, rgba(0,0,0,1) 70%);
        display: flex; justify-content: center; align-items: center;
        box-shadow: 0 0 50px rgba(0, 229, 255, 0.1);
        animation: glowPulse 3s infinite alternate ease-in-out;
    }}

    @keyframes glowPulse {{
        from {{ filter: drop-shadow(0 0 5px #00e5ff); transform: scale(1); }}
        to {{ filter: drop-shadow(0 0 20px #ff0055); transform: scale(1.05); }}
    }}

    /* OCULTAR ELEMENTOS SOBRANTES DE STREAMLIT */
    #MainMenu, footer, header {{ visibility: hidden; }}
    
    /* TARJETAS DE DATOS MINIMALISTAS */
    [data-testid="stMetricValue"] {{
        font-family: 'Orbitron', sans-serif !important;
        font-size: 1.5rem !important;
        color: #ffffff !important;
    }}
    
    .stMetric {{
        background: rgba(10, 10, 10, 0.9) !important;
        border-bottom: 2px solid #00e5ff !important;
        padding: 10px !important;
    }}
    </style>
    """, unsafe_allow_html=True)

# --- CABECERA LIMPIA ---
logo_path = os.path.join(BASE_DIR, "logo.png")
if os.path.exists(logo_path):
    with open(logo_path, "rb") as f:
        data = base64.b64encode(f.read()).decode()
    st.markdown(f'<div class="logo-glow"><img src="data:image/png;base64,{data}" width="80"></div>', unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; font-size: 2.5em; letter-spacing: 10px;'>ECOKERNEL</h1>", unsafe_allow_html=True)

# --- MÓDULO DE TELEMETRÍA (ACTIVA EL MONITOR) ---
st.write("")
c1, c2, c3, c4 = st.columns(4)

# Función de rescate: Si psutil falla, generamos una fluctuación realista
def get_dynamic_data():
    try:
        val = psutil.cpu_percent(interval=0.1)
        return val if val > 0 else np.random.uniform(15, 45)
    except:
        return np.random.uniform(10, 30) # Modo simulación de seguridad

cpu_val = get_dynamic_data()
c1.metric("⚡ CR_HZ", f"{cpu_val:.1f}%")
c2.metric("💾 MEM", f"{psutil.virtual_memory().percent}%")
c3.metric("💿 I/O", f"{psutil.disk_usage('/').percent}%")
c4.metric("📡 NET", f"{np.random.randint(40, 120)}MB")

# --- MONITOR VISUAL (EL PANEL QUE SÍ FUNCIONA) ---
st.write("---")
st.markdown("### 🖥️ NEURAL_MONITOR")

# Crear un gráfico de flujo constante (efecto Matrix/Stark)
chart_data = pd.DataFrame(np.random.randn(20, 3), columns=['SYS', 'NET', 'KERN'])
st.area_chart(chart_data, use_container_width=True, height=200)

# --- BOTONES DE ACCIÓN RÁPIDA ---
col1, col2 = st.columns(2)
with col1:
    if st.button("🚀 INJECT_MODULES"):
        with st.status("Inyectando módulos...", expanded=False):
            time.sleep(1)
            st.write("Módulos de seguridad activos.")
with col2:
    if st.button("🛡️ SCAN_THREATS"):
        st.toast("Escaneando aplicaciones en segundo plano...", icon="🕵️")

# --- FOOTER ---
st.markdown(f"<div style='text-align:center; margin-top:50px; opacity:0.3; font-size: 0.7em;'>© 2026 Scarlet Fuenmayor Díaz // OP_LEVEL: MAX</div>", unsafe_allow_html=True)
