
import { StandardElement } from "./StandardElement.js"
import { InnerStyle } from "./InnerStyle.js";
import { Btjs } from "../Btjs.js";

export class ClickBoxGeneric extends StandardElement {

    /*
        Widget que contiene un panel de botones
        ordenados en cuadricula y que comparten
        una callback con diferentes indices
        segun el texto del boton.

        Para utilizarlo debe enviarse 
        un array de IDs al constructor con
        el metodo set_id_array; que
        seran los IDs de cada boton; 
        y despues debe enviarse un array de 
        URLs o de textos al metodo
        set_content_array para pintar los 
        botones. Los botones se almacenan
        como diccionarios; por tanto no 
        permiten IDs repetidos.
        */
    
        constructor(key, key_arr) {
            super();
            //atributes
            this.node = null
            this.style = null
            this.title = null
            this.grid = null
            this.style_animation = null
            //calls
            this.dict_button = new Map()
            this.init_components(key)
            this.set_id_array(key_arr)
        }

        init_animation() {
            this.style_animation = Btjs
                .InnerStyle("active")
            this.style_animation.set_class(
                this.style.get_class()
            )
            this.style_animation
                .set_background("yellow")
            this.style_animation
                .set_transform("translateY(2px)")
            this.style_animation
                .set_box_shadow(
                    "0 2px 5px rgba(0, 0, 0, 0.2)")
            this.style_animation.to_document()
        }

        init_node() {
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
            this.node.setAttribute(
                "tag", "panel_button")
        }

        init_style() {
            this.style = new InnerStyle()
            this.style.set_margin("5px")
            this.style.set_font_size("16px")
            document.head.append(
                this.style.input_text)
        }

        init_grid() {
            //grid
            this.grid = document.createElement(
                "div")
            this.grid.setAttribute("style",
                `
                display: grid;
                `
            )
            this.node.append(this.grid)
        }

        init_title(title) {
            this.title = document.createElement(
                "label")
            this.set_text(title)
            this.title.style.fontSize = "16px"
            this.title.style.textAlign 
                = "center"
            this.node.append(this.title)
        }

        init_components(title) {
            this.init_node()
            this.init_style()
            this.init_title(title)
            this.init_grid()
            this.init_animation()
            this.set_id(title)
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
    
        set_content_array(data_arr) {
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
    
        set_text(text) {
            this.title.innerHTML = text 
                + "&nbsp:&nbsp"
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
    
        set_id_array(key_arr) {
            this.dict_button = new Map()
            for(let i in key_arr) {
                this.create_button(
                    key_arr[i])
            }
        }

}