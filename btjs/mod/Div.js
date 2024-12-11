



import { StandardElement } 
    from "./StandardElement.js"

export class Div extends StandardElement {

    constructor(text = "") {
        super();
        this.node = document
            .createElement("div")
        this.node.innerHTML = text
    }

}