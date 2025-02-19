

import { StandardElement } 
    from "./StandardElement.js";

export class StandardButton 
        extends StandardElement {

    constructor() {
        super("button");
        this.node.setAttribute("style",
            `
            padding: 3px;
            font-size: 16px;
            `
        )
    }

    add_click_listener(FUNCTION) {
        this.node.addEventListener("click",
            FUNCTION)
    }

    add_mouseover_listener(FUNCTION) {
        this.node.addEventListener("mouseover",
            FUNCTION)
    }

    add_mouseout_listener(FUNCTION) {
        this.node.addEventListener("mouseout",
            FUNCTION)
    }

    add_click_listener(FUNCTION) {
        this.node.addEventListener("click",
            FUNCTION)
    }

    destroy() {
        this.node.remove()
    }

}