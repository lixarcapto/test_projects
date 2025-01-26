


import { StandardElement } from "./StandardElement.js"

export class Gauge extends StandardElement {

    /*
    Es un componente que representar
    un medidor de aguja similar a los
    del panel de un automobil.
    */

    __ERROR_MARGIN_PERCENT = 20

    constructor(title = "") {
        super()
        this.input_text = null
        this.circle = null
        this.number = null
        this.title = null
        this.number = null
        this.range_arr = [0, 0]
        this.pointer_value = 0
        //
        this.init_components()
        this.set_size_card(100)
        this.set_pointer_width(4)
        this.set_title(title)
    }

    init_components() {
        this.init_node()
        this.init_circle()
        this.init_pointer()
        this.init_number()
        this.init_title()
    }

    init_node() {
        this.input_text = document.createElement(
            "span")
        this.input_text.setAttribute("tag",
            "gauge"
        )
        this.input_text.setAttribute("style",
            `
            display: inline-block;
            `
        )
    }

    init_circle() {
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
        this.input_text.append(this.circle)
    }

    init_title() {
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
        this.input_text.append(this.title)
    }

    init_pointer() {
        this.pointer = document
            .createElement("div")
        this.pointer.setAttribute("style",
            `
            position: absolute;
            background-color: #ff0000;
            transform-origin: 100% 100%;
            `
        )
        this.circle.append(this.pointer)
    }

    init_number() {
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
        this.input_text.append(this.number)
    }

    set_title(text) {
        this.title.innerHTML = text
    }

    draw_pointer_value(value) {
        this.pointer_value = value
    }

    set_range_arr(range_arr) {
        this.range_arr = range_arr
        this.__draw_pointer()
        this.__draw_text(
            this.range_arr)
    }

    __draw_text() {
        this.number.innerHTML = `
            ${this.pointer_value}
            (${this.range_arr[0]} 
            / ${this.range_arr[1]})
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
    set_size_card(size) {
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
        this.input_text.style.maxWidth = size_x + "px"
        this.set_size_circle(circle_w, circle_h)
        this.__set_pointer_location(
            pointer_x, pointer_y)
    }

    __set_pointer_location(x, y) {
        this.pointer.style.left = x +"px"
        this.pointer.style.top = y + "px"
    }

    set_pointer_value(value) {
        this.pointer_value = value
        this.__draw_pointer()
    }


    /*
    
    De un rango de [60, 120], con un valor
    de 80

    */
    __draw_pointer() {
        let degrees_total = 180
        let percent = 0
        //convierte el rango a un escala de 0
        let value_in0scale = this.pointer_value
            - this.range_arr[0]
        let range_in0scale = [
            0, 
            this.range_arr[1] 
            - this.range_arr[0]
        ]
        // convierte el valor a porcentaje
        percent = (value_in0scale 
            / range_in0scale[1]) * 100
        // convierte el porcentaje a grados
        let degree_parts
         = (percent / 100) * degrees_total
        // si supera al rango maximo
        if(degree_parts > 180) {
            this.pointer_value 
                = this.range_arr[1]
            degree_parts = 180
        // si es menor al rango minimo
        } else if(degree_parts < 0) {
            this.pointer_value 
                = this.range_arr[0]
            degree_parts = 0
        }
        // dibuja el puntero y el texto
        this.set_angle_degree(degree_parts)
        this.__draw_text()
    }


    set_angle_degree(angulo) {
        this.pointer.style.transform 
            = `rotate(${angulo}deg)`;
    }

}