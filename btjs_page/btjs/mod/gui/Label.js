


import { StandartText } from 
    "./StandardText.js";

export class Label extends StandartText {

    static GENERIC_CLASS = "LABEL3453"

    static {
        let style = document.createElement(
            "style")
        style.innerHTML = `
            .${Label.GENERIC_CLASS}{
            border: 1px solid gray;
            padding: 3px;
            background: white;
            border-radius: 3px;
            }
        `
        document.head.append(style)
    }

    constructor(text) {
        super("label");
        this.node.setAttribute("class",
            Label.GENERIC_CLASS
        )
        this.set_text(text)
    }

}