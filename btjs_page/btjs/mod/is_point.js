


/*
 Función que verifica  el dato 
 enviado es un punto 2D
*/
export function is_point_2d(data) {
    return __is_point(data, 2)
}


/*
 Función que verifica  el dato 
 enviado es un punto 3D
*/
export function is_point_3d(data) {
    return __is_point(data, 3)
}


export function __is_point(data, size) {
   // si no es lista
   if(! (Array.isArray(data))) {
        return false;
   }
   // si es mas pequeño o mas grande
   if(! (data.length == size)) {
        return false;
   }
   // si no son numeros
   for(let i in data) {
        if( ! (Number.isInteger(data[i]))
        && ! (data % 1 !== 0)) {
            return false;
        }
   }  
   return true;
}