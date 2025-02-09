

import { StandardElement } 
    from "./StandardElement.js";

export class StandartText extends StandardElement {

    constructor(tag) {
        super(tag);
    }

    set_text(text) {
        this.node.innerHTML = text
    }

    append_text(text) {
        this.node.innerHTML += text
    }

    extract_text() {
        let text = this.node.innerHTML
        this.node.innerHTML = ""
        return text
    }

    get_text(text) {
        return this.node.innerHTML
    }

}