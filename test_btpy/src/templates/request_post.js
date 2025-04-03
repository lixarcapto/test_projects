


export function request_post(URL, 
    REQUEST_DICT, CALLBACK) {

    // URL del servidor Flask (o cualquier servidor que acepte POST con JSON)
    const url = URL; 
    // Asegúrate de que esta URL sea correcta

    // El mensaje JSON que se 
    // enviará en el cuerpo de 
    // la solicitud
    const mensaje = REQUEST_DICT

    // Configuración de la solicitud POST
    const configuracion = {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'  // Indica que el cuerpo de la solicitud es JSON
        },
        body: JSON.stringify(mensaje) // Convierte el objeto JavaScript a cadena JSON
    };

    // Realiza la petición POST usando 
    // fetch
    fetch(url, configuracion)
        .then(response => {
            // Verifica si la respuesta 
            // del servidor es exitosa
            if (!response.ok) {
                throw new Error(`Error en la petición: ${response.status}`);
            }
            // Parsea la respuesta JSON
            return response.json();
        })
        .then(data => {
            // Muestra la respuesta del servidor en la página
            CALLBACK(data) 
        })
        .catch(error => {
            // Maneja los errores de la petición
            respuestaDiv.innerHTML = `<p>Error: ${error.message}</p>`;
        });
}