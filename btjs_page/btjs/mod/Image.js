

import { StandardElement } from "./StandardElement.js"

export class Image extends StandardElement {

    constructor() {
        super();
        this.node = document
            .createElement("img")
        this.node.setAttribute("style",
            `
            height: auto;
            object-fit: contain;
            `
        )
    }

    set_size(width, height) {
        this.node.setAttribute("width", url)
        this.node.setAttribute("height", url)
    }

    set_url(url) {
        this.node.setAttribute("src", url)
    }

    get_url() {
        return this.node.getAttribute("src")
    }

}