
import { StandardElement } from "./StandardElement.js"

export class Selector extends StandardElement {

    /*
    Modulo que permite crear una lista
    de opciones de forma facil.
    */

    constructor(text, array = []) {
        super("div");
        this.node.setAttribute("tag",
            "selector"
        )
        //this.node.style.display = "inline"
        this.label = document.createElement(
            "label")
        this.node.appendChild(
            this.label)
        this.select = document
            .createElement("select")
        this.node.appendChild(this.select)
        this.li_array = [] 
        this.create_list(array)
        this.set_title(text)
    }

    set_font_size(size) {
        this.label.style.fontSize = size +"px"
        this.select.style.fontSize = size +"px"
        for(let i=0; i< this.li_array.length;i++) {
            this.li_array[i].style.fontSize 
                = size + "px"
        }
        
    }

    get_value() {
        return this.select.value
    }

    set_title(text) {
        this.label.innerHTML 
            = text + "&nbsp:&nbsp"
    }

    create_list(ARRAY) {
        this.select.innerHTML = ""
        let option = null
        this.li_array = []
        for(let i=0;i < ARRAY.length;i++) {
            option = document.createElement(
                "option")
            option.innerHTML = ARRAY[i]
            this.li_array.push(option)
            this.select.append(option)
        }
    }

}