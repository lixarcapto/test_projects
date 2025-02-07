

import { StandardElement } from "./StandardElement.js"

export class CheckButton extends StandardElement {

    /*
    Clase que crea un checkbox clasico
    con un texto de titulo y una sola
    opcion binaria.

        El type puede ser checkbox 
        o radio
    */

    constructor(title, type) {
        super();
        this.input_text = document
            .createElement("div")
        this.input_text.setAttribute("tag",
            "checkbutton"
        )
        this.input_text.setAttribute("style",
            `
            display:inline;
            border: 1px solid gray;
            padding: 5px;
            background-color: #EFEFEF;
            `
        )
        this.checkbox = document
            .createElement("input")
        this.checkbox.setAttribute("type", 
            type)
        this.checkbox.setAttribute("id", title)
        this.title = document
            .createElement("label")
        this.title.setAttribute("for", title)
        this.set_title(title)
        this.input_text.append(this.title)
        this.input_text.append(this.checkbox)
        this.set_font_size("16")
    }

    set_font_size(size) {
        super.set_font_size(size)
        this.checkbox.style
            .width = size + "px"
        this.checkbox.style
            .height = size + "px"
    }

    destroy() {
        this.input_text.remove()
        this.input_text = null
        this.checkbox = null
        this.title = null
    }

    set_title(text) {
        this.input_text.setAttribute("id", text)
        this.title.innerHTML = text
    }

    get_title() {
        return this.title.innerHTML
    }

    set_value(value) {
        this.checkbox.checked = value
    }

    get_value() {
        return this.checkbox.checked
    }



}