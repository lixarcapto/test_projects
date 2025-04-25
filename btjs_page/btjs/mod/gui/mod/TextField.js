

import { StandardElement } from "./StandardElement.js"

export class TextField extends StandardElement {

    constructor(TITLE_STR) {
        super("span");
        this.label_title = null
        this.input_content = null
        this.__init_components()
        this.set_text(TITLE_STR)
    }

    __init_components() {
        this.__init_node();
        this.__init_label();
        this.__init_input();
    }

    __init_input() {
        this.input_content = document.createElement(
            "input")
        this.input_content.setAttribute("style",
            `
            display:inline;
            margin: 5px;
            `
        )
        this.input_content.type = "text"
        this.node.append(this.input_content)
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
        this.label_title = document.createElement(
            "label")
        this.label_title.setAttribute("style",
            `
            display:inline;
            margin: 5px;
            `
        )
        this.node.append(this.label_title)
    }

    set_text(title) {
        this.label_title.setAttribute("for", 
            title)
        this.label_title.innerHTML 
            = title + "&nbsp:&nbsp"
        this.input_content.name = title
        this.input_content.setAttribute("id", title)
    }

    get_value() {
        return this.input_content.value
    }

    set_value(value) {
        this.input_content.value = value
    }

    set_size(size) {
        this.input_content.size = size
    }

    set_placeholder(text) {
        this.input_content.placeholder = text
    }

    set_is_required(bool) {
        this.input_content.required = bool
    }

}