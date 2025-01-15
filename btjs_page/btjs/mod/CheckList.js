


import { StandardElement } from "./StandardElement.js"
import { CheckButton } from "./CheckButton.js";

export class CheckList extends StandardElement {

    constructor(title, text_arr) {
        super();
        this.node = document
            .createElement("div")
        this.node.style.display = "inline"
        this.node.setAttribute("tag", 
            "checkbox")
        this.title = document
            .createElement("label")
        this.set_title(title)
        this.node.append(this.title)
        this.check_button_arr = []
        this.create_list(text_arr)
    }

    set_title(text) {
        this.node.setAttribute("id", text)
        this.title.innerHTML = text + ":&nbsp&nbsp"
    }

    set_font_size(size) {
        super.set_font_size(size)
        for(let i in this.check_button_arr) {
            this.check_button_arr[i]
                .set_font_size(size)
        }
    }

    destroy() {
        this.node.remove()
        this.node = null
        this.title = null
        this.check_button_arr = []
    }

    /*
    Retorna los textos de los 
    checkbox marcados.
    */
    get_value() {
        let text_arr = []
        let e = null
        for(let i in this.check_button_arr) {
            e = this.check_button_arr[i]
            if(e.get_value() == true) { 
                text_arr.push(
                    this.check_button_arr[i]
                        .get_title()
                )
            }
        }
        return text_arr
    }

    create_list(text_arr) {
        this.check_button_arr = []
        let checkbox = null
        for(let i in text_arr) {
            checkbox = new CheckButton(
                text_arr[i], "checkbox")
            this.check_button_arr.push(checkbox)
            this.node.append(checkbox.node)
        }
    }

}