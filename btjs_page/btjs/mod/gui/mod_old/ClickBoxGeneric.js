
import { StandardElement } from "./StandardElement.js"
import { InnerStyle } from "./InnerStyle.js";
import { Btjs } from "../../../Btjs.js";

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
            super("span");
            //atributes
            this.style = null
            this.title = null
            this.grid = null
            //asigna una clase a los iconos
            this.class_icon = "icon_" + this
                .get_class()
            this.style_animation = null
            //calls
            this.dict_button = new Map()
            this.init_components(key)
            this.create_buttons(key_arr)
        }

        /*
        Crea la animacion principal
        de los iconos con el widget
        innerStyle usando pseudoclases.
        */
        init_animation() {
            this.style_animation = Btjs
                .InnerStyle(
                    this.class_icon, 
                    "active"
                )
            this.style_animation
                .set_background_color("yellow")
            this.style_animation
                .set_transform("translateY(2px)")
            this.style_animation
                .set_box_shadow(
                    "0 2px 5px rgba(0, 0, 0, 0.2)")
            this.style_animation.to_document()
        }

        /*
        Inicializa el componente principal
        contenedor.
        */
        init_node() {
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
            this.style = new InnerStyle(
                this.get_class())
            this.style.set_margin("5px")
            this.style.set_font_size("16px")
            this.style.set_transition(
                "background-color 0.2s ease")
            this.style.to_document()
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

        /*
        Agrega el background a todos los
        elementos internos.
        */
        set_background_color(color) {
            this.node.style.backgroundColor 
                = color
            this.grid.style.backgroundColor 
                = color
            this.title.style.backgroundColor 
                = color
        }
    
        /*
        Define el texto del titulo.
        */
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

        /*
        Crea un boton independiente
        pre-configurado y lo incluye en
        el array de botones.
        */
        create_button(text) {
            let button = document
                .createElement("button")
            button.setAttribute("class",
                this.class_icon
            )
            button.setAttribute("id", 
                text)
            this.dict_button.set(text, button)
            this.grid.append(button)
        }
    
        /*
        Crea una lista de botones por
        cada clave enviada en un string
        array.
        */
        create_buttons(key_arr) {
            this.dict_button = new Map()
            for(let i in key_arr) {
                this.create_button(
                    key_arr[i])
            }
        }

}