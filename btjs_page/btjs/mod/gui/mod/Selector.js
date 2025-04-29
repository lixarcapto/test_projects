
import { StandardElement } from "./StandardElement.js"

export class Selector extends StandardElement {

    /*
    Modulo que permite crear una lista
    de opciones de forma facil.
    */

    constructor(TITLE_STR, 
            CONTENT_LIST_STR = []) {
        super("span");
        this.node.style = `

            padding: 5px;
            border: 1px solid gray;
            background:#F0F0F0;
            border-radius: 3px;
            margin: 2px;
        `
        this.node.setAttribute("tag",
            "selector"
        )
        //this.node.style.display = "inline"
        this.label = document.createElement(
            "label")
        this.label.style = `
            padding: 4px;
        `
        this.node.appendChild(
            this.label)
        this.select = document
            .createElement("select")
        this.node.appendChild(this.select)
        this.content_list_str = []
        this.element_list = [] 
        if(CONTENT_LIST_STR != []) {
            this.set_content(
                CONTENT_LIST_STR)
        }
        this.set_title(TITLE_STR)
    }

    set_font_size(size) {
        this.label.style.fontSize = size +"px"
        this.select.style.fontSize = size +"px"
        for(let i=0; i< this.element_list.length;i++) {
            this.element_list[i].style.fontSize 
                = size + "px"
        }
        
    }

    set_value(INDEX_INT) {
        let text = this.content_list_str
            [INDEX_INT]
        this.select.value = text
    }

    get_value() {
        return this.content_list_str
            .indexOf(this.select.value)
    }

    set_title(text) {
        this.label.innerHTML 
            = text
    }

    add_on_change_listener(CALLBACK) {
        this.node.addEventListener(
            'change',
            CALLBACK
        )
    }

    set_content(CONTENT_LIST_STR) {
        this.select.innerHTML = ""
        let option = null
        this.content_list_str 
            = CONTENT_LIST_STR
        this.element_list = []
        let leng = CONTENT_LIST_STR.length
        for(let i=0;i < leng;i++) {
            option = document.createElement(
                "option")
            option.innerHTML 
                = CONTENT_LIST_STR[i]
            this.element_list.push(option)
            this.select.append(option)
        }
    }

}