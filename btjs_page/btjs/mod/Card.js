


import { StandardElement } from "./StandardElement.js"

export class Card extends StandardElement {

    constructor(title, src, 
            description = "") {
        super();
        this.node = document
            .createElement("span")
        this.node.setAttribute("tag", 
            "card")
        this.node.setAttribute("style",
            `
            display: flex;
            background-color: rgba(255, 255, 255, 1);
            background-color: #EBEBEB;
            flex-direction: column; /* Organiza los elementos en una columna */
            `
        )
        this.title = document
            .createElement("h3")
        this.set_title(title)
        this.img = document
            .createElement("img")
        this.set_image(src)
        this.description = document.createElement("span")
        this.set_description(description)
        this.node.append(this.title)
        this.node.append(this.img)
        this.node.append(this.description)
    }

    set_size(width, height) {
        let y_size_title = (5 / 100) * height
        let y_size_desc = (20 / 100) * height
        let y_size_image 
            = ((- 25 + 100) / 100) * height
        this.node.style.height = height +"px"
        this.node.style.width = width +"px"
        this.set_title_size(width,
            y_size_title
        )
        this.set_image_size(width, 
            y_size_image)
        this.set_description_size(width,
            y_size_desc
        )
    }

    set_description_size(width, height) {
        this.description.style
            .height = height + "px"
        this.description.style
            .width = width + "px"
    }

    set_image_size(width, height) {
        this.img.style.height = height +"px"
        this.img.style.width = width +"px"
    }

    set_title_size(width, height) {
        this.title.style.height = height +"px"
        this.title.style.width = width +"px"
    }

    set_title(title) {
        this.title.innerHTML = title
    }

    set_image(url) {
        this.img.setAttribute("src", url)
    }

    set_description(text) {
        this.description.innerHTML = text
    }

}