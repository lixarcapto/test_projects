

import { StandardElement } from "./StandardElement.js"

export class TextField extends StandardElement {

    constructor(title) {
        super();
        this.node = document.createElement(
            "span")
        this.node.setAttribute("style",
                `
                padding: 5px;
                margin: 3px;
                border: 1px solid gray;
                `
        )
        this.node.style.backgroundColor 
            = "#EFEFEF"
        this.label = document.createElement(
            "label")
        this.label.setAttribute("for", title)
        this.label.setAttribute("style",
            `
            display:inline;
            margin: 5px;
            `
        )
        this.node.append(this.label)
        this.input = document.createElement(
            "input")
        this.input.setAttribute("style",
            `
            display:inline;
            margin: 5px;
            `
        )
        this.input.name = title
        this.input.setAttribute("id", title)
        this.input.type = "text"
        this.node.append(this.input)
        this.set_text(title)
    }

    set_text(text) {
        this.label.innerHTML 
            = text + "&nbsp:&nbsp"
    }

    get_value() {
        return this.input.value
    }

    set_value(value) {
        this.input.value = value
    }

    set_size(size) {
        this.input.size = size
    }

    set_placeholder(text) {
        this.input.placeholder = text
    }

    set_is_required(bool) {
        this.input.required = bool
    }

}