

import { ConstBtjs } 
    from "../const/ConstBtjs.js";

export function random_string(SIZE, 
        CHAR_STRING = null) {
    if(CHAR_STRING == null) {
        CHAR_STRING = ConstBtjs.ANSII_ARRAY;
    }
    let r = "";
    let index = 0;
    let leng = CHAR_STRING.length;
    for (let i = 0; i < SIZE; i++) {
        index = Math.floor(
            Math.random() * leng)
        r += caracteres.charAt(index);
    }
    return r;
}