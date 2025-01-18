


import { StandardElement } from "./StandardElement.js"

export class Label extends StandardElement {

    constructor(text) {
        super();
        this.node = document
            .createElement("label")
        this.set_text(text)
    }

    set_text(text) {
        this.node.innerHTML = text + "&nbsp:&nbsp"
    }

}