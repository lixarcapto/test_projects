


export class Icon {

    /*
    Arreglar este porque no funciona.
    */

    constructor(url, height) {
        this.node = document.createElement(
            "button")
        this.img = document.createElement(
            "img")
        this.img.setAttribute("src", 
            url)
        this.node.append(this.img)
        this.set_height(height)
    }

    set_height(height) {
        this.img.setAttribute("height", height)
    }

    add_click_listener(FUNCTION) {
        this.node.addEventListener("click",
            FUNCTION)
    }

    add_mouseover_listener(FUNCTION) {
        this.node.addEventListener("mouseover",
            FUNCTION)
    }

    add_mouseout_listener(FUNCTION) {
        this.node.addEventListener("mouseout",
            FUNCTION)
    }

    add_click_listener(FUNCTION) {
        this.node.addEventListener("click",
            FUNCTION)
    }


}