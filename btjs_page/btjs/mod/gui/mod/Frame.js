

import { StandardElement } 
    from "./StandardElement.js";

export class Frame extends StandardElement {

    constructor(TITLE_STR) {
        super("span");
        this.node.style = `
            border:2px solid black;
            display: inline-block;
        `
        this.node.setAttribute("tag", 
            "Frame"
        )
        this.label_title = document
            .createElement("label")
        this.label_title
            .innerHTML = TITLE_STR
        this.label_title.setAttribute(
            "style",
                `
            border: 1px solid gray;
            padding: 3px;
            background: white;
            display: block; 
            `
        )
        this.node.append(this.label_title)
        this.inner_span = document
            .createElement("span")
        this.inner_span.setAttribute(
            "style",
            `
            border: 1px solid gray;
            padding: 3px;
            display: block; 
            `
        )
        this.node.append(this.inner_span)
    }

    append(WIDGET) {
        this.inner_span.append(
            WIDGET.node)
    }

    disable_guide_lines() {
        this.node.style.border = ""
    }

}