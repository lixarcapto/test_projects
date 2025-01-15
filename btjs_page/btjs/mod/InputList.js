

import { StandardElement } from "./StandardElement.js"

export class InputList extends StandardElement {

    /*
    Esta clave se usa para almacenar
    datos en el ID evitando conflictos
    de nombres con otros ID
    */
    static UNIQUE_KEY = "ax6d6%"

    constructor(text_arr) {
        super();
        this.node = document
            .createElement("div")
        this.node.style.display = "inline"
        this.node.setAttribute("tag", 
            "input_list")
        this.label_arr = []
        this.input_arr = []
        this.create_list(text_arr)
    }

    get_data_json() {
        let json = {}
        let k = ""
        let v = ""
        for(let i in this.label_arr) {
            k = this.input_arr[i]
                .getAttribute("id")
            k = k.replace(
                InputList.UNIQUE_KEY, "")
            v = this.input_arr[i].value
            json[k] = v
        }
        return json
    }

    extract_data_json() {
        let json = {}
        let k = ""
        let v = ""
        for(let i in this.label_arr) {
            k = this.input_arr[i]
                .getAttribute("id")
            k = k.replace(
                InputList.UNIQUE_KEY, "")
            v = this.input_arr[i].value
            this.input_arr[i].value = ""
            json[k] = v
        }
        return json
    }

    create_list(text_arr) {
        let label = null
        let input = null
        this.label_arr = []
        this.input_arr = []
        for(let i in text_arr) {
            label = document
                .createElement("label")
            label.innerHTML 
                = "   " + text_arr[i] + "   "
            this.node.append(label)
            this.label_arr.push(label)
            input = document
                .createElement("input")
            input.setAttribute(
                "type", "text")
            input.setAttribute(
                "id", 
                InputList.UNIQUE_KEY + text_arr[i]
            )
            this.input_arr.push(input)
            this.node.append(input)
        }
        
    }

}