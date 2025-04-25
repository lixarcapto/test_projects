

import { StandardElement } from "./StandardElement.js"

export class Image extends StandardElement {

    constructor(image_url = "") {
        super("img");
        this.node.setAttribute("style",
            `
            height: auto;
            object-fit: contain;
            `
        )
        this.set_image(image_url)
    }

    set_size(width, height) {
        this.node.style.width = width + "px"
        this.node.style.height = height + "px"
    }

    set_height_with_relation(height) {
        this.node.style.height = height 
            + "px"
        this.node.style.width = "auto" 
    }

    set_width_with_relation(width) {
        this.node.style.width = width
            + "px"
        this.node.style.height = "auto" 
    }

    set_image(url) {
        this.node.src = url
    }

    get_image() {
        return this.node.src
    }

}