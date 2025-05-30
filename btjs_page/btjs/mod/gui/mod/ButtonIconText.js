


import { ClickIconStandard } 
    from "./ClickIconStandard.js";

export class ButtonIconText 
        extends ClickIconStandard {

    /*
    Es un boton de icono con un texto
    al lado si se configura en put_horizontal
    y el texto abajo si se configura en
    put_upright.
    */

    constructor(TITLE_STR, IMAGE_URL_STR) {
        super(TITLE_STR, IMAGE_URL_STR);
        this.__customize_node()
        this.__init_label()
        this.__img.style.maxWidth = "100%"
        this.__img.style.flex =  "0 0 auto"
        this.set_text(TITLE_STR)
    }

    __customize_node() {
        this.node.setAttribute("style",
            `
            display: flex;
            align-items: center; 
            justify-content: center;
            background-color: #EFEFEF;
            border: 1px solid gray;
            cursor: pointer;
            `
        )
    }

    __init_label() {
        this.label = document
            .createElement("label")
        this.label.setAttribute("style",
            `
            display:flex;
            justify-content: center;
            padding: 5px;
            font-size: 16px;
            align-items: center;
            text-align: center;
            `
        )
        this.node.append(this.label)
    }

    put_upright() {
        this.node.style.display = "grid"
        this.node.style.gridTemplateRows 
            = "auto 1fr"
        this.node.style.backgroundColor 
            = "transparent"
        this.node.style.border = "none"
        
    }

    put_horizontally() {
        this.node.style.display =  "flex"
    }

    set_text(text) {
        this.label.innerHTML = text
    }

    set_foreground(color) {
        this.label.style.color = color
    }

}