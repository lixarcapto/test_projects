



import { StandardElement } from "./StandardElement.js"

export class ButtonList extends StandardElement {

    constructor(title, key_arr, 
            text_arr = "") {
        super();
        this.node = document.createElement(
            "div")
        this.node.style.display = "inline"
        this.node.setAttribute("tag", 
            "button_list")
        this.title = document
            .createElement("label")
        this.title.innerHTML = title
        this.node.append(this.title)
        this.list = document
            .createElement("ol")
        this.node.append(this.list)
        this.button_arr = []
        this.create_list(key_arr, text_arr)
    }

    destroy() {
        this.node.remove()
        this.node = null
        this.title = null
        this.list = null
        this.button_arr = []
    }

    create_list(key_arr, text_arr = "") {
        let li = null
        let button = null
        this.list.innerHTML = ""
        if(text_arr == "") {
            text_arr = key_arr
        }
        for(let i in text_arr) {
            button = document
                .createElement("button")
            button.innerHTML = text_arr[i]
            button.setAttribute("id", 
                key_arr[i])
            li = document.createElement("li")
            li.append(button)
            this.button_arr.push(button)
            this.list.append(li)
        }
    }

    /*
    La callback debe recibir como argumento
    el texto del boton.
    */
    add_listener(FUNCTION) {
        for(let i in this.button_arr) {
            let fn = ()=>{
                const key = this.button_arr[i]
                    .getAttribute("id")
                FUNCTION(key)
            }
            this.button_arr[i]
                .addEventListener(
                    "click", fn)
        }
    }

}