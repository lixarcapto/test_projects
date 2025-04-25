

import { ClickIconStandard } from "./ClickIconStandard.js";

export class ButtonIconTextOverlay 
        extends ClickIconStandard {

    /*
    Es un boton de click con un icono
    de imagen y un texto sobrepuesto 
    al centro; ademas el texto es mas grueso
    y tiene borde.
    */

    constructor(TITLE_STR, IMAGE_URL_STR) {
        super("", IMAGE_URL_STR);
        this.label = document
            .createElement("label")
        this.node.append(this.label)
        this.node.style.textAlign 
            = "center"
        this.node.style.position 
            = "relative"
        this.node.style.justifyContent 
            = "center"
        this.node.style.display = "flex"
        this.__img.setAttribute("style",
            `
            position: relative;
            top: 0;
            left: 0;
            object-fit: cover;
            `
        )
        this.label.setAttribute("style",
            `
            position: absolute;
            display: flex;
            color: white;
            justify-content: center;
            align-items: center;
            padding: 10px 10px;
            top: 15%;
            font-size: 30px;
            font-weight: bold;
            z-index: 1;
            text-shadow: 1px 1px 0 #000,
               -1px -1px 0 #000,  
               1px -1px 0 #000,
               -1px 1px 0 #000;
            `
        )
        this.set_text(TITLE_STR)
    }

    set_text(text) {
        this.label.innerHTML = text
    }

    set_foreground(color) {
        this.label.style.color = color
    }

}