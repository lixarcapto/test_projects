

import { StandardElement } from "./StandardElement.js"

export class ListStandard 
        extends StandardElement {

    /*
    Modulo que permite crear una lista
    ordenada de forma facil.
    */

    constructor(tag, text, array = []) {
        super("div");
        this.node.style.display = "inline"
        this.__title = document.createElement("p")
        this.__title.innerHTML = text
        this.node.appendChild(this.__title)
        this.__ol = document
            .createElement(tag)
        this.node.appendChild(this.__ol)
        this.__li_array = [] 
        this.set_content_array(array)
    }

    set_title(text) {
        this.__title.innerHTML = text
    }

    set_content_array(ARRAY) {
        this.__ol.innerHTML = ""
        let li = null
        for(let i=0;i < ARRAY.length;i++) {
            li = document.createElement("li")
            li.innerHTML = ARRAY[i]
            this.__ol.append(li)
        }
    }

}