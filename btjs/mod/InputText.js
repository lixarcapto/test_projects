



export class InputText {

    constructor() {
        this.node = document
            .createElement("textarea")
    }

    set_size(rows, cols) {
        this.node.setAttribute("rows", rows)
        this.node.setAttribute("cols", cols)
    }

    get_text() {
        return this.node.getAttribute("value")
    }

    set_text(text) {
        this.node.setAttribute("value", text)
    }


}