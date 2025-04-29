

/*
This function calculates the center 
point of a square represented by 
a dictionary.
*/
export function center_square(point_location,
            width, height) {
    return [
        point[0] + width,
        point[1] + height
    ]
}