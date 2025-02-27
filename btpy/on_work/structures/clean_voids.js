


/*
Función que crea un nuevo array
eliminando todos los valores 
None y void
*/
export function clean_voids(ARRAY) {
    new_array = []
    for(let i in ARRAY) {
        if(ARRAY[i] == null) {continue;}
        if(ARRAY[i] == "") {continue;}
        if(ARRAY[i] == []) {continue;}
        if(ARRAY[i] == {}) {continue;}
        new_array.append(ARRAY[i])
    }
    return new_array
}