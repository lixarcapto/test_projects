


import { Btjs } from "../Btjs.js"
import { Quote } from "./Quote.js"

/*
Funcion que obtiene un string y 
lo convierte en un texto con citaciones
*/
export function convert_to_quote(str) {
    let init_idx = 0
    let end_idx = 0
    let quote = new Quote()
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
            quote.set_data(json)
            new_string += quote
                .create_quote()
            is_json = false
        } else {
            if(! is_json) {
                new_string += char
            }
        }
        idx ++
    }
    return new_string
}