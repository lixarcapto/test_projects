

import { StandardElement } 
    from "./StandardElement.js";

export class Button 
        extends StandardElement {

    /*
    Widget que encapsula
    un button HTML.
    */

    constructor(TITLE_STR = "") {
        super("button");
        this.node.innerHTML = TITLE_STR
        this.node.setAttribute("style",
            `
            font-size: 14px;
            
            padding: 5px;
            border: 1px solid gray;
            background:#F0F0F0;
            border-radius: 3px;
            margin: 2px;
            `
        )
    }

    add_click_listener(FUNCTION) {
        this.node.addEventListener(
            "click",
            FUNCTION)
    }

    add_mouse_down_listener(FUNCTION) {
        this.node.addEventListener(
            "mousedown",
            FUNCTION)
    }

    add_mouse_over_listener(FUNCTION) {
        this.node.addEventListener(
            "mouseover",
            FUNCTION)
    }

    add_mouse_out_listener(FUNCTION) {
        this.node.addEventListener(
            "mouseout",
            FUNCTION)
    }

    add_mouse_up_listener(FUNCTION) {
        this.node.addEventListener(
            "mouseup",
            FUNCTION)
    }

    destroy() {
        this.node.remove()
    }

}