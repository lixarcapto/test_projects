


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
        this.node.setAttribute(
            "tag", "panel_button")
        this.node.style
            .border = "2px solid gray"
        this.node.style.padding = "3px"
        this.button_arr = []
        this.title = document.createElement(
            "label")
        this.title.innerHTML = title
        this.node.append(this.title)
        this.node.append(
            document.createElement("br"))
        this.grid = document.createElement(
            "div")
        this.grid.setAttribute("style",
            `
            display: grid;
            grid-template-columns: repeat(2, 2fr); /* Crea una cuadrícula de 2 columnas de igual tamaño */
            grid-gap: 1px; /* Espacio entre elementos */
            `
        )
        this.node.append(this.grid)
        this.create_list(key_arr, text_arr)
    }

    set_columns(number) {
        this.grid.style.gridTemplateColumns
            = `repeat(${number}, 1fr)`
    }

    set_rows(number) {
        this.grid.style.gridTemplateRows
            = `repeat(${number}, 1fr)`
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
            button.style.border 
                = "2px solid gray"
            this.button_arr.push(button)
            this.grid.append(button)
        }
        this.set_text_arr(text_arr)
    }

}