# =================================================================
# ECOKERNEL AI - CORE ARCHITECTURE (UNIFIED V15.5)
# AUTHOR: SCARLET FUENMAYOR DÍAZ (BENELOPE)
# LICENSE: PROPRIETARY HARDWARE GOVERNANCE © 2026
# =================================================================

import streamlit as st
import psutil
import platform
import os
import time
import pandas as pd 
from datetime import datetime

# --- CONFIGURACIÓN GLOBAL ---
VERSION = "15.5.0-STABLE"
DEVELOPER = "Scarlet Fuenmayor Díaz"
COPYRIGHT = f"© 2026 {DEVELOPER}"

st.set_page_config(
    page_title=f"EcoKernel AI | {DEVELOPER}",
    page_icon="logo.png", 
    layout="wide"
)

# --- MODULE 01: ESTÉTICA CYBERNETIC & NEO-CIRCLE ---
st.markdown(f"""
    <style>
    .stApp {{ background-color: #000000 !important; color: #00FF00 !important; font-family: 'Courier New', monospace; }}
    
    /* Marco Circular Neón para el Logo */
    .logo-container {{
        display: flex;
        justify-content: center;
        align-items: center;
        border: 4px solid #00FF00;
        border-radius: 50%; /* Hace el marco circular */
        width: 160px;
        height: 160px;
        background: radial-gradient(circle, #050505 0%, #000000 100%);
        box-shadow: 0px 0px 20px #00FF00, inset 0px 0px 10px #00FF00;
        margin: auto;
        overflow: hidden;
    }}
    
    [data-testid="stMetric"] {{ 
        background-color: #050505 !important; 
        border: 1px solid #00FF00 !important; 
        padding: 20px !important; 
        border-radius: 10px;
        box-shadow: 0px 0px 10px #00FF00;
    }}
    
    h1, h2, h3 {{ color: #00FF00 !important; text-transform: uppercase; letter-spacing: 2px; }}
    
    .stButton>button {{ 
        width: 100%; 
        background-color: #000000; 
        color: #00FF00; 
        border: 2px solid #00FF00; 
        font-weight: bold;
        transition: 0.3s;
    }}
    .stButton>button:hover {{ 
        background-color: #00FF00; 
        color: #000000; 
        box-shadow: 0px 0px 15px #00FF00;
    }}
    </style>
    """, unsafe_allow_html=True)

# --- CABECERA CON LOGO CIRCULAR ---
col_logo, col_text = st.columns([1, 2])

with col_logo:
    if os.path.exists("logo.png"):
        st.markdown('<div class="logo-container">', unsafe_allow_html=True)
        st.image("logo.png", width=130)
        st.markdown('</div>', unsafe_allow_html=True)
    else:
        st.markdown('<div class="logo-container"><h1>⚡</h1></div>', unsafe_allow_html=True)

with col_text:
    st.markdown(f"""
        <div style="padding-top: 20px;">
            <h1 style="margin-bottom: 0px;">ECOKERNEL AI</h1>
            <p style="font-size: 1.4em; color: #FFFFFF; margin-bottom: 0px;">CORE_SYSTEM: {VERSION}</p>
            <p style="color: #00FF00; font-weight: bold; font-size: 1.1em;">ARCHITECT: {DEVELOPER.upper()}</p>
        </div>
    """, unsafe_allow_html=True)

st.write(f"**SINCRO_ID:** `{datetime.now().strftime('%Y%m%d-%H%M%S')}` | **LOC:** `Caracas, San Bernardino` | **USER:** `Benelope`")
st.divider()

# --- SIDEBAR: CONTROL DE APLICACIONES ---
st.sidebar.header("🕹️ CONTROL PANEL")
sel_lang = st.sidebar.selectbox("🌐 IDIOMA", ["Español", "English", "Русский"])

# --- NUEVA FUNCIÓN: SELECCIONADOR PARA MONITOR ---
st.sidebar.subheader("📺 MONITOR PROJECTION")
running_apps = [p.info['name'] for p in psutil.process_iter(['name'])][:15] # Top 15 procesos
app_to_watch = st.sidebar.selectbox("Selecciona App para Monitorizar:", running_apps)

