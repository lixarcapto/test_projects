


import { StandardElement } from "./StandardElement.js"

export class InputSlider extends StandardElement {

    constructor(title, range_arr, value) {
        super();
        this.input_text = document.createElement(
            "div")
        this.input_text.style.display = "inline"
        this.input_text.setAttribute("tag",
            "input_slider")
        this.title = document.createElement(
            "label")
        this.title.innerHTML = title
        this.input = document.createElement(
            "input")
        this.input.setAttribute("type", 
            "range")
        this.result = document
            .createElement("label")
        this.input_text.append(this.title)
        this.input_text.append(this.input)
        this.input_text.append(this.result)
        this.__draw_text(range_arr)
        this.set_value(value)
        this.add_listener()
    }

    add_listener() {
        this.input.addEventListener(
            "change", 
            ()=>{
                this.update_text()
            }
        )
    }

    __draw_text(range_arr) {
        this.input.setAttribute("min", 
            range_arr[0])
        this.input.setAttribute("max", 
            range_arr[1])
    }

    set_value(value) {
        this.input.value = value
        this.update_text()
    }

    update_text() {
        this.result.innerHTML 
            = ` ${this.input.value} / 
            ${this.input.getAttribute("max")}`
        
    }

    get_value() {
        return this.input.value
    }

}