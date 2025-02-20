

import { sum_in_range } 
    from "./sum_in_range.js"

/*
Función que desplaza un a otro 
punto sin superar los límites 
que los ejes enviados como 
intervalos.
*/
export function sum_point_in_range( old_point, 
        new_point, range_x, range_y) {
    let result_point = [0, 0]
    result_point[0] = sum_in_range(
        old_point[0],
        new_point[0], 
        range_x
    )
    result_point[1] = sum_in_range(
        old_point[1],
        new_point[1], 
        range_y
    )
    return result_point
}