


import { is_number } from "./is_number.js";
import { is_range } from "./is_range.js";

/*
Function to identify if the input 
number is contained within the 
sending range.
*/
//return bool
export function in_range(NUMBER, 
        RANGE_ARRAY) {
    if( ! is_number(NUMBER)) {
        console.log(`<!> Error: NUMBER(${NUMBER}) is not a number`)
        return false
    }
    if( ! is_range(RANGE_ARRAY)) {
        console.log(`<!> Error: RANGE_ARRAY(${RANGE_ARRAY}) is not a range`)
    }
    if((NUMBER >= RANGE_ARRAY[0])
    && (NUMBER <= RANGE_ARRAY[1])) {
        return true;
    }   
    return false;
}