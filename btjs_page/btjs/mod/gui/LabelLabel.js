

import { StandardElement } 
    from "./StandardElement.js";

export class LabelLabel 
            extends StandardElement {

    constructor(title, text = "") {
        super("span");
        this.node.setAttribute("style",
            `
            border: 1px solid gray;
            padding: 3px;
            background: white;
            border-radius: 3px;
            `
        )
        this.title = document
            .createElement("span")
        this.node.append(this.title)
        this.label = document
            .createElement("span")
        this.node.append(this.label)
        this.set_title(title)
        this.set_text(text)
    }

    set_title(text) {
        this.title.innerHTML = text 
            + "&nbsp&nbsp:&nbsp&nbsp"
    }

    set_text(text) {
        this.label.innerHTML = text
    }

}