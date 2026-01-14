import streamlit as st
import psutil
import pandas as pd
import plotly.graph_objects as go
from datetime import datetime

# CONFIGURACIÓN DE GRADO INDUSTRIAL
st.set_page_config(page_title="EcoKernel AI | Global Governance", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #050505; color: #00FF41; }
    .stMetric { background-color: #111; border: 1px solid #00FF41; border-radius: 10px; padding: 10px; }
    </style>
    """, unsafe_allow_html=True)

st.title("🛡️ ECOKERNEL AI v2.0")
st.write(f"**Arquitecta de Sistemas:** Scarlet Fuenmayor Díaz")
st.divider()

# TELEMETRÍA REAL
c1, c2, c3 = st.columns(3)
cpu = psutil.cpu_percent(interval=1)
ram = psutil.virtual_memory().percent
boot = datetime.fromtimestamp(psutil.boot_time()).strftime("%H:%M:%S")

with c1: st.metric("NÚCLEO CPU", f"{cpu}%")
with c2: st.metric("MEMORIA RAM", f"{ram}%")
with c3: st.metric("UPTIME", boot)

# AUDITORÍA DE PROCESOS
st.subheader("🔍 Auditoría de Procesos Activos")
procs = []
for proc in psutil.process_iter(['pid', 'name', 'cpu_percent']):
    try: procs.append(proc.info)
    except: pass
df = pd.DataFrame(procs).sort_values(by='cpu_percent', ascending=False).head(8)
st.table(df)

# GOBERNANZA AMBIENTAL
st.divider()
eco_score = 100 - cpu
st.write(f"### 🌱 Eco-Score del Sistema: {eco_score}/100")
st.progress(eco_score / 100)

st.caption("© 2026 Scarlet Fuenmayor Díaz. Licencia Propietaria de Gobernanza de Hardware.")
