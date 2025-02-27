

/*
Funcion que suma dos valores en 
un rango limitado, si supera o es 
inferior al rango se limita a 
ajustar el limite.
*/
export function sum_in_range(value_a, 
        value_b, range_arr) {
    let result = value_a + value_b
    if(result > range_arr[1]) {
        return range_arr[1]
    } 
    if(result < range_arr[0]) {
        return range_arr[0]
    } 
    return result
}