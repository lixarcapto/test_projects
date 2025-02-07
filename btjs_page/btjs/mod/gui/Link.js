

import { StandardElement } from "./StandardElement.js"

export class Link extends StandardElement {

    constructor(text, url) {
        super();
        this.input_text = document
            .createElement("a")
        this.input_text.innerHTML = text
        this.set_url(url)
    }

    set_url(URL) {
        this.input_text.setAttribute("href", URL)
    }

    get_ulr() {
        return this.input_text.getAttribute("href")
    }

}