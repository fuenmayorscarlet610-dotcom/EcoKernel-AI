# =================================================================
# ECOKERNEL AI - OMNI GOVERNANCE (STARK-TORVALDS HYBRID)
# AUTHOR: SCARLET FUENMAYOR DIAZ
# LICENSE: PROPRIETARY HARDWARE GOVERNANCE (c) 2026
# =================================================================

import streamlit as st
import psutil
import os
import time
import requests
import pandas as pd
import numpy as np
from datetime import datetime

# --- CONFIGURACION - API KEY DIRECTA ---
OWM_KEY = "d6f4f14e05df727ec7b12bc21ee4ca49"
CIUDAD = "La Guaira"
PAIS = "VE"

# --- CONFIGURACION DE ENTORNO ---
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
VERSION = "26.9.5-OMNI-CORE"
DEVELOPER = "Scarlet Fuenmayor Diaz"
COPYRIGHT = f"(c) 2026 {DEVELOPER}"

st.set_page_config(page_title="EcoKernel AI", page_icon="🧬", layout="wide")

# --- SESSION STATE ---
if "cpu_hist" not in st.session_state: st.session_state.cpu_hist = [0.0] * 25
if "blood_mode" not in st.session_state: st.session_state.blood_mode = False
if "boot_complete" not in st.session_state: st.session_state.boot_complete = False

# --- COLORES DINAMICOS ---
PRIMARY = "#FF0055" if st.session_state.blood_mode else "#00FF00"
SECONDARY = "#FFFFFF" if st.session_state.blood_mode else "#00E5FF"
BG_COLOR = "#050000" if st.session_state.blood_mode else "#000000"

# --- FUNCIONES DE DATOS REALES ---
def fetch_clima():
    """Obtiene datos REALES de La Guaira"""
    try:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={CIUDAD},{PAIS}&appid={OWM_KEY}&units=metric"
        resp = requests.get(url, timeout=5).json()
        temp = f"{resp['main']['temp']:.1f} C"
        hum = f"{resp['main']['humidity']}%"
        return temp, hum
    except:
        return "--", "--"

# --- BOOT SEQUENCE ---
if not st.session_state.boot_complete:
    boot_placeholder = st.empty()
    boot_lines = [
        "Mounting ECOKERNEL core v26.9.5...",
        f"Sincronizando con estacion {CIUDAD}...",
        "NODE_AMBAR: Estableciendo logica sustentable...",
        "NODE_KENYA: Handshake de seguridad IA...",
        "EcoKernel AI Ready. Bienvenida, Scarlet."
    ]
    for i in range(len(boot_lines) + 1):
        with boot_placeholder.container():
            html = f"""
            <div style="position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: #000; z-index: 9999; display: flex; flex-direction: column; justify-content: center; align-items: center; font-family: monospace; border: 2px solid {PRIMARY};">
                <h2 style='color: {PRIMARY}; text-shadow: 0 0 20px {PRIMARY};'>SYSTEM BOOTING...</h2>
                <div style='text-align: left; width: 350px;'>
            """
            for j in range(i):
                c = PRIMARY if j == i-1 else SECONDARY
                html += f"<p style='color: {c}; font-size: 14px; margin: 2px 0;'>[LOG] > {boot_lines[j]}</p>"
            html += "</div></div>"
            st.markdown(html, unsafe_allow_html=True)
            time.sleep(0.4)
    boot_placeholder.empty()
    st.session_state.boot_complete = True

# --- CSS INTERFACE ---
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

# --- CABECERA ---
st.markdown(f"<h1 style='text-align: center; font-family: sans-serif; letter-spacing: 15px;'>ECOKERNEL</h1>", unsafe_allow_html=True)
st.markdown(f"<p style='text-align: center; color: {SECONDARY}; opacity: 0.6;'>LOCATION: {CIUDAD}, VE | {datetime.now().strftime('%H:%M:%S')}</p>", unsafe_allow_html=True)

# --- TELEMETRIA REAL ---
st.write("---")
t_real, h_real = fetch_clima()
c1, c2, c3, c4 = st.columns(4)

# Update hardware stats
cpu_usage = psutil.cpu_percent()
st.session_state.cpu_hist.append(cpu_usage)
st.session_state.cpu_hist = st.session_state.cpu_hist[-25:]

c1.metric("🌡️ TEMP_EXT", t_real)
c2.metric("💧 HUMIDITY", h_real)
c3.metric("⚡ CPU_SYNC", f"{cpu_usage}%")
c4.metric("💾 RAM_SYNC", f"{psutil.virtual_memory().percent}%")

# --- GRAFICO DE PULSO ---
st.write("")
st.area_chart(pd.DataFrame(st.session_state.cpu_hist, columns=['CPU']), color=PRIMARY)

# --- NODOS DE CONTROL ---
col_a, col_k = st.columns(2)
with col_a:
    st.markdown("### 🧬 NODE_AMBAR")
    if st.button("OPTIMIZE_FOR_HEAT"):
        st.toast("Calibrando para clima caribeño...")
with col_k:
    st.markdown("### 🛡️ NODE_KENYA")
    if st.button("ENCRYPT_ACCESS"):
        st.success("Protocolo de blindaje activo.")

# --- SIDEBAR ---
st.sidebar.markdown("### 🚨 GOVERNANCE")
st.session_state.blood_mode = st.sidebar.toggle("BLOOD_MODE", value=st.session_state.blood_mode)
if st.sidebar.button("REBOOT CORE"):
    st.session_state.boot_complete = False
    st.rerun()

st.markdown(f"<div style='text-align:center; margin-top:100px; opacity:0.1; font-size: 10px;'>{COPYRIGHT} // {VERSION}</div>", unsafe_allow_html=True)
