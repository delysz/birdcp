import pyperclip
import webbrowser
import urllib.parse
import time
import re
import os
import ctypes
import msvcrt
from datetime import datetime

# ╔══════════════════════════════════════════════════════════════════════════╗
# ║                  Á R E A   D E   C O N F I G U R A C I Ó N               ║
# ╚══════════════════════════════════════════════════════════════════════════╝

CC_FIJO = "sevovo9612@nazisat.com"
ARCHIVO_HISTORIAL = "historial_envios.csv"

PLANTILLAS = {
    "1": {
        "titulo_menu": "Oficina Virtual",
        "asunto": "Acceso Oficina Virtual", 
        "cuerpo": "Hola, adjunto los accesos para su Oficina Virtual.\n\nUn saludo."
    },
    "2": {
        "titulo_menu": "Gestión de Empresa",
        "asunto": "Documentación de Gestión de Empresa", 
        "cuerpo": "Estimados,\n\nEnviamos la documentación correspondiente a la gestión...\n\nGracias."
    },
    "3": {
        "titulo_menu": "Ciberseguridad",
        "asunto": "Reporte Ciberseguridad / Logs Azure", 
        "cuerpo": "Hola,\n\nSe adjuntan los logs de seguridad de Azure solicitados.\n\nUn saludo."
    },
    "4": {
        "titulo_menu": "Otro / General",
        "asunto": "Información General", 
        "cuerpo": "Hola,\n\nNos ponemos en contacto con usted para...\n\nSaludos."
    }
}

# ╔══════════════════════════════════════════════════════════════════════════╗
# ║                   F I N   D E   C O N F I G U R A C I Ó N                ║
# ╚══════════════════════════════════════════════════════════════════════════╝

CYAN = '\033[96m'
AMARILLO = '\033[93m'
VERDE = '\033[92m'
ROJO = '\033[91m'
MAGENTA = '\033[95m'
RESET = '\033[0m'
NEGRITA = '\033[1m'

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def alertar_ventana():
    """Restablece la ventana y hace parpadear la barra de tareas en Windows."""
    try:
        hwnd = ctypes.windll.kernel32.GetConsoleWindow()
        if hwnd:
            ctypes.windll.user32.ShowWindow(hwnd, 9)
            ctypes.windll.user32.SetForegroundWindow(hwnd)
    except Exception:
        pass

def imprimir_banner_gigante():
    banner = f"""{MAGENTA}{NEGRITA}
  ██████╗ ██╗██████╗ ██████╗  ██████╗██████╗ 
  ██╔══██╗██║██╔══██╗██╔══██╗██╔════╝██╔══██╗
  ██████╔╝██║██████╔╝██║  ██║██║     ██████╔╝
  ██╔══██╗██║██╔══██╗██║  ██║██║     ██╔═══╝ 
  ██████╔╝██║██║  ██║██████╔╝╚██████╗██║     
  ╚═════╝ ╚═╝╚═╝  ╚═╝╚═════╝  ╚═════╝╚═╝     
{CYAN}  > BIRDCP v1.0 | Coded by delysz < {RESET}
    """
    print(banner)
    print(f" {VERDE}● SISTEMA ONLINE Y ESCUCHANDO...{RESET}")
    print(f"{MAGENTA}================================================={RESET}")

def guardar_historial(email):
    try:
        nuevo_archivo = not os.path.exists(ARCHIVO_HISTORIAL)
        with open(ARCHIVO_HISTORIAL, "a", encoding="utf-8") as f:
            if nuevo_archivo:
                f.write("Fecha_Envio,Correo_Destinatario\n")
            f.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')},{email}\n")
    except Exception:
        pass

def es_correo(texto):
    if not texto: 
        return False
    return re.fullmatch(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', texto)

def mostrar_interfaz(email):
    limpiar_pantalla()
    imprimir_banner_gigante()
    print(f"\n {NEGRITA}⚡ BLANCO DETECTADO:{RESET} {AMARILLO}{email}{RESET}")
    print(f"\n {NEGRITA}SELECCIONA EL MENSAJE A ENVIAR:{RESET}")
    print(f" {CYAN}───────────────────────────────────────────────{RESET}")
    for clave, datos in PLANTILLAS.items():
        print(f"  {VERDE}[{clave}]{RESET} {datos['titulo_menu']}")
    print(f"  {ROJO}[N]{RESET} Cancelar / Descartar correo")
    print(f" {CYAN}───────────────────────────────────────────────{RESET}")

def esperar_tecla_o_portapapeles(email_actual):
    print(f"\n {NEGRITA}>> Ejecutar orden (1-4/N):{RESET} ", end="", flush=True)
    
    while True:
        clip = pyperclip.paste().strip()
        if es_correo(clip) and clip != email_actual:
            return "NUEVO_CORREO", clip
            
        if msvcrt.kbhit():
            tecla = msvcrt.getch()
            try:
                char = tecla.decode('utf-8').lower()
                if char in ['1', '2', '3', '4', 'n']:
                    print(char) 
                    return "OPCION", char
            except Exception:
                pass
                
        time.sleep(0.1)

if __name__ == "__main__":
    os.system("") 
    pyperclip.copy("") 
    
    limpiar_pantalla()
    imprimir_banner_gigante()
    print(f" {CYAN}>>{RESET} Copia un email en tu CRM (Ctrl+C) para empezar...")
    
    email_activo = ""
    
    try:
        while True:
            if not email_activo:
                clip = pyperclip.paste().strip()
                if es_correo(clip):
                    email_activo = clip
                    alertar_ventana()
                time.sleep(0.5)
                continue

            mostrar_interfaz(email_activo)
            tipo_evento, valor = esperar_tecla_o_portapapeles(email_activo)
            
            if tipo_evento == "NUEVO_CORREO":
                email_activo = valor
                alertar_ventana()
                continue 
                
            elif tipo_evento == "OPCION":
                if valor == 'n':
                    print(f"\n {ROJO}✘ Abortado. Limpiando para el siguiente...{RESET}")
                    time.sleep(1)
                elif valor in PLANTILLAS:
                    p = PLANTILLAS[valor]
                    asunto = urllib.parse.quote(p['asunto'])
                    cuerpo = urllib.parse.quote(p['cuerpo'])
                    url = f"mailto:{email_activo}?cc={CC_FIJO}&subject={asunto}&body={cuerpo}"
                    webbrowser.open(url)
                    guardar_historial(email_activo)
                    print(f"\n {VERDE}✔ Thunderbird abierto. Guardado en log.{RESET}")
                    time.sleep(1)
                
                pyperclip.copy("")
                email_activo = ""
                limpiar_pantalla()
                imprimir_banner_gigante()
                print(f" {VERDE}✔ Listo. {CYAN}>>{RESET} Copia el SIGUIENTE email...")
                
    except KeyboardInterrupt:
        limpiar_pantalla()
        print(f"\n {MAGENTA}Sistema BIRDCP apagado por delysz. ¡Hasta la próxima!{RESET}\n")