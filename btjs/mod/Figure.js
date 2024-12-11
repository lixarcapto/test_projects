


import { Quote } from "./Quote.js"

export class Figure {

    constructor(title, range_size, src, 
            description = "") {
        this.node = document
            .createElement("div")
        this.node.setAttribute("tag", 
            "figure")
        this.quote = new Quote()
        this.title = document
            .createElement("h3")
        this.set_title(title)
        this.img = document
            .createElement("img")
        this.set_size(range_size)
        this.set_url(src)
        this.p = document.createElement("p")
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

    set_description(text, dict_quote) {
        this.p.innerHTML = `
        ${text}. Available in `
        let src = this.img.getAttribute("src")
        let link = document
            .createElement("a")
        link.setAttribute("href", src)
        this.quote.set_data(dict_quote)
        let ref = this.quote.create_reference()
        this.p.innerHTML += ref.outerHTML
    }

}