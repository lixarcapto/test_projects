

import { Quote } from "./Quote.js";
import { Btjs } from "../../../Btjs.js";
import { StandardElement } from "./StandardElement.js"

export class VideoFigure extends StandardElement {

    constructor() {
        super();
        this.input_text = document
            .createElement("div")
        this.input_text.style.display = "inline"
        this.title = document
            .createElement("h3")
        this.section = document
            .createElement("section")
        this.input_text.append(this.title)
        this.section_iframe = document
            .createElement("section")
        this.description = document
            .createElement("section")
        this.input_text.append(this.title)
        this.input_text.append(this.section_iframe)
        this.input_text.append(this.description)
        this.quote = new Quote()
        /*

        <iframe width="560" 
        height="315" 
        src="https://www.youtube.com/embed/sVdP70QlHMs?si=woeu3UXu_HmT2I_5" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen>
        </iframe>
        
        */
    }

    set_title(text) {
        this.title.innerHTML = text
    }

    set_iframe_youtube(HTML_text) {
        this.section_iframe.innerHTML 
            = HTML_text
    }

    /*
    Funcion que obtiene un string y 
    lo convierte en un texto con citaciones
    */
    set_description(str) {
        let init_idx = 0
        let end_idx = 0
        let idx = 0
        let substring = ""
        let new_string = ""
        let char = ""
        let is_json = false
        for (let i=0;i<str.length;i++) {
            char = str[i]
            if(char == "{") {
                is_json = true
                init_idx = idx
            } else if(char == "}") {
                end_idx = idx
                substring = str.slice(
                    init_idx, end_idx)
                substring += "}"
                substring = Btjs.replace_string(
                    substring, "\n")
                let json = JSON.parse(
                    substring);
                this.quote.set_data(json)
                new_string += this.quote
                    .create_quote()
                is_json = false
            } else {
                if(! is_json) {
                    new_string += char
                }
            }
            idx ++
        }
        this.description.innerHTML 
            = new_string
    }

}