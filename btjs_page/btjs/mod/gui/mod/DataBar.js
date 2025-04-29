


import { Btjs } from "../../../Btjs.js";
import {LimitNumber} from 
    "../../util/mod/LimitNumber.js";
import { StandardElement } from "./StandardElement.js"

export class DataBar extends StandardElement {

    /*
    Este es un componente que facilita 
    trabajar con las barras de datos 
    añadiendo títulos e información extra.
    */

    constructor(title, range_arr =[0, 100]) {
        super("span");
        this.__label_value = null
        this.__label_range = null
        this.__bar_class = ""
        this.__title = null
        this.__bar = null
        this.__style_bar = null
        this.__limit_n = Btjs.LimitNumber(
            range_arr
        )
        //
        this.__init_components()
        this.set_text(title)
        this.set_size(27, 300)
        this.set_color_bar("#008f39", "#e5be01", "white")
    }

    __init_components() {
        this.__init_node()
        this.__init_bar_style()
        this.__init_title()
        this.__init_label_value()
        this.__init_bar()
        this.__init_label_range()
    }

    set_border_color(color) {
        this.__bar.style.borderColor = color
    }

    __init_label_range() {
        this.__label_range = document
            .createElement("span")
        this.__label_range.style = 
            `
            display: flex;
            justify-content: center;
            align-content: center;
            padding: 3px;
            `
        this.node.append(this.__label_range)
    }

    __init_label_value() {
        this.__label_value = document
            .createElement("span")
        this.__label_value.style = 
            `
            display: flex;
            justify-content: center;
            align-content: center;
            padding: 3px;
            `
        this.node.append(this.__label_value)
    }

    __init_title() {
        this.__title = document.createElement(
            "label")
        this.node.append(this.__title)
    }

    set_size(height, width) {  
        this.__bar.style.width = width + "px"
        this.__bar.style.height = height 
            + "px"
    }

    __init_bar() {
        this.__bar = document.createElement(
            "progress")
        this.__bar.style.display 
            = "inline-block";
        this.__bar.style.color
             = "#FFFFFF";
        this.__bar.style.border
             = "4px solid #808080";
        this.__bar.value = 0
        this.__bar.setAttribute("class",
            this.class_bar
        )
        this.node.append(this.__bar)
    }

    __init_node() {
        this.node.setAttribute("tag",
            "progress_bar")
        this.node.setAttribute("style",
            `
            display: flex;
            border: 1px solid gray;
            overflow: hidden;
            justify-content: left;
            align-items: center;
            max-width: fit-content;
            background-color: #EFEFEF;
            `
        )
    }

    __init_bar_style() {
        this.__style_bar = document
            .createElement("style")
        this.class_bar = this.get_class()
             + "_bar"
        this.__style_bar.setAttribute("class", 
            this.class_bar
        )
        document.head.append(this.__style_bar)
    }

    set_color_bar(part_color, total_color,
            border_color) {
        this.__style_bar.innerHTML = `
        .${this.class_bar}::-webkit-progress-bar {
            background-color:${total_color};
        }
        .${this.class_bar}::-webkit-progress-value {
            background-color:${part_color};
        }
        `
        this.set_border_color(border_color)
    }

    set_text(text) {
        this.__title.innerHTML 
            =  text + "&nbsp:&nbsp" 
    }

    set_range_arr(range_arr) {
        this.__limit_n.set_range_arr(
            range_arr)
        let range = this.__limit_n
            .get_range_arr()
        this.__bar.setAttribute("min", 
            range[0])
        this.__bar.setAttribute("max", 
            range[1])
    }


    /*
    Ajusta el valor de la barra al rango
    almacenado.
    */
    set_value(value) {
        this.__limit_n.set(value)
        this.__update_value()
    }


    __update_value() {
        this.__bar.value = this.__limit_n.get()
        let range = this.__limit_n
            .get_range_arr()
        this.__label_value.innerHTML
            = this.__limit_n.get()
        this.__label_range.innerHTML
            = `${range[0]} / ${range[1]}`
    }

    get_value() {
        return this.__limit_n.get()
    }

}