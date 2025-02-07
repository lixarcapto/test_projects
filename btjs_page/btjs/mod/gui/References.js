


import { Quote } from "./Quote.js";
import { Btjs } from "../../Btjs.js";

export class References {

    /*
    Clase que representa una seccion de 
    referencias biblograficas.
    */

    node = null
    title = null
    ol = null
    quote = null

    static {
        References.node = document
            .createElement("section")
        References.title = document
            .createElement("h4")
        References.ol = document
            .createElement("ol")
        References.quote = new Quote()
        References.title.innerHTML 
            = "References"
        References.node.setAttribute("tag", 
            "references")
        References.node.append(
            References.title)
        References.node.append(
            References.ol)
    }

    /*
    Esta funcion recibe un texto con 
    citas en formato diccionario y escribe
    sus referencias como una lista OL HTML
    */
    static sum(text) {
        //obtiene los quotes dict
        let json_arr = this
            .get_quotes_dict(text)
        let quote_str = null
        let final_str = ""
        for(let i=0; i< json_arr.length;i++) {
            References.quote.set_data(json_arr[i])
            quote_str = References.quote
                .create_reference()
            References.ol.append(quote_str)
        }
    }

    /*
    Funcion que obtiene diccionarios a 
    partir de JSON string de quotes en 
    el texto enviado. Como el siguiente:
    {
        text : "",
        autor : "",
        title : "",
        date : "",
        url : "",
        recovery_date: ""
    }
    */
    static get_quotes_dict(str) {
        let init_idx = 0;
        let end_idx = 0;
        let idx = 0;
        let substring = "";
        let new_string = "";
        let char = "";
        let is_json = false;
        let json_arr = [];
        for (let i=0;i<str.length;i++) {
            char = str[i];
            if(char == "{") {
                is_json = true;
                init_idx = idx;
            } else if(char == "}") {
                end_idx = idx;
                substring = str.slice(
                    init_idx, end_idx);
                substring += "}";
                substring = Btjs
                    .replace_string(
                        substring, "\n");
                let json = JSON.parse(
                    substring);
                console.log(json)
                json_arr.push(json);
                is_json = false;
            } else {
                if(! is_json) {
                    new_string += char
                }
            }
            idx ++
        }
        return json_arr
    }

}