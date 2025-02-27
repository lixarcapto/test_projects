

import { Btjs } from "../../Btjs.js"

/*
Función que itera sobre los elementos del
array enviado buscando si todos los 
elementos del array retornan true a la 
función enviada.
*/
export function has_all(ARRAY, 
        CHECK_FUNCTION) {
    let data = null
    if(Btjs.is_object_js(ARRAY)) {
        data = ARRAY.values()
    }
    else {
        data = ARRAY
    }
    for(let i in data) {
        if( ! CHECK_FUNCTION(data[i])) {
            return false
        }
    }
    return true
}
    