


import { StandardElement } from "./StandardElement.js"

export class Gauge extends StandardElement {

    __ERROR_MARGIN_PERCENT = 20

    constructor(title = "") {
        super()
        this.node = document.createElement(
            "span")
        this.node.setAttribute("tag",
            "gauge"
        )
        this.node.setAttribute("style",
            `
            display: inline-block;
            `
        )
        this.circle = document.createElement(
            "div")
        this.circle.setAttribute("style",
            `
            position: relative;
            background-color:rgb(145, 139, 164);
            background-color: #2E2E2E;
            border-radius: 50% 50% 0 0; /* Redondea la parte superior */
            `
        )
        //
        this.pointer = document
            .createElement("div")
        this.pointer.setAttribute("style",
            `
            position: absolute;
            background-color: #ff0000;
            transform-origin: 100% 100%;
            `
        )
        this.number = document.createElement(
            "div")
        this.number.setAttribute("style",
            `
            background-color: rgba(255, 255, 255, 0); /* Fondo blanco con 50% de opacidad */
            background-color: #2E2E2E;
            display:flex;
            color: white;
            padding: 3px;
            justify-content:center;
            border: 1px solid gray;
            `
        )
        this.title = document.createElement(
            "label")
        this.title.setAttribute("style",
            `
            background-color: #2E2E2E;
            display:flex;
            justify-content: center;
            color: #ffffff;
            padding: 4px;
            `
        )
        this.title.innerHTML = "titulo"
        this.circle.append(this.pointer)
        this.node.append(this.circle)
        this.node.append(this.title)
        this.node.append(this.number)
        this.range_arr = [0, 0]
        this.set_size(100)
        this.set_pointer_width(4)
        this.set_title(title)
    }

    set_title(text) {
        this.title.innerHTML = text
    }

    set_range_text(range_arr) {
        this.number.innerHTML = `
            ${range_arr[0]} / ${range_arr[1]}
        `
    }

    set_pointer_width(size) {
        this.pointer.style
            .height = size +"px"
    }

    set_size_circle(width, height) {
        this.circle.style.height = height +"px"
        this.circle.style.width = width+"px"
    }

    //TODO: organizar estos calculos
    set_size(size) {
        let size_y = (size / 2)
        let size_x = size
        let pointer_height = size_x / 2
        //le resta un 5% de su tamaño
        //al puntero
        pointer_height 
            += -(5 / 100) * pointer_height
        //calcula un porcentaje del error
        //de margen en el eje X.
        let percent_error = Gauge
            .__ERROR_MARGIN_PERCENT
        let margin_error 
            = (percent_error/ 100) * size_x
        
        let pointer_x =  margin_error
        // eleva la aguja un 4% del tamaño
        // del contenedor en y
        let pointer_y = size_y 
            - ((4/100) * size_y)
        let circle_h = size_y
        let circle_w = size_x
        let pointer_heigth = size_y
        this.pointer.style
            .width = pointer_height +"px"
        //
        this.node.style.maxWidth = size_x + "px"
        this.set_size_circle(circle_w, circle_h)
        this.__set_pointer_location(
            pointer_x, pointer_y)
    }

    __set_pointer_location(x, y) {
        this.pointer.style.left = x +"px"
        this.pointer.style.top = y + "px"
    }

    set_range(range_arr) {
        this.range_arr = range_arr
        let degrees_total = 180
        let percent = 0
        percent = (range_arr[0] 
            / range_arr[1]) * 100
        let degree_parts
         = (percent / 100) * degrees_total
        if(degree_parts > 180
        || degree_parts < 0) { 
                return null
        }
        this.set_angle_degree(degree_parts)
        this.set_range_text(range_arr)
    }


    set_angle_degree(angulo) {
        this.pointer.style.transform 
            = `rotate(${angulo}deg)`;
    }

}