


import { is_object_js } 
    from "../checkers/mod/is_object_js.js";

/*
Funcion que aplica un map a una estructura
que puede ser un array, un map o un objeto
javascript.
*/
export function map2(DATA, FUNCTION) {
    // if is an array
    if(Array.isArray(DATA)) {
        return DATA.map(FUNCTION);
    // if is an javascript object
    } else if (is_object_js(DATA)) {
        let new_data = {};
        for(let k in DATA) {
            new_data[k] = FUNCTION(DATA[k])
        }
        return new_data;
    //is is an map object
    } else if (DATA instanceof Map) {
        let new_map = new Map();
        for (let [k, v] of DATA) {
            new_map.set(k, v);
        }
        return new_map;
    }
}