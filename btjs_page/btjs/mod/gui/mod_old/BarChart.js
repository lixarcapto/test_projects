

import { Canvas } from "./Canvas.js";
import { ChartLegends } from "./chart_legends/ChartLegends.js";
import { StandardElement } 
    from "./StandardElement.js";
import { Btjs } from "../../../Btjs.js";

export class BarChart extends StandardElement {

    constructor(title) {
        super("span")
        this.node.setAttribute("style",
            `
            display: inline-block;
            background-color: black;
            `
        )
        this.title = document
            .createElement("div")
        this.title.style.backgroundColor 
            = "white"
        this.title.style.border = "3px solid gray"
        this.set_title(title)
        this.node.append(this.title)
        this.bar_number = 0
        this.canvas = new Canvas(300, 300)
        this.node.append(this.canvas.node)
        this.lengends = new ChartLegends()
        this.node.append(this.lengends.node)
        this.size_x = 40
        //es el valor mas alto + 10
        this.max_value = 0
        this.space_between = Math.round(
            this.size_x / 2)
        this.last_location_x 
            = this.space_between
    }

    set_title(text) {
        this.title.innerHTML = text
    }

    find_max_in_map(jsobject_arr) {
        // Obtener todos los valores del Map
        let valores = []
        for(let i in jsobject_arr) {
            valores.push(
                jsobject_arr[i]["value"])
        }
        // Encontrar el valor máximo 
        // utilizando Math.max()
        const valorMaximo 
            = Math.max(...valores);
        console.log("valorMaximo", valorMaximo)
        return valorMaximo;
    }

    percent_reescaling(value,
            maximum_value,
            total_value) {
        // calcula el porcentaje del 
        // valor de la barra usando como
        // total el valor mas alto
        let percent = (value / maximum_value) 
            * 100
        // calcula la parte del canvas 
        // usando el porcentaje y el 
        // tamaño del canvas
        let result = (percent / 100) 
            * total_value
        return Math.round(result)
    }

    convert_to_percent(value) {
        return this.percent_reescaling(
            value,
            this.max_value,
            this.canvas.size_y
        )
    }

    create_text(text) {

    }

    draw_bar(jsobject) {
        let key = jsobject["key"]
        let size = jsobject["value"]
        let color = jsobject["color"]
        let percent = this
            .convert_to_percent(size)
        this.canvas.set_pen_color(color)
        let location_y = percent
        //dibuja la barra
        console.log("y", location_y)
        console.log("x", this.last_location_x)
        console.log("height", percent)
        console.log("with", this.size_x)
        this.canvas.draw_fill_rect_origen_2(
            [this.last_location_x, 0],
            [this.size_x, percent -5]
        )
        this.last_location_x 
            += this.size_x 
                + this.space_between;
        this.bar_number += 1
        this.lengends.add_leyend(key, color)
    }

    /*
    Recibe un array con los valores de cada
    barra en formato de js object.
    {
        "value": "",
        "color": "",
        "key": ""
    }
    */
    set_data_bars(jsobject_arr) {
        this.max_value = this
            .find_max_in_map(jsobject_arr)
        for (let i in jsobject_arr) {
            this.draw_bar(
                jsobject_arr[i]
            )
        }
    }

}