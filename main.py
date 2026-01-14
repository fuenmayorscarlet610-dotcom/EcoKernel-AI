# =================================================================
# ECOKERNEL AI - GLOBAL GOVERNANCE CORE (STARK-LINUS EDITION)
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
VERSION = "24.0.0-OMNI-STARK"
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

# --- INTERFAZ ULTRA-CENTRADA Y NEÓN ---
st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&family=JetBrains+Mono:wght@300&display=swap');
    
    /* Fondo y Base */
    .stApp {{ 
        background-color: #000000 !important; 
        color: #00FF00 !important; 
        font-family: 'JetBrains Mono', monospace; 
    }}
    
    /* Logo Circular Neón - RESALTADO */
    .header-master {{
        display: flex; flex-direction: column; align-items: center; justify-content: center;
        width: 100%; padding-top: 30px;
    }}

    .logo-neon-circle {{
        border: 5px solid #00FF00;
        border-radius: 50% !important;
        padding: 10px;
        background: black;
        box-shadow: 0px 0px 60px #00FF00, inset 0px 0px 20px #00FF00;
        width: 200px; height: 200px;
        display: flex; justify-content: center; align-items: center;
        overflow: hidden; margin-bottom: 25px;
        transition: 0.8s cubic-bezier(0.4, 0, 0.2, 1);
    }}
    .logo-neon-circle:hover {{ transform: rotate(360deg) scale(1.1); box-shadow: 0px 0px 100px #00FF00; }}
    .logo-neon-circle img {{ width: 85%; height: 85%; object-fit: contain; }}

    /* Centrado de Guías y Títulos */
    h1, h2, h3, p, span {{ text-align: center !important; font-family: 'Orbitron', sans-serif !important; }}
    
    .main-title {{
        font-size: 4.5em !important; letter-spacing: 15px;
        text-shadow: 0px 0px 25px #00FF00; margin-bottom: 0px !important;
    }}

    /* Métricas Stark Style */
    [data-testid="stMetric"] {{ 
        background: rgba(0, 255, 0, 0.05) !important; 
        border: 2px solid #00FF00 !important; 
        border-radius: 20px !important;
        box-shadow: 0px 10px 30px rgba(0, 0, 0, 0.8);
    }}
    
    [data-testid="stMetricLabel"] {{ color: #FFF !important; font-size: 1.2em !important; }}
    [data-testid="stMetricValue"] {{ color: #00FF00 !important; font-weight: bold; }}

    /* Botones de Función */
    .stButton>button {{
        width: 100%; border-radius: 0px; background: transparent; 
        color: #00FF00; border: 2px solid #00FF00; font-family: 'Orbitron';
        padding: 12px; transition: 0.3s;
    }}
    .stButton>button:hover {{ background: #00FF00; color: #000; box-shadow: 0px 0px 40px #00FF00; }}
    </style>
    """, unsafe_allow_html=True)

# --- CABECERA MAESTRA (LOGO & IDENTITY) ---
st.markdown('<div class="header-master">', unsafe_allow_html=True)
if logo_b64:
    st.markdown(f'<div class="logo-neon-circle"><img src="{logo_b64}"></div>', unsafe_allow_html=True)
else:
    st.markdown('<div class="logo-neon-circle"><h1 style="font-size: 100px; margin:0; line-height: 200px;">⚡</h1></div>', unsafe_allow_html=True)

st.markdown(f"""
    <h1 class="main-title">ECOKERNEL AI</h1>
    <p style="letter-spacing: 12px; color: #FFF; font-size: 1.3em; margin-bottom: 10px;">GLOBAL HARDWARE GOVERNANCE</p>
    <div style="background: #00FF00; color: #000; padding: 5px 50px; font-weight: bold; display: inline-block;">
        MASTER ARCHITECT: {DEVELOPER.upper()}
    </div>
    <p style="opacity: 0.6; font-size: 0.8em; margin-top: 20px;">SYSTEM_SYNC: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} | CARACAS_SB</p>
""", unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

st.divider()

# --- PANEL DE COMANDO LATERAL ---
st.sidebar.markdown("### 🕹️ MASTER_CONTROL")
target_app = st.sidebar.selectbox("FOCAL_TARGET", ["Global System", "WhatsApp", "YouTube", "Apple Core", "Linux Kernel", "TikTok"])
mode = st.sidebar.radio("OP_MODE", ["Diagnostic", "Security", "Overclock"])

# --- MONITOR DE FRECUENCIA ULTRA-AVANZADO ---
st.markdown(f"### 📊 ANALIZADOR DE FRECUENCIA NEURAL: {target_app.upper()}")
cpu = psutil.cpu_percent(interval=0.1)
ram = psutil.virtual_memory().percent
disk = psutil.disk_usage('/').percent

# Gráfico de Frecuencia de Hilos Estilo Stark
fig = go.Figure()
fig.add_trace(go.Indicator(
    mode = "gauge+number+delta", value = cpu,
    title = {'text': "Frecuencia de Hilos (GHz/s)", 'font': {'size': 20, 'color': '#00FF00'}},
    gauge = {
        'axis': {'range': [None, 100], 'tickwidth': 1, 'tickcolor': "#00FF00"},
        'bar': {'color': "#00FF00"},
        'bgcolor': "black",
        'borderwidth': 2,
        'bordercolor': "#00FF00",
        'steps': [
            {'range': [0, 50], 'color': 'rgba(0, 255, 0, 0.1)'},
            {'range': [50, 85], 'color': 'rgba(255, 255, 0, 0.1)'},
            {'range': [85, 100], 'color': 'rgba(255, 0, 0, 0.3)'}
        ],
        'threshold': {'line': {'color': "red", 'width': 4}, 'thickness': 0.75, 'value': 90}
    }
))
fig.update_layout(paper_bgcolor='black', font={'color': "#00FF00", 'family': "Orbitron"}, height=350, margin=dict(t=0, b=0))
st.plotly_chart(fig, use_container_width=True)

# --- TELEMETRÍA DE ALTO IMPACTO ---
st.write("---")
c1, c2, c3 = st.columns(3)
c1.metric("NODAL_CPU", f"{cpu}%")
c2.metric("MEMORY_BUFFER", f"{ram}%")
c3.metric("NODAL_DISK", f"{100-disk:.1f}% FREE")

# --- FUNCIONES DE GOBERNANZA (ÁMBAR & KENYA) ---
st.divider()
col_a, col_k = st.columns(2)

with col_a:
    st.markdown("### 👁️ NEURAL: Ámbar")
    st.caption("ANÁLISIS DE ALMACENAMIENTO DINÁMICO")
    if st.button("EXECUTE STORAGE AUDIT"):
        usage = psutil.disk_usage('/')
        data_store = {
            "Métrica": ["Capacidad Total", "Espacio Usado", "Espacio Libre", "Punto de Montaje"],
            "Valor": [f"{usage.total // (2**30)} GB", f"{usage.used // (2**30)} GB", f"{usage.free // (2**30)} GB", "/root"]
        }
        st.table(pd.DataFrame(data_store))

with col_k:
    st.markdown("### 🧠 NEURAL: Kenya")
    st.caption("DIAGNÓSTICO DE HILOS Y PRIORIDAD")
    status = "⚡ OPTIMAL" if cpu < 70 else "🔥 OVERLOAD"
    st.info(f"Target: {target_app} | Status: {status} | Latencia: 2ms")
    if st.button("OPTIMIZE APP THREADS"):
        with st.spinner("Reordenando procesos..."):
            time.sleep(1.5)
            st.success("Prioridad asignada al Núcleo de Scarlet.")

# --- DNA & THERMAL MONITOR ---
st.divider()
cdna, ctherm = st.columns(2)
with cdna:
    st.markdown("### 🖥️ [SYSTEM_DNA]")
    st.code(f"USER: {DEVELOPER}\nNODE: {platform.node()}\nARCH: {platform.machine()}\nKERNEL: {platform.system()} {platform.release()}", language="bash")

with ctherm:
    st.markdown("### 🌡️ [THERMAL_SHIELD]")
    temp_sim = 32 + (cpu * 0.28)
    if temp_sim > 48:
        st.error(f"CRITICAL: {temp_sim:.1f}°C")
    else:
        st.success(f"NOMINAL: {temp_sim:.1f}°C")

# --- FOOTER ---
st.divider()
st.markdown(f"""
    <div style="text-align: center; padding: 30px;">
        <p style="color: #00FF00; letter-spacing: 5px; font-weight: bold;">{COPYRIGHT.upper()}</p>
        <p style="font-size: 0.8em; opacity: 0.5;">CARACAS, VENEZUELA | GLOBAL_GOVERNANCE_v{VERSION}</p>
        <p style="font-size: 0.7em; opacity: 0.3;">Compatible with: Server, Desktop, Mobile & Apple Architecture.</p>
    </div>
""", unsafe_allow_html=True)
