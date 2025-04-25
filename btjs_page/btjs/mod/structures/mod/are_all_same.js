



/*
This function checks if the elements 
of the passed array are all equal.
*/
export function are_all_same(array) {
    return array.every(
        element => element === array[0]);
}