

/*
Función que calcula el
promedio de los números en
la matriz enviada.
*/
export function mid(array) {
    let sum_number = 0
    for(let i in array) {
        sum_number += array[i]
    }
    return sum_number / array.length
}
    