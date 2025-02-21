

import { StandardElement } 
    from "./StandardElement.js";

export class Canvas extends StandardElement {

    /*
    
    Origenes: 
    0-sup izquierdo
    1-sup derecho
    2-inf izquierdo
    3-inf derecho
    */

    /*
    COMO PINTAR FIGURAS
        Para pintar figuras con este
    modulo debe llamarse al metodo clean,
    despues pintar las figuras finalmente
    llamar al metodo end_paint.
    */

    constructor(size_x, size_y) {
        super("span")
        this.__canvas_main = document
            .createElement('canvas');
        this.__canvas_main.setAttribute(
            "style", 
            `
            border; 2px solid gray;
            `
        )
        //canvas main
        this.__canvas_main.style
            .display = "inline"
        this.__canvas_context = this
            .__canvas_main.getContext('2d');
        this.__canvas_main.setAttribute(
            "style", 
            `
            position: absolute;
            background-color: black;
            `
        )
        this.node.append(
            this.__canvas_main)
        // BUFFER CANVAS -----------------
        // esto permite realizar la tecnica
        // del doble buffer.
        this.__buffer_canvas = document
            .createElement('canvas');
        this.__buffer_canvas.setAttribute(
            "style", 
            `
            position: absolute;
            background-color: black;
            `
        )
        this.__buffer_canvas.width = size_x;
        this.__buffer_canvas.height = size_y;
        this.__buffer_context = this
            .__buffer_canvas.getContext('2d');
        this.node.append(
            this.__buffer_canvas)
        //--------------------------------
        this.size_x = size_x
        this.size_y = size_y
        this.cursor_point = [0, 0]
        this.image_cache_dict = {}
        this.pen_color = "red"
        this.background_color = "black"
        this.pen_width = 1
        this.reference_line_width = 1
        this.reference_line_color = "red"
        this.font_size = 16
        this.font_type = "Arial"
        this.point_index = [0, 0]
        this.set_size(size_x, size_y)
        this.__add_sensor_listeners()
    }

    /*
    Esta funcion realiza un intercambio
    entre los dos canvas del doble buffer.
    */
    __swapp_canvas() {
        let canvas_temp = this
            .__canvas_main
        let buffer_temp = this
            .__buffer_canvas
        this.__canvas_main = buffer_temp
        this.__buffer_canvas = canvas_temp
        this.__buffer_context 
            = this.__buffer_canvas
                .getContext('2d');
        this.__canvas_context 
            = this.__canvas_main.getContext(
                '2d');
        this.__canvas_main.style.visibility
                = "visible"
        this.__buffer_canvas.style.visibility
                = "hidden"
    }

    __add_sensor_listeners() {
        this.node.addEventListener(
            'click', (e) => {
            // Aquí capturaremos las 
            // coordenadas
            this.cursor_point = [0, 0]
            this.cursor_point[0] = e.clientX 
                - this.node
                    .offsetLeft;
            this.cursor_point[1] = e.clientY 
                - this.node
                    .offsetTop;
            console.log("cursor", this.cursor_point)
        });
    }

    destroy() {
        this.__canvas_main.remove()
        this.__canvas_main = null
        this.__canvas_context = null
        this.font_type = null
        this.pen_color = ""
        this.point_index = null
    }

    add_click_listener(callback) {
        this.node.addEventListener(
            'click', callback);
    }

    /*
    Permite obtener las coordenadas del
    cursor en el canvas. Solo se actualiza
    despues de un click del usuario; 
    debido a que utiliza un listener 
    predeterminado.
    */
    get_cursor_point() {
        return this.cursor_point
    }

    get_center_point() {
        return [
            this.size_x / 2,
            this.size_y / 2
        ]
    }

    set_background_color(color) {
        this.background_color = color
        this.__canvas_main.style
            .backgroundColor = color 
    }

