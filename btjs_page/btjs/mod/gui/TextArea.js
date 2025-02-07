

import { StandardElement } from "./StandardElement.js"

export class TextArea extends StandardElement {

    constructor(key, text = "") {
        super();
        this.node = document
            .createElement("span")
        this.node.setAttribute("id",
            key
        )
        this.node.setAttribute("style",
            `
            display:block;
            border: 1px solid gray;
            padding: 4px;
            background-color: #EFEFEF;
            `
        )
        //
        this.title = document
            .createElement("label")
        this.title.setAttribute("for", key)
        this.title.style.display = "block"
        this.node.append(this.title)
        this.set_text(key)
        //
        this.input_text = document
            .createElement("textarea")
        this.input_text.style
            .display = "block"
        this.input_text.setAttribute("id", 
            key)
        this.input_text.setAttribute("style", 
        `
            overflow-y: auto;
            resize: none;
            width: 100%;
            box-sizing: border-box;
        `
        )
        this.node.append(this.input_text)
        //
        this.set_value(text)
    }

    set_id(ID) {
        this.node.setAttribute("id", ID)
        this.input_text.setAttribute(
            "id", ID)
        this.input_text.setAttribute("name", ID)
        this.set_text(ID)
    }

    set_text(text) {
        this.title.innerHTML = text 
            + "&nbsp:&nbsp"
    }

    set_size(rows, cols) {
        this.input_text.setAttribute("rows", rows)
        this.input_text.setAttribute("cols", cols)
    }

    set_lines_size(rows, cols) {
        this.input_text.setAttribute("rows", rows)
        this.input_text.setAttribute("cols", cols)
    }

    get_value() {
        return this.input_text.value
    }

    set_value(text) {
        this.input_text.value = text
    }

    append_value(text) {
        this.input_text.value += text
    }

    extract_value() {
        let text = this.input_text.value
        this.input_text.value = ""
        return text
    }


}