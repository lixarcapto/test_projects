

import { StandardElement } 
    from "./StandardElement.js";

export class LabelLabel 
            extends StandardElement {

    constructor(title, text = "") {
        super("span");
        this.node.setAttribute("style",
            `
            display:inline;
            padding: 5px;
            border: 1px solid gray;
            background:#F0F0F0;
            border-radius: 3px;
            margin: 2px;
            `
        )
        this.title = document
            .createElement("span")
        this.title.style.padding = "5px"
        this.title.style.border = "1px"
        this.node.append(this.title)
        this.label = document
            .createElement("span")
        this.label.style.padding = "5px"
        this.label.style.border = "1px"
        this.label.style
            .background = "white"
        this.node.append(this.label)
        this.set_title(title)
        this.set_text(text)
    }

    set_title(text) {
        this.title.innerHTML = text
    }

    set_text(text) {
        this.label.innerHTML = text
    }

}