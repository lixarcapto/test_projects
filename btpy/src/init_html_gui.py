

from flask import Flask, render_template, request, jsonify
import threading
import socket
import webbrowser
import time

def get_local_IP():
    """Obtiene la IP local de 
    la computadora."""
    nombre_host = socket.gethostname()
    ip_local = socket.gethostbyname(
        nombre_host)
    return ip_local

app = Flask(__name__)
PATH_INDEX_HTML:str = "index.html"

@app.route('/')
def index():
    global PATH_INDEX_HTML
    return render_template(PATH_INDEX_HTML)

def init_server():
    app.run( host="127.0.0.1", 
            port=5000)

def init_html_gui(PATH_HTML:str):
    """
    Esta funcion inicia directamente
    una interface del navegador en local
    utilizando un servidor flask y 
    un archivo index.html. Para que 
    funcione debe instalarse la libreria
    Flask, debe crearse una carpeta 
    templates en la raiz de la aplicacion
    y en su interior debe tener un index.html
    valido. La ruta relativa del index
    debe enviarse como PATH_HTML.
    """
    global PATH_INDEX_HTML
    PATH_INDEX_HTML = PATH_HTML
    hilo_servidor = threading\
        .Thread(target=init_server)
    detener_servidor = threading.Event()
    hilo_servidor.start()
    url = "http://127.0.0.1:5000"
    webbrowser.open(url)
    print("si permite otro hilo")