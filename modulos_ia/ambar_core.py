import psutil
import platform

def estado_sistema_ambar():
    # Lectura real del hardware del Samsung A31
    bateria = psutil.sensors_battery()
    cpu_uso = psutil.cpu_percent(interval=1)
    memoria = psutil.virtual_memory()
    
    info = {
        "sistema": platform.system(),
        "bateria_nivel": bateria.percent,
        "bateria_cargando": bateria.power_plugged,
        "cpu_uso_total": f"{cpu_uso}%",
        "ram_disponible": f"{memoria.available / (1024**2):.2f} MB"
    }
    return info
