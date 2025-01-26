



import { StandardElement } from "./StandardElement.js"

export class ButtonIndex extends StandardElement {

    /*
    Para añadir el comportamiento
    se debe iniciar el metodo
    add_listeners
    */

    constructor(name, range_arr) {
        super();
        this.decrement = null
        this.increment = null
        this.input_text = document
            .createElement("div")
        this.input_text.style.display = "inline"
        this.input_text.setAttribute("tag", 
            "button_index")
        this.value = 0
        this.range_arr = range_arr
        this.label = document.createElement(
            "label")
        this.label.innerHTML = name
        this.input_text.append(this.label)
        this.__init_components()
    }

    destroy() {
        this.input_text.remove()
        this.range_arr = []
        this.label.remove()
        this.increment.remove()
        this.decrement.remove()
    }

    __init_components() {
        this.decrement = document
            .createElement("button")
        this.decrement.innerHTML = " < "
        this.increment = document
            .createElement("button")
        this.increment.innerHTML = " > "
        this.label = document
            .createElement("label")
        this.__update_value()
        this.input_text.append(this.decrement)
        this.input_text.append(this.label)
        this.input_text.append(this.increment)
    }

    __update_value() {
        this.label.innerHTML 
            = `  ${this.value}  `
    }

    get_value() {
        return this.value
    }


    add_listeners(callback = ()=>{}) {
        this.decrement.addEventListener(
            "click", ()=>{
            if(this.range_arr[0] 
                < this.value) {
                this.value -= 1
            }
            this.__update_value()
            callback()
        })
        this.increment.addEventListener(
            "click", ()=>{
            if(this.range_arr[1] 
                > this.value) {
                this.value += 1
            }
            this.__update_value()
            callback()
        })
    }

}