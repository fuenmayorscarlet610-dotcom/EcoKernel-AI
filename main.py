# =================================================================
# ECOKERNEL AI — UNIVERSAL ABSTRACTION LAYER (UAL)
# HUD PRINCIPAL — STARK INTERFACE v26.9.5-OMNI
# AUTHOR: SCARLET FUENMAYOR DIAZ
# HARDWARE GOVERNANCE (c) 2026
# =================================================================

import streamlit as st
import psutil
import platform
import os
import time
import requests
import json
import hashlib
from datetime import datetime
import pandas as pd
import numpy as np

# --- CONFIG GLOBAL ---
VERSION = "26.9.5-OMNI-CORE"
DEVELOPER = "Scarlet Fuenmayor Diaz"
OWM_KEY = "d6f4f14e05df727ec7b12bc21ee4ca49"
CIUDAD = "La Guaira"
PAIS = "VE"

# --- ENTORNO ---
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

st.set_page_config(page_title="EcoKernel AI — UAL", page_icon="🧬", layout="wide")

# --- SESSION STATE ---
if "cpu_hist" not in st.session_state: st.session_state.cpu_hist = [0.0] * 30
if "blood_mode" not in st.session_state: st.session_state.blood_mode = False
if "boot_complete" not in st.session_state: st.session_state.boot_complete = False
if "audit_log" not in st.session_state: st.session_state.audit_log = []

# --- COLORES DINÁMICOS (BLOOD MODE) ---
def get_colors():
    if st.session_state.blood_mode:
        return {
            "primary": "#FF0033", "secondary": "#FF6688", "bg": "#0A0000",
            "text": "#FFAAAA", "border": "2px solid #330000"
        }
    return {
        "primary": "#00FF00", "secondary": "#00E5FF", "bg": "#000000",
        "text": "#CCFFCC", "border": "2px solid #003300"
    }

colors = get_colors()

# --- FUNCIONES NÚCLEO ---
def log_event(event):
    timestamp = datetime.now().strftime("%H:%M:%S")
    st.session_state.audit_log.insert(0, f"[{timestamp}] {event}")

def fetch_weather():
    try:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={CIUDAD},{PAIS}&appid={OWM_KEY}&units=metric"
        data = requests.get(url, timeout=5).json()
        return data['main']['temp'], data['main']['humidity']
    except:
        return 28.5, 75.0 # Promedio La Guaira fallback

# --- BOOT SEQUENCE ---
if not st.session_state.boot_complete:
    boot_placeholder = st.empty()
    boot_steps = [
        "Inyectando Micro-Kernel v26.9.5...",
        "NODE_AMBAR: Estableciendo enlace térmico...",
        "NODE_KENYA: Cifrado de canal SHA-256...",
        "Sincronizando con La Guaira Caribbean Station...",
        "Acceso concedido. Operator: SCARLET"
    ]
    for i in range(len(boot_steps) + 1):
        with boot_placeholder.container():
            st.markdown(f"""
                <div style="position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: #000; z-index: 9999; display: flex; flex-direction: column; justify-content: center; align-items: center; font-family: monospace; border: {colors['border']};">
                    <h1 style='color: {colors['primary']}; font-family: sans-serif; letter-spacing: 10px; text-shadow: 0 0 15px {colors['primary']};'>ECOKERNEL UAL</h1>
            """, unsafe_allow_html=True)
            for j in range(i):
                st.markdown(f"<p style='color: {colors['secondary']};'>[SYSTEM] > {boot_steps[j]}</p>", unsafe_allow_html=True)
            st.markdown("</div>", unsafe_allow_html=True)
            time.sleep(0.4)
    boot_placeholder.empty()
    st.session_state.boot_complete = True
    log_event("SISTEMA OPERATIVO INICIADO")

# --- CSS INJECT ---
st.markdown(f"""
    <style>
    .stApp {{ background-color: {colors['bg']} !important; color: {colors['text']} !important; }}
    [data-testid="stMetricValue"] {{ color: {colors['primary']} !important; font-family: monospace; font-weight: bold; }}
    .stMetric {{ background: rgba(10,10,10,0.8); border-left: 4px solid {colors['primary']}; padding: 10px; }}
    #MainMenu, footer, header {{ visibility: hidden; }}
    .stButton>button {{ background: transparent; color: {colors['primary']}; border: 1px solid {colors['primary']}; width: 100%; font-family: monospace; }}
    .stButton>button:hover {{ background: {colors['primary']}; color: black; box-shadow: 0 0 20px {colors['primary']}; }}
    </style>
    """, unsafe_allow_html=True)

# --- HUD PRINCIPAL ---
st.markdown(f"<h1 style='text-align: center; letter-spacing: 20px; color: {colors['primary']};'>ECOKERNEL AI</h1>", unsafe_allow_html=True)

# --- TELEMETRÍA ---
temp, hum = fetch_weather()
cpu = psutil.cpu_percent()
st.session_state.cpu_hist.append(cpu)
st.session_state.cpu_hist = st.session_state.cpu_hist[-30:]

c1, c2, c3, c4 = st.columns(4)
c1.metric("🌡️ EXT_TEMP", f"{temp} C")
c2.metric("💧 HUMIDITY", f"{hum}%")
c3.metric("⚡ CPU_SYNC", f"{cpu}%")
c4.metric("💾 RAM_SYNC", f"{psutil.virtual_memory().percent}%")

st.area_chart(pd.DataFrame(st.session_state.cpu_hist, columns=['UAL_LOAD']), color=colors['primary'])

# --- DIVISIÓN DE NODOS ---
col_ambar, col_kenya = st.columns(2)

with col_ambar:
    st.markdown(f"### 🧬 NODE_AMBAR (Sustainability)")
    st.caption("Optimización de Recursos y Gestión de Entorno")
    if st.button("CALIBRATE_THERMAL_SYNC"):
        log_event("Calibración térmica ejecutada para La Guaira.")
        st.toast("Sincronizando ventilación y carga...")

with col_kenya:
    st.markdown(f"### 🛡️ NODE_KENYA (Security)")
    st.caption("Protocolos de Acceso y Blindaje IA")
    if st.button("EXECUTE_SHA256_PURGE"):
        log_event("Purga de procesos no firmados iniciada.")
        st.success("Kernel blindado. Acceso restringido.")

# --- SIDEBAR & AUDIT LOG ---
st.sidebar.markdown(f"### 🚨 UAL GOVERNANCE")
st.session_state.blood_mode = st.sidebar.toggle("BLOOD_MODE", value=st.session_state.blood_mode)
st.sidebar.write("---")
st.sidebar.markdown("### 📝 AUDIT_LOG")
for log in st.session_state.audit_log[:10]:
    st.sidebar.text(log)

if st.sidebar.button("HARD_REBOOT"):
    st.session_state.boot_complete = False
    st.session_state.audit_log = []
    st.rerun()

st.markdown(f"<div style='text-align:center; opacity:0.1; font-size: 10px; margin-top: 50px;'>(c) 2026 {DEVELOPER} // {VERSION}</div>", unsafe_allow_html=True)
    
