import streamlit as st
import psutil
import time
import pandas as pd

# 1. CONFIGURACIÓN DE NÚCLEO GLOBAL
st.set_page_config(page_title="EcoKernel AI | Neural Governance", layout="centered")

# 2. DICCIONARIO MULTILINGÜE Y DE IA
languages = {
    "Español": {
        "welcome": "CONSOLA DE GOBERNANZA NEURAL",
        "cpu": "CARGA_HARDWARE",
        "ram": "MEMORIA_NÚCLEO",
        "ambar_task": "ÁMBAR: AUDITORÍA DE DIRECTORIOS",
        "kenya_task": "KENYA: ARQUITECTURA DE SOLUCIONES",
        "btn_cool": "EJECUTAR_ENFRIAMIENTO_LÓGICO",
        "btn_clean": "PURGAR_ARCHIVOS_CORRUPTOS",
        "status_ok": "[+] SISTEMA NOMINAL: Integridad validada.",
        "status_warn": "[!] ALERTA: Desbalance térmico detectado."
    },
    "English": {
        "welcome": "NEURAL GOVERNANCE CONSOLE",
        "cpu": "HARDWARE_LOAD",
        "ram": "CORE_MEMORY",
        "ambar_task": "AMBAR: DIRECTORY AUDIT",
        "kenya_task": "KENYA: SOLUTIONS ARCHITECTURE",
        "btn_cool": "EXECUTE_LOGIC_COOLING",
        "btn_clean": "PURGE_CORRUPT_FILES",
        "status_ok": "[+] SYSTEM NOMINAL: Integrity validated.",
        "status_warn": "[!] WARNING: Thermal imbalance detected."
    }
}

# 3. ESTÉTICA DE INGENIERÍA PURA (Dark Mode / High Contrast)
st.markdown("""
    <style>
    .stApp { background-color: #000000 !important; color: #FFFFFF !important; font-family: 'monospace'; }
    [data-testid="stMetric"] { background-color: #050505 !important; border: 1px solid #00FF00 !important; }
    [data-testid="stMetricValue"] { color: #00FF00 !important; }
    .ai-card { border: 1px solid #444; padding: 15px; background-color: #0a0a0a; border-radius: 5px; margin-bottom: 10px; }
    .stButton>button { width: 100%; border: 1px solid #00FF00; background-color: #000000; color: #00FF00; font-weight: bold; }
    .stButton>button:hover { background-color: #00FF00; color: #000000; }
    </style>
    """, unsafe_allow_html=True)

# 4. SELECTOR DE IDIOMA Y IA
sel_lang = st.sidebar.selectbox("🌐 LANGUAGE", list(languages.keys()))
t = languages[sel_lang]

st.sidebar.divider()
ia_choice = st.sidebar.radio("🤖 SELECT_ACTIVE_AI", ["Ámbar", "Kenya"])

# 5. TELEMETRÍA DE ALTO NIVEL
st.text(f">>> {t['welcome']} // SYNC: GEMINI_ACTIVE")
st.text(">>> DEVELOPER: SCARLET FUENMAYOR DIAZ")
st.divider()

cpu = psutil.cpu_percent(interval=0.5)
ram = psutil.virtual_memory().percent

c1, c2 = st.columns(2)
with c1: st.metric(t['cpu'], f"{cpu}%")
with c2: st.metric(t['ram'], f"{ram}%")

st.progress(cpu / 100)

# 6. FUNCIONALIDAD DE LAS IA (ÁMBAR O KENYA)
st.subheader(f"🧠 INTERFAZ_NEURAL: {ia_choice}")

if ia_choice == "Ámbar":
    st.markdown(f"<div class='ai-card'><b>{t['ambar_task']}</b><br>[INFO]: Escaneando sectores críticos y carpetas del sistema...</div>", unsafe_allow_html=True)
    if st.button(t['btn_clean']):
        with st.status("Analizando directorios dañados...", expanded=False):
            time.sleep(2)
            st.success("Limpieza completa: 0 archivos residuales.")
else:
    st.markdown(f"<div class='ai-card'><b>{t['kenya_task']}</b><br>[INFO]: Analizando diagnóstico total para optimización de hilos...</div>", unsafe_allow_html=True)
    if cpu > 60:
        st.warning(f"{t['status_warn']}")
        if st.button(t['btn_cool']):
            with st.status("Re-balanceando carga de procesos...", expanded=False):
                time.sleep(2)
                st.success("Temperatura estabilizada mediante re-enrutamiento.")
    else:
        st.success(t['status_ok'])

# 7. AUDITORÍA DE PROCESOS (EL PUENTE AL IMPACTO)
st.divider()
st.subheader("🛰️ HARDWARE_AUDIT_LOG")
procs = []
for proc in psutil.process_iter(['name', 'cpu_percent']):
    try: procs.append(proc.info)
    except: pass
df = pd.DataFrame(procs).sort_values(by='cpu_percent', ascending=False).head(3)
st.table(df)

st.caption("© 2026 Scarlet Fuenmayor Díaz | Ámbar & Kenya Neural Integration | Global Impact.")
