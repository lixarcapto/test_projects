


import { StandardButton } 
    from "./StandardButton.js";

export class IconButton extends StandardButton {

    constructor(image_url, text) {
        super();
        this.node = document
            .createElement("button")
        this.div = document
            .createElement("div")
        this.node.setAttribute("style",
            `
            border: none;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            `
        )
        this.image = document
            .createElement("img")
        this.node.append(this.image)
        this.node.append(this.div)
        this.set_image(image_url)
        this.set_range_text(text)
    }

    set_image(url) {
        this.image.setAttribute("src", url)
    }

    set_range_text(text) {
        this.div.innerHTML = text
        this.image.setAttribute("alt", text)
    }

}