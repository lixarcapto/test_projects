


export class StandardElement {

    constructor() {
        this.node = document.createElement(
            "button")
    }

    destroy() {}

    get_value() {
        return this.node.value
    }

    set_value(value) {
        this.node.value = value
    }

    get_text() {
        return this.node.innerHTML
    }

    set_text(text) {
        this.node.innerHTML = text
    }

}