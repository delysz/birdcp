# 🦅 BIRDCP

**BIRDCP** es una potente herramienta de automatización para terminal. Su función es actuar como un "escucha" inteligente que detecta correos electrónicos en el portapapeles y permite enviar respuestas predefinidas a través de Thunderbird de forma casi instantánea.

---

## ✨ Características Principales

- 🚀 **Detección Automática:** Reacciona al instante cuando haces `Ctrl + C` sobre una dirección de correo.
- ⚡ **Smart Focus:** La terminal salta automáticamente al frente (pop-up) cuando captura un objetivo.
- 📂 **Historial CSV:** Registra cada envío en un archivo `historial_envios.csv` con fecha y destinatario.
- 🧹 **Auto-Limpieza:** Vacía el portapapeles tras cada uso para evitar duplicados y estar listo para el siguiente.
- 🎨 **Interfaz Pro:** Estética de terminal tipo "Hacker" con banners ASCII y colores.

---

## 🛠️ Instalación y Configuración

### 1. Requisitos
- **Python 3.x** instalado.
- **Thunderbird** configurado como cliente de correo predeterminado.
- Librería `pyperclip` (para manejar el portapapeles).

### 2. Preparación
Clona este repositorio o descarga el archivo `main.py` y ejecuta:
```bash
pip install pyperclip
3. Ejecución
Simplemente lanza el script:

Bash
python main.py
⚙️ Personalización de Mensajes
El script está dividido para que sea fácil de editar. Abre main.py y busca el ÁREA DE CONFIGURACIÓN:

Python
# Puedes cambiar el correo en copia (CC)
CC_FIJO = "tu_compañero@empresa.com"

# Edita las plantillas aquí:
PLANTILLAS = {
    "1": {
        "titulo_menu": "Nuevo Acceso",
        "asunto": "Credenciales de Oficina Virtual", 
        "cuerpo": "Hola,\n\nAquí tienes tus accesos...\n\nSaludos."
    },
    # Añade tantas como necesites...
}
📊 Registro de Datos (Logs)
Cada vez que confirmas un envío, el sistema genera o actualiza un archivo llamado historial_envios.csv. Este archivo es ideal para importar datos a Excel o conectarlo con plugins de Figma para reportes visuales.



Proyecto creado y mantenido por delysz.
