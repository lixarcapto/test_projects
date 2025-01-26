

import { StandardElement } 
    from "./StandardElement.js";

export class StandardButton extends StandardElement {

    constructor() {
        super();
        this.node = null
        this.info_bubble = null
    }

    set_text_bubble(text) {
        this.add_info_bubble()
        this.info_bubble.innerHTML = text
    }

    add_info_bubble() {
        if(null != this.info_bubble) {
            return null
        }
        this.info_bubble = document
            .createElement("div")
        this.info_bubble.setAttribute("style",
            `
            display: none;
            position: absolute;
            z-index: 2;
            background-color:
                 rgb(255, 255, 255);
            bakground-color: white;
            opacity: 1;
            `
        )
        this.node.append(this.info_bubble)
        this.node.addEventListener(
            'mouseover', () => {
            this.info_bubble.style
                .display = 'block';
        });
        this.node.addEventListener(
            'mouseout', () => {
            this.info_bubble.style
                .display = 'none';
        });
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