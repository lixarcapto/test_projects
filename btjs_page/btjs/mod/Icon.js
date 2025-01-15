

import { StandardButton } 
    from "./StandardButton.js";

export class Icon extends StandardButton {

    /*
    Arreglar este porque no funciona.
    */

    constructor(url) {
        super();
        this.node = document.createElement(
            "button")
        this.node.setAttribute("style",
            `
            background-color: transparent;
            border: none;
            padding: 0;
            `
        )
        this.img = document.createElement(
            "img")
        this.img.setAttribute("src", 
            url)
        this.node.append(this.img)
    }


}