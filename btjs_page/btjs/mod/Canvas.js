


export class Canvas {

    constructor(size_x, size_y) {
        this.node = document
            .createElement("canvas")
        this.size_x = size_x
        this.size_y = size_y
        this.set_size(size_x, size_y)
        this.color = "#000000"
        this.node.fillStyle = this.color
        this.context = this.node
            .getContext('2d');
        this.pen_color = "white"
        this.pen_width = 1
        this.font_size = 50
        this.font_type = "Arial"
        this.point_index = [0, 0]
        this.update()
    }

    destroy() {
        this.node.remove()
        this.node = null
        this.context = null
        this.font_type = null
        this.pen_color = null
        this.point_index = null
        this.color = null
    }

    set_pen_color(color_code) {
        this.pen_color = color_code
    }

    get_pen_color() {
        return this.pen_color
    }

    set_font_type(type) {
        this.font_type = type
    }

    set_font_size(size) {
        this.font_size = size
    }

    draw_text(text, location_x, location_y) {
        this.context.fillStyle = this
            .pen_color; 
        // Color del relleno
        this.context.font = `
        ${this.font_size}px
        ${this.font_type}
        `
        this.context.fillText(
            text, location_x, location_y);
    }

    set_pen_width(width) {
        this.pen_width = width
    }

    get_pen_width() {
        return this.pen_width
    }

    update() {
        this.context.fillRect(
            10, 10, this.size_x, this.size_y);
        this.buffer_img = []
    }

    draw_line(point_1, point_2) {
        this.context.beginPath(); 
        // Inicia un nuevo camino
        this.context.moveTo(
            point_1[0], point_1[1]);
        this.context.lineTo(
            point_2[0], point_2[1]);
        this.context.strokeStyle 
            = this.pen_color; 
        this.context.lineWidth = this
            .pen_width
        // Color de la línea
        this.context.stroke();
        this.point_index = point_2.slice()
    }

    draw_image(url, location_x, location_y) {
        let img = new Image();
        img.onload = () => {
            this.context.drawImage(img, 
                location_x, location_y);
        };
        img.src = url
    }

    move_pen(point) {
        this.point_index = point.slice()
    }

    /*
    Funcion que traza una linea desde el
    ultimo punto de dibujado.
    */
    throw_line(point_2) {
        this.context.beginPath(); 
        // Inicia un nuevo camino
        
        this.context.moveTo(
            this.point_index[0], 
            this.point_index[1]);
        this.context.lineTo(
            point_2[0], point_2[1]);
        this.context.strokeStyle 
            = this.pen_color; 
        this.context.lineWidth = this
            .pen_width
        // Color de la línea
        this.context.stroke();
        this.point_index = point_2.slice()
        console.log(`point ${this.point_index}`)
    }

    set_size(size_x, size_y) {
        this.node.setAttribute(
            "height", size_y)
        this.node.setAttribute(
            "weight", size_x)
    }

}