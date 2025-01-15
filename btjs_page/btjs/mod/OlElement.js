

import { StandardElement } from "./StandardElement.js"

export class OLElement extends StandardElement {

    /*
    Modulo que permite crear una lista
    ordenada de forma facil.
    */

    constructor(text, array) {
        super();
        this.node = document
            .createElement("div")
        this.node.style.display = "inline"
        this.p = document.createElement("p")
        this.p.innerHTML = text
        this.node.appendChild(this.p)
        this.ol = document
            .createElement("ol")
        this.node.appendChild(this.ol)
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