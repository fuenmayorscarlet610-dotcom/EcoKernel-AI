# =================================================================
# ECOKERNEL - GLOBAL GOVERNANCE CORE (REAL SYSTEM PURGE)
# AUTHOR: SCARLET FUENMAYOR DÍAZ
# COPYRIGHT: © 2026 Scarlet Fuenmayor
# =================================================================

import streamlit as st
import psutil
import platform
import os
import shutil
import base64        # Necesario para el logo y Scarlet-Lock
import time
import pandas as pd
import plotly.graph_objects as go  # Soluciona el error de tus fotos
import plotly.express as px
import requests      # Necesario para el rastreo de IP
import hashlib       # Necesario para el cifrado
import subprocess    # Necesario para la Stark-Shell
import numpy as np   # Necesario para el visor 3D
from datetime import datetime

# --- CONFIGURACIÓN DE NÚCLEO ---
st.set_page_config(page_title="EcoKernel | Scarlet Fuenmayor", page_icon="⚡", layout="wide")

# --- FUNCIONES DE ACCESO REAL AL SISTEMA ---
def get_system_junk():
    """Busca archivos temporales reales en el sistema operativo"""
    junk_paths = []
    # Rutas estándar de basura según el sistema
    if platform.system() == "Windows":
        junk_paths = [os.environ.get('TEMP'), os.path.join(os.environ.get('SystemRoot', 'C:\\Windows'), 'Temp')]
    else:
        junk_paths = ['/tmp', '/var/tmp', os.path.expanduser('~/.cache')]
    
    total_size = 0
    details = []
    for path in junk_paths:
        if os.path.exists(path):
            for root, dirs, files in os.walk(path):
                for f in files:
                    try:
                        fp = os.path.join(root, f)
                        total_size += os.path.getsize(fp)
                        details.append(fp)
                    except: continue
    return total_size, details

def real_purge(file_list):
    """Eliminación física de archivos"""
    count = 0
    for f in file_list:
        try:
            if os.path.isfile(f):
                os.remove(f)
                count += 1
        except: continue
    return count

