


export class Gauge {

    __ERROR_MARGIN_PERCENT = 20

    constructor() {
        this.node = document.createElement(
            "span")
        this.node.setAttribute("style",
            "display: inline-block;"
        )
        this.circle = document.createElement(
            "div")
        this.circle.setAttribute("style",
            `
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
            position: relative;
            background-color: rgba(255, 255, 255, 0); /* Fondo blanco con 50% de opacidad */
            color: white;
            padding: 20px;
            `
        )
        this.circle.append(this.number)
        this.circle.append(this.pointer)
        this.node.append(this.circle)
        this.range_arr = [0, 0]
        this.set_size(200)
        this.set_pointer_width(4)
    }

    set_text(text) {
        this.number.innerHTML = text
    }

    set_pointer_width(size) {
        this.pointer.style
            .height = size +"px"
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
        console.log(pointer_x)
        this.circle.style
            .height = size_y +"px"
        this.circle.style.width = size_x +"px"
        this.number.style.left 
        = (size_x / 3.5)  + "px"
        let pointer_heigth = size_y
        this.pointer.style
            .width = pointer_height +"px"
        //
        this.node.style.maxWidth = size_x + "px"
        this.__set_pointer_location(
            pointer_x, size_y)
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
        this.set_text(`
            ${range_arr[0]} / ${range_arr[1]}  
        `)
    }


    set_angle_degree(angulo) {
        this.pointer.style.transform 
            = `rotate(${angulo}deg)`;
    }

}