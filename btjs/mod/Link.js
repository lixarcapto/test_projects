


export class Link {

    constructor(text, url) {
        this.node = document
            .createElement("a")
        this.node.innerHTML = text
        this.node.setAttribute("href", url)
    }

    set_url(URL) {
        this.node.setAttribute("href", URL)
    }

    get_ulr() {
        return this.node.getAttribute("href")
    }

}