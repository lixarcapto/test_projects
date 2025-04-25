

import { ConstBtjs } 
    from "../const/ConstBtjs.js";
//
import { array_to_jsobject } 
    from "./mod/array_to_jsobject.js";
import { base64_to_image } 
    from "./mod/base64_to_image.js";

export class BtjsConverters extends ConstBtjs {

    static base64_to_image(base64) {
        return base64_to_image(base64)
    }

    /*
    Funcion que convierte dos arrays en 
    un objeto javascript usando como claves
    el primer array y como valores el 
    segundo.
    */
    //return jsobject
    static array_to_jsobject(key_arr, 
            values_arr) {
        return array_to_jsobject(key_arr, 
            values_arr)
    }

}