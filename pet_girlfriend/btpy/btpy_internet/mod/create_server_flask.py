



from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Habilita CORS para toda la aplicación
pipe_function_post = (lambda e:e)

@app.route('/', methods=['POST'])
def handle_root():
    global pipe_function_post
    global pipes_function_dict
    if request.method == 'POST':
        try:
            data = request.get_json()
            if not data:
                return jsonify(
                    {"error": "No JSON data provided"}), 400
            
            # Aquí puedes procesar los datos recibidos en 'data'
            # y generar una respuesta JSON.
            response_data = pipe_function_post(
                data)
            
            return jsonify(response_data), 200

        except Exception as e:
            return jsonify({"error": f"An unexpected error occurred: {str(e)}"}), 500

def create_server_flask(debug, port, 
        pipe_function):
    global pipe_function_post
    pipe_function_post = pipe_function
    app.run(debug=True, port=5001)