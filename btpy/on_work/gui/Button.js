



import { StandardButton } 
    from "./StandardButton.js";

export class Button extends StandardButton {

    constructor(text = "") {
        super("button");
        this.node.innerHTML = text
    }

}