

import { StandardElement } from "./StandardElement.js"

export class Link extends StandardElement {

    constructor(text, url) {
        super();
        this.node = document
            .createElement("a")
        this.node.innerHTML = text
        this.set_url(url)
    }

    set_url(URL) {
        this.node.setAttribute("href", URL)
    }

    get_ulr() {
        return this.node.getAttribute("href")
    }

}