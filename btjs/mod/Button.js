



import { StandardElement } 
    from "./StandardElement.js"

export class Button extends StandardElement {

    constructor(text) {
        super();
        this.node = document
            .createElement("button")
        this.node.innerHTML = text
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