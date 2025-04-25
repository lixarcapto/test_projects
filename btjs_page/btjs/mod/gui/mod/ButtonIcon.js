



import { ClickIconStandard } from "./ClickIconStandard.js";

export class ButtonIcon extends 
    ClickIconStandard {

    /*
    Este componente está diseñado 
    exclusivamente para mostrar un 
    botón con una imagen y Añadir 
    un tooltip o info-buble que identifique 
    la función del botón.
    */

    constructor(TITLE_STR, IMAGE_URL_STR) {
        super(TITLE_STR, IMAGE_URL_STR);
        this.__info_bubble = null
        this.__init_node()
        this.set_text(TITLE_STR)
    }

    __init_node() {
        this.node.setAttribute("style",
            `
                display:flex;
                justify-content: center;
                width: fit-content;
                height: fit-content;
                background-color: transparent;
                border: none;
                padding: 0;
                cursor: pointer;
                transition: all 0.1s ease-in-out;
            `
        )
    }

    set_text(text) {
        this.__set_text_bubble(text)
        this.__img.alt = text
    }

    __set_text_bubble(text) {
        this.__add_info_bubble()
        this.__info_bubble.innerHTML = text
    }

    __add_info_bubble() {
        if(null != this.__info_bubble) {
            return null
        }
        this.__info_bubble = document
            .createElement("div")
        this.__info_bubble.setAttribute("style",
            `
            display: none;
            position: absolute;
            padding: 5px;
            z-index: 2;
            border: 2px solid gray;
            background-color:
                 rgb(255, 255, 255);
            bakground-color: white;
            opacity: 1;
            `
        )
        this.node.append(this.__info_bubble)
        this.node.addEventListener(
            'mouseover', () => {
            this.__info_bubble.style
                .display = 'block';
        });
        this.node.addEventListener(
            'mouseout', () => {
            this.__info_bubble.style
                .display = 'none';
        });
    }

}