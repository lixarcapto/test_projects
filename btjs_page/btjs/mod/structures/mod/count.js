
import { is_object_js } 
    from "../../checkers/mod/is_object_js.js"

/*
Funcion que cuenta el numero de 
verificaciones con una funcion 
checker enviada en un array o jsobject.
    Envia un lambda con esta estructura:
        (e)=>{return e == condicion};
*/
export function count(STRUCTURE, 
        CHECKER) {
    let n = 0
    let array = []
    if(is_object_js(STRUCTURE)) {
        array = STRUCTURE.values() 
    } else {
        array = STRUCTURE
    }
    for(let i in array) {
        console.log("e: ", array[i])
        if(CHECKER(array[i])) {
            n += 1
        }
    }
    return n
}