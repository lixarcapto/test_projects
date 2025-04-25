



import { StandartText } from 
    "./StandardText.js";

export class LabelArea extends 
        StandartText {

    constructor(TITLE_STR = "") {
        super();
        this.node = document
            .createElement("span")
        this.node.setAttribute("style",
            `
            background-color: rgb(255, 255, 255); /* Blanco con 80% de opacidad */
            color: black;
            border: 1px solid gray;
            padding: 3px;
            display: flex;
            overflow-y: auto;
            margin: 8px;
            border-radius: 3px;
            justify-content: flex-start;
            `
        )
        this.node.innerHTML = TITLE_STR
    }

    destroy() {
        this.node.remove()
        this.node = null
    }

}