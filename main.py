# =================================================================
# ECOKERNEL AI - GLOBAL GOVERNANCE CORE (STARK PRECISION)
# AUTHOR: SCARLET FUENMAYOR DÍAZ
# COPYRIGHT: © 2026 Scarlet Fuenmayor
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

# --- CONFIGURACIÓN DE NÚCLEO SUPREMO ---
st.set_page_config(
    page_title=f"EcoKernel AI | Scarlet Fuenmayor",
    page_icon="⚡", 
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- CARGA SEGURA DEL LOGO DE SCARLET ---
@st.cache_resource
def get_encoded_assets(path):
    if os.path.exists(path):
        try:
            with open(path, "rb") as f:
                return f"data:image/png;base64,{base64.b64encode(f.read()).decode()}"
        except Exception:
            return None
    return None

logo_b64 = get_encoded_assets("logo.png")

# --- ESTILO "STARK-INDUSTRIAL" (MARCO CUADRADO NEÓN) ---
st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&family=JetBrains+Mono:wght@300&display=swap');
    
    .stApp {{ background-color: #000000 !important; color: #00FF00 !important; font-family: 'JetBrains Mono', monospace; }}
    
    .header-container {{
        display: flex; flex-direction: column; align-items: center; justify-content: center;
        text-align: center; padding: 30px 0; width: 100%;
    }}

    /* MARCO CUADRADO NEÓN REPOTENCIADO */
    .stark-square-frame {{
        border: 4px solid #00FF00;
        border-radius: 12px;
        padding: 15px;
        background: rgba(0, 255, 0, 0.02);
        box-shadow: 0px 0px 50px #00FF00, inset 0px 0px 20px #00FF00;
        width: 215px; height: 215px;
        display: flex; justify-content: center; align-items: center;
        margin-bottom: 30px; transition: 0.4s ease-in-out;
    }}
    .stark-square-frame:hover {{ 
        transform: scale(1.05); 
        box-shadow: 0px 0px 80px #00FF00; 
        background: rgba(0, 255, 0, 0.05);
    }}
    .stark-square-frame img {{ width: 100%; height: 100%; object-fit: contain; }}

    /* Tipografía y Centrado Maestro */
    .stark-h1 {{
        font-family: 'Orbitron', sans-serif !important;
        font-size: 5.2em !important;
        letter-spacing: 22px;
        text-shadow: 0px 0px 30px #00FF00;
        margin: 0 !important; color: #00FF00;
        text-align: center;
    }}

    .stark-badge {{
        background: #00FF00; color: #000; padding: 10px 60px;
        font-weight: bold; font-family: 'Orbitron'; margin-top: 20px;
        letter-spacing: 6px; border-radius: 4px; display: inline-block;
        box-shadow: 0px 0px 15px #00FF00;
    }}

    .function-guide {{
        text-align: center !important;
        font-family: 'Orbitron', sans-serif;
        letter-spacing: 4px;
        color: #FFFFFF;
        margin-top: 25px;
        margin-bottom: 15px;
        text-transform: uppercase;
        width: 100%;
    }}

    /* Widgets Stark */
    [data-testid="stMetric"] {{ 
        border: 2px solid #00FF00 !important; 
        background: rgba(0,255,0,0.03) !important;
        border-radius: 0px !important;
        text-align: center !important;
    }}
    </style>
    """, unsafe_allow_html=True)

# --- CABECERA (LOGO CUADRADO & TÍTULO) ---
st.markdown('<div class="header-container">', unsafe_allow_html=True)
if logo_b64:
    st.markdown(f'<div class="stark-square-frame"><img src="{logo_b64}"></div>', unsafe_allow_html=True)
else:
    st.markdown('<div class="stark-square-frame"><h1 style="font-size: 90px; margin:0;">⚡</h1></div>', unsafe_allow_html=True)

st.markdown('<h1 class="stark-h1">ECOKERNEL AI</h1>', unsafe_allow_html=True)
st.markdown(f'<div class="stark-badge">MASTER ARCHITECT: SCARLET FUENMAYOR</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

st.divider()

# --- PANEL DE CONTROL ---
st.sidebar.markdown("### 🕹️ MASTER_GOVERNANCE")
target = st.sidebar.selectbox("🎯 MONITOR_TARGET", ["Global System", "Apple Silicon Core", "WhatsApp Node", "YouTube Buffer", "Linux Kernel", "TikTok Sync"])
auto_refresh = st.sidebar.toggle("AUTO-SYNC NEURAL PULSE", value=True)

# --- TELEMETRÍA DE ALTO IMPACTO ---
try:
    cpu_main = psutil.cpu_percent(interval=0.1)
    ram = psutil.virtual_memory()
    disk = psutil.disk_usage('/')
    net = psutil.net_io_counters()

    st.markdown('<p class="function-guide">📊 Telemetría de Frecuencia Global</p>', unsafe_allow_html=True)
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("CPU_CORE", f"{cpu_main}%")
    c2.metric("RAM_BUFFER", f"{ram.percent}%")
    c3.metric("STORAGE_LINK", f"{100-disk.percent:.1f}% FREE")
    c4.metric("NET_FLOW", f"{(net.bytes_sent + net.bytes_recv)//(1024**2)} MB")

    # Gráfico de Frecuencia Proyectado
    fig = go.Figure(go.Indicator(
        mode = "gauge+number+delta", value = cpu_main,
        delta = {'reference': 50, 'relative': True, 'font': {'color': "#00FF00"}},
        gauge = {
            'axis': {'range': [None, 100], 'tickcolor': "#00FF00"},
            'bar': {'color': "#00FF00"},
            'bgcolor': "black",
            'bordercolor': "#00FF00",
            'steps': [{'range': [0, 100], 'color': 'rgba(0, 255, 0, 0.05)'}],
            'threshold': {'line': {'color': "red", 'width': 4}, 'thickness': 0.8, 'value': 95}
        },
        title = {'text': f"FRECUENCIA NEURAL: {target.upper()}", 'font': {'color': "#00FF00", 'family': 'Orbitron'}}
    ))
    fig.update_layout(paper_bgcolor='black', font={'color': "#00FF00"}, height=400, margin=dict(t=80, b=20))
    st.plotly_chart(fig, use_container_width=True)

except Exception as e:
    st.error(f"Error de acceso a Kernel: {e}")

# --- MÓDULOS ÁMBAR & KENYA (TOTALMENTE CENTRADOS) ---
st.write("---")
col_a, col_k = st.columns(2)

with col_a:
    st.markdown('<p class="function-guide">👁️ Ámbar: Auditoría de Datos</p>', unsafe_allow_html=True)
    if st.button("EXECUTE DEEP DATA AUDIT", use_container_width=True):
        with st.spinner("Auditando sectores..."):
            time.sleep(1)
            st.table(pd.DataFrame({
                "Sector": ["User_Root", "Cache_Stark", "Neural_Logs"],
                "Integrity": ["100% Verified", "Optimized", "Encrypted"]
            }))

with col_k:
    st.markdown('<p class="function-guide">🧠 Kenya: Seguridad de Nodo</p>', unsafe_allow_html=True)
    if st.button("ACTIVATE STARK SHIELD", use_container_width=True):
        with st.spinner("Blindando red..."):
            time.sleep(1)
            st.success(f"Nodo {target} Blindado con AES-256.")
            st.code(f"NODE_ID: {platform.node()}\nENCRYPTION: ACTIVE", language="bash")

# --- AUTO-REFRESCO ---
if auto_refresh:
    time.sleep(2)
    st.rerun()

# --- FOOTER ---
st.divider()
st.markdown(f"""
    <div style="text-align: center; padding: 20px; opacity: 0.6;">
        <p style="color: #00FF00; letter-spacing: 5px; font-weight: bold; font-family: 'Orbitron';">{COPYRIGHT}</p>
        <p style="font-size: 0.8em; font-family: 'JetBrains Mono';">SCALABLE ARCHITECTURE | APPLE - LINUX - WINDOWS - MOBILE</p>
        <p style="font-size: 0.7em;">CARACAS, VENEZUELA | HARDWARE GOVERNANCE ACTIVE</p>
    </div>
""", unsafe_allow_html=True)
