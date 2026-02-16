

import webbrowser
import time
import subprocess
import os
import sys
import threading

def open_browser_in_time(tiempo_espera,
        url):
    """
    Abre una ventana del navegador con la URL especificada, espera el tiempo indicado y luego la cierra, usando threads.

    Args:
        url (str): La URL que se abrirá en el navegador.
        tiempo_espera (int, optional): El tiempo en segundos que se esperará antes de cerrar el navegador. Por defecto, 60 segundos.
    """
    def _cerrar_navegador():
        """Función interna para cerrar el navegador."""
        try:
            # Cierra la ventana del navegador de forma dependiente del sistema operativo
            if sys.platform.startswith('win'):
                # Windows: Intenta cerrar la ventana del navegador usando taskkill.
                try:
                    process = subprocess.Popen(['tasklist', '/v', '/fo', 'csv'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    stdout, stderr = process.communicate()
                    output = stdout.decode('utf-8', errors='ignore')
                    lines = output.strip().split('\r\n')
                    for line in lines[1:]:
                        parts = [p.strip().strip('"') for p in line.split(',')]
                        if len(parts) > 1 and "chrome.exe" in parts[0].lower():
                            pid = parts[1]
                            subprocess.run(['taskkill', '/F', '/PID', pid], check=False)
                            print(f"Ventana de Chrome (PID {pid}) cerrada.")
                            return
                except Exception as e:
                    print(f"No se pudo cerrar la ventana del navegador en Windows: {e}")

            elif sys.platform.startswith('darwin'):
                # macOS: Usa AppleScript para cerrar la ventana del navegador.
                try:
                    subprocess.run(['osascript', '-e', 'tell application "Safari" to close the front window'], check=False)
                    print("Ventana de Safari cerrada.")
                    return
                except Exception as e:
                    print(f"No se pudo cerrar la ventana del navegador en macOS: {e}")
            elif sys.platform.startswith('linux'):
                try:
                    subprocess.run(['xdotool', 'search', '--onlyvisible', '--class', 'Navigator', 'windowkill'], check=False)
                    print("Ventana del navegador cerrada")
                    return
                except Exception as e:
                    print(f"No se pudo cerrar la ventana del navegador en Linux: {e}")
            else:
                print("No se soporta el cierre automático del navegador en este sistema operativo.")

        except Exception as e:
            print(f"Ocurrió un error al cerrar el navegador: {e}")

    try:
        # Abre el navegador con la URL especificada
        webbrowser.open_new(url)
        print(f"Navegador abierto con la URL: {url}")
        print(f"Esperando {tiempo_espera} segundos antes de cerrar la ventana...")

        # Crea un thread para cerrar el navegador después del tiempo de espera
        cerrar_thread = threading.Timer(tiempo_espera, _cerrar_navegador)
        cerrar_thread.start()  # Inicia el thread

        # El programa principal puede continuar con otras tareas aquí
        # Por ejemplo, puedes imprimir algo mientras el temporizador está corriendo:
        # time.sleep(tiempo_espera + 5) # Espera un poco más que el thread
        # print("El programa principal ha terminado de esperar.")

    except Exception as e:
        print(f"Ocurrió un error: {e}")