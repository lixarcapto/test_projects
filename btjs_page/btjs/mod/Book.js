

import { Card } from "./Card.js";
import { Btjs } from "../Btjs.js";

import { StandardElement } from "./StandardElement.js";

export class Book extends StandardElement {

    constructor() {
        super();
        this.input_text = document.createElement(
            "div")
        this.input_text.setAttribute("style",
            `
            border: 2px solid gray;
            background-color:#EBEBEB;
            display: flex;
            margin: 5px;
            `
        )
        //
        this.backbutton = document
            .createElement("button")
        this.backbutton.innerHTML = " < "
        this.input_text.append(this.backbutton)
        //
        this.card = Btjs.Card("title", 
            "", "text")
        this.input_text.append(this.card.input_text)
        //
        this.forwardbutton = document
            .createElement("button")
        this.forwardbutton.innerHTML = " > "
        this.input_text.append(this.forwardbutton)
        this.dict_arr = []
        this.index = 0
        //es el valor de la imagen cargada
        this.value = ""
        this.__add_listeners()
    }

    set_dict_arr(dict_arr) {
        this.dict_arr = dict_arr
        this.update(

        )
    }

    __add_listeners() {
        this.backbutton.addEventListener(
            "click", ()=>{
                this.back()
        })
        this.forwardbutton.addEventListener(
            "click", ()=>{
                this.forward()
        })
    }

    back() {
        if(this.index > 0) {
            this.index -= 1
            this.update()
        }
        
    }

    forward() {
        if(this.dict_arr.length -1 
                    > this.index) {
            this.index += 1
            this.update()
        }
    }

    update() {
        let dict = this.dict_arr[this.index]
        this.card.set_title(dict["title"]) 
        this.card.set_description(
            dict["description"]) 
        this.card.set_image(dict["image"]) 
        this.value = dict["value"]
        console.log(this.index)
    }

    get_value() {
        return this.value
    }

    set_value(value) {
        let dict = null
        for(let i=0;i<this.dict_arr.length;i++) {
            dict = this.dict_arr[i];
            if(dict["value"] == value) {
                this.index = i;
                break;
            }
        }
    }

    set_size_card(x, y) {
        let size_x_button = (10 / 100) * x
        let size_x_card = (80 / 100) * x
        this.input_text.style.maxWidth = x +"px"
        this.backbutton.style.height
            = y + "px"
        this.backbutton.style.width 
            = size_x_button + "px"
        this.forwardbutton.style.height 
            = y + "px"
        this.forwardbutton.style.width
            = size_x_button + "px"
        this.card.set_size_card(size_x_card, y)
    }

}