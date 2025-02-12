


import { StandartText } from 
    "./StandardText.js";

export class Label extends StandartText {


    constructor(text) {
        super("label");
        this.node.setAttribute("style",
            `
            border: 1px solid gray;
            padding: 3px;
            background: white;
            border-radius: 3px;
            `
        )
        this.set_text(text)
    }

}