

from flask import Flask, render_template, request, jsonify
import threading
import socket
import webbrowser
import time
import json

def get_local_IP():
    """Obtiene la IP local de 
    la computadora."""
    nombre_host = socket.gethostname()
    ip_local = socket.gethostbyname(
        nombre_host)
    return ip_local

api_model = None

app = Flask(__name__)
PATH_INDEX_HTML:str = "index.html"

@app.route('/')
def index():
    global PATH_INDEX_HTML
    return render_template(PATH_INDEX_HTML)

@app.route('/request', 
        methods=['POST'])
def recibir_mensaje():
    """
    Esta función maneja las solicitudes POST a la ruta /api/recibir_mensaje.
    Espera recibir un mensaje JSON con la clave 'mensaje'.
    Responde con un JSON que contiene un mensaje de confirmación.
    """
    global api_model
    # Verifica si la solicitud tiene un 
    # cuerpo JSON.
    if not request.is_json:
        return jsonify(
            {'error': 'La solicitud debe ser JSON'}), 400  # Código de estado 400: Bad Request

    # Obtiene los datos JSON de la 
    # solicitud.
    request_json = request.get_json()

    response_dict = api_model.request(
        request_json)
    response_json = json.dumps(
        response_dict)
    # Imprime el mensaje recibido en 
    # la consola del servidor (útil 
    # para depuración)
    print("Mensaje recibido:",
          f"{request_json}")
    print("mensaje enviado", 
          f"{response_json}")
    # Devuelve una respuesta JSON con 
    # un mensaje de éxito.
    return jsonify(response_json), 200  
    # Código de estado 200: OK

port:int = 0
def init_server():
    global port
    app.run( host="127.0.0.1", 
            port=port)
    
def init_thread_server(PORT:int):
    global port
    port = PORT
    hilo_servidor = threading\
        .Thread(target=init_server)
    hilo_servidor.start()

def init_html_gui(MODEL_API, 
        PATH_HTML:str, 
        PORT:int = 5000):
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
    
    El parametro API_Model recibe una clase
    que debe contener como parametro 
    un metodo request que reciba un dict 
    y retorne un dict; el dict 
    es un json deserializado a dict 
    que es recibido de la request, y 
    el json retornado es el json de la 
    response.

    Para hacer request al servidor se 
    debe usar la PATH con el endpoint 
    /request, se debe usar el metodo 
    POST y enviar un json en el body.
    """
    global PATH_INDEX_HTML
    global api_model
    api_model = MODEL_API
    PATH_INDEX_HTML = PATH_HTML
    init_thread_server(PORT)
    url = "http://127.0.0.1:" + str(PORT)
    webbrowser.open(url)
    print("si permite otro hilo")