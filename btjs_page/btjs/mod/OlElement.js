

import { StandardElement } from "./StandardElement.js"

export class OLElement extends StandardElement {

    /*
    Modulo que permite crear una lista
    ordenada de forma facil.
    */

    constructor(text, array) {
        super();
        this.input_text = document
            .createElement("div")
        this.input_text.style.display = "inline"
        this.p = document.createElement("p")
        this.p.innerHTML = text
        this.input_text.appendChild(this.p)
        this.ol = document
            .createElement("ol")
        this.input_text.appendChild(this.ol)
        this.li_array = [] 
        this.create_list(array)
    }

    set_title(text) {
        this.p.innerHTML = text
    }

    create_list(ARRAY) {
        this.ol.innerHTML = ""
        let li = null
        for(let i=0;i < ARRAY.length;i++) {
            li = document.createElement("li")
            li.innerHTML = ARRAY[i]
            this.ol.append(li)
        }
    }

}