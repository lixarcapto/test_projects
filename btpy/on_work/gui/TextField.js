

import { StandardElement } from "./StandardElement.js"

export class TextField extends StandardElement {

    constructor(title) {
        super("span");
        this.__label = null
        this.__input = null
        this.__init_components()
        this.set_text(title)
    }

    __init_components() {
        this.__init_node();
        this.__init_label();
        this.__init_input();
    }

    __init_input() {
        this.__input = document.createElement(
            "input")
        this.__input.setAttribute("style",
            `
            display:inline;
            margin: 5px;
            `
        )
        this.__input.type = "text"
        this.node.append(this.__input)
    }

    __init_node() {
        this.node.setAttribute("style",
            `
            padding: 5px;
            margin: 3px;
            border: 1px solid gray;
            `
        )
        this.node.style.backgroundColor 
            = "#EFEFEF"
    }

    __init_label() {
        this.__label = document.createElement(
            "label")
        this.__label.setAttribute("style",
            `
            display:inline;
            margin: 5px;
            `
        )
        this.node.append(this.__label)
    }

    set_text(title) {
        this.__label.setAttribute("for", 
            title)
        this.__label.innerHTML 
            = title + "&nbsp:&nbsp"
        this.__input.name = title
        this.__input.setAttribute("id", title)
    }

    get_value() {
        return this.__input.value
    }

    set_value(value) {
        this.__input.value = value
    }

    set_size(size) {
        this.__input.size = size
    }

    set_placeholder(text) {
        this.__input.placeholder = text
    }

    set_is_required(bool) {
        this.__input.required = bool
    }

}