


/*
Function that adjusts the sent list
to the indicated size.
*/
export function fit_list(ARRAY, SIZE, 
        DEFAULT_VALUE = null) {
    //create copy of array
    let nuevoArray = [...ARRAY];
    // if is lower
    while (nuevoArray.length < SIZE) {
      nuevoArray.push(DEFAULT_VALUE);
    }
    // if is greater
    if (nuevoArray.length > SIZE) {
      nuevoArray.length = SIZE;
    }
    return nuevoArray;
}