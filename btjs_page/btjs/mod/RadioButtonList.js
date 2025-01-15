


import { Btjs } from "../Btjs.js";
import { StandardElement } from "./StandardElement.js"
import { CheckButton } from "./CheckButton.js";

export class RadioButtonList extends StandardElement {

    static last_id = 0

    constructor(title, key_arr, 
            text_arr = "") {
        super();
        this.node = document
            .createElement("div")
        this.node.style.display = "inline"
        this.radio_arr = []
        this.title = document
            .createElement("label")
        this.set_title(title)
        this.node.append(this.title)
        this.unique_id = String(
            RadioButtonList.last_id)
        RadioButtonList.last_id += 1
        this.node.setAttribute("tag", 
            "radio_button_list")
        this.create_list(key_arr, text_arr)
    }

    set_title(text) {
        this.node.setAttribute("id", text)
        this.title.innerHTML = text + ":&nbsp&nbsp"
    }

    set_font_size(size) {
        super.set_font_size(size)
        for(let i in this.radio_arr) {
            this.radio_arr[i]
                .set_font_size(size)
        }
    }

    get_value() {
        for(let i in this.radio_arr) {
            if(this.radio_arr[i].get_value()) {
                return this.radio_arr[i]
                .get_id()
            }
        }
        return "none"
    }

    create_list(key_arr, text_arr = "") {
        if(text_arr == "") {
            text_arr = key_arr
        }
        let radio = null
        let label = null
        for(let i in text_arr) {
            radio = new CheckButton(
                text_arr[i], "radio")
            radio.checkbox.setAttribute(
                "name", this.unique_id)
            radio.set_title(text_arr[i])
            this.node.append(radio.node)
            this.radio_arr.push(radio)
        }
    }

}