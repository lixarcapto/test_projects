


import { StandardElement } from "./StandardElement.js"

export class Body extends StandardElement {

    /*
    Es un elemento que representa a los 
    estilos CSS embebidos; pero que pueden
    controlarse facilmente desde Javascript.
    */

    constructor() {
        super();
        this.input_text = document.body
    }

}