

import { BaseElement } from "./BaseElement.js"

export class StandardElement extends BaseElement {

    constructor(tag_HTML) {
        super();
        this.node = document
            .createElement(tag_HTML)
        this.set_class(
            StandardElement.generic_class)
    }

}