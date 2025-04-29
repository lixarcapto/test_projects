


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
            border-radius: 3px;
            padding: 5px;
            border: 1px solid gray;
            border-radius: 3px;
            margin: 2px;
            `
        )
        this.set_text(TITLE_STR)
    }

}