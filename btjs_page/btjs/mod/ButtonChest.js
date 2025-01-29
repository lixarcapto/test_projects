

import { Selector } from "./Selector.js"
import { Button } from "./Button.js"
import { StandardElement } from "./StandardElement.js"

export class ButtonChest extends StandardElement {

    constructor(title) {
        super();
        this.input_text = document.createElement(
            "div")
        this.__node_key = this.create_
        this.input_text.setAttribute("tag", 
            "button_chest")
        this.__create_key()
        this.style = document.createElement(
            "style")
        this.button_class 
            = "button" + this.__node_key
        this.x_class 
            = "x" + this.__node_key
        this.style.innerHTML = `
            .${this.button_class } {
                background-color: #fff;
                color: #333;
                border: 2px solid gold;
                border-radius: 10px;
                padding: 9px;
                font-size: 16px;
                cursor: pointer;
                margin: 3px;
                display:inline-flex;
            }
            .${this.x_class } {
                border-radius: 50%;
                width: 18px;
                height: 18px;
                background-color: red;
                color: white;
                display: flex;
                justify-content: center;
                align-items: center;
                font-size: 16px;
                font-weight: bold;
            }
        `
        this.input_text.append(this.style)
        this.input_text.setAttribute("style",
            `
            border: 3px solid gray;
            padding: 7px;
            `
        )
        this.selector = new Selector(
            title, [])
        this.input_text.append(this.selector.node)
        this.chest = document.createElement(
            "div")
        this.chest.setAttribute("style",
            `
            `
        )
        this.button_dict = new Map()
        this.input_text.append(this.chest)
        this.selector.node.addEventListener(
            'change', () => {
                let v = this.selector
                    .get_value()
                this.__add_button(v)
            }
        );
    }

    set_title(text) {
        this.selector.set_title(text)
    }

    set_options_arr(array) {
        this.selector.create_list(array)
    }

    set_font_size(size) {
        this.input_text.style.fontSize = size +"px"
        this.selector.set_font_size(size)
        for (const [clave, valor] of this.button_dict) {
            this.button_dict[clave]
                .set_font_size(size)
        }
    }

    get_value() {
        let array = []
        for (const [clave, valor] of this.button_dict) {
            array.push(clave)
        }
        return array
    }

    has_key(text) {
        let array = this.get_value()
        for(let i=0;i<array.length;i++) {
            if(array[i] == text) {
                return true 
            }
        }
        return false
    }

    remove_button(text) {
        this.button_dict.get(text)
            .node.remove()
        this.button_dict.delete(text)
    }

    __create_red_x() {
        let element = document
            .createElement("label")
        element.innerHTML = "X"
        element.setAttribute("class",
            this.x_class
        )
        return element
    }

    __add_button(text) {
        if(this.has_key(text)) {
            return null
        }
        let button = this.create_button(text)
        button.node.append(
            this.__create_red_x())
        this.chest.append(button.node)
        button.node
            .addEventListener("click",
            ()=>{this.remove_button(text)}
            )
        this.button_dict.set(text, button)
    }

    create_button(text) {
        let button = new Button(text + "&nbsp")
        button.node.setAttribute("class", 
            this.button_class)
        return button
    }

}