


import { StandardElement } from "./StandardElement.js"

export class PanelButton extends StandardElement {

    /*
    Widget que contiene un panel de botones
    ordenados en cuadricula y que comparten
    una callback con diferentes indices
    segun el texto del boton.
    */

    static MAXIMUM_SIZE = 12

    constructor(title, key_arr, 
            text_arr = "") {
        super();
        this.node = document
            .createElement("div")
        this.node.style.display = "inline"
        this.node.setAttribute(
            "tag", "panel_button")
        this.button_arr = []
        this.node.setAttribute("style",
            `
            display: flex;
            flex-wrap: wrap;
            justify-content: center;
            gap: 2px; 
            /* Espacio entre los botones */
            `
        )
        this.title = document.createElement(
            "label")
        this.title.innerHTML = title
        this.node.append(this.title)
        this.create_list(key_arr, text_arr)
    }

    set_text_arr(text_arr) {
        for(let i in this.button_arr) {
            this.button_arr[i].innerHTML 
                = text_arr[i]
        }
    }

    /*
    La callback debe recibir como argumento
    el texto del boton.
    */
    add_listener(FUNCTION) {
        for(let i in this.button_arr) {
            let fn = ()=>{
                const key = this
                    .button_arr[i]
                    .getAttribute("id")
                FUNCTION(key)
            }
            this.button_arr[i]
                .addEventListener(
                    "click", fn)
        }
    }


    create_list(key_arr, text_arr = "") {
        let button = null
        if(text_arr == "") {
            text_arr = key_arr
        }
        for(let i in text_arr) {
            button = document.createElement(
                "button")
            button.setAttribute("id", 
                key_arr[i])
            button.setAttribute("style", 
                "font-size:1em;")
            this.button_arr.push(button)
            this.node.append(button)
        }
        this.set_text_arr(text_arr)
    }

}