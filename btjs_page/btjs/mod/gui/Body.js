


import { BaseElement } from "./BaseElement.js";

export class Body extends BaseElement {

    /*
    Es un elemento que representa a los 
    estilos CSS embebidos; pero que pueden
    controlarse facilmente desde Javascript.
    */

    constructor() {
        super();
        this.node = document.body
    }

    set_class(code_class) {}

}