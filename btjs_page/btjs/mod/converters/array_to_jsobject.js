


/*
Funcion que convierte dos arrays en 
un objeto javascript usando como claves
el primer array y como valores el 
segundo.
*/
//return jsobject
export function array_to_jsobject(key_arr, 
        values_arr) {
    let jsobject = {};
    for (let i = 0; i < key_arr.length; i++) {
        objeto[key_arr[i]] = values_arr[i];
    }
    return jsobject
}