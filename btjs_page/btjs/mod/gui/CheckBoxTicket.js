


import { StandardElement } from "./StandardElement.js"
import { CheckButton } from "./CheckButton.js";

export class CheckBoxTicket extends StandardElement {

    constructor(title, text_arr) {
        super();
        this.input_text = document
            .createElement("span")
        this.input_text.setAttribute("tag", 
            "checkbox")
        this.input_text.setAttribute("style",
            `
            margin: 3px;
            padding: 5px;
            display: grid-inline;
            gap: 0px; /* Espacio entre elementos */
            background-color: #EFEFEF;
            border: 1px solid gray;
            overflow: hidden;
            `
        )
        this.title = document
            .createElement("label")
        this.set_title(title)
        this.input_text.append(this.title)
        this.check_button_arr = []
        this.create_list(text_arr)
    }

    set_columns(number) {
        this.input_text.style
            .gridTemplateColumns = `
            repeat(${number}, minmax(100px, 1fr))
            `
    }

    set_title(text) {
        this.input_text.setAttribute("id", text)
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
        this.input_text.remove()
        this.input_text = null
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
            this.input_text.append(checkbox.input_text)
        }
    }

}