
import { StandardElement } from "./StandardElement.js"
import { InnerStyle } from "./InnerStyle.js";

export class ClickBoxGeneric extends StandardElement {

    /*
        Widget que contiene un panel de botones
        ordenados en cuadricula y que comparten
        una callback con diferentes indices
        segun el texto del boton.
        */
    
        constructor(title, key_arr) {
            super();
            this.node = document
                .createElement("div")
            this.node.setAttribute("style",
                `
                display: flex;
                flex-direction: column;
                background-color: #EFEFEF;
                border: 1px solid gray;
                padding: 5px;
                `
            )
            //style
            this.style = new InnerStyle()
            this.style.set_margin("5px")
            this.style.set_font_size("16px")
            document.head.append(
                this.style.node)
            //
            this.node.setAttribute(
                "tag", "panel_button")
            this.button_arr = []
            this.dict_button = new Map()
            this.title = document.createElement(
                "label")
            this.title.innerHTML = title
            this.title.style.fontSize = "16px"
            this.title.style.textAlign 
                = "center"
            this.node.append(this.title)
            this.grid = document.createElement(
                "div")
            this.grid.setAttribute("style",
                `
                display: grid;
                `
            )
            this.node.append(this.grid)
            this.create_list(key_arr)
        }

        add_listener_to(key, callback) {
            let button = this.dict_button
                .get(key)
            button.addEventListener("click",
                callback)
            this.dict_button.set(key, button)
        }
    
        set_columns(number) {
            this.grid.style.gridTemplateColumns
                = `repeat(${number}, 1fr)`
        }
    
        set_data_arr(data_arr) {
            this.grid.style.gridTemplateColumns 
                = "repeat(auto-fit, minmax(100px, 1fr))"
            this.style.set_padding("0")
            this.style.set_height("auto")
            this.style.set_width("auto")
            this.style.set_object_fit("contain")
            let img = document.createElement(
                "img")
            for(const[k, v] of this.dict_button) {
                img.src = data_arr[i]
                this.dict_button.get(k)
                    .innerHTML =  img.outerHTML
            }
        }

        set_background(color) {
            this.node.style.backgroundColor 
                = color
            this.grid.style.backgroundColor 
                = color
            this.title.style.backgroundColor 
                = color
        }
    
    
        /*
        Añade un listener event al componente.
        La callback debe recibir como argumento
        el texto del boton.
        */
        add_listener_for_all(FUNCTION) {
            for(const[k, v] of this.dict_button) {
                let fn = ()=>{
                    const key = this
                        .dict_button.get(k)
                        .getAttribute("id")
                    FUNCTION(key)
                }
                this.dict_button.get(k)
                    .addEventListener(
                        "click", fn)
            }
        }

        create_button(text) {
            let button = document
                .createElement("button")
            button.setAttribute("class",
                this.style.get_class()
            )
            button.setAttribute("id", 
                text)
            this.dict_button.set(text, button)
            this.grid.append(button)
        }
    
        create_list(key_arr) {
            this.dict_button = new Map()
            for(let i in key_arr) {
                this.create_button(key_arr[i])
            }
        }

}