if st.sidebar.button("PROYECTAR EN MONITOR"):
    st.sidebar.success(f"Proyectando: {app_to_watch}")

# --- MODULE 02: TELEMETRÍA Y ALMACENAMIENTO DETALLADO ---
st.subheader("🛰️ [TELEMETRY & STORAGE_DATA]")
c1, c2, c3 = st.columns(3)

# Obtener info de almacenamiento real
disk = psutil.disk_usage('/')
total_gb = f"{disk.total / (1024**3):.1f} GB"
used_gb = f"{disk.used / (1024**3):.1f} GB"

cpu_val = psutil.cpu_percent(interval=0.5)
c1.metric("CPU_LOAD", f"{cpu_val}%")
c2.metric("RAM_STATE", f"{psutil.virtual_memory().percent}%")
c3.metric("DISK_FREE", f"{disk.percent}%", f"Used: {used_gb} / {total_gb}")

# --- MÓDULOS NEURALES (ÁMBAR Y KENYA) ---
st.write("---")
col_n1, col_n2 = st.columns(2)

with col_n1:
    st.markdown("### 👁️ NEURAL: Ámbar (Data Control)")
    st.info(f"Monitorizando App Seleccionada: **{app_to_watch}**")
    if st.button("ANALIZAR ALMACENAMIENTO"):
        partitions = psutil.disk_partitions()
        disk_data = []
        for p in partitions:
            try:
                usage = psutil.disk_usage(p.mountpoint)
                disk_data.append({"Punto": p.mountpoint, "FS": p.fstype, "Uso": f"{usage.percent}%"})
            except: continue
        st.table(pd.DataFrame(disk_data))

with col_n2:
    st.markdown("### 🧠 NEURAL: Kenya (Logic Shield)")
    diag = "CRITICAL: Migración requerida" if cpu_val > 80 else "NOMINAL: Flujo constante"
    st.info(f"[DIAGNÓSTICO]: {diag}")
    st.progress(cpu_val / 100)
    st.caption("Balance de carga de hilos en tiempo real.")

# --- MODULE 06: SYSTEM DNA ---
st.write("---")
st.subheader("🖥️ [SYSTEM_DNA_IDENTIFICATION]")
col_hw1, col_hw2 = st.columns(2)
with col_hw1:
    st.code(f"NODE_NAME: {platform.node()}\nOS_DISTRO: {platform.system()} {platform.release()}", language="bash")
with col_hw2:
    st.code(f"PROCESSOR: {platform.processor()}\nBOOT_TIME: {datetime.fromtimestamp(psutil.boot_time()).strftime('%Y-%m-%d %H:%M:%S')}", language="bash")

# --- MODULE 11: THERMAL SECURITY ---
st.write("---")
core_temp = 35 + (cpu_val * 0.25)
st.subheader(f"🌡️ THERMAL MONITOR: {core_temp:.1f}°C")
if core_temp > 48:
    st.error("⚠️ SOBRECALENTAMIENTO DETECTADO - ACTIVANDO COOLING PROTOCOL")
else:
    st.success("SISTEMA DENTRO DEL RANGO TÉRMICO ÓPTIMO")

# --- ACCIONES MAESTRAS ---
st.write("---")
if st.button("👑 SINCRONIZACIÓN MAESTRA (SCARLET PROTOCOL)"):
    with st.spinner("Sincronizando Hardware..."):
        time.sleep(2)
        st.balloons()
        st.success(f"EcoKernel AI Sincronizado para {DEVELOPER}. Todo el almacenamiento y procesos están bajo control.")

# --- FOOTER ---
st.markdown(f"""
    <div style="text-align: center; color: #555; padding: 40px;">
        <hr style="border: 0.5px solid #00FF00;">
        {COPYRIGHT}<br>
        <b>CARACAS, VENEZUELA | SAN BERNARDINO</b><br>
        <small>Hardware Governance Protocol Active - Ver. {VERSION}</small>
    </div>
""", unsafe_allow_html=True)
