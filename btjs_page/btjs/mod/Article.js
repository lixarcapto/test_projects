

import { Quote } from "./Quote.js";
import { Btjs } from "../Btjs.js";
import { convert_to_quote } from "./convert_to_quote.js";
import { References } from "./References.js";
import { StandardElement } from "./StandardElement.js";

export class Article extends StandardElement {

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
        super()
        this.node = document
            .createElement("section")
        this.node.setAttribute("tag", 
            "article")
        this.node.style.display = "inline"
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
        this.__draw_text(text)
    }

    destroy() {
        this.node.remove()
        this.node = null
        this.quote = null
        this.title = null
        this.section = null
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
    Funcion que obtiene un string y 
    lo convierte en un texto con citaciones
    */
    __draw_text(str) {
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