


import { StandartText } from 
    "./StandardText.js";

export class Label extends StandartText {

    constructor(text) {
        super();
        this.node = document
            .createElement("label")
        this.set_text(text)
    }

}