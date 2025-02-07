

import { StandardElement } 
    from "./StandardElement.js";

export class Frame extends StandardElement {

    constructor() {
        super();
        this.node = document
            .createElement("span")
        this.node.style
            .border = "2px solid red"
    }

    disable_guide_lines() {
        this.node.style.border = ""
    }

}