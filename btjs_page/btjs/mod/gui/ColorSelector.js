

import { StandardElement } 
    from "./StandardElement.js";

export class ColorSelector extends StandardElement {

    constructor() {
        super();
        this.input_text = document.createElement(
            "input")
        this.input_text.setAttribute("type", "color")
        this.input_text.value = "#ff0000"
    }

    destroy() {
        this.input_text.remove()
        this.input_text = null
    }

}