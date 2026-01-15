import streamlit as st
import psutil
import platform
import time

# --- CONFIGURACIÓN BÁSICA ---
st.set_page_config(page_title="EcoKernel AI", page_icon="⚡", layout="wide")

# --- CSS MINIMALISTA NEÓN ---
st.markdown("""
    <style>
    .stApp { background-color: #000000; color: #00FF00; font-family: 'Courier New', monospace; }
    .stark-card { border: 2px solid #00FF00; padding: 20px; border-radius: 10px; text-align: center; box-shadow: 0px 0px 20px #00FF00; }
    h1 { letter-spacing: 10px; text-shadow: 0px 0px 10px #00FF00; }
    </style>
""", unsafe_allow_html=True)

# --- HEADER ---
st.markdown('<div class="stark-card">', unsafe_allow_html=True)
st.title("⚡ ECOKERNEL AI")
st.subheader("GLOBAL GOVERNANCE CORE")
st.write(f"**ARCHITECT:** SCARLET FUENMAYOR DÍAZ")
st.markdown('</div>', unsafe_allow_html=True)

st.divider()

# --- TELEMETRÍA SEGURA ---
try:
    c1, c2 = st.columns(2)
    cpu = psutil.cpu_percent(interval=1)
    ram = psutil.virtual_memory().percent
    
    c1.metric("NÚCLEO_CPU", f"{cpu}%")
    c2.metric("MEMORIA_RAM", f"{ram}%")
    
    st.progress(cpu / 100)
    st.info(f"Sistema Operativo Detectado: {platform.system()} {platform.release()}")
except Exception as e:
    st.error(f"Error de lectura: {e}")

st.write("---")
st.caption("© 2026 Scarlet Fuenmayor | Caracas, Venezuela")
