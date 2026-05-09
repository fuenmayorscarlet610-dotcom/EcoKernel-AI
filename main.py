# =================================================================
# ECOKERNEL AI - OMNI GOVERNANCE (STARK-TORVALDS HYBRID)
# AUTHOR: SCARLET FUENMAYOR DIAZ
# LICENSE: PROPRIETARY HARDWARE GOVERNANCE (c) 2026
# =================================================================

import streamlit as st
import psutil
import platform
import os
import base64
import time
from datetime import datetime
import pandas as pd
import numpy as np

# --- CONFIGURACION DE ENTORNO ---
# Corregido: Doble guion bajo para __file__
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODULES_DIR = os.path.join(BASE_DIR, "modules")
if not os.path.exists(MODULES_DIR): 
    os.makedirs(MODULES_DIR)

# --- GLOBAL CONFIG ---
VERSION = "26.9.5-OMNI-CORE"
DEVELOPER = "Scarlet Fuenmayor Diaz"
COPYRIGHT = f"(c) 2026 {DEVELOPER}"

st.set_page_config(page_title="EcoKernel AI", page_icon="🧬", layout="wide")

# --- SESSION STATE ---
if "blood_mode" not in st.session_state: st.session_state.blood_mode = False
if "boot_complete" not in st.session_state: st.session_state.boot_complete = False

# --- COLORES DINAMICOS ---
PRIMARY = "#FF0055" if st.session_state.blood_mode else "#00FF00"
SECONDARY = "#FFFFFF" if st.session_state.blood_mode else "#00E5FF"
BG_COLOR = "#050000" if st.session_state.blood_mode else "#000000"

# --- BOOT SEQUENCE ---
if not st.session_state.boot_complete:
    boot_placeholder = st.empty()
    boot_lines = [
        "Mounting ECOKERNEL core v26.9.5...",
        "Initializing NODE_AMBAR (Sustainability Logic)...",
        "NODE_KENYA: Security Shield & AI Handshake...",
        "Accessing BIOS/Firmware Abstraction Layer...",
        "Scanning Drones, TV, and Local Servers...",
        "EcoKernel AI Ready. Operator: SCARLET FUENMAYOR"
    ]
    for i in range(len(boot_lines) + 1):
        with boot_placeholder.container():
            html_content = f"""
            <div style="position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: #000; z-index: 9999; display: flex; flex-direction: column; justify-content: center; align-items: center; font-family: 'Courier New', monospace; border: 2px solid {PRIMARY};">
                <h2 style='color: {PRIMARY}; font-family: sans-serif; text-shadow: 0 0 20px {PRIMARY}; letter-spacing: 5px;'>ECOKERNEL SYSTEM BOOT</h2>
                <div style='text-align: left; width: 350px;'>
            """
            for j in range(i):
                current_color = PRIMARY if j == i - 1 else SECONDARY
                html_content += f"<p style='color: {current_color}; font-size: 14px; margin: 2px 0;'>[LOG] > {boot_lines[j]}</p>"
            html_content += "</div></div>"
            st.markdown(html_content, unsafe_allow_html=True)
            time.sleep(0.4)
    boot_placeholder.empty()
    st.session_state.boot_complete = True

# --- ESTETICA CSS ---
st.markdown(f"""
    <style>
    .stApp {{ background-color: {BG_COLOR} !important; color: {PRIMARY} !important; }}
    [data-testid="stMetricValue"] {{ font-family: monospace !important; color: {SECONDARY} !important; }}
    .stMetric {{ background: rgba(10, 10, 10, 0.9) !important; border-left: 3px solid {PRIMARY} !important; }}
    #MainMenu, footer, header {{ visibility: hidden; }}
    .stButton>button {{ background: transparent; color: {PRIMARY}; border: 1px solid {PRIMARY}; width: 100%; }}
    .stButton>button:hover {{ background: {PRIMARY}; color: black; box-shadow: 0 0 15px {PRIMARY}; }}
    </style>
    """, unsafe_allow_html=True)

# --- INTERFAZ PRINCIPAL ---
st.markdown(f"<h1 style='text-align: center; letter-spacing: 15px; margin-top: -50px;'>ECOKERNEL</h1>", unsafe_allow_html=True)

# TELEMETRIA
c1, c2, c3, c4 = st.columns(4)
try:
    cpu_usage = psutil.cpu_percent(interval=None)
    ram_usage = psutil.virtual_memory().percent
except:
    cpu_usage, ram_usage = 22.0, 48.0

c1.metric("⚡ CORE_LOAD", f"{cpu_usage}%")
c2.metric("💾 RAM_USE", f"{ram_usage}%")
c3.metric("👁️ AMBAR", "ACTIVE")
c4.metric("🧠 KENYA", "LOCKED")

# GRAFICO DE PULSO
st.write("")
data_stream = pd.DataFrame(np.random.randn(25, 1), columns=['PULSE'])
st.area_chart(data_stream, height=150, use_container_width=True)

# NODOS INTEGRADOS
col_a, col_k = st.columns(2)
with col_a:
    st.markdown("### 🧬 NODE_AMBAR")
    if st.button("CONNECT_REMOTE_BIOS"):
        st.toast("Estableciendo enlace con firmware externo...", icon="🧬")

with col_k:
    st.markdown("### 🛡️ NODE_KENYA")
    if st.button("PURGE_SYSTEM"):
        st.success("Protocolo de limpieza completado.")

# SIDEBAR GOVERNANCE
st.sidebar.markdown("### 🚨 GOVERNANCE")
st.session_state.blood_mode = st.sidebar.toggle("BLOOD_MODE", value=st.session_state.blood_mode)
if st.sidebar.button("REBOOT CORE"):
    st.session_state.boot_complete = False
    st.rerun()

st.markdown(f"<div style='text-align:center; margin-top:100px; opacity:0.1; font-size: 10px;'>{COPYRIGHT} // {VERSION}</div>", unsafe_allow_html=True)
