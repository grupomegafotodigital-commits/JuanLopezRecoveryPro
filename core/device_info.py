import platform
import psutil


class DeviceInfo:

    @staticmethod
    def get_system_info():

        return {
            "Sistema": platform.system(),
            "Versión": platform.version(),
            "Arquitectura": platform.machine(),
            "Procesador": platform.processor(),
            "RAM": round(psutil.virtual_memory().total / (1024**3), 2)
        }
        