

import { StandardElement } 
    from "./StandardElement.js";

export class IconBar extends StandardElement {

    constructor(title) {
        super("canvas");
        this.node.setAttribute("style",
            `
            background: transparent;
            `
        )
        this.context = this.node
            .getContext('2d');
        this.width_canvas = 0
        this.height_canvas = 0
        this.url_image = ""
        this.width_icon = 0
        this.height_icon = 0
    }

    __update() {
        this.context.clearRect(0, 0, 
            this.width_canvas, 
            this.height_canvas);
    }

    set_image(url_image, width, height) {
        this.url_image = url_image
        this.width_icon = width
        this.height_icon = height
        this.width_canvas = width 
        this.height_canvas = height
    }

    draw_icon(quantity) {
        this.node.width = this.width_icon * quantity 
        this.node.height = this.height_icon
        this.__update()
        let img = null
        img = new Image();
        img.onload = () => {
            let location_x = 0
            for(let i=0;i<quantity;i++) {
                this.context.drawImage(
                    img, 
                    location_x, 0);
                location_x += this.width_icon
            }
        };
        img.src = this.url_image
        
    }

}