

import { Btjs } from "../../Btjs.js"

export function find_closest_lower_array(
        ARRAY, NUMBER) {
    let last_element = 0
    let array = Btjs.sort_from_largest(
        ARRAY)
    console.log(array)
    for(let i in array) {
        if(array[i] < NUMBER) {
            last_element = array[i]
            return last_element
        }
    }
    return last_element
}

export function find_closest_highest_array(
    ARRAY, NUMBER) {
let last_element = 0
let array = Btjs.sort_from_smallest(
    ARRAY)
for(let i in array) {
    if(array[i] > NUMBER) {
        return last_element
    }
    last_element = array[i]
}
return last_element
}