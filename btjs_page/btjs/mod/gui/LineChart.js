


import { StandardElement } 
    from "./StandardElement.js";
import { Canvas } from "./Canvas.js";
import { ChartLegends } 
    from "./chart_legends/ChartLegends.js";

export class LineChart
        extends StandardElement {

    /*
    Recibe un objeto que representa a los 
    datos de una linea para el grafico; este
    objeto tiene como atributo "line" que es
    un poligono de lineas; un atributo 
    name con el nombre y un atributo color
    con el color de la linea.
    Formato de line chart:
    {
            "line": [[0,0], [0,0], [0,0]],
            "name": "",
            "color": "blue"
    }
    este formato puede enviarse como 
    un array.
    */

    constructor(width, height) {
        super("span");
        this.canvas = new Canvas(
            width, height)
        this.node.style.display = "inline"
        this.node.append(this.canvas.node)
        this.canvas.set_pen_color("red")
        this.canvas.set_pen_width(2)
        this.legend = null;
        this.__init_chart_legends()
    }

    __init_chart_legends() {
        this.legend = new ChartLegends()
        this.node.append(this.legend.node)
    }

    get_height() {
        return this.canvas.size_y
    }

    get_width() {
        return this.canvas.size_x
    }

    draw_graphic_line(point_origen, 
            point_destiny) {
        let new_p_origen = [
            point_origen["time"],
                this.canvas.size_y 
            - point_origen["value"]
        ]
        let new_p_destiny = [
            point_destiny["time"],
                this.canvas.size_y 
                - 
            point_destiny["value"]
        ]
        this.canvas.draw_line(
            new_p_origen,
            new_p_destiny
        )
    }

    convert_line_to_polygon(line) {
        let line_matrix = []
        line_matrix.push([
            0,
            this.canvas.size_y
        ])
        for(let i in line) {
            line_matrix.push([
                line[i][0],
                this.canvas.size_y 
                - line[i][1]
            ])
        }
        return line_matrix
    }

    update() {
        this.canvas.update()
        this.canvas.reference_line_color 
            = "gray"
        this.canvas.draw_vertical_grid(
           5,
           Math.round(
            this.canvas.size_x / 5)
        )
    }

    set_background_color(color) {
        this.canvas.set_background_color(
            color)
    }


    draw_object_line(objs_line) {
        let polygon = this
            .convert_line_to_polygon(
                objs_line["line"])
        this.canvas.set_pen_color(
            objs_line["color"])
        this.legend.add_leyend(
            objs_line["name"],
            objs_line["color"]
        )
        this.canvas.draw_poligon_point(
            polygon)
    }

    draw_object_line_array(object_js_arr) {
        let objs = {}
        let time = 0
        let value = 0
        let line = []
        let point_destiny = [0, 0]
        let point_origen = {
            "time": 0,
            "value": 0
        }
        let polygon = [[0, 0], [0, 0]]
        for(let i in object_js_arr) {
            objs = object_js_arr[i]
            this.draw_object_line(objs)
        }
    }

}