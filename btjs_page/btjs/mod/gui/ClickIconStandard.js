

import { StandardButton } 
    from "./StandardButton.js";
import { InnerStyle } from "./InnerStyle.js";

export class ClickIconStandard 
        extends StandardButton {

    /*
    Es un icono clickeable: pero no esta
    diseñado para ordenar texto por defecto.
    */

    constructor(title, url) {
        super();
        this.__animation = null
        this.__img = null
        this.__init_components()
        this.set_image(url)
    }

    set_image(url) {
        this.__img.src = url
    }

    __init_components() {
        this.__init_img()
        this.__init_animation_style()
    }

    __init_img() {
        this.__img = document.createElement(
            "img")
        this.__img.style.border = "none"
        this.node.append(this.__img)
    }

    __init_animation_style() {
        this.__animation = new InnerStyle(
            this.get_unique_class(),
            "active")
        this.__animation.set_background_color(
            "green")
        this.__animation.set_transform(
            "translateY(4px)")
        this.__animation.to_document()
    }

}