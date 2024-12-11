

import { Btjs } from "../Btjs.js"

export class PageTitle {

    constructor(title, subtitle) {
        this.node = document.createElement(
            "div")
        this.title = document.createElement(
            "h1")
        this.title.setAttribute("style",
            "text-align: center;")
        this.subtitle = document.createElement(
            "h3")
        this.subtitle.setAttribute("style",
            "text-align: center;")
        this.set_titles(title, subtitle)
        this.node.append(this.title)
        this.node.append(this.subtitle)
    }

    set_titles(title, subtitle) {
        title = Btjs.capitalize(title)
        this.title.innerHTML = title
        document.title = title
        subtitle = Btjs.capitalize(subtitle)
        this.subtitle.innerHTML = subtitle
    }

}