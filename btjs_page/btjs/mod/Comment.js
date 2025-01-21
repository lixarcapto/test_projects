

import { StandardElement } from "./StandardElement.js"

export class Comment extends StandardElement {

    /*
    Comment json structure:
    {
        "autor":"",
        "text":"",
        "image_url":""
    }
    */

    constructor(json) {
        super();
        this.node = document
            .createElement("div")
        this.node.style.display = "inline"
        this.node.setAttribute(
            "tag", "comment")
        this.node.setAttribute(
            "style", `
            background-color: #f2f2f2; /* Color de fondo gris claro */
            border: 1px solid #ddd; /* Borde gris */
            padding: 6px;
            margin-bottom: 20px;
            border-radius: 5px;
        `)
        this.image = document
            .createElement("img")
        this.title = document
            .createElement("h4")
        this.title.setAttribute("style",
            "line-height: 0.6;")
        this.text = document
            .createElement("p")
        this.text.setAttribute("style",
            "line-height: 0.6;")
        this.image.setAttribute("style",
            "float: left;")
        this.set_json_comment(json)
        this.node.append(this.image)
        this.node.append(this.title)
        this.node.append(this.text)
    }

    destroy() {
        this.node.remove()
        this.node = null
        this.title = null
        this.image = null
        this.text = null
    }

    set_json_comment(json) {
        this.set_autor(json["autor"])
        this.__draw_text(json["text"])
        this.set_image(json["image_url"])
    }

    set_image(url) {
        this.image.setAttribute("src", url)
    }

    set_autor(autor) {
        this.title.innerHTML = autor
    }

    __draw_text(text) {
        this.text.innerHTML = text
    }

}