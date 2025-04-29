


import { StandardElement } from "./StandardElement.js"

export class InputSlider extends StandardElement {

    constructor(TITLE_STR, RANGE_LIST) {
        super();
        this.node = document.createElement(
            "div")
        this.node.style = `
            display: inline;
            padding: 5px;
            border: 1px solid gray;
            background:#F0F0F0;
            border-radius: 3px;
            margin: 2px;
        `
        this.node.setAttribute("tag",
            "input_slider")
        this.label_title = document
            .createElement("label")
        this.label_title.style
            .padding = "5px"
        this.label_title.innerHTML 
            = TITLE_STR
        this.input = document.createElement(
            "input")
        this.input.setAttribute("type", 
            "range")
        this.result = document
            .createElement("label")
        this.node.append(this.label_title)
        this.node.append(this.input)
        this.node.append(this.result)
        this.__draw_text(RANGE_LIST)
        this.__add_default_listener()
    }

    __add_default_listener() {
        this.input.addEventListener(
            "change", 
            ()=>{
                this.__update_text()
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
        this.__update_text()
    }

    __update_text() {
        this.result.innerHTML 
            = ` ${this.input.value} / 
            ${this.input.getAttribute("max")}`
        
    }

    get_value() {
        return this.input.value
    }

}