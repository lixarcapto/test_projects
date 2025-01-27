

import { StandardElement } from "./StandardElement.js"

export class TextField extends StandardElement {

    constructor(title) {
        super();
        this.input_text = document.createElement(
            "span")
        this.input_text.setAttribute("style",
                `
                padding: 5px;
                margin: 3px;
                border: 1px solid gray;
                `
        )
        this.input_text.style.backgroundColor 
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
        this.input_text.append(this.label)
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
        this.input_text.append(this.input)
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