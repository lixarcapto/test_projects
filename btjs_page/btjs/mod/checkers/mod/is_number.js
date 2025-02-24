

/*
This function is used to verify if 
the data sent is of numeric type, 
returning true if it is.
*/
// return bool
export function is_number(ANY) {
    if((Number.isInteger(ANY))
    || (ANY % 1 !== 0)) {
        return true
    }
    return false
}