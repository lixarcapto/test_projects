

import { BaseElement } from "./BaseElement.js"

export class StandardElement extends BaseElement {

    constructor(tag_HTML) {
        super();
        this.node = document
            .createElement(tag_HTML)
        this.set_class(
            this.get_unique_class())
    }

    is_custom() {
        this.node.setAttribute(
            this.get_class())
    }

}