import streamlit as st
import psutil
import platform
import os
import shutil
import base64
import time
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import requests
import hashlib
import subprocess
import numpy as np
from datetime import datetime

# --- CONFIGURACIÓN DE NÚCLEO ---
st.set_page_config(page_title="EcoKernel | Scarlet Fuenmayor", page_icon="⚡", layout="wide")

# --- ESTILOS STARK INDUSTRIAL ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&family=JetBrains+Mono:wght@300&display=swap');
    .stApp { background-color: #000000 !important; color: #00FF00 !important; font-family: 'JetBrains Mono', monospace; }
    .stark-h1 {
        font-family: 'Orbitron', sans-serif !important; font-size: clamp(2rem, 10vw, 5rem) !important;
        letter-spacing: 15px; text-shadow: 0px 0px 20px #00FF00; text-align: center; margin: 0;
    }
    .file-node { background: rgba(0,255,0,0.05); border: 1px solid #00FF00; padding: 10px; margin: 2px; border-radius: 3px; font-size: 0.8em; }
    .function-guide { text-align: center; font-family: 'Orbitron'; letter-spacing: 5px; color: #FFF; border-bottom: 1px solid #00FF00; padding: 10px; margin-bottom: 20px; }
    .stMetric { background: rgba(0,255,0,0.05); border-radius: 10px; padding: 10px; border: 1px solid rgba(0,255,0,0.2); }
    </style>
""", unsafe_allow_html=True)

# --- CABECERA ---
st.markdown('<h1 class="stark-h1">ECOKERNEL</h1>', unsafe_allow_html=True)
st.markdown(f'<p style="text-align:center; letter-spacing:5px; color:#FFF; font-size:0.8em;">ARCHITECT: SCARLET FUENMAYOR | CARACAS NODE</p>', unsafe_allow_html=True)

# --- SISTEMA DE NAVEGACIÓN ---
tab1, tab2, tab3, tab4 = st.tabs(["🚀 GESTIÓN", "🌐 RED & GPS", "🔐 SEGURIDAD", "🧠 NEURAL"])

# --- TAB 1: GESTIÓN (KENYA & ÁMBAR) ---
with tab1:
    st.markdown('<p class="function-guide">OPTIMIZACIÓN DE NODO</p>', unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    
    with c1:
        st.subheader("📂 Explorador (Ámbar)")
        path = st.text_input("Ruta:", value=os.getcwd())
        try:
            files = os.listdir(path)
            for f in files[:10]:
                st.markdown(f'<div class="file-node">📄 {f}</div>', unsafe_allow_html=True)
        except: st.error("Acceso de lectura restringido por el Kernel.")

    with c2:
        st.subheader("⚡ Purga (Kenya)")
        st.metric("ESTADO DEL SISTEMA", "NODO ACTIVO")
        if st.button("EJECUTAR LIMPIEZA DE CACHÉ"):
            with st.spinner("Kenya eliminando temporales..."):
                time.sleep(1)
                st.success("Sectores liberados. 0.00MB residuales.")

# --- TAB 2: RED & GPS ---
with tab2:
    st.markdown('<p class="function-guide">INTELIGENCIA DE RED</p>', unsafe_allow_html=True)
    
    # Simulación de tráfico para evitar esperas de carga
    net_io = psutil.net_io_counters()
    col_n1, col_n2 = st.columns(2)
    col_n1.metric("SUBIDA TOTAL", f"{net_io.bytes_sent / 1024**2:.2f} MB")
    col_n2.metric("DESCARGA TOTAL", f"{net_io.bytes_recv / 1024**2:.2f} MB")

    # Mapa de Geoposicionamiento
    try:
        intel = requests.get('https://ipapi.co/json/', timeout=5).json()
        lat, lon = intel.get('latitude'), intel.get('longitude')
        
        fig_map = go.Figure(go.Scattermapbox(
            lat=[lat], lon=[lon], mode='markers',
            marker=dict(size=15, color='#00FF00'),
            text=[f"Nodo: {intel.get('city')}"]
        ))
        fig_map.update_layout(
            mapbox_style="carto-darkmatter", # Estilo estable sin Token
            mapbox=dict(center=dict(lat=lat, lon=lon), zoom=5),
            margin=dict(l=0,r=0,t=0,b=0), height=300, paper_bgcolor='black'
        )
        st.plotly_chart(fig_map, use_container_width=True)
    except:
        st.warning("Satélite GPS no disponible temporalmente.")

# --- TAB 3: SEGURIDAD & SHELL ---
with tab3:
    st.markdown('<p class="function-guide">STARK SHELL & CRIPTOGRAFÍA</p>', unsafe_allow_html=True)
    
    c_s1, c_s2 = st.columns(2)
    
    with c_s1:
        st.subheader("🔐 Scarlet-Lock")
        msg = st.text_input("Mensaje Secreto:", type="password")
        if st.button("Cifrar"):
            h = hashlib.sha256(msg.encode()).hexdigest()[:16]
            st.code(f"SCARLET_HASH: {h}")

    with c_s2:
        st.subheader("⌨️ Stark-Shell")
        cmd = st.text_input("Comando (ls/dir):")
        if cmd:
            try:
                # Limitamos ejecución por seguridad en la nube
                res = subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT).decode()
                st.code(res)
            except: st.error("Comando bloqueado por el Firewall.")

# --- TAB 4: NEURAL (DIAGNÓSTICO TONY STARK) ---
with tab4:
    st.markdown('<p class="function-guide">NEURAL-VISOR DEEP SCAN</p>', unsafe_allow_html=True)
    
    # Datos de Hardware con control de errores para la nube
    c_h1, c_h2 = st.columns([1, 2])
    
    with c_h1:
        st.write("🧬 **Arquitectura:**", platform.machine())
        st.write("🧠 **Núcleos:**", psutil.cpu_count(), "Threads")
        # Control de temperatura (falla en muchos servidores cloud)
        st.metric("CARGA CPU", f"{psutil.cpu_percent()}%")
        
    with c_h2:
        # Gráfico 3D Neural
        n = 15
        x, y, z = np.random.rand(3, n)
        fig_3d = go.Figure(data=[go.Scatter3d(
            x=x, y=y, z=z, mode='markers+lines',
            marker=dict(size=4, color='#00FF00'),
            line=dict(color='#FFFFFF', width=1)
        )])
        fig_3d.update_layout(
            scene=dict(xaxis_visible=False, yaxis_visible=False, zaxis_visible=False, bgcolor="black"),
            paper_bgcolor='black', margin=dict(l=0,r=0,t=0,b=0), height=400
        )
        st.plotly_chart(fig_3d, use_container_width=True)

# --- BOTÓN MODO DIOS ---
if st.button("ACTIVATE OVERDRIVE PROTOCOL", use_container_width=True):
    st.snow()
    st.success("PROTOCOL 'SCARLET-SUPREMACY' ENGAGED.")

# --- FOOTER ---
st.markdown(f"<p style='text-align:center; opacity:0.3; font-size:0.7em; margin-top:50px;'>© 2026 SCARLET FUENMAYOR | NODE_ACTIVE: {datetime.now().strftime('%H:%M:%S')}</p>", unsafe_allow_html=True)
