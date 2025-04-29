

import { BaseElement } from "./BaseElement.js"

export class StandardElement extends 
        BaseElement {

    /*
    Esta clase sirve para crear componentes
    graficos de tipo widget; es decir 
    los componentes que se incluyen al
    interior de una ventana.
    */

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