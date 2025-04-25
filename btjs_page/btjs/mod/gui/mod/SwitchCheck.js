

import { StandardElement } from "./StandardElement.js"

export class SwitchCheck extends 
    StandardElement {

    /*
    Clase que crea un checkbox clasico
    con un texto de titulo y una sola
    opcion binaria.

        El type puede ser checkbox 
        o radio
    */

    constructor(TITLE_STR, 
            type = "checkbox") {
        super("div");
        this.node.setAttribute("tag",
            "SwitchCheck"
        )
        this.node.setAttribute("style",
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
        this.checkbox.setAttribute("id", TITLE_STR)
        this.node.append(this.checkbox)
        //
        this.title = document
            .createElement("label")
        this.title.setAttribute("for", TITLE_STR)
        this.set_title(TITLE_STR)
        this.node.append(this.title)
        this.set_font_size("16")
    }

    set_name(NAME_STR) {
        this.checkbox.setAttribute(
            "name",
            NAME_STR
        )
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