import streamlit as st
import psutil
import platform
import os
import shutil
import base64
import time
import pandas as pd
import plotly.graph_objects as go
import numpy as np
import requests
import hashlib
import subprocess
from datetime import datetime

# --- AJUSTE DE PANTALLA PARA MÓVIL (A31) ---
st.set_page_config(page_title="EcoKernel | Scarlet Fuenmayor", layout="wide")

# --- FUNCIONES DE ACCIÓN DIRECTA ---
def execute_system_purge():
    """Busca y elimina archivos reales en el servidor"""
    temp_path = "/tmp" 
    files_cleaned = 0
    if os.path.exists(temp_path):
        for root, dirs, files in os.walk(temp_path):
            for f in files:
                try:
                    os.remove(os.path.join(root, f))
                    files_cleaned += 1
                except: continue
            if files_cleaned > 50: break # Seguridad
    return files_cleaned

# --- ESTILOS STARK PARA MÓVIL ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&family=JetBrains+Mono&display=swap');
    .stApp { background-color: #000000; color: #00FF00; font-family: 'JetBrains Mono', monospace; }
    .stark-title { font-family: 'Orbitron'; font-size: 2.5rem; text-align: center; color: #00FF00; text-shadow: 0 0 10px #00FF00; }
    /* Botones más grandes para dedos en móvil */
    .stButton>button { width: 100%; height: 3.5rem; border: 1px solid #00FF00; background-color: rgba(0,255,0,0.1); color: #00FF00; font-weight: bold; }
    </style>
""", unsafe_allow_html=True)

st.markdown('<h1 class="stark-title">ECOKERNEL</h1>', unsafe_allow_html=True)
st.write(f"<center><b>MASTER ARCHITECT: SCARLET FUENMAYOR</b><br>Samsung A31 Control Node</center>", unsafe_allow_html=True)

# --- MENÚ TÁCTIL ---
tab1, tab2, tab3 = st.tabs(["🚀 ACCIÓN", "📊 RADAR", "⌨️ SHELL"])

# TAB 1: ACCIÓN REAL (KENYA & ÁMBAR)
with tab1:
    st.subheader("⚡ Purga de Nodo (Kenya)")
    st.info("Esta acción elimina archivos temporales reales del servidor de despliegue.")
    if st.button("EJECUTAR PURGA FÍSICA"):
        with st.spinner("Kenya operando..."):
            count = execute_system_purge()
            time.sleep(1)
            st.success(f"NÚCLEO LIMPIO: {count} archivos eliminados físicamente.")
            st.balloons()

# TAB 2: RADAR DE RED (PLOTLY REAL)
with tab2:
    st.subheader("🌐 Tráfico de Datos")
    net = psutil.net_io_counters()
    
    # Gráfico optimizado para pantalla vertical de A31
    fig = go.Figure(data=[
        go.Bar(name='Bytes', x=['Subida', 'Descarga'], y=[net.bytes_sent, net.bytes_recv], marker_color='#00FF00')
    ])
    fig.update_layout(paper_bgcolor='black', plot_bgcolor='black', font_color='#00FF00', height=350, margin=dict(l=10, r=10, t=10, b=10))
    st.plotly_chart(fig, use_container_width=True)

# TAB 3: STARK-SHELL (COMANDOS REALES)
with tab3:
    st.subheader("⌨️ Consola de Sistema")
    cmd = st.text_input("Ingrese comando (ej: ls, whoami, uname -a):")
    if st.button("EJECUTAR COMANDO"):
        try:
            # Ejecución real en el servidor
            resultado = subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT).decode()
            st.code(resultado, language="bash")
        except Exception as e:
            st.error(f"Kernel bloqueado o comando inválido: {e}")

# --- MONITOR LATERAL (PARA MÓVIL SE VE ABAJO) ---
st.write("---")
st.markdown("### 📊 ESTADO DE HARDWARE")
c1, c2 = st.columns(2)
c1.metric("CPU", f"{psutil.cpu_percent()}%")
c2.metric("RAM", f"{psutil.virtual_memory().percent}%")

st.markdown(f"<p style='text-align:center; opacity:0.3; font-size:0.6em;'>© 2026 SCARLET FUENMAYOR | A31_MOBILE_INTERFACE</p>", unsafe_allow_html=True)
