

import { Quote } from "./Quote.js"
import { Btjs } from "../Btjs.js"
import { convert_to_quote } from "./convert_to_quote.js"
import { References } from "./References.js"

export class Article {

    /* 
    TODO: 
    añadir las citas a este articulo.
    añadir un tipo de parrafo con las citas.
    
    {
        text : "",
        autor : "",
        title : "",
        date : "",
        url : "",
        recovery_date: ""
    }
    
    */

    constructor(title, text = "", level = 0) {
        this.node = document
            .createElement("div")
        this.node.setAttribute("tag", 
            "article")
        this.quote = new Quote()
        this.title = document
            .createElement("h3")
        this.section = document
            .createElement("section")
        this.section.setAttribute("style", 
            "text-indent: 2em;")
        this.set_title(title)
        this.node.append(this.title)
        this.node.append(this.section)
        this.config_title(level)
    }

    config_title(level) {
        if(level == 0) {
            this.title.setAttribute(
                "style",
                "text-align: center;"
            )
        } else if (level == 1) {

        } else if (level == 2) {
            this.title.setAttribute(
                "style",
                "font-style: italic;"
            )
        } else if (level == 3) {
            this.title.setAttribute(
                "style", 
                "text-indent: 1em;"
            )
        } else if (level == 4) {
            this.title.setAttribute(
                "style", 
                `text-indent: 1em;
                font-style: italic;`
            )
        }
    }

    /*
    Funcion que inserta el parrafo en 
    buffer actualmente. TODO: convertir
    esta funcion en una funcion que 
    convierta los saltos de linea dobles
    en parrafo con sangria y mayus inicial.
    */
    create_paragraph() {
        this.paragraph = document
            .createElement("p")
        this.paragraph.setAttribute("style", 
            "text-indent: 2em;")
    }

    /*
    Funcion que obtiene un string y 
    lo convierte en un texto con citaciones
    */
    set_text(str) {
        let new_string = convert_to_quote(
            str)
        this.section.innerHTML = new_string
        References.sum(str)
    }

    set_title(text) {
        let new_text = Btjs.capitalize(text)
        this.title.innerHTML = new_text
    }


}