

import { Canvas } from "./Canvas.js";
import { ChartLegends } from "./chart_legends/ChartLegends.js";

export class BarChart {

    static color_arr = [
        "red",
        "orange",
        "yellow",
        "green",
        "blue",
        "violet",
        "pink",
        "brown",
        "gray",
        "black",
        "white",
        "silver"
    ];

    constructor(title) {
        this.node = document
            .createElement("span")
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

    find_max_in_map(map) {
        // Obtener todos los valores del Map
        const valores = Array.from(
            map.values());
        // Encontrar el valor máximo 
        // utilizando Math.max()
        const valorMaximo 
            = Math.max(...valores);
        return valorMaximo;
    }

    convert_to_percent(size) {
        let height_canvas = Number(
            this.canvas.node.height)
        // calcula el porcentaje del 
        // valor de la barra usando como
        // total el valor mas alto
        let percent = (size / 100) 
            * this.max_value
        // calcula la parte del canvas 
        // usando el porcentaje y el 
        // tamaño del canvas
        console.log("percent", percent)
        let result = (percent / 100) 
            * height_canvas
        console.log(result)
        return Math.round(result)
    }

    create_text(text) {

    }

    draw_bar(key, size) {
        let percent = this
            .convert_to_percent(size)
        //asigna un color
        let color = BarChart.color_arr[
            this.bar_number]
        this.canvas.set_pen_color(color)
        let location_y = this.canvas
            .node.height - percent
        //dibuja la barra
        this.canvas.draw_fill_rect(
            [this.last_location_x, location_y],
            [this.size_x, Number(percent)]
        )
        this.last_location_x 
            += this.size_x 
                + this.space_between;
        this.bar_number += 1
        this.lengends.add_leyend(key, color)
    }

    /*
    Recibe un array con los valores de cada
    barra en formato de dict.
    */
    set_data_bars(map) {
        this.max_value = this.find_max_in_map(
            map) - 10
        for (const [key, value] of map) {
            this.draw_bar(key, value)
        }
    }

}