


/*
Encuentra el punto de origen 
(esquina superior izquierda) 
de un rectángulo.
Calculamos las coordenadas del 
origen restando la mitad de las 
dimensiones al centro
*/
export function origin_by_center(point, 
        width, height) {
    const xOrigen = point[0] 
        - Math.floor(width / 2);
    const yOrigen = point[1] 
        - Math.floor(height / 2);
    return [xOrigen, yOrigen];
}