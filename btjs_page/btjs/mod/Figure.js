


import { StandardElement } from "./StandardElement.js"

export class Figure extends StandardElement {

    constructor(title, src, 
            description = "") {
        super();
        this.node = document
            .createElement("div")
        this.node.style.display = "inline"
        this.node.setAttribute("tag", 
            "figure")
        this.title = document
            .createElement("h3")
        this.set_title(title)
        this.img = document
            .createElement("img")
        this.set_url(src)
        this.p = document.createElement("p")
        this.set_description(description)
        this.node.append(this.title)
        this.node.append(this.img)
        this.node.append(this.p)
    }

    set_size(range_size) {
        this.img.setAttribute("height", 
            range_size[0])
        this.img.setAttribute("width", 
            range_size[1])
    }

    set_title(title) {
        this.title.innerHTML = title
    }

    set_url(url) {
        this.img.setAttribute("src", url)
    }

    set_description(text) {
        this.p.innerHTML = text
    }

}