



import { StandardElement } from "./StandardElement.js"

export class SwiperRange extends 
    StandardElement {

    /*
    Es un componente de swiper que 
    permite cambiar un número utilizando 
    las flechas en un Rango determinado.
    */

    constructor(TITLE_STR, RANGE_LIST_X2) {
        super("div");
        //propertys
        this.__number = 0
        this.__range_arr = [0, 0]
        //components
        this.__decrement = null
        this.__increment = null
        this.__label_content = null
        this.__label_title = null
        this.callback = null
        //calls
        this.__init_components(TITLE_STR)
        this.__add_listeners()
        this.set_range(RANGE_LIST_X2)
    }

    // PUBLIC --------------------------------

    /*
    Asigna un rango limite en formato 
    int array.
    */
    set_range(range_arr) {
        this.__range_arr = range_arr
    }

    set_text(text) {
        this.__label_title.innerHTML = text 
            + "&nbsp:&nbsp"
    }

    destroy() {
        this.node.remove()
        this.__range_arr = []
        this.__label_content.remove()
        this.__increment.remove()
        this.__decrement.remove()
    }

    set_value(value) {
        this.__number = value
        this.__update_value()
    }

    add_listeners(callback) {
        this.callback = callback
    }

    get_value() {
        return this.__number
    }

    // PRIVATE ---------------------------

    __init_node() {
        this.node.setAttribute("style",
            `
            display:flex;
            align-content: center;
            background-color: #f0f0f0;
            border: 1px solid gray;
            padding: 3px;
            width: fit-content;
            `
        )
        this.node.setAttribute("tag", 
            "button_index")
    }

    __init_label_title(text) {
        this.__label_title = document
            .createElement("label")
        this.node.append(this.__label_title)
        this.set_text(text)
    }

    __init_components(text) {
        this.__init_node()
        this.__init_label_title(text)
        this.__decrement = document
            .createElement("button")
        this.__decrement.innerHTML = " < "
        this.__increment = document
            .createElement("button")
        this.__increment.innerHTML = " > "
        this.__label_content = document
            .createElement("label")
        this.__update_value()
        this.node.append(this.__decrement)
        this.node.append(this.__label_content)
        this.node.append(this.__increment)
    }

    __update_value() {
        if(this.callback != null) {
            this.callback()
        }
        this.__paint_value()
    }

    __paint_value() {
        this.__label_content.innerHTML 
            = "&nbsp&nbsp" + this.__number 
                + "&nbsp&nbsp"
    }

    __react_to_decrement() {
        if(this.__range_arr[0] 
            < this.__number) {
            this.__number -= 1
        } else {
            this.__number = this
                .__range_arr[1]
        }
        this.__update_value()
    }

    __react_to_increment() {
        if(this.__range_arr[1] 
            > this.__number) {
            this.__number += 1
        } else {
            this.__number = this
                .__range_arr[0]
        }
        this.__update_value()
    }

    __add_listeners() {
        this.__decrement.addEventListener(
            "click", ()=>{
                this.__react_to_decrement()
        })
        this.__increment.addEventListener(
            "click", ()=>{
                this.__react_to_increment()
        })
    }

}