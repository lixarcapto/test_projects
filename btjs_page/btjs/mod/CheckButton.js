

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
        this.node = document
            .createElement("div")
        this.node.setAttribute("tag",
            "checkbutton"
        )
        this.node.setAttribute("style",
            `
            display: inline;
            `
        )
        this.checkbox = document
            .createElement("input")
        this.checkbox.setAttribute("type", 
            type)
        this.title = document
            .createElement("label")
        this.set_title(title)
        this.node.append(this.title)
        this.node.append(this.checkbox)
    }

    set_font_size(size) {
        super.set_font_size(size)
        this.checkbox.style
            .width = size + "px"
        this.checkbox.style
            .height = size + "px"
    }

    destroy() {
        this.node.remove()
        this.node = null
        this.checkbox = null
        this.title = null
    }

    set_title(text) {
        this.node.setAttribute("id", text)
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