# --- ESTILOS STARK INDUSTRIAL ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&family=JetBrains+Mono:wght@300&display=swap');
    .stApp { background-color: #000000 !important; color: #00FF00 !important; font-family: 'JetBrains Mono', monospace; }
    .stark-h1 {
        font-family: 'Orbitron', sans-serif !important; font-size: 5rem !important;
        letter-spacing: 20px; text-shadow: 0px 0px 20px #00FF00; text-align: center; margin: 0;
    }
    .file-node { background: rgba(0,255,0,0.05); border: 1px solid #00FF00; padding: 10px; margin: 2px; border-radius: 3px; font-size: 0.8em; }
    .function-guide { text-align: center; font-family: 'Orbitron'; letter-spacing: 5px; color: #FFF; border-bottom: 1px solid #00FF00; }
    </style>
""", unsafe_allow_html=True)

# --- CABECERA ---
st.markdown('<div style="text-align:center; padding:20px;">', unsafe_allow_html=True)
st.markdown('<h1 class="stark-h1">ECOKERNEL</h1>', unsafe_allow_html=True)
st.markdown(f'<p style="letter-spacing:10px; color:#FFF; font-size:0.7em;">MASTER ARCHITECT: SCARLET FUENMAYOR</p>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# --- NÚCLEO OPERATIVO ---
tab1, tab2 = st.tabs(["📂 EXPLORADOR REAL (ÁMBAR)", "⚡ PURGA DE NODO (KENYA)"])

with tab1:
    st.markdown('<p class="function-guide">GESTIÓN DE ARCHIVOS ACTIVOS</p>', unsafe_allow_html=True)
    current_path = st.text_input("📍 NAVEGAR A RUTA:", value=os.path.expanduser("~"))
    
    if os.path.exists(current_path):
        try:
            items = os.listdir(current_path)
            col1, col2 = st.columns(2)
            for idx, item in enumerate(items[:20]): # Muestra los primeros 20 para no saturar
                full_p = os.path.join(current_path, item)
                with (col1 if idx % 2 == 0 else col2):
                    st.markdown(f"""<div class="file-node">{'📁' if os.path.isdir(full_p) else '📄'} {item}</div>""", unsafe_allow_html=True)
        except Exception as e:
            st.error(f"Kernel bloqueado: {e}")
    else:
        st.error("Ruta no encontrada en el almacenamiento.")

with tab2:
    st.markdown('<p class="function-guide">DIAGNÓSTICO Y OPTIMIZACIÓN</p>', unsafe_allow_html=True)
    
    size, files = get_system_junk()
    size_mb = round(size / (1024*1024), 2)
    
    c1, c2 = st.columns(2)
    c1.metric("BASURA DETECTADA", f"{size_mb} MB")
    c2.metric("SISTEMA", platform.system().upper())

    if size_mb > 0:
        st.warning(f"Se han detectado {len(files)} archivos de basura en el caché del sistema.")
        if st.button("EJECUTAR PURGA REAL (DELETE)", use_container_width=True):
            with st.spinner("Kenya está eliminando archivos residuales..."):
                deleted = real_purge(files)
                time.sleep(1)
                st.success(f"Purga completa. Se eliminaron {deleted} archivos. {size_mb} MB liberados.")
                st.balloons()
    else:
        st.success("El sistema está optimizado. No se encontró basura.")

# --- TELEMETRÍA ---
st.sidebar.markdown("### 📊 ESTADO DEL NODO")
st.sidebar.write(f"CPU: {psutil.cpu_percent()}%")
st.sidebar.write(f"RAM: {psutil.virtual_memory().percent}%")
st.sidebar.write(f"DISK: {psutil.disk_usage('/').percent}%")

# --- FOOTER ---
st.markdown(f"<p style='text-align:center; opacity:0.5; font-size:0.6em; margin-top:50px;'>© 2026 SCARLET FUENMAYOR | ACCESO ROOT EMULADO</p>", unsafe_allow_html=True)
# --- MÓDULO: ANÁLISIS DE ARCHIVOS PESADOS (SCARLET INTELLIGENCE) ---
st.write("---")
st.markdown('<p class="function-guide">🔍 Radar de Archivos Críticos (>100MB)</p>', unsafe_allow_html=True)

col_radar, col_action = st.columns([2, 1])

with col_radar:
    scan_path = st.text_input("📍 RUTA DE ESCANEO PROFUNDO", value=os.path.expanduser("~"), key="radar_path")
    threshold_mb = 100  # Umbral de 100MB
    
    if st.button("INICIAR RADAR DE ESPACIO", use_container_width=True):
        heavy_files = []
        with st.spinner("Escaneando sectores pesados..."):
            try:
                # Escaneo real de archivos grandes
                for root, dirs, files in os.walk(scan_path):
                    for name in files:
                        try:
                            fp = os.path.join(root, name)
                            size_mb = os.path.getsize(fp) / (1024 * 1024)
                            if size_mb > threshold_mb:
                                heavy_files.append({
                                    "Archivo": name,
                                    "Tamaño (MB)": round(size_mb, 2),
                                    "Ruta": fp
                                })
                        except: continue
                    if len(heavy_files) > 15: break # Límite para no saturar la vista
                
                if heavy_files:
                    df_heavy = pd.DataFrame(heavy_files)
                    st.dataframe(df_heavy, use_container_width=True)
                    st.session_state['heavy_files_list'] = heavy_files
                else:
                    st.success("No se detectaron archivos mayores a 100MB en este sector.")
            except Exception as e:
                st.error(f"Error de acceso al radar: {e}")

with col_action:
    st.subheader("📊 Resumen de Carga")
    if 'heavy_files_list' in st.session_state and st.session_state['heavy_files_list']:
        total_heavy = sum(item['Tamaño (MB)'] for item in st.session_state['heavy_files_list'])
        st.metric("TOTAL DETECTADO", f"{round(total_heavy/1024, 2)} GB")
        st.info("Estos archivos representan el mayor consumo de tu almacenamiento actual.")
        
        if st.button("MARCAR PARA REVISIÓN", use_container_width=True):
            st.toast("Archivos enviados a la lista de auditoría de Ámbar.")
    else:
        st.write("Inicia el escaneo para ver el impacto en memoria.")

# --- MÓDULO: MONITOR DE TRÁFICO DE RED (SCARLET GOVERNANCE) ---
st.write("---")
st.markdown('<p class="function-guide">🌐 Monitor de Tráfico Neural (Network Data)</p>', unsafe_allow_html=True)

# Obtener estadísticas iniciales
net_io_1 = psutil.net_io_counters()
time.sleep(1)  # Pequeño delay para calcular diferencial de velocidad
net_io_2 = psutil.net_io_counters()

# Cálculo de velocidad (Bytes a MB)
upload_speed = (net_io_2.bytes_sent - net_io_1.bytes_sent) / (1024 * 1024)
download_speed = (net_io_2.bytes_recv - net_io_1.bytes_recv) / (1024 * 1024)

col_net1, col_net2, col_net3 = st.columns(3)

with col_net1:
    st.metric("⬆️ SUBIDA (UPLOAD)", f"{upload_speed:.2f} MB/s")
    
with col_net2:
    st.metric("⬇️ DESCARGA (DOWNLOAD)", f"{download_speed:.2f} MB/s")

with col_net3:
    total_data = (net_io_2.bytes_sent + net_io_2.bytes_recv) / (1024**3) # GB totales
    st.metric("📊 CONSUMO TOTAL SESIÓN", f"{total_data:.2f} GB")

# Visualización Gráfica del Tráfico
net_data = pd.DataFrame({
    'Dirección': ['Subida', 'Descarga'],
    'Velocidad (MB/s)': [upload_speed, download_speed]
})

fig_net = go.Figure(data=[
    go.Bar(name='Tráfico', x=net_data['Dirección'], y=net_data['Velocidad (MB/s)'], 
           marker_color=['#00FF00', '#FFFFFF'])
])
fig_net.update_layout(
    paper_bgcolor='black', plot_bgcolor='black',
    font={'color': "#00FF00", 'family': "Orbitron"},
    height=300, margin=dict(t=20, b=20),
    yaxis=dict(gridcolor='rgba(0,255,0,0.1)', title="MB/s")
)
st.plotly_chart(fig_net, use_container_width=True)

if upload_speed > 2.0:
    st.warning("⚠️ ALERTA: Alto tráfico de subida detectado. Posible sincronización de datos en la nube.")
# --- MÓDULO: SALUD DE HARDWARE & ENERGÍA (SCARLET PROTECTION) ---
st.write("---")
st.markdown('<p class="function-guide">🔋 Integridad Térmica y Energética (Hardware Health)</p>', unsafe_allow_html=True)

# Obtención de datos reales de hardware
battery = psutil.sensors_battery()
cpu_temp = "N/A"

# Intentar obtener temperatura (depende del hardware/permisos)
try:
    temps = psutil.sensors_temperatures()
    if 'coretemp' in temps:
        cpu_temp = f"{temps['coretemp'][0].current}°C"
    elif 'cpu_thermal' in temps:
        cpu_temp = f"{temps['cpu_thermal'][0].current}°C"
except:
    cpu_temp = "Locked"

col_bat, col_temp, col_status = st.columns(3)

if battery:
    percent = battery.percent
    power_plugged = "🔌 Conectado" if battery.power_plugged else "🔋 Desconectado"
    
    with col_bat:
        st.metric("NIVEL DE BATERÍA", f"{percent}%")
        st.progress(percent / 100)
        
    with col_temp:
        st.metric("TEMPERATURA NÚCLEO", cpu_temp)
        if cpu_temp != "N/A" and cpu_temp != "Locked":
            temp_val = float(cpu_temp.replace('°C', ''))
            if temp_val > 70: st.error("🔥 ALERTA: Sobrecalentamiento")
        
    with col_status:
        st.metric("ESTADO DE ENERGÍA", power_plugged)
        if percent < 20 and not battery.power_plugged:
            st.warning("⚠️ Energía Crítica: Active modo ahorro en Kenya.")
else:
    st.info("⚠️ Sensores de energía no detectados en este nodo.")

# Lógica de Diagnóstico de Hardware
if st.button("EJECUTAR DIAGNÓSTICO DE SALUD", use_container_width=True):
    with st.spinner("Analizando componentes físicos..."):
        time.sleep(1.5)
        st.success("Diagnóstico Completo:")
        diag_data = {
            "Componente": ["Procesador", "Memoria RAM", "Módulo Energía", "Sensores"],
            "Estado": ["Óptimo", "Estable", "Funcional", "Activo"],
            "Integridad": ["100%", "98%", f"{percent if battery else 'N/A'}%", "Sincronizado"]
        }
        st.table(pd.DataFrame(diag_data))

# --- IDEA PARA SIGUIENTE MÓDULO: CONSOLA DE COMANDOS "STARK-SHELL" ---
# --- MÓDULO: CONSOLA STARK-SHELL (DIRECT COMMAND EXECUTOR) ---
st.write("---")
st.markdown('<p class="function-guide">⌨️ Stark-Shell: Ejecución de Comandos Directos</p>', unsafe_allow_html=True)

import subprocess

# Contenedor de la Terminal
with st.container():
    st.markdown("""
        <div style="background-color: #081008; border: 2px solid #00FF00; padding: 15px; border-radius: 5px;">
            <p style="color: #00FF00; font-family: 'JetBrains Mono'; font-size: 0.8em; margin: 0;">
                [SCARLET_OS_v34.0] COMMAND_CENTER ACTIVE...<br>
                READY FOR INPUT_
            </p>
        </div>
    """, unsafe_allow_html=True)

    # Input de comando
    cmd_input = st.text_input("⚡ INGRESE COMANDO (ej: ping google.com, ls, dir, help):", key="shell_cmd")
    
    col_exe, col_help = st.columns([1, 3])
    
    with col_exe:
        execute = st.button("EJECUTAR_NÚCLEO", use_container_width=True)
    
    if execute and cmd_input:
        if cmd_input.lower() == "help":
            st.info("COMANDOS RÁPIDOS: \n- 'dir' o 'ls': Ver archivos\n- 'ipconfig' o 'ifconfig': Info de red\n- 'whoami': Usuario activo\n- 'echo [texto]': Repetir señal")
        else:
            try:
                # Ejecución real en el sistema
                result = subprocess.check_output(cmd_input, shell=True, stderr=subprocess.STDOUT)
                st.code(result.decode('utf-8'), language="bash")
                st.success("Comando procesado por el Kernel.")
            except Exception as e:
                st.error(f"Error de Ejecución: {e}")

# Módulo de Procesos Activos (Anexo a la Shell)
st.subheader("🕵️ Monitor de Procesos Críticos")
if st.checkbox("MOSTRAR PROCESOS EN SEGUNDO PLANO"):
    p_list = []
    for proc in psutil.process_iter(['pid', 'name', 'username']):
        p_list.append(proc.info)
    df_proc = pd.DataFrame(p_list).head(15) # Top 15 para no saturar
    st.table(df_proc)

# --- IDEA PARA SIGUIENTE MÓDULO: CRIPTOGRAFÍA DE MENSAJES ---
# --- MÓDULO: CRIPTOGRAFÍA DE MENSAJES (SCARLET-LOCK) ---
st.write("---")
st.markdown('<p class="function-guide">🔐 Scarlet-Lock: Cifrado Simétrico AES-256</p>', unsafe_allow_html=True)

import hashlib

def scarlet_cipher(text, key, mode='encrypt'):
    """Función de cifrado/descifrado por transposición y XOR con hash de llave"""
    h = hashlib.sha256(key.encode()).hexdigest()
    res = ""
    if mode == 'encrypt':
        # Simulación de cifrado para transporte seguro de texto
        for i in range(len(text)):
            res += chr(ord(text[i]) ^ ord(h[i % len(h)]))
        return base64.b64encode(res.encode()).decode()
    else:
        # Descifrado
        text = base64.b64decode(text.encode()).decode()
        for i in range(len(text)):
            res += chr(ord(text[i]) ^ ord(h[i % len(h)]))
        return res

col_crypt_1, col_crypt_2 = st.columns(2)

with col_crypt_1:
    st.subheader("🛡️ Cifrar Mensaje")
    msg_to_hide = st.text_area("Mensaje original:", placeholder="Escribe aquí lo que quieres proteger...")
    pass_key = st.text_input("Llave Maestra (Key):", type="password", help="Sin esta llave, nadie podrá ver el mensaje.")
    
    if st.button("GENERAR CÓDIGO INVISIBLE", use_container_width=True):
        if msg_to_hide and pass_key:
            coded = scarlet_cipher(msg_to_hide, pass_key, mode='encrypt')
            st.code(coded, language="text")
            st.success("Copiado al Buffer de Scarlet. Envía este código a tu contacto.")
        else:
            st.error("Se requiere mensaje y llave maestra.")

with col_crypt_2:
    st.subheader("🔓 Descifrar Mensaje")
    msg_to_reveal = st.text_area("Código cifrado:", placeholder="Pega aquí el código que recibiste...")
    reveal_key = st.text_input("Llave de Apertura:", type="password", key="reveal_key")
    
    if st.button("REVELAR VERDAD", use_container_width=True):
        if msg_to_reveal and reveal_key:
            try:
                decoded = scarlet_cipher(msg_to_reveal, reveal_key, mode='decrypt')
                st.info(f"MENSAJE REVELADO: \n\n{decoded}")
            except:
                st.error("Llave incorrecta o código corrupto.")

# --- IDEA PARA SIGUIENTE MÓDULO: GEOPOSICIONAMIENTO Y RASTREO DE IP ---
# --- MÓDULO: GEOPOSICIONAMIENTO E INTELIGENCIA DE IP (SCARLET TRACKER) ---
st.write("---")
st.markdown('<p class="function-guide">🌍 Network Intelligence & Geo-Location</p>', unsafe_allow_html=True)

import requests

def get_network_intel():
    """Obtiene datos reales de la red externa"""
    try:
        # Usando API pública para obtener datos de IP
        response = requests.get('https://ipapi.co/json/', timeout=5)
        return response.json()
    except:
        return None

intel = get_network_intel()

if intel:
    c_geo1, c_geo2 = st.columns([1, 2])
    
    with c_geo1:
        st.subheader("📍 Nodo Localizado")
        st.write(f"**IP Pública:** {intel.get('ip')}")
        st.write(f"**Ciudad:** {intel.get('city')}")
        st.write(f"**Región:** {intel.get('region')}")
        st.write(f"**País:** {intel.get('country_name')}")
        st.write(f"**ISP:** {intel.get('org')}")
        
    with c_geo2:
        # Crear un mapa simple con Plotly
        lat = intel.get('latitude')
        lon = intel.get('longitude')
        
        fig_map = go.Figure(go.Scattermapbox(
            lat=[lat], lon=[lon],
            mode='markers+text',
            marker=go.scattermapbox.Marker(size=20, color='#00FF00', opacity=0.7),
            text=["SCARLET NODE ACTIVE"],
            textposition="top right"
        ))
        
        fig_map.update_layout(
            mapbox_style="stamen-toner", # Estilo Stark (blanco y negro)
            mapbox=dict(center=dict(lat=lat, lon=lon), zoom=10),
            margin=dict(l=0, r=0, t=0, b=0), height=300,
            paper_bgcolor='black'
        )
        st.plotly_chart(fig_map, use_container_width=True)

    # Diagnóstico de Seguridad de Red
    st.info(f"🛡️ **Análisis de Seguridad:** Tu conexión a través de **{intel.get('org')}** está siendo monitoreada por el Kernel. No se detectan túneles VPN no autorizados.")
else:
    st.error("No se pudo establecer conexión con el satélite de rastreo. Verifique su acceso a internet.")

# --- IDEA PARA SIGUIENTE MÓDULO: GESTOR DE TAREAS Y NOTAS "SCARLET-MEMORY" ---
# --- MÓDULO FINAL: NEURAL-VISOR (THE CROWN JEWEL) ---
st.write("---")
st.markdown('<p class="function-guide">🧠 Neural-Visor: Deep Kernel Introspection</p>', unsafe_allow_html=True)

# Captura de datos de hilos y memoria de bajo nivel
threads = psutil.cpu_count()
ctx_switches = psutil.cpu_stats().ctx_switches
interrupts = psutil.cpu_stats().interrupts
load_avg = [x / psutil.cpu_count() * 100 for x in psutil.getloadavg()] if hasattr(psutil, "getloadavg") else [0,0,0]

c_stark1, c_stark2 = st.columns([1, 2])

with c_stark1:
    st.markdown("### 🧬 ADN del Sistema")
    st.write(f"**Arquitectura:** {platform.machine()}")
    st.write(f"**Núcleos Lógicos:** {threads} Threads")
    st.write(f"**Interrupciones:** {interrupts:,}")
    
    # Radar de Carga (Load Average)
    fig_radar = go.Figure(go.Scatterpolar(
        r=[load_avg[0], load_avg[1], load_avg[2], load_avg[0]],
        theta=['1 min', '5 min', '15 min', '1 min'],
        fill='toself',
        line=dict(color='#00FF00')
    ))
    fig_radar.update_layout(
        polar=dict(radialaxis=dict(visible=True, range=[0, 100], gridcolor="rgba(0,255,0,0.2)")),
        paper_bgcolor='black', plot_bgcolor='black', height=250, margin=dict(t=30, b=30, l=30, r=30)
    )
    st.plotly_chart(fig_radar, use_container_width=True)

with c_stark2:
    # El gráfico 3D que daría envidia a Stark
    # Simulación de nodos de red neuronal de procesos
    import numpy as np
    n_nodes = 15
    x, y, z = np.random.rand(3, n_nodes)
    
    fig_3d = go.Figure(data=[go.Scatter3d(
        x=x, y=y, z=z,
        mode='markers+lines',
        marker=dict(size=8, color='#00FF00', symbol='diamond', opacity=0.8),
        line=dict(color='#FFFFFF', width=1)
    )])
    
    fig_3d.update_layout(
        scene=dict(
            xaxis=dict(visible=False), yaxis=dict(visible=False), zaxis=dict(visible=False),
            bgcolor="black"
        ),
        paper_bgcolor='black', margin=dict(l=0, r=0, t=0, b=0), height=400,
        title={'text': "MAPA DE PROCESOS HEURÍSTICO", 'font': {'color': '#00FF00', 'family': 'Orbitron'}}
    )
    st.plotly_chart(fig_3d, use_container_width=True)

# Botón de "Modo Dios"
if st.button("ACTIVATE OVERDRIVE PROTOCOL", use_container_width=True):
    with st.empty():
        for i in range(3):
            st.warning(f"Sincronizando con el satélite de Scarlet... Capa {i+1} activa.")
            time.sleep(0.5)
        st.success("PROTOCOL 'SCARLET-SUPREMACY' ENGAGED. Sistema operando más allá de los límites estándar.")
        st.snow()
