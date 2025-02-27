


export function base64_to_image(base64) {
    // Crear la URL de datos
    var dataURL = base64;
  
    // Crear un elemento de imagen 
    // y asignarle la URL
    var img = new Image();
    img.src = dataURL;
    return img
  }