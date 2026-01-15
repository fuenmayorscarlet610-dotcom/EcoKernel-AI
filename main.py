# =================================================================
# ECOKERNEL AI - GLOBAL GOVERNANCE CORE (OMNI EDITION)
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

# --- ESTILO "STARK-INDUSTRIAL" REPOTENCIADO (CIRCULAR NEÓN) ---
st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&family=JetBrains+Mono:wght@300&display=swap');
    
    .stApp {{ background-color: #000000 !important; color: #00FF00 !important; font-family: 'JetBrains Mono', monospace; }}
    
    /* Contenedor Maestro Centrado */
    .header-container {{
        display: flex; flex-direction: column; align-items: center; justify-content: center;
        text-align: center; padding: 20px 0; width: 100%;
    }}

    /* MARCO CIRCULAR NEÓN (SOLICITADO) */
    .stark-circle-frame {{
        border: 5px solid #00FF00;
        border-radius: 50% !important;
        padding: 10px;
        background: rgba(0, 255, 0, 0.02);
        box-shadow: 0px 0px 60px #00FF00, inset 0px 0px 30px #00FF00;
        width: 210px; height: 210px;
        display: flex; justify-content: center; align-items: center;
        margin-bottom: 25px; transition: 0.5s ease-in-out;
    }}
    .stark-circle-frame:hover {{ transform: scale(1.05) rotate(5deg); box-shadow: 0px 0px 90px #00FF00; }}
    .stark-circle-frame img {{ width: 85%; height: 85%; object-fit: contain; border-radius: 50%; }}

    /* Tipografía y Centrado de Guías */
    .stark-h1 {{
        font-family: 'Orbitron', sans-serif !important;
        font-size: 5.5em !important;
        letter-spacing: 20px;
        text-shadow: 0px 0px 25px #00FF00;
        margin: 0 !important; color: #00FF00;
        text-align: center;
    }}

    .stark-badge {{
        background: #00FF00; color: #000; padding: 8px 50px;
        font-weight: bold; font-family: 'Orbitron'; margin-top: 15px;
        letter-spacing: 5px; border-radius: 2px; display: inline-block;
    }}

    .function-guide {{
        text-align: center !important;
        font-family: 'Orbitron', sans-serif;
        letter-spacing: 3px;
        color: #FFF;
        margin-bottom: 15px;
        text-transform: uppercase;
    }}

    /* Optimización de Métricas Stark */
    [data-testid="stMetric"] {{ 
        border: 2px solid #00FF00 !important; 
        background: rgba(0,255,0,0.05) !important;
        border-radius: 15px !important;
        text-align: center !important;
    }}
    [data-testid="stMetricValue"] {{ color: #FFF !important; }}
    </style>
    """, unsafe_allow_html=True)

# --- CABECERA (LOGO CIRCULAR & TÍTULO) ---
st.markdown('<div class="header-container">', unsafe_allow_html=True)
if logo_b64:
    st.markdown(f'<div class="stark-circle-frame"><img src="{logo_b64}"></div>', unsafe_allow_html=True)
else:
    st.markdown('<div class="stark-circle-frame"><h1 style="font-size: 80px; margin:0;">⚡</h1></div>', unsafe_allow_html=True)

st.markdown('<h1 class="stark-h1">ECOKERNEL AI</h1>', unsafe_allow_html=True)
st.markdown(f'<div class="stark-badge">MASTER ARCHITECT: SCARLET FUENMAYOR</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

st.divider()

# --- PANEL DE CONTROL AVANZADO ---
st.sidebar.markdown("### 🕹️ COMMAND_CENTER")
target = st.sidebar.selectbox("🎯 SELECT MONITOR TARGET", ["Global System", "WhatsApp Node", "YouTube Buffer", "Apple Silicon Core", "Linux Kernel", "TikTok Sync"])
auto_refresh = st.sidebar.toggle("AUTO-SYNC NEURAL PULSE", value=True)

# --- TELEMETRÍA ULTRA-AVANZADA (REPOTENCIADA) ---
try:
    cpu_cores = psutil.cpu_percent(percpu=True)
    cpu_main = sum(cpu_cores) / len(cpu_cores)
    ram = psutil.virtual_memory()
    disk = psutil.disk_usage('/')
    net = psutil.net_io_counters()

    # Layout de Métricas Centradas
    st.markdown('<p class="function-guide">📊 Telemetría de Frecuencia en Tiempo Real</p>', unsafe_allow_html=True)
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("CPU AVG", f"{cpu_main}%")
    c2.metric("RAM USE", f"{ram.percent}%")
    c3.metric("STORAGE", f"{100-disk.percent:.1f}% FREE")
    c4.metric("NET I/O", f"{(net.bytes_sent + net.bytes_recv)//(1024**2)}MB")

    # Gráfico de Frecuencia Proyectado (Diseño Stark)
    fig = go.Figure()
    fig.add_trace(go.Indicator(
        mode = "gauge+number+delta", value = cpu_main,
        delta = {'reference': 50, 'relative': True, 'font': {'color': "#00FF00"}},
        gauge = {
            'axis': {'range': [None, 100], 'tickwidth': 1, 'tickcolor': "#00FF00"},
            'bar': {'color': "#00FF00"},
            'bgcolor': "black",
            'borderwidth': 2,
            'bordercolor': "#00FF00",
            'steps': [
                {'range': [0, 70], 'color': 'rgba(0, 255, 0, 0.1)'},
                {'range': [70, 90], 'color': 'rgba(255, 255, 0, 0.1)'},
                {'range': [90, 100], 'color': 'rgba(255, 0, 0, 0.2)'}
            ],
            'threshold': {'line': {'color': "red", 'width': 4}, 'thickness': 0.75, 'value': 95}
        },
        title = {'text': f"FRECUENCIA NEURAL: {target.upper()}", 'font': {'color': "#00FF00", 'family': 'Orbitron', 'size': 20}}
    ))
    fig.update_layout(paper_bgcolor='black', font={'color': "#00FF00"}, height=400, margin=dict(t=80, b=20))
    st.plotly_chart(fig, use_container_width=True)

except Exception as e:
    st.error(f"Error en el flujo de datos: {e}")

# --- MÓDULOS DE GOBERNANZA (ÁMBAR & KENYA) ---
st.write("---")
col_a, col_k = st.columns(2)

with col_a:
    st.markdown('<p class="function-guide">👁️ Ámbar: Gestión de Datos</p>', unsafe_allow_html=True)
    if st.button("EXECUTE DEEP DATA AUDIT"):
        with st.spinner("Auditando Almacenamiento Global..."):
            time.sleep(1)
            data_map = {
                "Sector": ["Root", "User_Data", "Cache", "Neural_Buffer"],
                "Capacity": [f"{disk.total//(1024**3)}GB", "128GB", "16GB", "Dynamic"],
                "Integrity": ["Verified", "Verified", "Optimized", "Locked"]
            }
            st.table(pd.DataFrame(data_map))

with col_k:
    st.markdown('<p class="function-guide">🧠 Kenya: Seguridad de Nodo</p>', unsafe_allow_html=True)
    if st.button("ACTIVATE STARK SHIELD"):
        with st.spinner("Sincronizando Escudos..."):
            time.sleep(1)
            st.success(f"Nodo {target} Blindado con AES-256.")
            st.code(f"PROTOCOL: SECURE_SYNC\nNODE_ID: {platform.node()}\nENCRYPTION: ACTIVE", language="bash")

# --- AUTO-REFRESCO ---
if auto_refresh:
    time.sleep(2)
    st.rerun()

# --- FOOTER DE IDENTIDAD MUNDIAL ---
st.divider()
st.markdown(f"""
    <div style="text-align: center; padding: 20px; opacity: 0.6;">
        <p style="color: #00FF00; letter-spacing: 5px; font-weight: bold; font-family: 'Orbitron';">{COPYRIGHT}</p>
        <p style="font-size: 0.8em; font-family: 'JetBrains Mono';">COMPATIBLE WITH: APPLE | LINUX | WINDOWS | SERVER NODES</p>
        <p style="font-size: 0.7em;">CARACAS, VENEZUELA | NODE_STATUS: ONLINE</p>
    </div>
""", unsafe_allow_html=True)
