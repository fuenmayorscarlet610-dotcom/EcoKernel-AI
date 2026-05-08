# =================================================================
# ECOKERNEL AI - NETWORK SECURITY & VIGILANCE
# MODULE ID: KENYA-SHIELD-02
# =================================================================
import streamlit as st
import psutil
import socket

def show_security_monitor():
    st.markdown("### 🧠 KENYA NEURAL SHIELD: Vigilancia de Red")
    
    # 1. Escaneo de Conexiones Activas
    st.write("🔍 **CONEXIONES ACTIVAS EN EL KERNEL:**")
    connections = psutil.net_connections()
    conn_data = []
    
    for conn in connections:
        if conn.status == 'ESTABLISHED':
            # Intentar obtener el nombre del host para ver quién está conectado
            try:
                remote_ip = conn.raddr.ip
                status = "⚠️ EXTERNA" if remote_ip != '127.0.0.1' else "✅ LOCAL"
            except:
                remote_ip = "N/A"
                status = "🔒 PROTEGIDO"
            
            conn_data.append({
                "Protocolo": "TCP" if conn.type == 1 else "UDP",
                "IP Remota": remote_ip,
                "Puerto": conn.laddr.port,
                "Estado": status
            })

    if conn_data:
        st.dataframe(conn_data)
    else:
        st.success("No hay conexiones externas sospechosas detectadas.")

    # 2. Botón de Escudo Activo
    if st.button("🛡️ ACTIVAR PROTOCOLO DE AISLAMIENTO"):
        st.warning("Protocolo Stark activo: Monitoreando puertos críticos...")
        # Aquí podrías añadir lógica para cerrar puertos o alertar
      
