

import { StandardElement } from "./StandardElement.js"

export class Link extends StandardElement {

    constructor(TITLE_STR, URL_STR) {
        super("a");
        this.node = document
            .createElement("a")
        this.node.innerHTML = TITLE_STR
        this.set_url(URL_STR)
    }

    set_url(URL) {
        this.node.setAttribute(
            "href", URL)
    }

    get_ulr() {
        return this.node
            .getAttribute("href")
    }

}