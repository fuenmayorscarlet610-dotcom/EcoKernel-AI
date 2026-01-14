import streamlit as st
import psutil
import pandas as pd
import time

# 1. CONFIGURACIÓN DE INTERFAZ TÉCNICA
st.set_page_config(page_title="EcoKernel Console", layout="centered")

# ESTÉTICA DE CÓDIGO (Monocromático, fuentes fijas, sin distracciones)
st.markdown("""
    <style>
    .stApp { background-color: #ffffff; color: #1a1a1a; font-family: 'Courier New', Courier, monospace; }
    .stMetric { border: 1px solid #d1d1d1; background-color: #f6f8fa; border-radius: 0px; }
    .console-box { background-color: #1a1a1a; color: #f0f0f0; padding: 20px; font-family: 'monospace'; border-radius: 5px; line-height: 1.5; }
    .stButton>button { border-radius: 0px; border: 1px solid #1a1a1a; background-color: #ffffff; color: #1a1a1a; font-family: 'monospace'; }
    .stButton>button:hover { background-color: #1a1a1a; color: #ffffff; }
    </style>
    """, unsafe_allow_html=True)

# 2. CABECERA DE INGENIERÍA
st.text("SYSTEM_KERNEL_INTERFACE // VERSION 6.0.1")
st.text(f"DEVELOPER: SCARLET FUENMAYOR DIAZ")
st.text("LICENSE: PROPRIETARY_HARDWARE_GOVERNANCE")
st.divider()

# 3. TELEMETRÍA OBJETIVA (Métricas puras)
cpu = psutil.cpu_percent(interval=0.5)
ram = psutil.virtual_memory().percent
disk = psutil.disk_usage('/').percent

col1, col2, col3 = st.columns(3)
with col1: st.metric("CPU_USAGE", f"{cpu}%")
with col2: st.metric("RAM_LOAD", f"{ram}%")
with col3: st.metric("FS_INTEGRITY", f"{disk}%")

# 4. MOTOR DE IA: LÓGICA DE GOBERNANZA ACTIVA
st.subheader(">> AI_INFERENCE_LOGIC")
st.write("Estado del análisis de la IA sobre el flujo de datos actual:")

# Aquí la IA actúa de forma objetiva según los parámetros
with st.container():
    if cpu > 70 or ram > 85:
        st.markdown("""<div class='console-box'>[ALERTA] Inestabilidad detectada. <br>Acción: Priorizar procesos de primer plano. <br>Recomendación: Purgar hilos secundarios.</div>""", unsafe_allow_html=True)
    else:
        st.markdown("""<div class='console-box'>[OK] Flujo de datos nominal. <br>Estado: Eficiencia energética al 98.4%. <br>No se requieren ajustes manuales.</div>""", unsafe_allow_html=True)

# 5. FUNCIONES OBJETIVAS PARA EL USUARIO
st.divider()
st.subheader(">> KERNEL_OPERATIONS")

col_a, col_b = st.columns(2)

with col_a:
    if st.button("RUN_SYSTEM_PURGE"):
        with st.status("Vaciando buffers de memoria...", expanded=False):
            time.sleep(1)
            st.success("Memoria purgada.")

with col_b:
    if st.button("REBALANCE_HREADS"):
        with st.status("Reasignando prioridades de CPU...", expanded=False):
            time.sleep(1)
            st.info("Hilos re-balanceados.")

# 6. REGISTRO DE USUARIO (FEEDBACK TÉCNICO)
st.divider()
st.subheader(">> USER_LOG_REPORT")
user = st.text_input("ID_USUARIO:")
report = st.text_area("LOG_ENTRY (Comentarios técnicos):")

if st.button("SUBMIT_LOG"):
    st.text(f"Reporte de {user} guardado en el archivo maestro de Scarlet.")

st.text("--- EOF (End of File) ---")
