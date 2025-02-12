

import { Btjs } from "../../Btjs.js"

/*
Función que itera sobre los 
elementos del array enviado 
buscando si alguno de los 
elementos del array retornan 
true a la función enviada.
Se diferencia de has_all en que este
se detiene al encontrar el valor
indicado.
*/
export function has_some(ARRAY, 
        CHECK_FUNCTION) {
    let data = null
    if(Btjs.is_object_js(ARRAY)) {
        data = ARRAY.values()
    }
    else {
        data = ARRAY
    }
    for(let i in data) {
        if(CHECK_FUNCTION(data[i])) {
            return true
        }
    }
    return false
}
    