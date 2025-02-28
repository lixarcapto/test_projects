


from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Habilita CORS para toda la aplicación

@app.route('/', methods=['POST'])
def handle_root():
    if request.method == 'POST':
        try:
            data = request.get_json()
            if not data:
                return jsonify({"error": "No JSON data provided"}), 400
            
            # Aquí puedes procesar los datos recibidos en 'data'
            # y generar una respuesta JSON.

            response_data = {
                "status": "success",
                "received_data": "si funciona"
            }
            return jsonify(response_data), 200

        except Exception as e:
            return jsonify({"error": f"An unexpected error occurred: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5001)