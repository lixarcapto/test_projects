

export class Icon {

    /*
    Arreglar este porque no funciona.
    */

    constructor(url, width, height) {
        this.node = document.createElement(
            "button")
        this.img = document.createElement(
            "img")
        this.img.setAttribute("src", 
            url)
        this.node.append(this.img)
        this.set_size(width, height)
    }

    set_size(width, height) {
        this.img.setAttribute("width", width)
        this.img.setAttribute("height", height)
    }


}