

import { StandardElement } 
    from "./StandardElement.js";

export class ColorSelector extends StandardElement {

    constructor() {
        super();
        this.node = document.createElement(
            "input")
        this.node.setAttribute("type", "color")
        this.node.value = "#ff0000"
    }

    destroy() {
        this.node.remove()
        this.node = null
    }

}