

import { Card } from "./Card.js";
import { Btjs } from "../../../Btjs.js";

import { StandardElement } from "./StandardElement.js";

export class Book extends StandardElement {

    /*
    Es un widget swipper de cards simples; 
    recibe en el metodo set_content 
    un array de diccionarios de cartas con 
    esta sintaxis:
    {
        "image":"",
        "title": "",
        "description": ""
    }
    Image es una URL de imagen, title es 
    el titulo de la carta y description 
    es un largo texto para la parte inferior.
    NOTA: Es recomendable que la descripcion
    tenga maximo 5 lineas; aunque puede 
    tener scroll.
    */

    constructor() {
        super("div");
        //ATRIBUTES
        this.__objs_arr = []
        this.__index = 0
        //es el valor de la imagen cargada
        this.__value = ""
        this.__init_components()
        this.__add_listeners()
    }

    // PUBLIC---------------------------------

    /*
    Este metodo recibe un array de objetos
    javascript que contienen los datos de 
    cada carta; su sintaxis es esta:
    {
        "image":"",
        "title": "",
        "description": ""
    }
    */
    set_component_objs_arr(objs_arr) {
        this.__objs_arr = objs_arr
        this.__update()
    }

    /*
    Obtiene el titulo de la carta 
    seleccionada actualmente.
    */
    get_value() {
        return this.__value
    }

    /*
    Ajusta la carta seleccionada actualmente
    por su titulo.
    */
    set_value(value) {
        let dict = null
        for(let i=0;i<this.__objs_arr.length;i++) {
            dict = this.__objs_arr[i];
            if(dict["value"] == value) {
                this.__index = i;
                break;
            }
        }
    }

    set_size(x, y) {
        let size_x_button = (10 / 100) * x
        let size_x_card = (80 / 100) * x
        this.node.style.maxWidth = x +"px"
        this.backbutton.style.height
            = y + "px"
        this.backbutton.style.width 
            = size_x_button + "px"
        this.forwardbutton.style.height 
            = y + "px"
        this.forwardbutton.style.width
            = size_x_button + "px"
        this.card.set_size(size_x_card, y)
    }

    // PRIVATE -----------------------------

    __init_node() {
        this.node.setAttribute("style",
            `
            border: 2px solid gray;
            background-color:#EBEBEB;
            display: flex;
            margin: 5px;
            `
        )
    }

    __init_components() {
        this.__init_node()
        //
        this.__init_back_button()
        //
        this.__init_card_simple()
        //
        this.__init_forward_button()
    }

    __init_card_simple() {
        this.card = Btjs.Card("title", 
            "", "text")
        this.node.append(this.card.node)
    }

    __init_forward_button() {
        this.forwardbutton = document
            .createElement("button")
        this.forwardbutton.innerHTML = " > "
        this.node.append(this.forwardbutton)
    }

    __init_back_button() {
        this.backbutton = document
            .createElement("button")
        this.backbutton.innerHTML = " < "
        this.node.append(this.backbutton)
    }

    __add_listeners() {
        this.backbutton.addEventListener(
            "click", ()=>{
                this.__react_to_back()
        })
        this.forwardbutton.addEventListener(
            "click", ()=>{
                this.__react_to_forward()
        })
    }

    __react_to_back() {
        if(this.__index > 0) {
            this.__index -= 1
            this.__update()
        }
        
    }

    __react_to_forward() {
        if(this.__objs_arr.length -1 
                    > this.__index) {
            this.__index += 1
            this.__update()
        }
    }

    __update() {
        let dict = this.__objs_arr[this.__index]
        this.card.set_title(dict["title"]) 
        this.card.set_description(
            dict["description"]) 
        this.card.set_image(dict["image"]) 
        this.__value = dict["value"]
        console.log(this.__index)
    }


}