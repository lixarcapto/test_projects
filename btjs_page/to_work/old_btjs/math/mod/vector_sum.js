

/*
Función que suma los elementos 
de dos arrays de números en la 
misma posición del array.
*/
export function vector_sum(ARRAY_1, 
            ARRAY_2) {
    let new_array = [...ARRAY_1];
    for (let i = 0; i < ARRAY_1.length; i++) {
      new_array[i] += ARRAY_2[i];
    }
    return new_array;
}