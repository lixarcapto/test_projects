

import { StandardButton } 
    from "./StandardButton.js";
import { InnerStyle } from "./InnerStyle.js";

export class ClickIcon extends StandardButton {

    /*
    Es un icono clickeable: pero no esta
    diseñado para ordenar texto por defecto.
    */

    constructor(title, url) {
        super();
        this.node = document.createElement(
            "button")
        this.animation = new InnerStyle(
            ":active")
        this.animation.set_background_color(
            "green")
        this.animation.set_transform(
            "translateY(4px)")
        this.animation.to_document()
        this.node.setAttribute("style",
            `
                background-color: transparent;
                border: none;
                padding: 0;
                cursor: pointer;
                transition: all 0.1s ease-in-out;
            `
        )
        this.img = document.createElement(
            "img")
        this.img.setAttribute("style",
            `
            border:none;
            `
        )
        this.img.setAttribute("src", 
            url)
        this.node.append(this.img)
        this.node.setAttribute("class",
            this.animation.get_class()
        )
    }

    set_image(url_image) {
        this.node.style.backgroundImage 
            = `url(${url_image})`;
    }


}