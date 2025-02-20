

/*
Encuentra el nuevo punto de origen
de un rectangulo centrandolo en su 
anterior punto de origen.
*/

export function center_rect_in_origin(point, 
        sizeX, sizeY) {
    const xOrigen = point[0] 
        - Math.floor(sizeX / 2);
    const yOrigen = point[1] 
        - Math.floor(sizeY / 2);
    return [xOrigen, yOrigen];
  }