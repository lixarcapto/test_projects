

 
/*
Function to identify if the input 
number is contained within the 
sending range.
*/
export function in_range(number, range_arr) {
    if((number >= range_arr[0])
    && (number <= range_arr[1])) {
        return true;
    }   
    return false;
}