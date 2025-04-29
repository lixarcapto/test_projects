



/*
Determina si un punto se encuentra 
dentro de un rectángulo.
*/
export function point_in_rect(point_location, 
        width, height) {
    let origen_x = point_location[0]
    let origen_y = point_location[1]
    let extension_point = __get_extension_point()
    let punto_x = extension_point[0]
    let punto_y = extension_point[1]
    // Calculamos las coordenadas de 
    // la esquina inferior derecha del 
    // rectángulo
    let x_max = origen_x + width
    let y_max = origen_y + height
    // Verificamos si las coordenadas 
    // del punto están dentro de los 
    // límites del rectángulo
    let result = (origen_x <= punto_x <= x_max)
        && (origen_y <= punto_y <= y_max)
    return result
}

/*
Calcula el punto de extensión 
derecho de un rectángulo.
*/
function __get_extension_point(
        point_location, width, height) {
    // El punto de extensión derecho 
    // tiene la misma coordenada y que 
    // el punto de origen
    y = point_location[1]
    // La coordenada x se calcula 
    // sumando el ancho al origen_x
    x = point_location[0] + width
    return [x, y]
}