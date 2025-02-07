



import { StandartText } from 
    "./StandardText.js";

export class LabelArea extends StandartText {

    constructor(text = "") {
        super();
        this.node = document
            .createElement("span")
        this.node.setAttribute("style",
            `
            background-color: rgb(255, 255, 255); /* Blanco con 80% de opacidad */
            color: black;
            padding: 3px;
            display: flex;
            overflow-y: auto;
            margin: 8px;
            justify-content: flex-start;
            `
        )
        this.node.innerHTML = text
    }

    destroy() {
        this.node.remove()
        this.node = null
    }

}