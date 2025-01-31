


import { StandardElement } 
    from "./StandardElement.js";

export class LabelColor 
        extends StandardElement {

    /*
    Este componente contiene un texto y 
    un cuadrado de color despues; sirve
    para crear leyendas.
    */

    constructor(text, color_hex_rgb) {
        super("span");
        this.node.style.display = "flex"
        this.__color_square = null
        this.__label = null
        this.__init_components()
        this.set_title(text)
        this.set_color_square(color_hex_rgb)
    }

    set_title(text) {
        this.__label.innerHTML 
            = "&nbsp&nbsp" + text
    }

    __init_components() {
        this.__init_label()
        this.__init_color_square()
    }

    __init_label() {
        this.__label = document
            .createElement("span")
        this.__label.style.display = "inline-flex";
        this.__label.style.padding = "3px"
        this.node.append(this.__label)
    }

    __init_color_square() {
        this.__color_square = document
            .createElement("span")
        this.__color_square.setAttribute(
                "style",
            `
            width: 16px;
            height: 16px;
            border: 2px solid black;
            `
        )
        this.node.append(this.__color_square)
    }

    set_color_square(color_hex_rgb) {
        this.__color_square.style
            .backgroundColor = color_hex_rgb
    }

}