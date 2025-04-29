


export function create_array(SIZE, 
        DATA = null) {
    let new_array = [];
    for (let i = 0; i < SIZE; i++) {
      new_array.push(DATA);
    }
    return new_array;
}