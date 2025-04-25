


import { StandartText } from 
    "./StandardText.js";

export class Label extends StandartText {

    /*
    Widget que encapsula un label HTML.
    */

    constructor(TITLE_STR = "") {
        super("label");
        this.node.setAttribute("style",
            `
            border: 1px solid gray;
            padding: 3px;
            background: white;
            border-radius: 3px;
            `
        )
        this.set_text(TITLE_STR)
    }

}