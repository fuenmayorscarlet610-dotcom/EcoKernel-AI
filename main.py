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

# --- CONFIGURACIÓN DE NUCLEO ---
st.set_page_config(page_title="EcoKernel | Scarlet Fuenmayor", layout="wide")

# --- FUNCIONES DE EJECUCIÓN REAL ---
def get_real_junk():
    """Escaneo real de directorios temporales del sistema operativo"""
    temp_dir = "/tmp" if platform.system() != "Windows" else os.environ.get('TEMP')
    junk_files = []
    total_size = 0
    if temp_dir and os.path.exists(temp_dir):
        for root, dirs, files in os.walk(temp_dir):
            for f in files:
                try:
                    fp = os.path.join(root, f)
                    total_size += os.path.getsize(fp)
                    junk_files.append(fp)
                except: continue
            if len(junk_files) > 1000: break # Seguridad para no saturar
    return total_size, junk_files

def run_stark_shell(command):
    """Ejecución directa en la terminal del sistema"""
    try:
        # Ejecuta el comando y captura la salida real
        output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT)
        return output.decode('utf-8')
    except subprocess.CalledProcessError as e:
        return f"ERROR_DE_KERNEL: {e.output.decode('utf-8')}"
    except Exception as e:
        return f"FALLA_CRITICA: {str(e)}"

# --- INTERFAZ STARK INDUSTRIAL ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&family=JetBrains+Mono&display=swap');
    .stApp { background-color: #000000; color: #00FF00; font-family: 'JetBrains Mono', monospace; }
    .stark-header { font-family: 'Orbitron'; text-align: center; color: #00FF00; text-shadow: 0 0 15px #00FF00; padding: 20px; }
    .console-box { background: #080808; border: 1px solid #00FF00; padding: 15px; border-radius: 5px; color: #00FF00; }
    </style>
""", unsafe_allow_html=True)

st.markdown('<h1 class="stark-header">ECOKERNEL v3.0</h1>', unsafe_allow_html=True)
st.write(f"**OPERADOR:** Scarlet Fuenmayor | **NODO:** {platform.node()} | **SISTEMA:** {platform.system()}")

# --- PANEL DE CONTROL ---
tab_sys, tab_net, tab_sec = st.tabs(["🚀 SISTEMA Y PURGA", "🌐 RED Y GPS", "🔐 STARK-SHELL"])

# 1. GESTIÓN DE SISTEMA (KENYA & ÁMBAR)
with tab_sys:
    st.subheader("⚡ Purga de Nodo (Kenya)")
    size, files = get_real_junk()
    c1, c2 = st.columns(2)
    c1.metric("BASURA REAL DETECTADA", f"{size / (1024*1024):.2f} MB")
    
    if st.button("EJECUTAR PURGA FÍSICA"):
        count = 0
        progress = st.progress(0)
        for i, f in enumerate(files[:200]): # Borra los primeros 200
            try:
                if os.path.isfile(f):
                    os.remove(f)
                    count += 1
                progress.progress((i + 1) / 200)
            except: continue
        st.success(f"PROCESO COMPLETADO: {count} archivos eliminados físicamente del servidor.")

# 2. RED Y TRÁFICO (MONITOR REAL)
with tab_net:
    st.subheader("🌐 Telemetría de Red")
    net1 = psutil.net_io_counters()
    time.sleep(0.5)
    net2 = psutil.net_io_counters()
    
    upspeed = (net2.bytes_sent - net1.bytes_sent) / 1024
    downspeed = (net2.bytes_recv - net1.bytes_recv) / 1024
    
    st.write(f"**Velocidad Actual:** ⬆️ {upspeed:.2f} KB/s | ⬇️ {downspeed:.2f} KB/s")
    
    # Gráfico Real Plotly
    fig = go.Figure(data=[go.Bar(x=['Upload', 'Download'], y=[upspeed, downspeed], marker_color='#00FF00')])
    fig.update_layout(paper_bgcolor='black', plot_bgcolor='black', font_color='#00FF00', height=300)
    st.plotly_chart(fig, use_container_width=True)

# 3. STARK-SHELL (COMANDOS REALES)
with tab_sec:
    st.subheader("⌨️ Stark-Shell: Acceso Root")
    command = st.text_input("Ingrese comando de sistema (ej: ls -la, df -h, whoami):")
    if st.button("EJECUTAR"):
        if command:
            resultado = run_stark_shell(command)
            st.markdown('<div class="console-box">', unsafe_allow_html=True)
            st.code(resultado, language="bash")
            st.markdown('</div>', unsafe_allow_html=True)

# --- FOOTER ---
st.sidebar.markdown("### 📊 RECURSOS REALES")
st.sidebar.write(f"CPU: {psutil.cpu_percent()}%")
st.sidebar.write(f"RAM: {psutil.virtual_memory().percent}%")
if st.sidebar.button("HARD RESET"): st.rerun()
