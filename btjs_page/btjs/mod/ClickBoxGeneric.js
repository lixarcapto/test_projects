
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
            this.class_button_key
                = this.get_element_key()
            //style
            this.style = new InnerStyle(
                this.class_button_key
            )
            this.style.set_margin("5px")
            document.body.append(
                this.style.node)
            //
            this.node.setAttribute(
                "tag", "panel_button")
            this.button_arr = []
            this.title = document.createElement(
                "label")
            this.title.innerHTML = title
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
            for(let i in this.button_arr) {
                img.src = data_arr[i]
                this.button_arr[i]
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
    
    
        create_list(key_arr) {
            let button = null
            for(let i in key_arr) {
                button = document.createElement(
                    "button")
                button.setAttribute("class",
                    this.class_button_key
                )
                button.setAttribute("id", 
                    key_arr[i])
                this.button_arr.push(button)
                this.grid.append(button)
            }
    }

}