


import { StandardElement } from "./StandardElement.js"

export class Card extends StandardElement {

    constructor(title, src, 
            description = "") {
        super();
        this.title_y_percent = 5
        this.img_y_percent = 65
        this.description_y_percent = 30
        this.node = document
            .createElement("span")
        this.node.setAttribute("tag", 
            "card")
        this.node.setAttribute("style",
            `
            display: flex;
            background-color: rgba(255, 255, 255, 1);
            background-color: #EBEBEB;
            border: 2px solid gray;
            flex-direction: column; /* Organiza los elementos en una columna */
            padding: 0px;
            `
        )
        this.title = document
            .createElement("span")
        this.title.setAttribute("style",
            `
            display: flex;
            justify-content: center;
            align-items: center;
            font-size: 20px;
            padding: 2px;
            font-weight: bold;
            border: 2px solid gray;
            font-family: Arial;
            `
        )
        this.set_title(title)
        this.img = document
            .createElement("img")
        this.img.setAttribute("style",
            `
            border: 2px solid gray;
            `
        )
        this.set_image(src)
        this.description = document
            .createElement("span")
        this.description.setAttribute("style",
            `
            padding: 2px;
            border: 2px solid gray;
            background-color: white;
            overflow: auto;
            `
        )
        this.set_description(description)
        this.node.append(this.title)
        this.node.append(this.img)
        this.node.append(this.description)
    }

    set_size(width, height) {
        let y_size_title = (
            this.title_y_percent / 100) 
            * height
        let y_size_desc = (
            this.description_y_percent / 100) 
            * height
        let y_size_image 
            = (this.img_y_percent / 100) 
            * height
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