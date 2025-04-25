

import { StandardElement } 
    from "./StandardElement.js";

export class SwiperStandard extends 
    StandardElement {

    /*
    Clase estandarizada para crear 
    componentes de tipo swipper.

    El importante llamar al inicio al
    metodo __update_content para añadir
    un valor inicial.
    */

    constructor(title) {
        super("span");
        this.__decrement = null
        this.__increment = null
        this.__callback = null
        this.__label_title = null 
        this.__label_content = null
        //calls
        this.__init_components()
        this.__add_listeners_default()
        this.set_title(title)
    }

    // PUBLIC ------------------------------

    set_title(text) {
        this.__label_title.innerHTML 
            = text + "&nbsp:&nbsp"
    }

    add_listeners(callback) {
        this.__callback = callback
    }

    destroy() {
        this.node.remove()
        this.node = null
        this.__increment = null
        this.__decrement = null
        this.__label_content = null
        this.__label_title = null
    }

    /*
    Sobrescribe este metodo para añadir un
    get_value.
    */
    //return any
    get_value() {
        //abstract
    }

    /*
    Sobrescribe este metodo para añadir un
    set_value.
    */
    set_value(any) {
        //abstract
    }

    // PRIVATE ------------------------------

    /* 
    Sobreescribe este metodo para 
    actualizar el contenido principal
    con cada click del usuario.
    */
    __update_content() {
        //abstract
    }
    
    /*
    Sobreescribe este metodo para 
    añadir un comportamiento a increment.
    */
    __react_to_increment() {
        //abstract
    }

    /*
    Sobreescribe este metodo para 
    añadir un comportamiento a decrement.
    */
    __react_to_decrement() {
        //abstract
    }

    __init_label_title() {
        this.__label_title = document
            .createElement("label")
        this.node.append(this.__label_title)
    }

    /*
    Llama a la callback almacenada por el
    usuario cuando los botones son 
    clickeados.
    */
    __call_callback() {
        if(this.__callback != null) {
            this.__callback()
        }
    }

    __add_listeners_default() {
        this.__decrement.addEventListener(
            "click", 
            ()=>{
                this.__react_to_decrement()
                this.__update_content()
                this.__call_callback()
            }
        )
        this.__increment.addEventListener(
            "click", 
            ()=>{
                this.__react_to_increment()
                this.__update_content()
                this.__call_callback()
            }
        )
    }

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
            "swipper")
    }

    __init_label_content() {
        this.__label_content = document
            .createElement("label")
        this.node.append(
            this.__label_content)
    }

    __init_decrement_button() {
        this.__decrement = document
            .createElement("button")
        this.__decrement.innerHTML = " < "
        this.node.append(this.__decrement)
    }

    __init_increment_button() {
        this.__increment = document
            .createElement("button")
        this.__increment.innerHTML = " > "
        this.node.append(this.__increment)
    }

    __init_components() {
        this.__init_node()
        this.__init_label_title()
        this.__init_decrement_button()
        this.__init_label_content()
        this.__init_increment_button()
    }

}