    set_pen_color(color_code) {
        this.pen_color = color_code
        this.__buffer_context.fillStyle 
            = color_code;
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

    draw_reference_in_x(point) {
        this.__draw_line_reference(
            [0, point[1]],
            [this.size_x, point[1]]
        )
    }

    draw_reference_in_y(point) {
        this.__draw_line_reference(
            [point[0], 0],
            [point[0], this.size_y]
        )
    }

    draw_reference_line(point) {
        console.log(point)
        this.draw_reference_in_x(point)
        this.draw_reference_in_y(point)
    }

    draw_horizontal_grid(grid_by_side, size) {
        let y = 0
        for(let i=0; i < grid_by_side; i++) {
            y += size
            this.draw_reference_in_x([0, y])
        }
    }

    draw_vertical_grid(grid_by_side, size) {
        let x = 0
        for(let i=0; i < grid_by_side; i++) {
            x += size
            this.draw_reference_in_y([x, 0])
        }
    }

    draw_grid(grid_by_side, size_grid) {
        this.draw_horizontal_grid(grid_by_side,
            size_grid
        )
        this.draw_vertical_grid(grid_by_side,
            size_grid
        )
    }

    draw_text(text, location_x, location_y) {      this.__canvas_context.beginPath();
        this.__buffer_context.fillStyle 
            = this.pen_color; 
        // Color del relleno
        this.__buffer_context.font = 
        `
        ${this.font_size}px ${this.font_type}
        `
        this.__canvas_context.fillText(
            text, location_x, location_y);
    }

    set_pen_width(width) {
        this.pen_width = width
    }

    get_pen_width() {
        return this.pen_width
        this.end_paint
    }

    clear() {
        this.__buffer_context.fillStyle 
            = this.background_color
        this.__buffer_context.fillRect(
            0, 0, 
            this.size_x, 
            this.size_y
        );
    }

    draw_poligon_point(polygon) {
        let point = [0, 0]
        let last_point = [0, 0]
        for(let i in polygon) {
            point = polygon[i]
            if(i != 0) {
                this.draw_line(
                    last_point,
                    point
                )
            }
            last_point = polygon[i]
        }
    }

    draw_image_order_list(image_order_list) {
        let order = {}
        console.log(image_order_list)
        for(let i in image_order_list) {
            order = image_order_list[i]
            this.draw_image(
                order["image"],
                order["x"],
                order["y"]
            )
        }
    }

    draw_poligon_line(polygon) {
        let line = [[0, 0], [0, 0]]
        for(let i in polygon) {
            line = polygon[i]
            this.draw_line_matrix(line)
        }
    }

    draw_line_matrix(line_matrix) {
        this.draw_line(
            line_matrix[0],
            line_matrix[1]
        )
    }

    __draw_line_reference(point_1, point_2) {
        this.__buffer_context.beginPath(); 
        // Inicia un nuevo camino
        this.__buffer_context.moveTo(
            point_1[0], point_1[1]);
        this.__buffer_context.lineTo(
            point_2[0], point_2[1]);
        this.__buffer_context.strokeStyle 
            = this.reference_line_color; 
        this.__buffer_context.lineWidth 
            = this.reference_line_width;
        // Color de la línea
        this.__buffer_context.stroke();
    }

    end_paint() {
        this.__swapp_canvas()
    }

    draw_line(point_1, point_2) {
        this.__buffer_context.beginPath(); 
        this.__buffer_context.strokeStyle 
            = this.pen_color; 
        this.__buffer_context.lineWidth = this
            .pen_width
        // Inicia un nuevo camino
        this.__buffer_context.moveTo(
            point_1[0], point_1[1]);
        this.__buffer_context.lineTo(
            point_2[0], point_2[1]);
        // Color de la línea
        this.__buffer_context.stroke();
        this.point_index = point_2.slice()
    }

    free_image_chache() {
        this.image_cache_dict = {}
    }

    draw_image(url, x, y) {
        //carga imagenes del cache
        if(url in this.image_cache_dict) {
            this.__buffer_context.drawImage(
                this.image_cache_dict[url], 
                x, 
                y
            );
            return null;
        }
        //carga la imagen de la url
        //y la almacena en un cache de 
        //diccionario usando como clave
        //la url.
        let img = new Image();
        img.onload = () => {
            this.__buffer_context.drawImage(
                img, x, y);
            this.image_cache_dict[url] = img
        };
        img.src = url;
    }

    /*
    Dibuja un rectangulo recto usando 
    un punto array y un intervalo 
    de tamaños(x, y); lo dibuja 
    desde el origen 0
    */
    draw_fill_rect_origen_0(point_arr, 
            width, height) {
        this.__buffer_context.fillRect(
            point_arr[0], 
            point_arr[1], 
            width[0], 
            height[1]
        );
    }
    
    /*
    Dibuja un rectangulo desde el origen 1
    que es punto superior izquierdo
    */
    draw_fill_rect_origen_1(point_arr, 
            width, height) {
        this.__buffer_context.fillRect(
            this.size_x - point_arr[0] - size_range[0], 
            point_arr[1], 
            width[0], 
            height[1]
        );
    }

    /*
    Dibuja un rectangulo desde el origen 2
    que es punto inferior izquierdo
    */
    draw_fill_rect_origen_2(point_arr, 
            width, height) {
        this.__buffer_context.fillRect(
            point_arr[0], 
            this.size_y - point_arr[1] 
                - size_range[1], 
            width[0], 
            height[1]
        );
    }

    /*
    Dibuja un rectangulo desde el origen 3
    que es punto inferior derecho.
    */
    draw_fill_rect_origen_3(point_arr, 
            width, height) {
        this.__buffer_context.fillRect(
            this.size_x - point_arr[0] 
            - size_range[0], 
            this.size_y - point_arr[1] 
            - size_range[1], 
            width[0], 
            height[1]
        );
    }

    /*
    Dibuja un rectangulo desde el centro
    del canvas.
    */
    draw_fill_rect_centered(point_arr, 
            width, height) {
        let center_canvas = this
            .get_center_point()
        this.__buffer_context.fillRect(
            (center_canvas[0] 
                - size_range[0] / 2) 
                + point_arr[0], 
            (center_canvas[1] 
                - size_range[1] / 2) 
                + point_arr[1], 
            width[0], 
            height[1]
        );
    }

    draw_circle(point, diameter) {
        this.__buffer_context.beginPath(); 
        // Iniciar un nuevo trazado
        // Dibujar el círculo
        let radio = diameter /2
        let new_point = point
        new_point[0] += radio
        new_point[1] += radio
        this.__buffer_context.arc(
            new_point[0], new_point[1],
            radio, 0, Math.PI * 2
        ); 
        // (x, y, radio, ángulo inicial, ángulo final)
        this.__buffer_context.fillStyle 
            = this.pen_color; 
        // Establecer el color de relleno
        this.__buffer_context.fill(); 
        // Rellenar el círculo
    }

    draw_point_cloud(point_array) {
        for(let i in point_array) {
            this.draw_point(point_array[i])
        }
    }

    draw_point(point) {
        this.__buffer_context.beginPath(); 
        this.__buffer_context.arc(
            point[0], point[1],
            this.pen_width, 0, Math.PI * 2
        ); 
        // (x, y, radio, ángulo inicial, ángulo final)
        this.__buffer_context.fillStyle 
            = this.pen_color; 
        // Establecer el color de relleno
        this.__buffer_context.fill(); 
        // Rellenar el círculo
    }

    move_pen(point) {
        this.point_index = point.slice()
    }

    /*
    Funcion que traza una linea desde el
    ultimo punto de dibujado.
    */
    throw_line(point_2) {
        this.__buffer_context.beginPath(); 
        // Inicia un nuevo camino
        
        this.__buffer_context.moveTo(
            this.point_index[0], 
            this.point_index[1]);
        this.__buffer_context.lineTo(
            point_2[0], point_2[1]);
        this.__buffer_context.strokeStyle 
            = this.pen_color; 
        this.__buffer_context.lineWidth 
            = this.pen_width
        // Color de la línea
        this.__buffer_context.stroke();
        this.point_index = point_2.slice()
        console.log(`point ${this.point_index}`)
    }

    set_size(size_x, size_y) {
        this.size_x = size_x
        this.size_y = size_y
        this.node.style.width 
            = this.size_x + "px"
        this.node.style.height 
            = this.size_y + "px"
        this.__buffer_canvas.width = size_x
        this.__buffer_canvas.height = size_y
        this.__canvas_main.width = size_x
        this.__canvas_main.height = size_y
    }

}