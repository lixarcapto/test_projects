

import { StandardElement } from "./StandardElement.js"

export class TextArea extends StandardElement {

    constructor(text) {
        super();
        this.node = document
            .createElement("textarea")
        this.node.setAttribute("style", 
        `
        overflow-y: auto;
        resize: none;
        `
        )
        this.set_value(text)
    }

    set_size(rows, cols) {
        this.node.setAttribute("rows", rows)
        this.node.setAttribute("cols", cols)
    }

    set_lines_size(rows, cols) {
        this.node.setAttribute("rows", rows)
        this.node.setAttribute("cols", cols)
    }

    get_value() {
        return this.node.value
    }

    set_value(text) {
        this.node.value = text
    }


}