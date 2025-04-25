



import { SwiperStandard } 
    from "./SwiperStandard.js";

export class SwiperText extends 
    SwiperStandard {

    /*
    Es un componente de swiper que 
    permite cambiar el elemento de un 
    array string con las flechas en un 
    Rango determinado.
    */

    constructor(TITLE_STR, 
            CONTENT_LIST_STR) {
        super(TITLE_STR);
        this.__callback = null
        this.__index = 0
        this.__content_array = []
        this.__content_array = CONTENT_LIST_STR
        this.__update_content()
    }

    // PUBLIC ------------------------------

    set_content_list(CONTENT_LIST) {
        this.__content_array 
            = CONTENT_LIST
    }

    get_value() {
        return this.__content_array
            [this.__index]
    }

    set_value(index) {
        this.__index = index
        this.__update_content()
    }

    // PRIVATE ----------------------------

    __update_content() {
        let e = this.__content_array[
            this.__index ]
        this.__label_content.innerHTML
            = "&nbsp&nbsp" 
            + e + "&nbsp&nbsp"
    }

    //override
    __react_to_decrement() {
        const leng = this.__content_array
            .length -1
        if(this.__index > 0) {
            this.__index -= 1
            
        } else {
            this.__index = leng
        }
    }

    //override
    __react_to_increment() {
        const leng = this.__content_array
            .length -1
        if(this.__index < leng) {
            this.__index += 1
        } else {
            this.__index = 0
        }
    }

}