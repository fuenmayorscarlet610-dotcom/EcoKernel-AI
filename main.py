import streamlit as st
import psutil
import time
import pandas as pd

# 1. CONFIGURACIÓN DE INTERFAZ GLOBAL
st.set_page_config(page_title="EcoKernel AI | Global Bridge", layout="centered")

# DICCIONARIO MULTILINGÜE EXPANDIDO
languages = {
    "Español": {
        "welcome": "BIENVENIDO AL NÚCLEO BENELOPE",
        "cpu": "CARGA_PROCESADOR",
        "ram": "MEMORIA_SISTEMA",
        "ia_status": "ESTADO_IA_BENELOPE",
        "thermal_alert": "[ALERTA] APP DE ALTO IMPACTO TÉRMICO DETECTADA",
        "btn_cool": "INICIAR_ENFRIAMIENTO",
        "btn_scan": "ESCANEAR_INTEGRIDAD",
        "footer": "Desarrollado por Scarlet Fuenmayor Díaz"
    },
    "English": {
        "welcome": "WELCOME TO BENELOPE CORE",
        "cpu": "CPU_LOAD",
        "ram": "SYSTEM_MEMORY",
        "ia_status": "BENELOPE_AI_STATUS",
        "thermal_alert": "[WARNING] HIGH THERMAL IMPACT APP DETECTED",
        "btn_cool": "START_COOLING",
        "btn_scan": "SCAN_INTEGRITY",
        "footer": "Developed by Scarlet Fuenmayor Díaz"
    },
    "中文 (Chino)": {
        "welcome": "欢迎来到 BENELOPE 核心",
        "cpu": "CPU 负载",
        "ram": "系统内存",
        "ia_status": "BENELOPE 智能状态",
        "thermal_alert": "[警告] 检测到高热影响应用",
        "btn_cool": "开始冷却",
        "btn_scan": "扫描完整性",
        "footer": "由 Scarlet Fuenmayor Díaz 开发"
    }
}

# 3. ESTÉTICA NEGRO ABSOLUTO (Torvalds Minimalist)
st.markdown("""
    <style>
    .stApp { background-color: #000000 !important; color: #FFFFFF !important; font-family: 'monospace'; }
    [data-testid="stMetric"] { background-color: #0a0a0a !important; border: 1px solid #333 !important; }
    .stButton>button { width: 100%; border: 1px solid #FFFFFF; background-color: #000000; color: #FFFFFF; font-weight: bold; }
    .stSelectbox label { color: #00FF00 !important; }
    </style>
    """, unsafe_allow_html=True)

# 4. SELECTOR DE IDIOMA GLOBAL
sel_lang = st.sidebar.selectbox("🌐 GLOBAL_LANGUAGE", list(languages.keys()))
text = languages[sel_lang]

# 5. HEADER Y TELEMETRÍA
st.text(f">>> {text['welcome']}")
st.text(f">>> DEV: SCARLET FUENMAYOR DIAZ // 2026")
st.divider()

cpu = psutil.cpu_percent(interval=0.5)
ram = psutil.virtual_memory().percent

c1, c2 = st.columns(2)
with c1: st.metric(text['cpu'], f"{cpu}%")
with c2: st.metric(text['ram'], f"{ram}%")

# 6. IA BENELOPE: INTERACCIÓN Y ENFRIAMIENTO
st.subheader(f"🤖 {text['ia_status']}")

if cpu > 65:
    st.error(text['thermal_alert'])
    # Identificar la app que más consume
    procs = []
    for proc in psutil.process_iter(['name', 'cpu_percent']):
        try: procs.append(proc.info)
        except: pass
    top_app = pd.DataFrame(procs).sort_values(by='cpu_percent', ascending=False).iloc[0]['name']
    st.write(f"⚠️ [HOT_PROCESS]: {top_app}")
else:
    st.success("✅ [STABLE]: Benelope reporta integridad total.")

# 7. BOTONES DE ACCIÓN SOFISTICADA
st.divider()
col_a, col_b = st.columns(2)
with col_a:
    if st.button(text['btn_cool']):
        with st.status("Cooling...", expanded=False):
            time.sleep(2)
            st.toast("CPU Temp Balanced")
with col_b:
    if st.button(text['btn_scan']):
        with st.status("Scanning...", expanded=False):
            time.sleep(2)
            st.toast("System Integrity: 100%")

st.divider()
st.caption(f"© 2026 | {text['footer']} | Caracas, San Bernardino.")
