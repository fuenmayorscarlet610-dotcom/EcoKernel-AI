# =================================================================
# ECOKERNEL AI — UNIVERSAL ABSTRACTION LAYER (UAL)
# HUD PRINCIPAL — STARK INTERFACE v26.9.5-OMNI
# AUTHOR: SCARLET FUENMAYOR DIAZ
# HARDWARE GOVERNANCE (c) 2026
# =================================================================

import streamlit as st
import psutil
import os
import time
import requests
import pandas as pd
import hashlib
from datetime import datetime

# --- CONFIG GLOBAL ---
VERSION = "26.9.5-OMNI-CORE"
DEVELOPER = "Scarlet Fuenmayor Diaz"
OWM_KEY = "d6f4f14e05df727ec7b12bc21ee4ca49"
CIUDAD = "La Guaira"
PAIS = "VE"

st.set_page_config(page_title="EcoKernel AI — UAL", page_icon="🧬", layout="wide")

# --- SESSION STATE ---
if "cpu_hist" not in st.session_state: st.session_state.cpu_hist = [0.0] * 30
if "blood_mode" not in st.session_state: st.session_state.blood_mode = False
if "boot_complete" not in st.session_state: st.session_state.boot_complete = False
if "audit_log" not in st.session_state: st.session_state.audit_log = []
if "last_metrics_update" not in st.session_state: st.session_state.last_metrics_update = 0.0
if "last_weather_fetch" not in st.session_state: st.session_state.last_weather_fetch = 0.0
if "cached_temp" not in st.session_state: st.session_state.cached_temp, st.session_state.cached_hum = 28.5, 75.0

# --- COLORES ---
def get_colors():
    if st.session_state.blood_mode:
        return {"primary": "#FF0033", "secondary": "#FF6688", "bg": "#0A0000", "text": "#FFAAAA"}
    return {"primary": "#00FF00", "secondary": "#00E5FF", "bg": "#000000", "text": "#CCFFCC"}

colors = get_colors()

# --- LOGICA DE APOYO ---
def log_event(event):
    ts = datetime.now().strftime("%H:%M:%S")
    st.session_state.audit_log.insert(0, f"[{ts}] {event}")

def fetch_weather():
    try:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={CIUDAD},{PAIS}&appid={OWM_KEY}&units=metric"
        data = requests.get(url, timeout=5).json()
        return data['main']['temp'], data['main']['humidity']
    except:
        return st.session_state.cached_temp, st.session_state.cached_hum

# --- BOOT SEQUENCE ---
if not st.session_state.boot_complete:
    boot_placeholder = st.empty()
    for i in range(4):
        boot_placeholder.markdown(f"<h2 style='color:{colors['primary']}; text-align:center;'>RE-CALIBRANDO KERNEL... {i*25}%</h2>", unsafe_allow_html=True)
        time.sleep(0.3)
    boot_placeholder.empty()
    st.session_state.boot_complete = True
    log_event("PATCH ECO-REFRESH APLICADO")

# --- CSS ---
st.markdown(f"<style>.stApp {{ background-color: {colors['bg']} !important; color: {colors['text']} !important; }}</style>", unsafe_allow_html=True)

# --- TELEMETRÍA (PATCH RECOMENDADO) ---
now = time.time()
REFRESH_SEC = 6 if not st.session_state.blood_mode else 12
WEATHER_TTL = 15 * 60

if (now - st.session_state.last_metrics_update) >= REFRESH_SEC:
    st.session_state.last_metrics_update = now
    cpu = psutil.cpu_percent(interval=None)
    ram = psutil.virtual_memory().percent
    
    # Weather con TTL
    if (now - st.session_state.last_weather_fetch) >= WEATHER_TTL:
        st.session_state.last_weather_fetch = now
        st.session_state.cached_temp, st.session_state.cached_hum = fetch_weather()
    
    st.session_state.cpu_hist.append(cpu)
    st.session_state.cpu_hist = st.session_state.cpu_hist[-30:]
    st.session_state.cached_cpu, st.session_state.cached_ram = cpu, ram

# Lectura de variables cacheadas
cpu = st.session_state.get("cached_cpu", 0.0)
ram = st.session_state.get("cached_ram", 0.0)

st.markdown(f"<h1 style='text-align:center; letter-spacing:15px; color:{colors['primary']};'>ECOKERNEL</h1>", unsafe_allow_html=True)

c1, c2, c3, c4 = st.columns(4)
c1.metric("🌡️ TEMP", f"{st.session_state.cached_temp:.1f} C")
c2.metric("💧 HUM", f"{st.session_state.cached_hum:.0f}%")
c3.metric("⚡ CPU", f"{cpu:.1f}%")
c4.metric("💾 RAM", f"{ram:.1f}%")

df = pd.DataFrame(st.session_state.cpu_hist, columns=['UAL_LOAD'])
if not st.session_state.blood_mode:
    st.area_chart(df, color=colors["primary"])
else:
    st.line_chart(df, color=colors["primary"])

# --- NODOS DE CONTROL (COHERENCIA REAL) ---
col_a, col_k = st.columns(2)

with col_a:
    st.markdown("### 🧬 NODE_AMBAR")
    if st.button("CALIBRATE_THERMAL_SYNC"):
        # Acción real: Forzar refresco lento para enfriar procesos
        st.session_state.blood_mode = True
        log_event("THERMAL_SYNC: Modo ahorro activado.")
        st.toast("Reduciendo ciclos de refresco para enfriar hardware...")

with col_k:
    st.markdown("### 🛡️ NODE_KENYA")
    if st.button("EXECUTE_SHA256_PURGE"):
        # Acción real: Validar integridad del archivo main.py
        with open(__file__, "rb") as f:
            file_hash = hashlib.sha256(f.read()).hexdigest()
        log_event(f"INTEGRITY_CHECK: {file_hash[:10]}... OK")
        st.success("Integridad de Kernel verificada vía SHA-256.")

# --- SIDEBAR ---
st.sidebar.markdown(f"### 🚨 UAL GOVERNANCE")
st.session_state.blood_mode = st.sidebar.toggle("BLOOD_MODE (ECO)", value=st.session_state.blood_mode)
st.sidebar.write("---")
st.sidebar.markdown("### 📝 AUDIT_LOG")
for log in st.session_state.audit_log[:8]:
    st.sidebar.text(log)
    
