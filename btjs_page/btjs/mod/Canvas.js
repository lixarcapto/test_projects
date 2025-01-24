

import { StandardElement } 
    from "./StandardElement.js";

export class Canvas {

    constructor(size_x, size_y) {
        this.node = document
            .createElement("canvas")
        this.size_x = 0
        this.size_y = 0
        this.context = this.node
            .getContext('2d');
        this.pen_color = "red"
        this.background_color = "black"
        this.node.style.border = "2px solid gray"
        this.pen_width = 1
        this.font_size = 16
        this.font_type = "Arial"
        this.point_index = [0, 0]
        this.set_size(size_x, size_y)
        this.update()
    }

    destroy() {
        this.node.remove()
        this.node = null
        this.context = null
        this.font_type = null
        this.pen_color = ""
        this.point_index = null
    }

    set_background(color) {
        this.background_color = color
        this.update()
    }

    set_pen_color(color_code) {
        this.pen_color = color_code
        this.context.fillStyle = color_code;
    }

    get_pen_color() {
        return this.pen_color
    }

    set_font_type(type) {
        this.font_type = type
    }

    get_font_size() {
        return this.font_size
    }

    set_font_size(size) {
        this.font_size = size
    }

    draw_images_inline(url_arr, img_width,
        img_height
    ) {
        let point = [0, 0]
        for(let i in url_arr) {
            this.draw_image(url_arr[i],
                point[0], point[1]
            )
            if(point[0] < this.size_x
                -img_width*2
            ) {
                point[0] += img_width
            } else {
                point[0] = 0
                point[1] += img_height
            }
            
        }
    }

    draw_text(text, location_x, location_y) {      this.context.beginPath();
        this.context.fillStyle = this
            .pen_color; 
        // Color del relleno
        this.context.font = 
        `
        ${this.font_size}px ${this.font_type}
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
        this.context.fillStyle = this
            .background_color;
        this.context.fillRect(
            0, 0, this.size_x, this.size_y);
        this.context.fillStyle 
            = this.pen_color;
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

    /*
    Dibuja un rectangulo recto usando 
    un punto array y un intervalo 
    de tamaños(x, y)
    */
    draw_fill_rect(point_arr, size_range) {
        this.context.fillRect(
            point_arr[0], 
            point_arr[1], 
            size_range[0], 
            size_range[1]
        );
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
        this.size_x = size_x
        this.size_y = size_y
        this.node.width = size_x
        this.node.height = size_y
    }

}