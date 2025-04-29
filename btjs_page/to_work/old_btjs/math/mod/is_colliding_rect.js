



export function is_colliding_rect(rect_a, 
        rect_b) {
    // 1. Verificar si los argumentos son objetos
    if (typeof rect_a !== 'object' 
    || typeof rect_b !== 'object') {
      return "Error: Los argumentos deben ser objetos.";
    }
    /*
    // 2. Verificar si los objetos tienen las propiedades necesarias
    if (!rect_a.x 
        || !rect_a.y 
        || !rect_a.width 
        || !rect_a.height 
                ||
        !rect_b.x 
        || !rect_b.y 
        || !rect_b.width 
        || !rect_b.height) {
      return "Error: Los objetos deben tener las propiedades x, y, ancho y alto.";
    }
    */
  
    // 3. Detectar colisión
    if (rect_a.x < rect_b.x 
        + rect_b.height &&
        rect_a.x + rect_a.width 
        > rect_b.x &&
        rect_a.y < rect_b.y 
        + rect_b.width &&
        rect_a.y + rect_a.height 
        > rect_b.y) {
      return true; // Hay colisión
    } else {
      return false; // No hay colisión
    }
  }