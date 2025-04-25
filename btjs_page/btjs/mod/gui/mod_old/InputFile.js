


import { StandardElement } 
    from "./StandardElement.js";

export class InputFile extends StandardElement {


    constructor(title) {
        super("span");
        this.node.setAttribute("style",
            `
            display: flex;
            background-color: #EFEFEF;
            border: 1px solid gray;
            width: fit-content;
            `
        )
        this.title = document.createElement(
            "label")
        this.node.append(this.title)
        this.input = document.createElement(
            "input")
        this.input.type = "file"
        this.node.append(this.input)
        this.set_title(title)
    }

    set_title(text) {
        this.title.innerHTML = text 
            + "&nbsp:&nbsp"
    }

    set_file_type(file_type) {
        this.input.accept=file_type
    }

    // return File
    get_value() {
        return this.input.files[0]
    }

}