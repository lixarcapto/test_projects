



import { StandardButton } 
    from "./StandardButton.js";

export class Button extends StandardButton {

    constructor(text = "") {
        super();
        this.node = document
            .createElement("button")
        this.node.innerHTML = text
    }

}