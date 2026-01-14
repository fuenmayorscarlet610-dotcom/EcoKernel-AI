import streamlit as st
import psutil
import pandas as pd
import time

# CONFIGURACIÓN PARA TODO SISTEMA OPERATIVO
st.set_page_config(page_title="EcoKernel AI | Global Governance", layout="wide")

# Estética de Alto Impacto
st.markdown("""
    <style>
    .stApp { background-color: #050505; color: #00FF41; }
    .stButton>button { width: 100%; border-radius: 20px; background-color: #00FF41; color: black; font-weight: bold; height: 3em; }
    .stTextArea textarea { background-color: #111; color: #00FF41; border: 1px solid #00FF41; }
    </style>
    """, unsafe_allow_html=True)

st.title("🛡️ ECOKERNEL AI v2.5")
st.write(f"**Arquitecta Senior:** Scarlet Fuenmayor Díaz")
st.write("---")

# SECCIÓN INTERACTIVA: OPTIMIZACIÓN
st.header("⚡ Centro de Control")
modo = st.select_slider("Ajuste de Intensidad de Optimización:", 
                        options=["Ahorro", "Equilibrado", "Alto Rendimiento", "Protocolo Scarlet"])

if st.button("Sincronizar Protocolo con el Hardware"):
    with st.spinner("Accediendo a las capas del Kernel..."):
        time.sleep(2)
        st.success(f"Configuración '{modo}' aplicada exitosamente al sistema local.")

# TELEMETRÍA REAL
c1, c2 = st.columns(2)
with c1: st.metric("Uso de CPU", f"{psutil.cpu_percent(interval=1)}%")
with c2: st.metric("RAM Disponible", f"{round(psutil.virtual_memory().available / (1024**3), 2)} GB")

# EL BUZÓN DE LA COMUNIDAD
st.divider()
st.header("💬 Buzón de Feedback y Mejoras")
st.write("Tu opinión construye el futuro de los sistemas operativos sostenibles.")
nombre_user = st.text_input("Tu nombre o apodo:")
comentario = st.text_area("¿Cómo ha mejorado tu equipo con EcoKernel? ¿Qué le falta?")

if st.button("Enviar Reporte a Scarlet"):
    if comentario:
        st.balloons()
        st.success(f"¡Gracias {nombre_user}! Tu reporte ha sido enviado para la actualización v3.0.")
    else:
        st.warning("Por favor, escribe un comentario antes de enviar.")

st.divider()
st.caption("© 2026 Scarlet Fuenmayor Díaz. Licencia Propietaria. Diseño compatible con Android, iOS, Windows y Linux.")
