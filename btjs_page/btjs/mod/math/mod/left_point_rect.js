


/*
calcula las coordenadas del punto 
inferior izquierdo de un rectángulo 
dado su ubicación superior derecha 
y su tamaño.
*/
export function left_point_rect(
        range_location, width, height) {
    let top_right_y = range_location[0]
    let top_right_x = range_location[1]
    let bottom_left_x = top_right_x + width
    // Calculate bottom-left x-coordinate
    let bottom_left_y = top_right_y + height
    // Calculate bottom-left y-coordinate
    let point_ar = [
        bottom_left_y, 
        bottom_left_x
    ]
    return point_ar
}

