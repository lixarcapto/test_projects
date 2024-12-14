



export class Image {

    constructor() {
        this.node = document
            .createElement("img")
    }

    set_size(width, height) {
        this.node.setAttribute("width", url)
        this.node.setAttribute("height", url)
    }

    set_url(url) {
        this.node.setAttribute("href", url)
    }

    get_url() {
        return this.node.getAttribute("href")
    }

}