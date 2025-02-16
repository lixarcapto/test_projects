


export function random_element(ARRAY) {
    // Verificamos si el array tiene 
    // elementos
    if (ARRAY.length === 0) {
      return null; // Si el array está 
      // vacío, retornamos null
    }
    // Generamos un índice aleatorio 
    // dentro del rango del array
    const indiceAleatorio = Math.floor(
        Math.random() * ARRAY.length);

    // Retornamos el elemento en el índice 
    // aleatorio
    return ARRAY[indiceAleatorio];
}