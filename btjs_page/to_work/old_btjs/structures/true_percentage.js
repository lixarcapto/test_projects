


/*
Función que calcula el 
porcentaje de datos verdaderos 
de una lista booleana
*/
//return float
export function true_percentage(
        BOOL_ARRAY) {
    let true_number = 0
    for(let i in BOOL_ARRAY) {
        if(BOOL_ARRAY[i]) { 
            true_number += 1 
        }
    }
    let percent = true_number 
        * (100 / len(BOOL_ARRAY))
    percent = float(percent)
    return percent
}
    
    