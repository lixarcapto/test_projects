

import { is_number } from "./is_number.js"

/*
Function that returns true if the 
data sent is of range array type. 
*/
// return bool
export function is_range(RANGE_ARRAY) {
    //if it is not x 2 array
    if( ! (RANGE_ARRAY.length == 2)) {
        return false
    }
    //if it is not a number
    if( ! is_number(RANGE_ARRAY[0])
    || ! is_number(RANGE_ARRAY[1])) {
        return false
    }
    //if it is not min and max
    if( ! (RANGE_ARRAY[0] < RANGE_ARRAY[1])) {
        return false
    }
    return true
}