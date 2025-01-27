

import { StandardElement } from "./StandardElement.js"

export class Image extends StandardElement {

    constructor() {
        super();
        this.input_text = document
            .createElement("img")
        this.input_text.setAttribute("style",
            `
            height: auto;
            object-fit: contain;
            `
        )
    }

    set_size(width, height) {
        this.input_text.style.width = width
    }

    set_url(url) {
        this.input_text.setAttribute("src", url)
    }

    get_url() {
        return this.input_text.getAttribute("src")
    }

}