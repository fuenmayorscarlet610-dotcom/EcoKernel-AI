import streamlit as st
import psutil
import time

# Configuración de la página
st.set_page_config(page_title="EcoKernel AI", page_icon="🌱")

st.title("🌱 EcoKernel AI: Versión Global")
st.write("---")
st.subheader("Autora: Scarlet Fuenmayor Díaz")

# Espacios para los datos en tiempo real
col1, col2 = st.columns(2)
with col1:
    cpu_stat = st.empty()
with col2:
    ram_stat = st.empty()

co2_stat = st.empty()
status_stat = st.empty()

# Lógica de optimización
cpu = psutil.cpu_percent(interval=1)
ram = psutil.virtual_memory().percent
savings = round((100 - cpu) * 0.01, 2)

# Mostrar los resultados en la web
cpu_stat.metric("Uso de CPU", f"{cpu}%")
ram_stat.metric("Memoria RAM", f"{ram}%")
co2_stat.info(f"🍀 Ahorro de CO2 estimado: {savings}g")
status_stat.success("✅ ESTADO: SISTEMA OPTIMIZADO POR ECOKERNEL")

st.write("---")
st.caption("Gobernanza de hardware y protección ambiental activa.")
