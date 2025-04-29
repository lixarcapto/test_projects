
import { StandardElement } from 
    "./StandardElement.js";

export class CompositeWidget extends 
        StandardElement {

    constructor(TITLE_STR) {
        super("span");
        this.node.style = `
            border: 1px solid black;
            margin: 2px;
            display:inline-block;
            max-width: auto-fit;
            height:auto-fit;
        `
        this.label_title = document
            .createElement("label")
        this.label_title.style = `
            display: block;
            padding: 5px;
        `
        this.node.append(this.label_title)
        this.inner_span = document
            .createElement("span")
        this.inner_span.style = `
            display: block-flex;
        `
        this.node.append(this.inner_span)
        this.set_title(TITLE_STR)
    }

    set_title(TITLE_STR) {
        this.label_title.innerHTML 
            = TITLE_STR
    }

    get_title(TITLE_STR) {
        return this.label_title.innerHTML
    }

    set_in_horizontal() {
        this.label_title.style
            .display = "inline"
        this.inner_span.style
            .display = "inline-flex"
    }

    set_in_vertical() {
        this.label_title.style
            .display = "block"
        this.inner_span.style
            .display = "block-flex"
    }

}