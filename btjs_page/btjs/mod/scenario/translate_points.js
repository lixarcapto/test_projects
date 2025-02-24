


/*
Traslada una lista de puntos a un 
nuevo espacio rectangular.
*/
export function translate_points(
        point_list, origen_x, 
        origen_y, width, height) {
    let listaPuntosTrasladada = [];
    for (const punto of point_list) {
      const [x, y] = punto;
      // Verificamos si el punto está dentro del nuevo espacio
      if (origen_x <= x && x < origen_x + width && origen_y <= y && y < origen_y + height) {
        // Trasladamos el punto restando las coordenadas del origen
        const xNuevo = x - origen_x;
        const yNuevo = y - origen_y;
        listaPuntosTrasladada.push([xNuevo, yNuevo]);
      } else {
        console.log("El punto", punto, "está fuera del nuevo espacio.");
      }
    }
    return listaPuntosTrasladada;
}